import numpy as np

def eggholder(X):
    x = X[0]
    y = X[1]
    f = (-(y + 47.0) * np.sin(np.sqrt(abs(x/2.0 + (y + 47.0)))) - x * np.sin(np.sqrt(abs(x - (y + 47.0)))))
    return f


def rastrigin(X):
    A = 10
    y = A * len(X) + sum([(x ** 2 - A * np.cos(2 * np.pi * x)) for x in X])
    return y
