#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
import re
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    print("Installing python-dotenv...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-dotenv"])
    from dotenv import load_dotenv

from llm import ENV_PATH, add_llm_args, complete, resolve_llm

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_CHUNK_CHARS = 8000

SYSTEM_PROMPT = """你係一個專業嘅技術文件翻譯員，將英文翻譯成**香港繁體中文（書面語正式文體）**。最重要係：**所有 Markdown 結構、語法、檔案路徑、代碼必須原封不動，只翻譯純文字內容。**

## 黃金規則（絕對必須遵守）：

### 1. Markdown 結構一字不變
- 標題符號 `#` `##` `###` `####` 保留原樣，數量唔好變，位置唔好變
  - ✅ 正確：`## 第二章 — 演變：每個版本改動嘅原因`
  - ❌ 錯誤：`第二章** — 演變`（刪除咗 `##`）
- 分隔線 `---` 原封不動，唔好刪除、唔好改
- 圖片 `![Alt 文字](路徑)`：只翻譯 `Alt 文字`，括號入面嘅路徑**完全唔好改**
  - ✅ 正確：`![運作循環](svg/operating_loop.svg)`
  - ❌ 錯誤：`![Operating Loop](svg/operating_loop_tc.svg)`
- 列表 `- * 1. 2. 3.` 符號保留，只翻譯後面文字
- 清單縮排保留，空格數唔好變
- 粗體 `**文字**` 同斜體 `*文字*` 符號保留，只翻譯星號中間嘅內容
  - ✅ 正確：`**驗證：** 26 個場景`
- 超連結 `[文字](url)`：只翻譯方括號入面嘅文字，URL 完全唔好改

### 2. 代碼（絕對唔好翻譯）
- 代碼區塊：` ```語言 ` 開頭到 ` ``` ` 結尾，**入面所有內容原封不動，一個字都唔好改**
  - 包括偽代碼、文字公式、狀態圖、名稱列表等任何喺代碼區塊入面嘅內容
- 行內代碼 `` `代碼` ``：反引號中間所有內容**完全唔好改**
  - ✅ 正確：八個狀態其中之一為 `RESOURCE_LIMITED`
  - ❌ 錯誤：`資源不足`（翻譯咗代碼內容）
- 技術代碼名詞：出現喺普通句子入面但冇反引號包住，但明顯係程式/系統名稱嘅 (e.g. `LoopMonitor`, `BudgetController`, `Cynefin`, `WHAT`, `WHY`, `HOW`, `DO`, `REVIEW`, `META-CONTROL`, `VERIFY`, `Safety Kernel`, `EvaluationPlane`, `Gro`, `ReAct`, `Tree-of-Thoughts`) — 呢啲**保留原英文**，唔好翻譯

### 3. 表格（結構完全保留）
- `|` 管線符號一個都唔好少，數量唔好變
- `|---|---|` 分隔行原封不動，連破折號數量同冒號位置都唔好改
- 只翻譯表格格內嘅文字內容
- 表格行嘅順序完全唔好變，包括第 1 行 header、第 2 行 separator、其餘 data rows

### 4. 翻譯風格
- **香港繁體中文書面語**，唔好使用口語化廣東話字（例如「嘅」「咁」「佢」用喺 YouTube 腳本就可以，但呢份係技術書籍文件，要用正式中文「的」「如此」「它」「其」）
  - ✅ 正確：「的」「它」「因此」「然而」「此外」「換言之」
  - ❌ 錯誤：「嘅」「佢」「咁樣」「跟住」「講起」
- 語氣：正式、學術、技術文件風格，準確、清晰、一致
- 專有名詞保持一致：例如每個章節都出現嘅 `graceful state` → 統一譯做「優雅狀態」；`stage gate` → 統一「階段閘門」；`control flow` → 統一「控制流程」；`provenance` → 統一「出處/來源」；`allowlist` → 「允許清單」；`escalate` → 「升級」；`verify` → 「驗證」

### 5. 其他唔好改嘅內容
- 日期 `August 7, 2026`、數字 `36 scenarios`、百分比 `33.6 %` 保留數字，單位可翻譯
- 人名、學術文獻引用標記保留
- 章節編號 `§31`、`§15.4`、`§22.3` 保留原樣
- 狀態代號 `SOLVED`, `APPROXIMATED`, `NEEDS_EVIDENCE`, `NEEDS_EXPERIMENT`, `INFEASIBLE`, `UNSAFE`, `ESCALATED`, `RESOURCE_LIMITED` — 首次出現時格式：`已解決 (SOLVED)`，之後可直接 `SOLVED` 或視乎上下文，但代碼本身一定要保留原狀態字

## 回應要求
- 直接輸出完整翻譯後嘅 Markdown，**唔好加任何前言、解釋、註解、總結**
- 輸出嘅 Markdown 要同輸入嘅行數大致對應，段落順序唔好變
- 如果遇到唔確定嘅翻譯，優先保留英文加括號註解，例如：`演算法（Algorithm）`
"""


def parse_args():
    p = argparse.ArgumentParser(
        description="Translate a markdown book into Traditional Chinese (HK, formal written).")
    p.add_argument("-i", "--input", required=True, help="input markdown file")
    p.add_argument("-o", "--output", required=True, help="output markdown file")
    p.add_argument(
        "--chunk-chars",
        type=int,
        default=int(os.getenv("TRANSLATE_CHUNK_CHARS", str(DEFAULT_CHUNK_CHARS))),
        help=f"max prose characters per request (default {DEFAULT_CHUNK_CHARS})",
    )
    p.add_argument(
        "--no-resume",
        action="store_true",
        help="ignore checkpoint and retranslate every chunk",
    )
    add_llm_args(p)
    return p.parse_args()


def resolve_path(value: str) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = Path.cwd() / path
    return path.resolve()


def load_dotenv_file():
    if not ENV_PATH.is_file():
        raise FileNotFoundError(f"dotenv file not found: {ENV_PATH}")
    load_dotenv(dotenv_path=ENV_PATH)


def load_input_markdown(path: Path):
    if not path.exists():
        raise FileNotFoundError(f"Markdown file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def split_fences(md_text: str) -> list[tuple[str, str]]:
    """Split markdown into ('fence', text) and ('prose', text) parts. Fences stay untranslated."""
    parts: list[tuple[str, str]] = []
    current: list[str] = []
    in_fence = False
    fence_mark = ""

    def flush(kind: str) -> None:
        if current:
            parts.append((kind, "".join(current)))
            current.clear()

    for line in md_text.splitlines(keepends=True):
        stripped = line.lstrip()
        if stripped.startswith("```"):
            mark = stripped.strip()
            if not in_fence:
                flush("prose")
                in_fence = True
                fence_mark = mark
                current.append(line)
            else:
                current.append(line)
                in_fence = False
                fence_mark = ""
                flush("fence")
            continue
        current.append(line)

    if current:
        parts.append(("fence" if in_fence else "prose", "".join(current)))
    return parts


def split_prose(text: str, max_chars: int) -> list[str]:
    if len(text) <= max_chars:
        return [text] if text else []
    chunks: list[str] = []
    buf: list[str] = []
    size = 0
    for para in re.split(r"(?<=\n\n)", text):
        if size and size + len(para) > max_chars:
            chunks.append("".join(buf))
            buf = [para]
            size = len(para)
        else:
            buf.append(para)
            size += len(para)
    if buf:
        chunks.append("".join(buf))
    oversized: list[str] = []
    for chunk in chunks:
        if len(chunk) <= max_chars:
            oversized.append(chunk)
            continue
        line_buf: list[str] = []
        line_size = 0
        for line in chunk.splitlines(keepends=True):
            if line_size and line_size + len(line) > max_chars:
                oversized.append("".join(line_buf))
                line_buf = [line]
                line_size = len(line)
            else:
                line_buf.append(line)
                line_size += len(line)
        if line_buf:
            oversized.append("".join(line_buf))
    return [item for item in oversized if item]


_LETTERS_RE = re.compile(r"[A-Za-z\u4e00-\u9fff]")


def needs_translation(text: str) -> bool:
    """Skip LLM for empty, punctuation-only, or identifier-only chunks."""
    stripped = re.sub(r"`[^`]+`", " ", text)
    stripped = re.sub(r"https?://\S+", " ", stripped)
    letters = _LETTERS_RE.findall(stripped)
    return len(letters) >= 40


def build_jobs(md_text: str, max_chars: int) -> list[dict]:
    jobs: list[dict] = []
    index = 0
    for kind, text in split_fences(md_text):
        if kind == "fence":
            jobs.append(
                {
                    "index": index,
                    "kind": "copy",
                    "source": text,
                    "digest": hashlib.sha256(text.encode("utf-8")).hexdigest(),
                }
            )
            index += 1
            continue
        for chunk in split_prose(text, max_chars):
            kind_job = "translate" if needs_translation(chunk) else "copy"
            jobs.append(
                {
                    "index": index,
                    "kind": kind_job,
                    "source": chunk,
                    "digest": hashlib.sha256(chunk.encode("utf-8")).hexdigest(),
                }
            )
            index += 1
    return jobs


def checkpoint_path(output_path: Path) -> Path:
    return output_path.with_name(output_path.name + ".progress.json")


def load_checkpoint(path: Path) -> dict[str, str]:
    if not path.is_file():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    if not isinstance(payload, dict):
        return {}
    done = payload.get("done")
    if not isinstance(done, dict):
        return {}
    return {str(key): str(value) for key, value in done.items()}


def save_checkpoint(path: Path, done: dict[str, str], total: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        json.dumps({"total": total, "completed": len(done), "done": done}, ensure_ascii=False),
        encoding="utf-8",
    )
    tmp.replace(path)


def translate_chunk(job: dict, client, total: int) -> str:
    sidx = job["index"] + 1
    user_msg = (
        f"呢份係書籍嘅第 {sidx}/{total} 塊。請嚴格遵守 system prompt 所有規則，"
        f"保留全部 Markdown 結構、代碼、表格、圖片路徑，只翻譯文字內容做香港繁體中文（正式書面語）。\n\n"
        f"--- 以下係要翻譯嘅 Markdown 內容 ---\n\n"
        f"{job['source']}"
    )
    return complete(client, SYSTEM_PROMPT, user_msg, temperature=0.3)


def main():
    args = parse_args()
    input_path = resolve_path(args.input)
    output_path = resolve_path(args.output)
    chunk_chars = max(1000, args.chunk_chars)
    progress_file = checkpoint_path(output_path)

    print(f"Env: {ENV_PATH}")
    print("Loading environment...")
    load_dotenv_file()
    client = resolve_llm(args.llm, args.model)
    print(f"LLM: {client.provider} ({client.label})")
    print(f"Model: {client.model}")
    print(f"Base: {client.base_url}")
    print(f"Chunk chars: {chunk_chars}")
    print("Mode: sequential")

    print(f"\nLoading: {input_path}")
    md_text = load_input_markdown(input_path)
    print(f"Input length: {len(md_text)} chars")

    jobs = build_jobs(md_text, chunk_chars)
    copy_n = sum(1 for job in jobs if job["kind"] == "copy")
    translate_n = sum(1 for job in jobs if job["kind"] == "translate")
    print(f"Chunks: {len(jobs)} (translate {translate_n}, copy-as-is {copy_n})")

    done: dict[str, str] = {} if args.no_resume else load_checkpoint(progress_file)
    results: dict[int, str] = {}
    pending: list[dict] = []

    for job in jobs:
        if job["kind"] == "copy":
            results[job["index"]] = job["source"]
            continue
        cached = done.get(job["digest"])
        if cached is not None:
            results[job["index"]] = cached
        else:
            pending.append(job)

    print(f"Cached: {translate_n - len(pending)}  Remaining LLM calls: {len(pending)}")
    if pending:
        print("\nTranslating sequentially...")
        for completed, job in enumerate(pending, start=1):
            head = job["source"].splitlines()[0][:80] if job["source"].splitlines() else ""
            print(f"  [{completed}/{len(pending)}] {len(job['source'])}c | {head}")
            try:
                text = translate_chunk(job, client, len(jobs))
                results[job["index"]] = text
                done[job["digest"]] = text
                save_checkpoint(progress_file, done, translate_n)
                preview = text.replace("\n", " ")[:120]
                print(f"      OK {len(text)}c | {preview}...")
            except Exception as extra:
                print(f"      ERROR: {extra}")
                fallback = (
                    f"\n\n> [翻譯失敗：塊 {job['index'] + 1} - {extra}]\n"
                    f"> 以下保留原文：\n\n"
                    f"{job['source']}"
                )
                results[job["index"]] = fallback

    print("\nCombining chunks...")
    output = "".join(results[i] for i in range(len(jobs)))
    if not output.endswith("\n"):
        output += "\n"

    print(f"Writing output: {output_path}")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"\nDone! Output saved to: {output_path}")
    print(f"  Input:  {len(md_text)} chars (EN)")
    print(f"  Output: {len(output)} chars (Traditional Chinese HK)")
    print(f"  Chunks: {len(jobs)} (LLM {translate_n}, copy {copy_n})")
    print(f"  Checkpoint: {progress_file}")


if __name__ == "__main__":
    main()
