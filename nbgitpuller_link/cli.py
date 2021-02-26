"""Command-line interface for nbgitpuller-link """
import click

from .link import Link


@click.command()
@click.version_option()
@click.option("-q", "--quiet", is_flag=True, help="Enables quiet mode.")
@click.option(
    "--jupyterhub-url",
    help="JupyterHub target for link.",
)
@click.option(
    "--repository-url",
    help="Source repository for link.",
)
@click.option(
    "--branch",
    help="Branch to use from source repository.",
)
@click.option(
    "--launch-path",
    help="File or directory from source repository to launch on target JupyterHub",
)
def main(jupyterhub_url, repository_url, branch, launch_path, quiet):
    """Generate an nbgitpuller link for a JupyterHub"""
    linker = Link(jupyterhub_url, repository_url, branch, launch_path)
    if not quiet:
        click.secho(linker.link, fg="green")
