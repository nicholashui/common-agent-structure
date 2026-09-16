import { BrowserRouter, Navigate, Route, Routes, useParams } from "react-router-dom";
import { AppShell } from "./shell/AppShell";
import { AgentProfileLayout } from "./shell/AgentProfileLayout";
import { SessionProvider } from "./state/session";
import { ThemeProvider } from "./theme/ThemeProvider";
import { FleetPage } from "./pages/Fleet";
import { AgentOverviewPage } from "./pages/AgentOverview";
import { StructurePage } from "./pages/Structure";
import { FilesPage } from "./pages/Files";
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
import { ProgramNewPage } from "./pages/ProgramNew";
import { ProgramViewPage } from "./pages/ProgramView";
import { ProjectNewPage } from "./pages/ProjectNew";
import { ProjectStartPage } from "./pages/ProjectStart";
import { ProjectFlowPage } from "./pages/ProjectFlow";
import { ProjectChatPage } from "./pages/ProjectChat";

function ProjectWorkflowRedirect() {
  const { projectId } = useParams();
  return <Navigate to={`/projects/${encodeURIComponent(projectId || "")}/workflow`} replace />;
}

export function App() {
  return (
    <ThemeProvider>
      <SessionProvider>
        <BrowserRouter>
          <Routes>
            <Route element={<AppShell />}>
              <Route path="/" element={<FleetPage />} />
              <Route path="/programs/new" element={<ProgramNewPage />} />
              <Route path="/programs/:programId" element={<ProgramViewPage />} />
              <Route path="/programs" element={<ProgramNewPage />} />
              <Route path="/projects/new" element={<ProjectNewPage />} />
              <Route path="/projects/:projectId/start" element={<ProjectStartPage />} />
              <Route path="/projects/:projectId/workflow" element={<ProjectFlowPage />} />
              <Route path="/projects/:projectId/chat" element={<ProjectChatPage />} />
              <Route path="/projects/:projectId" element={<ProjectWorkflowRedirect />} />
              <Route path="/projects" element={<ProjectNewPage />} />
              <Route path="/org-chat" element={<OrgChatPage />} />
              <Route path="/workflow" element={<WorkflowPage kind="main" />} />
              <Route path="/workflow/sub" element={<WorkflowPage kind="sub" />} />
              <Route path="/settings" element={<SettingsPage />} />
              <Route path="/help" element={<HelpPage />} />
              <Route path="/traces/:tid" element={<TracePage />} />
              <Route path="/agents/:agentId" element={<AgentProfileLayout />}>
                <Route index element={<AgentOverviewPage />} />
                <Route path="chat" element={<ChatPage />} />
                <Route path="structure" element={<StructurePage />} />
                <Route path="files" element={<FilesPage />} />
                <Route path="compose" element={<ComposePage />} />
                <Route path="run" element={<RunPage />} />
                <Route path="traces" element={<TracePage />} />
                <Route path="traces/:tid" element={<TracePage />} />
                <Route path="capabilities" element={<CapabilitiesPage />} />
                <Route path="protocols" element={<ProtocolsPage />} />
                <Route path="memory" element={<MemoryPage />} />
                <Route path="plugins" element={<PluginsPage />} />
                <Route path="cache" element={<CachePage />} />
                <Route path="safety" element={<SafetyPage />} />
                <Route path="improvement" element={<ImprovementPage />} />
                <Route path="validation" element={<ValidationPage />} />
                <Route path="corrigibility" element={<CorrigibilityPage />} />
              </Route>
              <Route path="*" element={<Navigate to="/" replace />} />
            </Route>
          </Routes>
        </BrowserRouter>
      </SessionProvider>
    </ThemeProvider>
  );
}
