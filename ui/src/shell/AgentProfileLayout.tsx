import { Outlet, useLocation, useNavigate } from "react-router-dom";
import { useAgentId } from "../lib/hooks";
import { useSession } from "../state/session";
import { AgentSwitcher } from "./AgentSwitcher";
import { agentHref, agentTabPath } from "./nav";

export function AgentProfileLayout() {
  const session = useSession();
  const navigate = useNavigate();
  const location = useLocation();
  const agentId = useAgentId();
  const tab = agentTabPath(location.pathname);

  return (
    <div data-testid="agent-profile">
      <div className="mb-4 max-w-2xl" data-testid="agent-profile-switcher">
        <AgentSwitcher
          agents={session.agents}
          extraIds={session.settings.knownIds}
          currentId={agentId}
          onSelect={(id) => {
            if (id && id !== agentId) {
              navigate(agentHref(id, tab));
            }
          }}
        />
      </div>
      <Outlet />
    </div>
  );
}
