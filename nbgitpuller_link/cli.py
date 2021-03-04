"""Command-line interface for nbgitpuller-link """
import click

from .link import Link


@click.command()
@click.version_option()
@click.option(
    "--jupyterhub-url",
    help="Target JupyterHub for link.",
    required=True,
)
@click.option(
    "--repository-url",
    help="Source repository for link.",
    required=True,
)
@click.option(
    "--branch",
    help="Branch to use from source repository.",
    default="main",
    show_default=True,
)
@click.option(
    "--launch-path",
    help="Relative path to file or directory in source repository to launch on target JupyterHub.",
    default="",
    show_default=True,
)
@click.option(
    "--interface",
    type=click.Choice(["notebook", "lab"], case_sensitive=False),
    default="notebook",
    help="Open with classic Jupyter Notebook interface or next-generation JupyterLab.",
    show_default=True,
)
def main(jupyterhub_url, repository_url, branch, launch_path, interface):
    """Generate an nbgitpuller link to load a repository on a JupyterHub"""
    linker = Link(jupyterhub_url, repository_url, branch, launch_path, interface)
    click.secho(linker.link, fg="green")
