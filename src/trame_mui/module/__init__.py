from pathlib import Path

from trame_mui import __version__

serve_path = str(Path(__file__).with_name("serve").resolve())

serve = {f"__trame_mui_{__version__}": serve_path}
scripts = [f"__trame_mui_{__version__}/trame-mui.umd.js"]
styles = [
    # Self-hosted Roboto (copied from @fontsource/roboto at build time)
    f"__trame_mui_{__version__}/roboto/300.css",
    f"__trame_mui_{__version__}/roboto/400.css",
    f"__trame_mui_{__version__}/roboto/500.css",
    f"__trame_mui_{__version__}/roboto/700.css",
]
# Requires a trame-server with `react_use` module-key aggregation
react_use = ["TrameMui"]


def setup(server, **_):
    if server.client_type != "react":
        msg = f"Server using client_type='{server.client_type}' while we expect 'react'"
        raise TypeError(msg)
