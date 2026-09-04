import {
  Archive,
  BadgeCheck,
  Blocks,
  Bot,
  ChevronDown,
  ClipboardCheck,
  Database,
  FileCode,
  FileText,
  FolderTree,
  GitMerge,
  Home,
  Layers,
  Share2,
  Workflow,
  GitBranch,
  ListTree,
  Lock,
  Menu,
  MessageSquare,
  Network,
  BookOpen,
  PanelLeftClose,
  PanelLeftOpen,
  PanelRight,
  Play,
  ScrollText,
  Settings,
  Shield,
  Sparkles,
  X,
  type LucideIcon,
} from "lucide-react";
import { useEffect, useState, type ReactNode } from "react";
import { RightHelpPanel } from "../help/RightHelpPanel";
import { HELP_FULL_PAGE_PATH } from "../help/tabs";
import { helpPageFrom, helpPageHref } from "../help/paths";
import { useHelpPanel } from "../help/useHelpPanel";
import { RightLogPanel } from "../log/RightLogPanel";
import { recordNavigation } from "../log/install";
import { useLogPanel } from "../log/useLogPanel";
import { ThemeToggle } from "../theme/ThemeToggle";
import { Link, NavLink, Outlet, useLocation, useNavigate, useParams } from "react-router-dom";
import { RecoveryBanner } from "../components/RecoveryBanner";
import { StatusPill } from "../components/StatusPill";
import { useSession } from "../state/session";
import { AgentSwitcher } from "./AgentSwitcher";
import {
  AGENT_MENU_LABEL,
  AGENT_TABS,
  HOME_LABEL,
  WORKFLOW_MENU_LABEL,
  WORKFLOW_TABS,
  agentHref,
  loadNavChrome,
  locationLabel,
  saveNavChrome,
} from "./nav";

const TAB_ICONS: Record<string, LucideIcon> = {
  overview: Home,
  chat: MessageSquare,
  structure: FolderTree,
  files: FileText,
  compose: GitMerge,
  run: Play,
  trace: ListTree,
  capabilities: BadgeCheck,
  protocols: FileCode,
  memory: Database,
  plugins: Blocks,
  cache: Archive,
  safety: Shield,
  improvement: Sparkles,
  validation: ClipboardCheck,
  corrigibility: Lock,
};

const WORKFLOW_TAB_ICONS: Record<string, LucideIcon> = {
  main: ListTree,
  sub: GitBranch,
};

function navClass(isActive: boolean, collapsed: boolean): string {
  return [
    "flex items-center rounded-lg text-xs",
    collapsed ? "justify-center px-2 py-2" : "gap-2 px-3 py-1.5",
    isActive ? "bg-white text-indigo-700 shadow-sm" : "text-stone-600 hover:bg-white",
  ].join(" ");
}

export function AppShell() {
  const session = useSession();
  const location = useLocation();
  const navigate = useNavigate();
  const params = useParams();
  const [mobileOpen, setMobileOpen] = useState(false);
  const [chrome, setChrome] = useState(loadNavChrome);
  const help = useHelpPanel();
  const logs = useLogPanel();
  const agentId = params.agentId ? decodeURIComponent(params.agentId) : session.agents[0]?.agent_id;

  useEffect(() => {
    saveNavChrome(chrome);
  }, [chrome]);

  useEffect(() => {
    recordNavigation(location.pathname);
  }, [location.pathname]);

  useEffect(() => {
    function onResize() {
      if (window.matchMedia("(min-width: 768px)").matches) {
        setMobileOpen(false);
      }
    }
    window.addEventListener("resize", onResize);
    return () => window.removeEventListener("resize", onResize);
  }, []);

  const crumb = locationLabel(location.pathname);
  const collapsed = chrome.collapsed && !mobileOpen;
  const agentOn = location.pathname.startsWith("/agents/");
  const orgOn = location.pathname === "/org-chat";
  const workflowOn = location.pathname === "/workflow" || location.pathname.startsWith("/workflow/");

  function closeMobile() {
    setMobileOpen(false);
  }

  return (
    <div className="min-h-screen bg-white text-stone-900">
      <header className="sticky top-0 z-50 overflow-visible border-b border-stone-200 bg-white/95 backdrop-blur-md">
        <div className="flex flex-wrap items-center gap-x-3 gap-y-2 px-4 py-2">
          <div className="flex items-center gap-2">
            <button
              type="button"
              className="rounded-lg p-1.5 text-stone-600 hover:bg-stone-100 md:hidden"
              aria-label="Open navigation"
              onClick={() => setMobileOpen(true)}
            >
              <Menu size={18} />
            </button>
            <Link to="/" className="flex items-center gap-2 shrink-0">
              <div className="flex h-7 w-7 items-center justify-center rounded-lg bg-indigo-600 shadow-sm">
                <Network size={13} className="text-white" />
              </div>
              <span className="hidden text-sm font-semibold text-stone-900 sm:block">{HOME_LABEL}</span>
            </Link>
          </div>
          <AgentSwitcher
            agents={session.agents}
            extraIds={session.settings.knownIds}
            currentId={agentId}
            onSelect={(id) => navigate(agentHref(id, ""))}
          />
          <div className="ml-auto flex shrink-0 items-center gap-1">
            <button
              type="button"
              className="rounded-lg p-1.5 text-stone-500 hover:bg-stone-100 hover:text-stone-900"
              aria-label="Open documents"
              title="Open documents"
              data-testid="help-open-docs"
              onClick={() => navigate(helpPageHref(location.pathname, location.search))}
            >
              <BookOpen size={16} />
            </button>
            <button
              type="button"
              className={`rounded-lg p-1.5 hover:bg-stone-100 ${logs.logPanelOpen ? "bg-indigo-50 text-indigo-700" : "text-stone-500 hover:text-stone-900"}`}
              aria-label="Toggle log panel"
              aria-pressed={logs.logPanelOpen}
              title="Toggle log panel"
              data-testid="log-toggle-drawer"
              onClick={() => {
                if (!logs.logPanelOpen) {
                  help.closeRightPanel();
                }
                logs.toggleLogPanel();
              }}
            >
              <ScrollText size={16} />
            </button>
            <button
              type="button"
              className={`rounded-lg p-1.5 hover:bg-stone-100 ${help.rightPanelOpen ? "bg-indigo-50 text-indigo-700" : "text-stone-500 hover:text-stone-900"}`}
              aria-label="Toggle help panel"
              aria-pressed={help.rightPanelOpen}
              title="Toggle help panel"
              data-testid="help-toggle-drawer"
              onClick={() => {
                if (!help.rightPanelOpen) {
                  logs.closeLogPanel();
                }
                help.toggleRightPanel();
              }}
            >
              <PanelRight size={16} />
            </button>
            <ThemeToggle />
            <StatusPill status={session.connection} />
          </div>
        </div>
      </header>

      <div className="flex min-h-[calc(100vh-3.5rem)]">
        {mobileOpen ? (
          <button
            type="button"
            className="fixed inset-0 z-30 bg-stone-900/20 md:hidden"
            aria-label="Dismiss navigation"
            onClick={closeMobile}
          />
        ) : null}
        <aside
          className={[
            "border-r border-stone-200 bg-stone-50 transition-[width] duration-200",
            mobileOpen ? "fixed inset-y-0 left-0 z-40 flex flex-col p-3 md:static md:z-auto" : "hidden md:flex",
            "md:flex-col",
            collapsed ? "w-14 p-2" : "w-56 p-3",
          ].join(" ")}
        >
          <div className={`mb-2 flex items-center ${collapsed ? "justify-center" : "justify-between px-1"}`}>
            {collapsed ? null : <span className="text-xs font-semibold uppercase tracking-wide text-stone-400">Navigate</span>}
            <div className="flex items-center gap-1">
              <button
                type="button"
                className="rounded-lg p-1.5 text-stone-500 hover:bg-white hover:text-stone-900"
                aria-expanded={!chrome.collapsed}
                aria-label={chrome.collapsed ? "Expand navigation" : "Collapse navigation"}
                title={chrome.collapsed ? "Expand navigation" : "Collapse navigation"}
                onClick={() => setChrome((current) => ({ ...current, collapsed: !current.collapsed }))}
              >
                {chrome.collapsed ? <PanelLeftOpen size={16} /> : <PanelLeftClose size={16} />}
              </button>
              <button
                type="button"
                className="rounded-lg p-1.5 text-stone-500 hover:bg-white md:hidden"
                aria-label="Close navigation"
                onClick={closeMobile}
              >
                <X size={16} />
              </button>
            </div>
          </div>
          <nav className="flex flex-1 flex-col gap-0.5 overflow-y-auto text-xs">
            <SideLink to="/" end collapsed={collapsed} icon={Layers} onClick={closeMobile}>
              {HOME_LABEL}
            </SideLink>
            <SideLink to="/org-chat" collapsed={collapsed} icon={Share2} onClick={closeMobile}>
              Agent Org Chat
            </SideLink>
            <button
              type="button"
              className={navClass(workflowOn && !collapsed, collapsed)}
              aria-expanded={chrome.workflowOpen}
              title={WORKFLOW_MENU_LABEL}
              data-testid="nav-agent-workflow"
              onClick={() => setChrome((current) => ({ ...current, workflowOpen: !current.workflowOpen }))}
            >
              <Workflow size={16} className="shrink-0" />
              {collapsed ? <span className="sr-only">{WORKFLOW_MENU_LABEL}</span> : <span className="flex-1 text-left">{WORKFLOW_MENU_LABEL}</span>}
              {collapsed ? null : (
                <ChevronDown size={14} className={`shrink-0 text-stone-400 transition-transform ${chrome.workflowOpen ? "" : "-rotate-90"}`} />
              )}
            </button>
            {chrome.workflowOpen
              ? WORKFLOW_TABS.map((tab) => {
                  const Icon = WORKFLOW_TAB_ICONS[tab.id] ?? Workflow;
                  return (
                    <SideLink
                      key={tab.id}
                      to={tab.path}
                      end
                      collapsed={collapsed}
                      icon={Icon}
                      inset={!collapsed}
                      insetDepth={!collapsed ? tab.depth : 0}
                      onClick={closeMobile}
                    >
                      {tab.label}
                    </SideLink>
                  );
                })
              : null}
            <button
              type="button"
              className={navClass(agentOn && !collapsed && !orgOn, collapsed)}
              aria-expanded={chrome.agentOpen}
              title={AGENT_MENU_LABEL}
              onClick={() => setChrome((current) => ({ ...current, agentOpen: !current.agentOpen }))}
            >
              <Bot size={16} className="shrink-0" />
              {collapsed ? <span className="sr-only">{AGENT_MENU_LABEL}</span> : <span className="flex-1 text-left">{AGENT_MENU_LABEL}</span>}
              {collapsed ? null : (
                <ChevronDown size={14} className={`shrink-0 text-stone-400 transition-transform ${chrome.agentOpen ? "" : "-rotate-90"}`} />
              )}
            </button>
            {chrome.agentOpen
              ? AGENT_TABS.map((tab) => {
                  const Icon = TAB_ICONS[tab.id] ?? Home;
                  const to = agentId ? agentHref(agentId, tab.path === "traces" ? "traces" : tab.path) : "/";
                  return (
                    <SideLink
                      key={tab.id}
                      to={to}
                      end={tab.path === ""}
                      collapsed={collapsed}
                      icon={Icon}
                      inset={!collapsed}
                      onClick={closeMobile}
                    >
                      {tab.label}
                    </SideLink>
                  );
                })
              : null}
            <SideLink to="/settings" collapsed={collapsed} icon={Settings} onClick={closeMobile}>
              Settings
            </SideLink>
          </nav>
        </aside>
        <main id="main" className="min-w-0 flex-1 px-4 py-6 md:px-8">
          <div className="mb-4">
            <h1 className="break-all text-2xl font-bold tracking-tight text-stone-900" data-testid="page-location">
              {crumb}
            </h1>
            {session.stale || session.actor === "agent_runtime" ? (
              <p className="mt-1 text-xs text-stone-400">
                {session.stale ? "Stale — Refresh First" : ""}
                {session.stale && session.actor === "agent_runtime" ? " · " : ""}
                {session.actor === "agent_runtime" ? "Agent identities cannot approve." : ""}
              </p>
            ) : null}
          </div>
          <RecoveryBanner
            error={session.lastError}
            onReload={() => {
              if (agentId) {
                void session.client.getAttestation(agentId);
              }
            }}
          />
          <Outlet />
        </main>
        {help.rightPanelOpen && !logs.logPanelOpen ? (
          <RightHelpPanel
            width={help.rightPanelWidth}
            dragging={help.rightPanelDragging}
            pathname={location.pathname === HELP_FULL_PAGE_PATH ? helpPageFrom(location.search, "/") : location.pathname}
            params={params}
            onClose={help.closeRightPanel}
            onWidthChange={help.updateWidth}
            onDraggingChange={help.setRightPanelDragging}
          />
        ) : null}
        {logs.logPanelOpen ? (
          <RightLogPanel
            width={logs.logPanelWidth}
            dragging={logs.logPanelDragging}
            onClose={logs.closeLogPanel}
            onWidthChange={logs.updateLogWidth}
            onDraggingChange={logs.setLogPanelDragging}
          />
        ) : null}
      </div>

      <div className="pointer-events-none fixed bottom-4 right-4 z-50 flex w-80 flex-col gap-2">
        {session.toasts.map((toast) => (
          <button
            key={toast.id}
            type="button"
            className="pointer-events-auto rounded-2xl border border-red-200 bg-white p-3 text-left shadow-md"
            onClick={() => session.dismissToast(toast.id)}
          >
            <p className="font-mono text-xs text-red-700">{toast.code}</p>
            <p className="mt-1 text-sm text-stone-800">{toast.message}</p>
          </button>
        ))}
      </div>
    </div>
  );
}

function SideLink({
  to,
  end,
  collapsed,
  icon: Icon,
  inset,
  insetDepth,
  onClick,
  children,
}: {
  to: string;
  end?: boolean;
  collapsed: boolean;
  icon: LucideIcon;
  inset?: boolean;
  insetDepth?: number;
  onClick?: () => void;
  children: ReactNode;
}) {
  const indent = insetDepth === 2 ? "ml-6" : inset || insetDepth === 1 ? "ml-3" : "";
  return (
    <NavLink
      to={to}
      end={end}
      title={typeof children === "string" ? children : undefined}
      onClick={onClick}
      className={({ isActive }) => `${navClass(isActive, collapsed)} ${indent}`}
    >
      <Icon size={16} className="shrink-0" />
      {collapsed ? <span className="sr-only">{children}</span> : children}
    </NavLink>
  );
}
