from typing import Optional

import typer

from {{ cookiecutter.project_slug }} import __version__

app = typer.Typer()


def version_callback(value: bool):
    if value:
        typer.echo(f"{{ cookiecutter.project_slug }} version {__version__}")
        raise typer.Exit()


@app.callback()
def callback(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-V",
        callback=version_callback,
        help="Show {{ cookiecutter.project_name }} version.",
    ),
):
    """{{ cookiecutter.project_short_description }}"""


@app.command()
def command():
    """A command description."""
    typer.echo("Running command...")


if __name__ == "__main__":
    app()
