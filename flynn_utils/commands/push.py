import click

from flynn_utils.cli import cli
from flynn_utils.utilities import get_projects, push_project, app_exists, app_create


@cli.command()
@click.option('--project-dir', '-d', multiple=True, default=['~/Projects',], envvar='PROJECT_DIR')
def push(project_dir):
    projects = get_projects(project_dir)
    for project in projects:
        if not app_exists(project):
            app_create(project)

        push_project(project)
