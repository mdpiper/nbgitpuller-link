import pathlib
import shutil
from itertools import chain

import nox

PROJECT = "nbgitpuller-link"
PACKAGE = "nbgitpuller_link"
ROOT = pathlib.Path(__file__).parent


@nox.session(python=False)
def clean(session):
    """Remove virtual environments, build files, and caches."""
    shutil.rmtree("build", ignore_errors=True)
    shutil.rmtree("wheelhouse", ignore_errors=True)
    shutil.rmtree(f"{PACKAGE}.egg-info", ignore_errors=True)
    shutil.rmtree(".pytest_cache", ignore_errors=True)
    shutil.rmtree(".venv", ignore_errors=True)
    for p in chain(ROOT.rglob("*.py[co]"), ROOT.rglob("__pycache__")):
        if p.is_dir():
            p.rmdir()
        else:
            p.unlink()


@nox.session(python=False)
def cleaner(session):
    """Remove the .nox directory."""
    shutil.rmtree(".nox", ignore_errors=True)


@nox.session
def test_cli(session: nox.Session) -> None:
    """Test the command line interface."""
    session.install(".")
    session.run(PROJECT, "--version")
    session.run(PROJECT, "--help")
