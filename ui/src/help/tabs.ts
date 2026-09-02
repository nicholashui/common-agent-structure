export type HelpTab = {
  id: string;
  label: string;
  mdPath: string | null;
};

export const HELP_TABS: HelpTab[] = [
  { id: "spec", label: "Spec", mdPath: null },
  { id: "userguide", label: "User guide", mdPath: null },
];

export const HELP_DEFAULT_TAB = HELP_TABS[0]?.id ?? "spec";
export const HELP_FULL_PAGE_PATH = "/help";
