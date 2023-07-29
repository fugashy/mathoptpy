import click
import yaml
from copy import deepcopy
import numpy as np

_FIlEPATH="/tmp/mathoptpy.yaml"


@click.group()
def noise():
    pass


@noise.command()
@click.option("--std", type=(float, float), default=(0., 0.01))
def norm(std):
    with open(_FIlEPATH, "r") as f:
        root_node = yaml.safe_load(f)

    data = np.array(deepcopy(root_node["datagen"]["values"]))
    noised = np.random.normal(data, std)
    param = {
        "type": "norm",
        "std": list(std),
        }
    root_node["noise"] = {"param": param, "values": noised.tolist()}

    with open(_FIlEPATH, "w") as f:
        yaml.dump(root_node, f, default_flow_style=False)


@noise.command()
@click.option("--theta", type=float, default=np.pi/6.)
@click.option("--translation", type=(float, float), default=(5., 6.))
def rigid_motion(theta, translation):
    with open(_FIlEPATH, "r") as f:
        root_node = yaml.safe_load(f)
    data = np.array(deepcopy(root_node["datagen"]["values"]))

    rot_mat = np.array(
        [
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ])

    translate = lambda xy: np.array([xy[0] + translation[0], xy[1] + translation[1]])
    transform = lambda data: np.array([translate(rot_mat @ xy) for xy in data])
    noised = transform(data)

    param = {
        "type": "rigid_motion",
        "theta": theta,
        "translation": list(translation),
        }
    root_node["noise"] = {"param": param, "values": noised.tolist()}

    with open(_FIlEPATH, "w") as f:
        yaml.dump(root_node, f, default_flow_style=False)
