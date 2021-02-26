"""Base class to create an nbgitpuller link"""
import urllib
from pathlib import Path


class Link:

    """Generate an nbgitpuller link."""

    def __init__(
        self, jupyterhub_url, repository_url=None, branch=None, launch_path=None
    ):

        self._jupyterhub = urllib.parse.urlsplit(jupyterhub_url)
        self._repository = repository_url
        self._branch = branch or "main"
        self._launch = launch_path or ""

        repo_name = urllib.parse.urlsplit(self._repository).path.split("/")[-1]
        urlpath = "tree/{0}/{1}".format(repo_name, self._launch)

        self._scheme = self._jupyterhub.scheme
        self._netloc = self._jupyterhub.netloc
        self._path = "hub/user-redirect/git-pull"
        self._query = urllib.parse.urlencode(
            {
                "repo": self._repository,
                "urlpath": urlpath,
                "branch": self._branch,
            }
        )
        self._fragment = ""

        self._link = urllib.parse.urlunsplit(
            (
                self._scheme,
                self._netloc,
                self._path,
                self._query,
                self._fragment,
            )
        )

    @property
    def link(self):
        return self._link
