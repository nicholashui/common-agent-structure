import { asRecord, asString } from "./json";

export interface PluginInterface {
  id: string;
  input_schema: string;
  output_schema: string;
}

export interface AgentIo {
  defined: boolean;
  merged: boolean;
  source: string;
  inputs: string[];
  outputs: string[];
  role: string;
  prompt_reference: string;
  rubric_reference: string;
  protocols: string[];
  plugin_interfaces: PluginInterface[];
}

export const EMPTY_IO: AgentIo = {
  defined: false,
  merged: false,
  source: "none",
  inputs: [],
  outputs: [],
  role: "",
  prompt_reference: "",
  rubric_reference: "",
  protocols: [],
  plugin_interfaces: [],
};

function asStringList(value: unknown): string[] {
  if (!Array.isArray(value)) {
    return [];
  }
  const items: string[] = [];
  for (const item of value) {
    const text = typeof item === "string" ? item.trim() : String(item).trim();
    if (text && !items.includes(text)) {
      items.push(text);
    }
  }
  return items;
}

export function parseAgentIo(value: unknown): AgentIo {
  const record = asRecord(value);
  const plugins = Array.isArray(record.plugin_interfaces)
    ? record.plugin_interfaces
        .map((item) => {
          const row = asRecord(item);
          return {
            id: asString(row.id),
            input_schema: asString(row.input_schema),
            output_schema: asString(row.output_schema),
          };
        })
        .filter((item) => item.id)
    : [];
  return {
    defined: Boolean(record.defined),
    merged: Boolean(record.merged),
    source: asString(record.source, "none"),
    inputs: asStringList(record.inputs),
    outputs: asStringList(record.outputs),
    role: asString(record.role),
    prompt_reference: asString(record.prompt_reference),
    rubric_reference: asString(record.rubric_reference),
    protocols: asStringList(record.protocols),
    plugin_interfaces: plugins,
  };
}

export function ioHasContract(io: AgentIo): boolean {
  return io.inputs.length > 0 || io.outputs.length > 0 || io.plugin_interfaces.length > 0;
}
