import rich_click as click

from {{ cookiecutter.project_slug }} import __version__, logger


@click.group()
@click.version_option(
    __version__, "-V", "--version", help="Show version information and exit."
)
@click.option(
    "--debug/--no-debug",
    default=False,
    help="Print debug information (used for development).",
)
def app(debug):
    """{{ cookiecutter.project_short_description }}"""
    if debug:
        logger.setLevel("DEBUG")
        click.echo(" * Debug mode: on")
    else:
        logger.setLevel("INFO")


@app.command()
def command():
    """A command description."""
    click.echo("Running command...")


if __name__ == "__main__":
    app()
