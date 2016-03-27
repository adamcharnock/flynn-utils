import click

from flynn_utils.cli import cli
from flynn_utils import utilities


@cli.command()
@click.option('--project-dir', '-d', multiple=True, default=['~/Projects',], envvar='PROJECT_DIR')
def dump_env(project_dir):
    projects = utilities.get_projects(project_dir)
    for project in projects:
        utilities.dump_env(project)


@cli.command()
@click.option('--project-dir', '-d', multiple=True, default=['~/Projects',], envvar='PROJECT_DIR')
def set_env(project_dir):
    projects = utilities.get_projects(project_dir)
    for project in projects:
        utilities.set_env(project)
