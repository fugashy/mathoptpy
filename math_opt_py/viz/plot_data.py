# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import cv2
import click


@click.group()
def plot():
    pass


@plot.command(help="plot generated data")
@click.option("-i", "--data_filepath", type=str, default="/tmp/data.yaml")
@click.option("--equal", is_flag=True)
def data(data_filepath, equal):
    fh = cv2.FileStorage(data_filepath, cv2.FileStorage_READ)
    fig, ax = plt.subplots(1, 1)

    gt = fh.getNode("ground_truth").mat()
    if gt is not None:
        ax.plot(gt.T[0], gt.T[1], color="b", label="ground truth")

    obs = fh.getNode("observed").mat()
    if obs is not None:
        ax.scatter(obs.T[0], obs.T[1], color="r", marker=".", label="observed")

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("data")
    if equal:
        ax.axis("equal")
    ax.legend()
    plt.show()

