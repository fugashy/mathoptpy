# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import click
import yaml
import numpy as np


@click.group()
def viz():
    pass


@viz.command(help="plot generated data and noise")
@click.option("--equal", is_flag=True)
def data(equal):
    with open("/tmp/mathoptpy.yaml", "r") as f:
        root_node = yaml.safe_load(f)
    fig, ax = plt.subplots(1, 1)

    gt = np.array(root_node["datagen"]["values"])
    ax.plot(gt.T[0], gt.T[1], color="b", label="ground truth")

    try:
        obs = np.array(root_node["noise"]["values"])
        ax.scatter(obs.T[0], obs.T[1], color="r", marker=".", label="observed")
    except KeyError:
        print("failed to read noise values.")

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("data")
    if equal:
        ax.axis("equal")
    ax.legend()
    plt.show()

