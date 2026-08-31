from pathlib import Path

from casops.api.control import create_control_plane

app = create_control_plane(agents_root=Path("agents"))
