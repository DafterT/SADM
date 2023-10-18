import numpy as np
from matplotlib import pyplot as plt

from all_functions import get_C, get_H, draw, print_table
from daviden_fletcher_powell_variable_metric_method import daviden_fletcher_powell_variable_metric_method

if __name__ == '__main__':
    start_x = np.array([1, 5])
    C = get_C()
    stop = 0.1
    H = get_H(C)

    # x, y = relaxation_method(start_x, C, stop, H)
    # x, y = steepest_descent_method(start_x, C, stop, H)
    # x, y = newton_method(start_x, C, stop, H)
    # x, y = conjugate_gradient_method(start_x, C, stop, H)
    # x, y = broyden_method(start_x, C, stop, H)
    # x, y = daviden_fletcher_powell_variable_metric_method(start_x, C, stop, H)
    print_table()
    draw(x, y, C)
    plt.show()
