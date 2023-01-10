"""Example of constructing an nbgitpuller link."""
from nbgitpuller_link import Link

HUB = "https://lab.openearthscape.org"
REPO = "https://github.com/csdms/ivy"
BRANCH = "main"
FILE = "lessons/bmi/index.ipynb"
INTERFACE = "lab"


linker = Link(
    jupyterhub_url=HUB,
    repository_url=REPO,
    branch=BRANCH,
    launch_path=FILE,
    interface=INTERFACE,
)

print(f"The nbgitpuller link is:\n{linker.link}")
