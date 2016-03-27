import os
import os.path
from itertools import chain
from subprocess import check_output, CalledProcessError, Popen, PIPE, call

import click

DEVNULL = open(os.devnull, 'wb')

def has_flynn_remote(directory):
    git_dir = os.path.join(directory, '.git')
    if not os.path.isdir(git_dir):
        return False
    git_directory = os.path.join(directory, '.git')
    try:
        remotes = check_output(['git', '--git-dir', git_directory, 'remote'], stderr=DEVNULL)
    except CalledProcessError as e:
        return False
    remotes = remotes.split('\n')
    return 'flynn' in remotes


def list_directories(directory):
    for sub_dir in os.listdir(directory):
        path = os.path.join(directory, sub_dir)
        if os.path.isdir(path):
            yield path


def get_projects(project_dirs):
    # Expand out the paths to the dirs where our projects are located
    project_dirs = map(os.path.expanduser, project_dirs)
    # List the contents of each
    projects = chain.from_iterable(list_directories(d) for d in project_dirs)
    # Does it have a 'flynn' git remote?
    projects = (d for d in projects if has_flynn_remote(d))
    return projects


def push_project(project_dir):
    click.secho('Pushing {}'.format(project_dir), fg='green')

    git_directory = os.path.join(project_dir, '.git')
    try:
        remotes = check_output(['git', '--git-dir', git_directory, 'push', 'flynn'])
    except CalledProcessError as e:
        click.secho('Failed to push: {}'.format(e), fg='yello')
        return False
    else:
        click.secho('Pushed {}'.format(project_dir), fg='green')

def app_exists(project_dir):
    p = Popen(['flynn', 'ps'], cwd=project_dir, stderr=DEVNULL, stdout=PIPE)
    p.wait()
    return p.returncode == 0


def app_create(project_dir):
    click.secho('Creating app for {}'.format(project_dir), fg='green')

    p = Popen(['flynn', 'info'], cwd=project_dir, stdout=PIPE)
    p.wait()
    info = p.stdout.read()
    name_line = [l for l in info.split('\n') if l.startswith('===')]
    name_line = name_line[0]
    name = name_line.split(' ', 2)[-1]
    call(['flynn', 'create', '-y', name])

    click.secho('Created {}'.format(name), fg='green')
