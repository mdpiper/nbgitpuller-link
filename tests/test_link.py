"""Test Topography class"""
import pytest
import validators

from nbgitpuller_link import Link

from . import BRANCH, FILE, HUB, REPO


def test_invalid_jupyterhub_url():
    with pytest.raises(ValueError):
        Link(jupyterhub_url="foo", repository_url=REPO)


def test_invalid_repository_url():
    with pytest.raises(ValueError):
        Link(jupyterhub_url=HUB, repository_url="bar")


def test_valid_link():
    link = Link(jupyterhub_url=HUB, repository_url=REPO)
    assert validators.url(link.link)


def test_branch():
    link = Link(jupyterhub_url=HUB, repository_url=REPO, branch=BRANCH)
    assert validators.url(link.link)


def test_launch_path():
    link = Link(jupyterhub_url=HUB, repository_url=REPO, launch_path=FILE)
    assert validators.url(link.link)


def test_all_arguments():
    link = Link(
        jupyterhub_url=HUB, repository_url=REPO, branch=BRANCH, launch_path=FILE
    )
    assert validators.url(link.link)