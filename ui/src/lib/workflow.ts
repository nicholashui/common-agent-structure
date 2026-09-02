export const WORKFLOW_SVG: Record<string, string> = {
  video: "/svg/video.workflow.svg",
};

export interface SubWorkflowOption {
  id: string;
  group: string;
  kind: "template" | "scale";
  code: string;
  label: string;
  src: string;
}

const VIDEO_TEMPLATE_CODES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"] as const;
const VIDEO_SCALE_CODES = ["S1", "S2", "S3", "S4", "S5", "S6", "S7"] as const;

function videoTemplate(code: string): SubWorkflowOption {
  const key = code.toLowerCase();
  return {
    id: `video.template.${key}`,
    group: "video",
    kind: "template",
    code,
    label: `Template ${code}`,
    src: `/svg/video.template.${key}.workflow.svg`,
  };
}

function videoScale(code: string): SubWorkflowOption {
  const key = code.toLowerCase();
  return {
    id: `video.scale.${key}`,
    group: "video",
    kind: "scale",
    code,
    label: `Scale ${code}`,
    src: `/svg/video.scale.${key}.workflow.svg`,
  };
}

export const SUB_WORKFLOWS: SubWorkflowOption[] = [
  ...VIDEO_TEMPLATE_CODES.map(videoTemplate),
  ...VIDEO_SCALE_CODES.map(videoScale),
];

export function workflowSvgSrc(group: string): string | null {
  const src = WORKFLOW_SVG[group];
  return src || null;
}

export function listSubWorkflows(group: string): SubWorkflowOption[] {
  return SUB_WORKFLOWS.filter((item) => item.group === group);
}

export function subWorkflowSvgSrc(group: string, id?: string): string | null {
  const options = listSubWorkflows(group);
  if (!options.length) {
    return null;
  }
  const match = id ? options.find((item) => item.id === id) : options[0];
  return match?.src ?? null;
}

export function workflowAgentChatHrefs(svg: string): string[] {
  return [...svg.matchAll(/class="agent-link" href="\/agents\/([^"/]+)\/chat"/g)].map((match) => match[1]);
}
