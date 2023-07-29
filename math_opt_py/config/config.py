import click

from .datagen import datagen
from .noise import noise
# from .opt import opt


@click.group(help="A subcommand that contains the model parameters and the noise, target model, etc...")
def config():
    pass


def get_cli():
    config.add_command(datagen)
    config.add_command(noise)
    # config.add_command(opt)

    return config
