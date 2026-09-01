import {
  Archive,
  BadgeCheck,
  Blocks,
  Bot,
  ChevronDown,
  ClipboardCheck,
  Database,
  FileCode,
  FolderTree,
  GitMerge,
  Home,
  Layers,
  Share2,
  ListTree,
  Lock,
  Menu,
  Network,
  PanelLeftClose,
  PanelLeftOpen,
  Play,
  Settings,
  Shield,
  Sparkles,
  X,
  type LucideIcon,
} from "lucide-react";
import { useEffect, useState, type ReactNode } from "react";
import { Link, NavLink, Outlet, useLocation, useNavigate, useParams } from "react-router-dom";
import { ActorStrip } from "../components/ActorStrip";
import { RecoveryBanner } from "../components/RecoveryBanner";
import { StatusPill } from "../components/StatusPill";
import { useSession } from "../state/session";
import { AgentSwitcher } from "./AgentSwitcher";
import { AGENT_TABS, agentHref, loadNavChrome, saveNavChrome } from "./nav";

const TAB_ICONS: Record<string, LucideIcon> = {
  overview: Home,
  structure: FolderTree,
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

function navClass(isActive: boolean, collapsed: boolean): string {
  return [
    "flex items-center rounded-lg text-sm",
    collapsed ? "justify-center px-2 py-2" : "gap-2 px-3 py-2",
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
  const agentId = params.agentId ? decodeURIComponent(params.agentId) : session.agents[0]?.agent_id;

  useEffect(() => {
    saveNavChrome(chrome);
  }, [chrome]);

  const crumb =
    location.pathname === "/"
      ? "Fleet"
      : location.pathname === "/org-chat"
        ? "Agent Org Chat"
        : location.pathname.replace(/^\//, "");
  const collapsed = chrome.collapsed && !mobileOpen;
  const agentOn = location.pathname.startsWith("/agents/");
  const orgOn = location.pathname === "/org-chat";

  function closeMobile() {
    setMobileOpen(false);
  }

  return (
    <div className="min-h-screen bg-white text-stone-900">
      <header className="sticky top-0 z-50 overflow-visible border-b border-stone-200 bg-white/95 backdrop-blur-md">
        <div className="flex flex-wrap items-end gap-x-3 gap-y-2 px-4 py-2">
          <div className="mb-0.5 flex items-center gap-2">
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
              <span className="hidden text-sm font-semibold text-stone-900 sm:block">caso</span>
            </Link>
          </div>
          <AgentSwitcher
            agents={session.agents}
            extraIds={session.settings.knownIds}
            currentId={agentId}
            onSelect={(id) => navigate(agentHref(id, ""))}
          />
          <ActorStrip />
          <div className="mb-0.5 shrink-0">
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
          <nav className="flex flex-1 flex-col gap-0.5 overflow-y-auto text-sm">
            <SideLink to="/" end collapsed={collapsed} icon={Layers} onClick={closeMobile}>
              Fleet
            </SideLink>
            <SideLink to="/org-chat" collapsed={collapsed} icon={Share2} onClick={closeMobile}>
              Agent Org Chat
            </SideLink>
            <button
              type="button"
              className={navClass(agentOn && !collapsed && !orgOn, collapsed)}
              aria-expanded={chrome.agentOpen}
              title="Agent workspace"
              onClick={() => setChrome((current) => ({ ...current, agentOpen: !current.agentOpen }))}
            >
              <Bot size={16} className="shrink-0" />
              {collapsed ? <span className="sr-only">Agent workspace</span> : <span className="flex-1 text-left">Agent</span>}
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
          <p className="mb-4 text-xs text-stone-400">
            Fleet / {crumb}
            {session.stale ? " · Stale — Refresh First" : ""}
            {session.actor === "agent_runtime" ? " · Agent identities cannot approve." : ""}
          </p>
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
  onClick,
  children,
}: {
  to: string;
  end?: boolean;
  collapsed: boolean;
  icon: LucideIcon;
  inset?: boolean;
  onClick?: () => void;
  children: ReactNode;
}) {
  return (
    <NavLink
      to={to}
      end={end}
      title={typeof children === "string" ? children : undefined}
      onClick={onClick}
      className={({ isActive }) => `${navClass(isActive, collapsed)} ${inset ? "ml-3" : ""}`}
    >
      <Icon size={16} className="shrink-0" />
      {collapsed ? <span className="sr-only">{children}</span> : children}
    </NavLink>
  );
}
