import ast
import click
import yaml
import numpy as np


@click.group()
def datagen():
    pass


class ListOption(click.Option):
    def type_cast_value(self, ctx, value):
        try:
            return ast.literal_eval(value)
        except:
            raise click.BadParameter(value)


def update_config(data, param):
    # すでにあれば読み込んで更新
    # 新規なら新規作成
    filepath = "/tmp/mathoptpy.yaml"
    try:
        f = open(filepath, "r")
        root_node = yaml.safe_load(f)
        print("use exist file")
    except:
        f = open(filepath, "w")
        root_node = {}
        print("create new file")


    root_node["datagen"] = {"model": param, "values": data.tolist()}

    try:
        yaml.dump(root_node, f, default_flow_style=False)
    except:
        f.close()
        f = open(filepath, "w")
        yaml.dump(root_node, f, default_flow_style=False)

    f.close()
    print(f"update {filepath}")


@datagen.command(help="generate linear line data")
@click.option("-a", "--slope", type=float, default=5.)
@click.option("-b", "--intercept", type=float, default=2.)
@click.option("--start", type=float, default=-50.)
@click.option("--end", type=float, default=50.)
@click.option("--step", type=float, default=0.5)
def linear(slope: float, intercept: float, start: float, end: float, step: float):
    x_range = np.arange(start, end, step)
    f = lambda x: slope * x + intercept
    data = np.array([[x, f(x)] for x in x_range])

    param = {
        "type": "linear",
        "slope": slope,
        "intercpet": intercept,
        "start": start,
        "end": end,
        "step": step,
        }

    update_config(data, param)



@datagen.command(help="generate curve line data")
@click.option("--coefficients", cls=ListOption, default="[1., 1., 1.]")
@click.option("--start", type=float, default=-50.)
@click.option("--end", type=float, default=50.)
@click.option("--step", type=float, default=0.5)
def curve(coefficients, start, end, step):
    if len(coefficients) == 3:
        f = lambda x: coefficients[0] * x**2 + coefficients[1] * x + coefficients[2]
    elif len(coefficients) == 4:
        f = lambda x: coefficients[0] * x**3 + coefficients[1] * x**2 + coefficients[2] * x + coefficients[3]
    else:
        raise Exception('Invalid parameter length.')

    param = {
        "type": "curve",
        "coefficients": coefficients,
        "start": start,
        "end": end,
        "step": step,
        }
    data = np.array([[x, f(x)] for x in np.arange(start, end, step)])

    update_config(data, param)


@datagen.command(help="generate Michaelis Menten line data")
@click.option("-b1", type=float, default=0.362)
@click.option("-b2", type=float, default=0.556)
@click.option("--start", type=float, default=0.001)
@click.option("--end", type=float, default=10.)
@click.option("--step", type=float, default=0.2)
def michaelis_menten(b1, b2, start, end, step):
    x_range = np.arange(start, end, step)
    f = lambda x: b1 * x / (b2 + x)
    data = np.array([[x, f(x)] for x in x_range])

    param = {
        "type": "michaelis menten",
        "b1": b1,
        "b2": b2,
        "start": start,
        "end": end,
        "step": step,
        }

    update_config(data, param)


@datagen.command(help="generate ellipse line data")
@click.option("-a", type=float, default=5.)
@click.option("-b", type=float, default=5.)
@click.option("--rotation", type=float, default=np.pi/6.)
@click.option("--translation", type=(float, float), default=(5., 6.))
@click.option("--theta_start", type=float, default=0.)
@click.option("--theta_end", type=float, default=np.pi*2.)
@click.option("--step", type=float, default=np.pi/100.)
def ellipse(a, b, rotation, translation, theta_start, theta_end, step):
    theta_range = np.arange(theta_start, theta_end, step)
    xy = lambda t: np.array(
        [a * np.cos(t) + translation[0], b * np.sin(t) + translation[1]])
    rot_mat = np.array(
        [
            [np.cos(rotation), -np.sin(rotation)],
            [np.sin(rotation), np.cos(rotation)]
        ])
    data = np.array([(rot_mat @  xy(t)).tolist() for t in theta_range])

    param = {
        "type": "ellipse",
        "a": a,
        "b": b,
        "rotation": rotation,
        "translation": list(translation),
        "start": theta_start,
        "end": theta_end,
        "step": step,
        }

    update_config(data, param)

