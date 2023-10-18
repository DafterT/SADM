import numpy as np
from matplotlib import pyplot as plt

from all_functions import get_C, get_H, draw, print_table
from broyden_method import broyden_method
from conjugate_gradient_method import conjugate_gradient_method
from daviden_fletcher_powell_variable_metric_method import daviden_fletcher_powell_variable_metric_method
from newton_method import newton_method
from relaxation_method import relaxation_method
from steepest_descent_method import steepest_descent_method

if __name__ == '__main__':
    start_x = np.array([1, 5])
    start_x = np.array([5, 1])
    start_x = np.array([-2, -3])
    C = get_C()
    stop = 0.01
    H = get_H(C)

    #x, y = relaxation_method(start_x, C, stop, H)
    #x, y = steepest_descent_method(start_x, C, stop, H)
    #x, y = newton_method(start_x, C, stop, H)
    #x, y = conjugate_gradient_method
    #x, y = broyden_method(start_x, C, stop, H)
    x, y = daviden_fletcher_powell_variable_metric_method(start_x, C, stop, H)
    print_table()
    draw(x, y, C)
    plt.show()
