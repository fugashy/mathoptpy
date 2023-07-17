# -*- coding: utf-8 -*-
import click
import cv2
import numpy as np

from .data_2d import (
        Const,
        Linear,
        Quadratic,
        Cubic,
        Ellipse,
        MichaelisMenten,
        Cos,
        )

"""
イメージ
data line -a 3.0 -b 5.0 --start -50 --end 50 --step 0.1 -o /tmp/data_raw.csv
modulate_data norm --std 0.0 0.01 -i /tmp/data.csv
fit ...
"""


def _process(model, output_filepath):
    file_handle = cv2.FileStorage(output_filepath, cv2.FileStorage_WRITE)
    file_handle.write('ground_truth', model.gt)


@click.group()
def data():
    pass


@data.command(help="generate const data")
@click.option("-t", "--translation", type=(float, float), default=(5., 6.))
@click.option("-n", "--num", type=int, default=100)
@click.option("-o", "--output", type=str, default="/tmp/data_raw.yaml")
def const(translation, num, output):
    model = Const(translation, num)
    _process(model, output)


@data.command(help="generate 2D linear data")
@click.option("-a", "--slope", type=float, default=5.)
@click.option("-b", "--intercept", type=float, default=2.)
@click.option("--start", type=float, default=-50.)
@click.option("--end", type=float, default=50.)
@click.option("--step", type=float, default=0.5)
@click.option("-o", "--output", type=str, default="/tmp/data_raw.yaml")
def linear(slope: float, intercept: float, start: float, end: float, step: float, output: str):
    model = Linear(slope, intercept, start, end, step)
    _process(model, output)


@data.command(help="generate quadratic line data")
@click.option("--coefficients", type=(float, float), default=(1., 1.))
@click.option("--constant", type=float, default=1.)
@click.option("--start", type=float, default=-50.)
@click.option("--end", type=float, default=50.)
@click.option("--step", type=float, default=0.5)
@click.option("-o", "--output", type=str, default="/tmp/data_raw.yaml")
def quadratic(coefficients, constant, start, end, step, output):
    model = Quadratic(coefficients, coefficients, start, end, step)
    _process(model, output)


@data.command(help="generate cubic line data")
@click.option("--coefficients", type=(float, float, float), default=(1., 1., 1.))
@click.option("--constant", type=float, default=1.)
@click.option("--start", type=float, default=-50.)
@click.option("--end", type=float, default=50.)
@click.option("--step", type=float, default=0.5)
@click.option("-o", "--output", type=str, default="/tmp/data_raw.yaml")
def cubic(coefficients, constant, start, end, step, output):
    model = Cubic(coefficients, constant, start, end, step)
    _process(model, output)


@data.command(help="generate ellipse data")
@click.option("-a", type=float, default=5.)
@click.option("-b", type=float, default=5.)
@click.option("-r", type=float, default=np.pi/6.)
@click.option("-t", type=(float, float), default=(5., 6.))
@click.option("--theta_start", type=float, default=0.)
@click.option("--theta_end", type=float, default=np.pi*2.)
@click.option("--step", type=float, default=np.pi/100.)
@click.option("-o", "--output", type=str, default="/tmp/data_raw.yaml")
def ellipse(a, b, r, t, theta_start, theta_end, step, output):
    model = Ellipse(a, b, r, t, theta_start, theta_end, step)
    _process(model, output)


@data.command(help="generate Michaelis Menten model data")
@click.option("-b1", type=float, default=0.362)
@click.option("-b2", type=float, default=0.556)
@click.option("--start", type=float, default=0.001)
@click.option("--end", type=float, default=10.)
@click.option("--step", type=float, default=0.2)
@click.option("-o", "--output", type=str, default="/tmp/data_raw.yaml")
def michaelis_menten(b1, b2, start, end, step, output):
    model = MichaelisMenten(b1, b2, start, end, step)
    _process(model, output)
