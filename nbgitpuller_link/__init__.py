import pkg_resources

from .link import Link

__all__ = ["Link"]
__version__ = pkg_resources.get_distribution("nbgitpuller_link").version
