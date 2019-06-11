import click


@click.group()
@click.version_option()
def cli():
    "Tool for scraping data sources and creating readable deltas"
    pass


@cli.command()
@click.argument(
    "path",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, allow_dash=False),
    required=False,
    default="."
)
def run(path):
    """Run all scraper classes in the specified directory"""
    click.echo(path)
    # Not yet implemented
