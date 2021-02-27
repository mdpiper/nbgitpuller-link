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

        self._generate_link()

    @property
    def link(self):
        return self._link

    def _generate_query(self):
        repo_name = urllib.parse.urlsplit(self._repository).path.split("/")[-1]
        urlpath = "tree/{0}/{1}".format(repo_name, self._launch)

        query = urllib.parse.urlencode(
            {
                "repo": self._repository,
                "urlpath": urlpath,
                "branch": self._branch,
            }
        )

        return query

    def _generate_link(self):
        self._link = urllib.parse.urlunsplit(
            (
                self._jupyterhub.scheme,
                self._jupyterhub.netloc,
                "hub/user-redirect/git-pull",
                self._generate_query(),
                "",
            )
        )
