"""I1 capability-based WASM runtime (Wasmtime, no WASI FS/network)."""

from __future__ import annotations

from dataclasses import dataclass
from wasmtime import Engine, FuncType, Linker, Module, Store, ValType

from casops.auth.handles import CapabilityHandle, HandleBroker
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError

IDENTITY_WAT = """
(module
  (memory (export "memory") 1)
  (func (export "transform") (param $ptr i32) (param $len i32) (result i32)
    local.get $len))
"""

CAP_WAT = """
(module
  (import "casops" "cap_len" (func $cap_len (param i32) (result i32)))
  (memory (export "memory") 1)
  (func (export "transform") (param $ptr i32) (param $len i32) (result i32)
    i32.const 0
    call $cap_len
    drop
    local.get $len))
"""


@dataclass
class I1Result:
    output: bytes
    executed: bool
    mechanism: str = "wasmtime"
    tier: str = "I1"


class I1Runtime:
    def __init__(self, broker: HandleBroker | None = None) -> None:
        self.broker = broker or HandleBroker()
        self.engine = Engine()

    def run(
        self,
        wat: str,
        payload: bytes,
        *,
        handle: CapabilityHandle | None = None,
        audience: str = "plugin",
        scope: str = "transform",
    ) -> I1Result:
        store = Store(self.engine)
        linker = Linker(self.engine)
        granted: dict[int, CapabilityHandle] = {}
        if handle is not None:
            self.broker.verify(handle, audience=audience, scope=scope)
            granted[0] = handle

        def cap_len(index: int) -> int:
            token = granted.get(index)
            if token is None:
                raise CasopsError(ErrorCode.PLG_HANDLE_FORGERY)
            self.broker.verify(token, audience=audience, scope=scope)
            return len(payload)

        linker.define_func("casops", "cap_len", FuncType([ValType.i32()], [ValType.i32()]), cap_len)
        try:
            module = Module(self.engine, wat)
            instance = linker.instantiate(store, module)
        except CasopsError:
            raise
        except Exception as exc:
            # Missing WASI/FS/network imports fail closed — not a silent in-process fallback.
            raise CasopsError(ErrorCode.PLG_ISOLATION_TIER, detail=str(exc)) from exc
        exports = instance.exports(store)
        memory = exports["memory"]
        transform = exports["transform"]
        if len(payload) > int(memory.data_len(store)):
            raise CasopsError(ErrorCode.PLG_PERMISSION, detail="payload exceeds WASM memory")
        memory.write(store, payload, 0)
        length = int(transform(store, 0, len(payload)))
        output = bytes(memory.read(store, 0, length))
        if handle is not None:
            self.broker.revoke(handle.handle_id)
        return I1Result(output=output, executed=True)
