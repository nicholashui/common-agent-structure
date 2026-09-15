/** ISSUE-0009 P5: T4 heading → owner + canonical path. Mirrors casops.video_prompt.owners. */

export const OWNER_PATHS: Record<string, string[]> = {
  "video.creativedirector": ["intent", "creative.continuity"],
  "video.promptengineer": ["generation", "classification", "creative.audio"],
  "video.continuity": ["creative.shots.subjects"],
  "video.mua_makeup": ["creative.shots.subjects.scene_state"],
  "video.cinematographer": ["creative.shots.lighting", "creative.shots.look"],
  "video.director": ["creative.shots.action"],
  "video.cameraoperator": ["creative.shots.camera"],
  "video.critic": ["constraints", "provenance.diagnostics"],
};

export const HEADING_OWNERS: Record<string, { owner: string; path: string }> = {
  "Creative direction": { owner: "video.creativedirector", path: "intent" },
  Frame: { owner: "video.promptengineer", path: "generation" },
  Subject: { owner: "video.continuity", path: "creative.shots.subjects" },
  Hair: { owner: "video.continuity", path: "creative.shots.subjects.anchors" },
  Skin: { owner: "video.continuity", path: "creative.shots.subjects.anchors" },
  Makeup: { owner: "video.mua_makeup", path: "creative.shots.subjects.scene_state" },
  Light: { owner: "video.cinematographer", path: "creative.shots.lighting" },
  "Coverage / performance": { owner: "video.director", path: "creative.shots.action" },
  "Camera lock": { owner: "video.cameraoperator", path: "creative.shots.camera" },
  Sound: { owner: "video.promptengineer", path: "creative.audio" },
  "Sound, if the model supports native audio": { owner: "video.promptengineer", path: "creative.audio" },
  Negatives: { owner: "video.critic", path: "constraints" },
};

const PROJECTION_HEADINGS = new Set(Object.keys(HEADING_OWNERS));

export type ProjectionSection = {
  heading: string;
  body: string;
  owner: string;
  path: string;
};

export function ownerPathsFor(agentId: string): string[] {
  return OWNER_PATHS[String(agentId || "").trim()] || [];
}

export function headingOwner(heading: string): { owner: string; path: string } {
  const key = String(heading || "").trim();
  if (HEADING_OWNERS[key]) {
    return HEADING_OWNERS[key];
  }
  if (key.startsWith("Sound")) {
    return { owner: "video.promptengineer", path: "creative.audio" };
  }
  if (key.includes(" | ") && /^\d/.test(key)) {
    return { owner: "video.director", path: "creative.shots.action" };
  }
  return { owner: "", path: "" };
}

export function splitProjection(text: string): { intro: string; sections: ProjectionSection[] } {
  const sections: ProjectionSection[] = [];
  let current = "";
  let intro = "";
  const buf: string[] = [];

  function flush() {
    const body = buf.join("\n").trim();
    buf.length = 0;
    if (!current) {
      intro = body;
      return;
    }
    const owned = headingOwner(current);
    sections.push({ heading: current, body, owner: owned.owner, path: owned.path });
  }

  for (const line of String(text || "").split(/\r?\n/)) {
    const stripped = line.trim();
    if (stripped && !stripped.startsWith("•") && stripped.length < 80) {
      const key = stripped.replace(/^#+\s*/, "").trim();
      if (PROJECTION_HEADINGS.has(key) || (key.includes(" | ") && /^\d/.test(key))) {
        flush();
        current = key.startsWith("Sound") ? "Sound" : key;
        continue;
      }
    }
    buf.push(line);
  }
  flush();
  return { intro, sections };
}

export function dispositionChips(
  coverage: { disposition?: string }[] | undefined,
): { disposition: string; count: number }[] {
  const counts = new Map<string, number>();
  for (const row of coverage || []) {
    const key = String(row.disposition || "").trim();
    if (!key) {
      continue;
    }
    counts.set(key, (counts.get(key) || 0) + 1);
  }
  const order = ["exact", "prompted", "approximated", "post", "unsupported", "not_applicable"];
  const keys = [...counts.keys()].sort((a, b) => {
    const ia = order.indexOf(a);
    const ib = order.indexOf(b);
    return (ia === -1 ? order.length : ia) - (ib === -1 ? order.length : ib);
  });
  return keys.map((disposition) => ({ disposition, count: counts.get(disposition) || 0 }));
}
