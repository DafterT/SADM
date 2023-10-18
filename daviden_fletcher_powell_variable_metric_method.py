import numpy as np

# Пусть так будет, я не хочу сидеть сокращать тут что-то
from all_functions import calculate_fX, calculate_dfX, create_table, add_row


def daviden_fletcher_powell_variable_metric_method(start_x, C, stop, H):
    create_table(['i', 'x1', 'x2', 'fX'])
    X = start_x
    fX, dfX = calculate_fX(X, C), calculate_dfX(X, C)
    x, y = [X[0]], [X[1]]
    n = -np.eye(2)
    K = -n.dot(dfX)
    t = -(dfX.dot(K)) / ((H.dot(K)).dot(K))
    i = 1
    add_row([f'{i:<4d}', f'{X[0]:<10.3f}', f'{X[1]:<10.3f}', f'{fX:<10.3f}'])
    while np.linalg.norm(dfX) > stop:
        dfbXinitial = dfX
        t = -(dfX.dot(K)) / ((H.dot(K)).dot(K))
        deltaX = t * K
        X = X + deltaX
        fX, dfX = calculate_fX(X, C), calculate_dfX(X, C)
        deltaG = dfX - dfbXinitial
        A = (deltaX.dot(deltaX)) / (deltaX.dot(deltaG))
        B = (n.dot(deltaG) * deltaG.dot(n)) / (deltaG.dot(n).dot(deltaG))
        delta_n = A - B
        n = n + delta_n
        K = -n.dot(dfX)
        x.append(X[0])
        y.append(X[1])
        i += 1
        add_row([f'{i:<4d}', f'{X[0]:<10.3f}', f'{X[1]:<10.3f}', f'{fX:<10.3f}'])
    return x, y
