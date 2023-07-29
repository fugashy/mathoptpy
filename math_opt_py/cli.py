import click

from .config import config
from .viz import viz

u"""
mathoptpy config datagen linear -a 4.0 -b 5.0 -s -10. -e 10 -st 0.1
mathoptpy config noise norm --std 0 0.1
mathoptpy config opt model linear -a 5.0 -b 4.0
mathoptpy config opt updater levenberg_marquardt --weight 0.0001
mathoptpy optimize --tolerance 0.00001
"""


@click.group()
def mathoptpy():
    pass


def main():
    mathoptpy.add_command(config.get_cli())
    mathoptpy.add_command(viz.viz)
    mathoptpy()
