"""Import specials pack agents into CASOPS v3 baseline_safe folders.

Source: C:\\Project\\common-agent-swarm-ops\\business\\specials\\agents
Dest:   agents/<agent_id>/

Does not enable network, plugins, memory writes, T3, or production.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from import_video_agents import main

DEFAULT_SOURCE = Path(r"C:\Project\common-agent-swarm-ops\business\specials\agents")


if __name__ == "__main__":
    main(DEFAULT_SOURCE, domain="specials")
