import numpy as np
# Пусть так будет, я не хочу сидеть сокращать тут что-то
from all_functions import calculate_fX, calculate_dfX, create_table, add_row


def broyden_method(start_x, C, stop, H):
    create_table(['i', 'x1', 'x2', 'fX'])
    X = start_x
    fX = calculate_fX(X, C)
    dfX = calculate_dfX(X, C)
    i = 1
    x, y = [X[0]], [X[1]]
    n = np.eye(2)
    K = dfX
    t = - dfX.dot(K) / ((K.dot(H)).dot(K))
    add_row([f'{i:<4d}', f'{X[0]:<10.3f}', f'{X[1]:<10.3f}', f'{fX:<10.3f}'])
    bX = X
    fbX = calculate_fX(bX, C)
    dfbX = calculate_dfX(bX, C)
    X = X + t * K
    fX = calculate_fX(X, C)
    dfX = calculate_dfX(X, C)
    i = 2
    x.append(X[0])
    y.append(X[1])
    dg = dfX - dfbX
    dx = X - bX
    z = dx - n.dot(dg)
    dn = (z.dot(z)) / (z.dot(dg))
    n = n + dn
    K = -n.dot(dfX)
    t = -(dfX.dot(K)) / ((K.dot(H)).dot(K))
    add_row([f'{i:<4d}', f'{X[0]:<10.3f}', f'{X[1]:<10.3f}', f'{fX:<10.3f}'])
    while np.linalg.norm(dfX) > stop:
        bX = X
        X = X + t * K
        i += 1
        x.append(X[0])
        y.append(X[1])
        fbX, dfbX = calculate_fX(bX, C), calculate_dfX(bX, C)
        fX, dfX = calculate_fX(X, C), calculate_dfX(X, C)
        dg = dfX - dfbX
        dx = X - bX
        z = dx - n.dot(dg)
        dn = (z.dot(z)) / (z.dot(dg))
        n = n + dn
        K = -n.dot(dfX)
        t = - (dfX.dot(K)) / ((K.dot(H)).dot(K))
        add_row([f'{i:<4d}', f'{X[0]:<10.3f}', f'{X[1]:<10.3f}', f'{fX:<10.3f}'])
    return x, y
