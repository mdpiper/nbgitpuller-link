"""Test bmi-topography command-line interface"""
import validators
from click.testing import CliRunner

from nbgitpuller_link.cli import main


def test_help():
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.output


def test_version():
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert "version" in result.output


def test_fail_with_no_options():
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code != 0
    assert "Error" in result.output


def test_fail_without_jupyterhub_option():
    runner = CliRunner()
    result = runner.invoke(main, ["--repository-url=foo"])
    assert result.exit_code != 0
    assert "Error: Missing option '--jupyterhub-url'" in result.output


def test_fail_without_repository_option():
    runner = CliRunner()
    result = runner.invoke(main, ["--jupyterhub-url=bar"])
    assert result.exit_code != 0
    assert "Error: Missing option '--repository-url'" in result.output


def test_with_required_options():
    runner = CliRunner()
    result = runner.invoke(main, ["--jupyterhub-url=bar", "--repository-url=foo"])
    assert result.exit_code == 0


def test_optional_branch():
    runner = CliRunner()
    result1 = runner.invoke(main, ["--jupyterhub-url=bar", "--repository-url=foo", "--branch=main"])
    assert result1.exit_code == 0
    result2 = runner.invoke(main, ["--jupyterhub-url=bar", "--repository-url=foo"])
    assert result2.exit_code == 0
    assert result1.output == result2.output


def test_optional_launch_path():
    runner = CliRunner()
    result1 = runner.invoke(main, ["--jupyterhub-url=bar", "--repository-url=foo", "--launch-path="])
    assert result1.exit_code == 0
    result2 = runner.invoke(main, ["--jupyterhub-url=bar", "--repository-url=foo"])
    assert result2.exit_code == 0
    assert result1.output == result2.output


def test_valid_result():
    runner = CliRunner()
    result = runner.invoke(main, ["--jupyterhub-url=https://jupyter.org", "--repository-url=https://github.com"])
    assert result.exit_code == 0
    assert validators.url(result.output)
