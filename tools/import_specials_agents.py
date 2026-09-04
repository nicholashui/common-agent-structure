"""Import specials pack agents into CASOPS v3 baseline_safe folders.

Source: vendor/common-agent-swarm-ops/business/specials/agents
Dest:   agents/<agent_id>/

Does not enable network, plugins, memory writes, T3, or production.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from import_video_agents import main
from reloc import VENDOR_SPECIALS_AGENTS

DEFAULT_SOURCE = VENDOR_SPECIALS_AGENTS


if __name__ == "__main__":
    main(DEFAULT_SOURCE, domain="specials")
