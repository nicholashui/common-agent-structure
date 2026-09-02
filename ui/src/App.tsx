import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import { AppShell } from "./shell/AppShell";
import { SessionProvider } from "./state/session";
import { ThemeProvider } from "./theme/ThemeProvider";
import { FleetPage } from "./pages/Fleet";
import { AgentOverviewPage } from "./pages/AgentOverview";
import { StructurePage } from "./pages/Structure";
import { ChatPage } from "./pages/Chat";
import { ComposePage } from "./pages/Compose";
import { RunPage } from "./pages/Run";
import { TracePage } from "./pages/Trace";
import { CapabilitiesPage } from "./pages/Capabilities";
import { ProtocolsPage } from "./pages/Protocols";
import { MemoryPage } from "./pages/Memory";
import { PluginsPage } from "./pages/Plugins";
import { CachePage } from "./pages/Cache";
import { SafetyPage } from "./pages/Safety";
import { ImprovementPage } from "./pages/Improvement";
import { ValidationPage } from "./pages/Validation";
import { CorrigibilityPage } from "./pages/Corrigibility";
import { SettingsPage } from "./pages/Settings";
import { OrgChatPage } from "./pages/OrgChat";
import { WorkflowPage } from "./pages/Workflow";
import { HelpPage } from "./pages/Help";

export function App() {
  return (
    <ThemeProvider>
      <SessionProvider>
        <BrowserRouter>
          <Routes>
            <Route element={<AppShell />}>
              <Route path="/" element={<FleetPage />} />
              <Route path="/org-chat" element={<OrgChatPage />} />
              <Route path="/workflow" element={<WorkflowPage kind="main" />} />
              <Route path="/workflow/sub" element={<WorkflowPage kind="sub" />} />
              <Route path="/settings" element={<SettingsPage />} />
              <Route path="/help" element={<HelpPage />} />
              <Route path="/traces/:tid" element={<TracePage />} />
              <Route path="/agents/:agentId" element={<AgentOverviewPage />} />
              <Route path="/agents/:agentId/chat" element={<ChatPage />} />
              <Route path="/agents/:agentId/structure" element={<StructurePage />} />
              <Route path="/agents/:agentId/compose" element={<ComposePage />} />
              <Route path="/agents/:agentId/run" element={<RunPage />} />
              <Route path="/agents/:agentId/traces" element={<TracePage />} />
              <Route path="/agents/:agentId/traces/:tid" element={<TracePage />} />
              <Route path="/agents/:agentId/capabilities" element={<CapabilitiesPage />} />
              <Route path="/agents/:agentId/protocols" element={<ProtocolsPage />} />
              <Route path="/agents/:agentId/memory" element={<MemoryPage />} />
              <Route path="/agents/:agentId/plugins" element={<PluginsPage />} />
              <Route path="/agents/:agentId/cache" element={<CachePage />} />
              <Route path="/agents/:agentId/safety" element={<SafetyPage />} />
              <Route path="/agents/:agentId/improvement" element={<ImprovementPage />} />
              <Route path="/agents/:agentId/validation" element={<ValidationPage />} />
              <Route path="/agents/:agentId/corrigibility" element={<CorrigibilityPage />} />
              <Route path="*" element={<Navigate to="/" replace />} />
            </Route>
          </Routes>
        </BrowserRouter>
      </SessionProvider>
    </ThemeProvider>
  );
}
