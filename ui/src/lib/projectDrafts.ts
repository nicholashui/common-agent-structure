/** Draft shape taken from the four Auto Pilot Chat samples. Intent only — not a shot list. */

export type ProjectDraftFields = {
  name: string;
  title: string;
  brief: string;
  audience: string;
  duration: string;
  outlets: string;
  risk: string;
  notes: string;
};

export type StudyDraft = ProjectDraftFields & {
  id: string;
  label: string;
};

export const STUDY_DRAFTS: StudyDraft[] = [
  {
    id: "asain-beauty",
    label: "Asain Beauty",
    name: "asain-beauty",
    title: "Asain Beauty",
    brief: "Short vertical beauty clip. Adult East Asian woman.",
    audience: "18-34 beauty shoppers on social",
    duration: "15s",
    outlets: "social",
    risk: "low",
    notes: "Pack map only — Chat lock is a phone-macro skin study, not a UGC ad.",
  },
  {
    id: "european-handsome",
    label: "European Handsome",
    name: "european-handsome",
    title: "European Handsome",
    brief: "Short vertical beauty clip. Adult European man.",
    audience: "18-34 on social",
    duration: "15s",
    outlets: "social",
    risk: "low",
    notes: "Pack map only — Chat lock is a rooftop phone-macro, not a UGC ad.",
  },
  {
    id: "japanese-grandma-gta",
    label: "Japanese Grandma GTA",
    name: "japanese-grandma-gta",
    title: "Japanese Grandma GTA",
    brief: "Short 16:9 chase clip. Adult Japanese grandma on a senior scooter.",
    audience: "18-34 on social",
    duration: "15s",
    outlets: "social",
    risk: "low",
    notes: "Pack map only — Chat lock is a rural-Japan scooter chase, not a UGC ad.",
  },
  {
    id: "hongkong-grandma-gta",
    label: "Hong Kong Grandma GTA",
    name: "hongkong-grandma-gta",
    title: "Hong Kong Grandma GTA",
    brief: "Short 16:9 chase clip. Adult Hong Kong grandma walking home at night.",
    audience: "18-34 on social",
    duration: "15s",
    outlets: "social",
    risk: "low",
    notes: "Pack map only — Chat lock is a Hong Kong night walk, not a UGC ad.",
  },
];

export const STUDY_PLACEHOLDER: ProjectDraftFields = {
  name: STUDY_DRAFTS[0].name,
  title: STUDY_DRAFTS[0].title,
  brief: STUDY_DRAFTS[0].brief,
  audience: STUDY_DRAFTS[0].audience,
  duration: STUDY_DRAFTS[0].duration,
  outlets: STUDY_DRAFTS[0].outlets,
  risk: STUDY_DRAFTS[0].risk,
  notes: STUDY_DRAFTS[0].notes,
};

export function applyStudyDraft(current: ProjectDraftFields, draft: StudyDraft): ProjectDraftFields {
  return {
    ...current,
    title: draft.title,
    brief: draft.brief,
    audience: draft.audience,
    duration: draft.duration,
    outlets: draft.outlets,
    risk: draft.risk,
    notes: draft.notes,
  };
}
