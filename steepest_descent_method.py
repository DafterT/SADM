import numpy as np

from all_functions import calculate_fX, calculate_dfX, create_table, add_row


def steepest_descent_method(start_x, C, stop, H):
    X = start_x
    dfX = calculate_dfX(X, C)
    K = dfX
    x, y = [], []
    i = 1
    create_table(['i', 'x1', 'x2', 'fX'])

    while True:
        x.append(X[0])
        y.append(X[1])
        fX = calculate_fX(X, C)
        add_row([f'{i:<4d}', f'{X[0]:<10.3f}', f'{X[1]:<10.3f}', f'{fX:<10.3f}'])
        if np.linalg.norm(dfX) < stop:
            break
        t = - (np.transpose(dfX) @ K) / (np.transpose(K) @ H @ K)
        X = X + t * K
        dfX = calculate_dfX(X, C)
        i += 1
        K = dfX
    return x, y
