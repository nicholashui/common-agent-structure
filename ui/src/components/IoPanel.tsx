import { EMPTY_IO, ioHasContract, type AgentIo } from "../lib/io";
import { Card } from "./ui";

function ChipList({ items, empty, testId }: { items: string[]; empty: string; testId: string }) {
  if (!items.length) {
    return (
      <p className="text-sm text-stone-500" data-testid={testId}>
        {empty}
      </p>
    );
  }
  return (
    <ul className="flex flex-wrap gap-2" data-testid={testId}>
      {items.map((item) => (
        <li key={item} className="rounded-full bg-indigo-50 px-2.5 py-1 font-mono text-xs text-indigo-800">
          {item}
        </li>
      ))}
    </ul>
  );
}

export function IoPanel({
  io = EMPTY_IO,
  title = "Inputs and outputs",
}: {
  io?: AgentIo;
  title?: string;
}) {
  return (
    <Card>
      <div data-testid="io-panel">
        <h2 className="mb-1 text-sm font-semibold text-stone-900">{title}</h2>
        <p className="mb-3 text-xs text-stone-500">
          {io.merged ? "Merged compose contract" : "Folder-declared contract"}
          {io.source === "critique_edges" ? " · critique_edges" : ""}
          {ioHasContract(io) ? "" : " · none declared"}
        </p>
        <div className="space-y-3">
          <div>
            <h3 className="mb-1 text-xs font-medium uppercase tracking-wide text-stone-400">Inputs</h3>
            <ChipList items={io.inputs} empty="None declared" testId="io-inputs" />
          </div>
          <div>
            <h3 className="mb-1 text-xs font-medium uppercase tracking-wide text-stone-400">Outputs</h3>
            <ChipList items={io.outputs} empty="None declared" testId="io-outputs" />
          </div>
          {io.prompt_reference ? (
            <p className="font-mono text-xs text-stone-500">prompt {io.prompt_reference}</p>
          ) : null}
          {io.plugin_interfaces.length ? (
            <div>
              <h3 className="mb-1 text-xs font-medium uppercase tracking-wide text-stone-400">Plugin schemas</h3>
              <ul className="space-y-1 font-mono text-xs text-stone-700">
                {io.plugin_interfaces.map((plugin) => (
                  <li key={plugin.id}>
                    {plugin.id}: {plugin.input_schema || "—"} → {plugin.output_schema || "—"}
                  </li>
                ))}
              </ul>
            </div>
          ) : null}
        </div>
      </div>
    </Card>
  );
}
