"""Example of constructing an nbgitpuller link."""
from nbgitpuller_link import Link

HUB="https://csdms.rc.colorado.edu"
REPO="https://github.com/csdms/espin"
BRANCH="main"
FILE="lessons/jupyter/index.ipynb"


linker = Link(
    jupyterhub_url=HUB,
    repository_url=REPO,
    branch=BRANCH,
    launch_path=FILE,
    )

print("The nbgitpuller link is:\n{}".format(linker.link))
