import click

from .data.entrypoints import data
from .viz.plot_data import plot
from .mod.modurators import mod
from .opt.optimize import opt


@click.group()
def mathoptpy():
    pass


def main():
    mathoptpy.add_command(data)
    mathoptpy.add_command(mod)
    mathoptpy.add_command(plot)
    mathoptpy.add_command(opt)
    mathoptpy()
