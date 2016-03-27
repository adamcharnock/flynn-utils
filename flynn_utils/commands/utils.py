import os
import os.path
from itertools import chain

import click

from flynn_utils.cli import cli
from flynn_utils.utilities import get_projects


@cli.command()
@click.option('--project-dir', '-d', multiple=True, default=['~/Projects',], envvar='PROJECT_DIR')
def list_repos(project_dir):
    click.echo('\n'.join(get_projects(project_dir)))
