# -*- coding: utf-8 -*-
import click
import numpy as np
import cv2


@click.group()
def mod():
    pass


@mod.command()
@click.option("--std", type=(float, float), default=(0., 0.01))
@click.option("-i", "--input_filepath", type=str, default="/tmp/data_raw.yaml")
@click.option("-o", "--output_filepath", type=str, default="/tmp/data.yaml")
def norm(std, input_filepath, output_filepath):
    fi = cv2.FileStorage(input_filepath, cv2.FileStorage_READ)
    gt = fi.getNode("ground_truth").mat()
    obs = np.random.normal(gt, std)
    fo = cv2.FileStorage(output_filepath, cv2.FileStorage_WRITE)
    fo.write("ground_truth", gt)
    fo.write("observed", obs)


@mod.command()
@click.option("--theta", type=float, default=np.pi/6.)
@click.option("--translation", type=(float, float), default=(5., 6.))
@click.option("-i", "--input_filepath", type=str, default="/tmp/data_raw.yaml")
@click.option("-o", "--output_filepath", type=str, default="/tmp/data.yaml")
def rigid_motion(theta, translation, input_filepath, output_filepath):
    fi = cv2.FileStorage(input_filepath, cv2.FileStorage_READ)
    gt = fi.getNode("ground_truth").mat()

    rot_mat = np.array(
        [
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ])

    translate = lambda xy: np.array([xy[0] + translation[0], xy[1] + translation[1]])
    transform = lambda data: np.array([translate(rot_mat @ xy) for xy in data])

    obs = transform(gt)

    fo = cv2.FileStorage(output_filepath, cv2.FileStorage_WRITE)
    fo.write("ground_truth", gt)
    fo.write("observed", obs)




#   class RigidMotion(ModelModurator):
#       @staticmethod
#       def create(config_dict):
#           rot_rad = config_dict['rot_rad']
#           trans = config_dict['trans']
#           return RigidMotion(rot_rad, trans)
#
#       def __init__(self, rot_rad, trans):
#           rot_mat = np.array(
#               [
#                   [np.cos(rot_rad), -np.sin(rot_rad)],
#                   [np.sin(rot_rad), np.cos(rot_rad)]
#               ])
#           translate = lambda xy: np.array([xy[0] + trans[0], xy[1] + trans[1]])
#           self._transform = lambda data: np.array([translate(rot_mat @ xy) for xy in data])
#
#       def modurate(self, data):
#           return self._transform(data)
