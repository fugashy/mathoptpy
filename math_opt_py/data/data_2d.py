# -*- coding: utf-8 -*-
import numpy as np


class Const():
    def __init__(self, trs, num):
        generate_data = lambda : np.array([trs for i in range(num)])
        self.gt = generate_data()


class Linear():
    def __init__(self, a, b, start, end, step):
        x_range = np.arange(start, end, step)
        f = lambda x: a * x + b
        generate_data = lambda: np.array([[x, f(x)] for x in x_range])
        self.gt = generate_data()


class Quadratic():
    def __init__(self, coefficients, constant, s, e, st):
        f = lambda x: coefficients[0] * x**2 + coefficients[1] * x + constant
        generate_data = lambda : np.array(
            [[x, f(x)] for x in np.arange(s, e, st)])
        self.gt = generate_data()


class Cubic():
    def __init__(self, coefficients, constant, s, e, st):
        f = lambda x: coefficients[0] * x**3 + coefficients[1] * x**2 + coefficients[2] * x + constant
        generate_data = lambda : np.array(
            [[x, f(x)] for x in np.arange(s, e, st)])
        self.gt = generate_data()


class Ellipse():
    def __init__(self, a, b, r, trs, s, e, st):
        theta_range = np.arange(s, e, st)

        xy = lambda t: np.array(
            [a * np.cos(t) + trs[0], b * np.sin(t) + trs[1]])
        rot_mat = np.array(
            [
                [np.cos(r), -np.sin(r)],
                [np.sin(r), np.cos(r)]
            ])
        generate_data = lambda: np.array(
            [rot_mat @  xy(t) for t in theta_range])
        self.gt = generate_data()


class MichaelisMenten():
    def __init__(self, b1, b2, s, e, st):
        x_range = np.arange(s, e, st)
        f = lambda x: b1 * x / (b2 + x)
        generate_data = lambda: np.array([[x, f(x)] for x in x_range])
        self.gt = generate_data()


class Cos():
    def __init__(self, a, b, start, end, step):
        x_range = np.arange(start, end, step)
        f = lambda x: a * np.cos(b * x)
        generate_data = lambda: np.array([[x, f(x)] for x in x_range])
        self.gt = generate_data()
