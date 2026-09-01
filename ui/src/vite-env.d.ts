/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_CASOPS_BASE?: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
