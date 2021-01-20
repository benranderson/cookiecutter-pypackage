import pytest
from typer.testing import CliRunner

import {{ cookiecutter.project_slug }}.__main__ as main
from {{ cookiecutter.project_slug }} import __version__


@pytest.fixture
def runner():
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


class TestApp:
    def test_help(self, runner):
        result = runner.invoke(main.app, ["--help"])
        assert result.exit_code == 0

    def test_version(self, runner):
        result = runner.invoke(main.app, ["--version"])
        assert result.exit_code == 0
        assert __version__ in result.stdout
