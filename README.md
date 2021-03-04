![PyPI](https://img.shields.io/pypi/v/nbgitpuller-link)
[![Build/Test CI](https://github.com/mdpiper/nbgitpuller-link/actions/workflows/build-test-ci.yml/badge.svg)](https://github.com/mdpiper/nbgitpuller-link/actions/workflows/build-test-ci.yml)

# nbgitpuller-link

Generate an [nbgitpuller](https://jupyterhub.github.io/nbgitpuller/index.html) link
through a command-line interface or Python code.

## Installation

Install the latest stable release of *nbgitpuller-link* with `pip`:
```
pip install nbgitpuller-link
```

Or install from source:
After cloning or downloading the *nbgitpuller-link* [repository](https://github.com/mdpiper/nbgitpuller-link),
change into the repository directory
and install the package with `pip`:
```
pip install .
```

## Examples

The *nbgitpuller-link* package includes a CLI and a Python API.
The repository holds short [examples](https://github.com/mdpiper/nbgitpuller-link/tree/main/examples)
of both, which are adapted here.

### Shell

To see how to use the CLI,
call `nbgitpuller-link` with the `--help` option:
```bash
$ nbgitpuller-link --help
Usage: nbgitpuller-link [OPTIONS]

  Generate an nbgitpuller link to load a repository on a JupyterHub

Options:
  --version                   Show the version and exit.
  --jupyterhub-url TEXT       Target JupyterHub for link.  [required]
  --repository-url TEXT       Source repository for link.  [required]
  --branch TEXT               Branch to use from source repository.  [default:
                              main]
  --launch-path TEXT          Relative path to file or directory in source
                              repository to launch on target JupyterHub.
                              [default: ]
  --interface [notebook|lab]  Open with classic Jupyter Notebook interface or
                              next-generation JupyterLab.  [default: notebook]
  --help                      Show this message and exit.
``` 

Generate a link to load a repository on a JupyterHub,
specifying the file to launch
and the branch to use:
```bash
nbgitpuller-link \
    --jupyterhub-url=https://csdms.rc.colorado.edu \
    --repository-url=https://github.com/csdms/espin \
    --branch=main \
    --launch-path=lessons/jupyter/index.ipynb
```

The resulting link:
```bash
https://csdms.rc.colorado.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcsdms%2Fespin&urlpath=tree%2Fespin%2Flessons%2Fjupyter%2Findex.ipynb&branch=main
```

### Python

Start a Python session and import the `Link` class from the *nbgitpuller-link* package:
```python
from nbgitpuller_link import Link
```

Generate a link though a `Link` instance:
```python
linker = Link(
    jupyterhub_url="https://csdms.rc.colorado.edu",
    repository_url="https://github.com/csdms/espin",
    branch="main",
    launch_path="lessons/jupyter/index.ipynb",
    interface="lab",
    )
```
Note that this example uses the JupyterLab interface.

The `link` property holds the URL:
```python
print("The nbgitpuller link is:\n{}".format(linker.link))
```
```
The nbgitpuller link is:
https://csdms.rc.colorado.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcsdms%2Fespin&urlpath=lab%2Ftree%2Fespin%2Flessons%2Fjupyter%2Findex.ipynb%3Fautodecode&branch=main
```
