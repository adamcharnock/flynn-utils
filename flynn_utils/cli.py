import click

@click.group()
def cli():
    pass

import flynn_utils.commands.utils
import flynn_utils.commands.push
