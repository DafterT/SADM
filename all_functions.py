import numpy as np
from matplotlib import pyplot as plt
from prettytable import PrettyTable


def draw(x, y, C):
    x_1 = np.arange(min(x) - 1, max(x) + 1.01, 0.01)
    x_2 = np.arange(min(y) - 1, max(y) + 1.01, 0.01)
    x_1, x_2 = np.meshgrid(x_1, x_2)
    w = (C[0] * x_1 ** 2 + C[1] * x_2 ** 2 + C[2] * x_1 * x_2 + C[3] * x_1 + C[4] * x_2)
    plt.contour(x_1, x_2, w, 30)
    plt.plot(x, y, '.-')


def calculate_fX(X, C):
    return C[0] * X[0] ** 2 + C[1] * X[1] ** 2 + C[2] * X[0] * X[1] + C[3] * X[0] + C[4] * X[1]


def get_C():
    return [-7, -7, 2, 34, 50]


# Матрица Гессе
def get_H(C):
    return np.array([[C[0] * 2, C[2]], [C[2], C[1] * 2]])


# Гардиент
def calculate_dfX(X, C):
    return np.array([C[0] * 2 * X[0] + C[2] * X[1] + C[3], C[1] * 2 * X[1] + C[2] * X[0] + C[4]])


table = None


def create_table(header):
    global table
    table = PrettyTable(header)


def add_row(row):
    table.add_row(row)


def print_table():
    print(table)
