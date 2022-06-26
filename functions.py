import numpy as np


def eggholder(x1, x2):
    a = np.sqrt(np.fabs(x2 + x1 / 2 + 47))
    b = np.sqrt(np.fabs(x1 - (x2 + 47)))
    return -(x2 + 47) * np.sin(a) - x1 * np.sin(b)


def eggholder1(X):
    x = X[0]
    y = X[1]
    f = (-(y + 47.0) * np.sin(np.sqrt(abs(x/2.0 + (y + 47.0)))) - x * np.sin(np.sqrt(abs(x - (y + 47.0)))))
    return f


def rastrigin(X):
    A = 10
    y = A * len(X) + sum([(x ** 2 - A * np.cos(2 * np.pi * x)) for x in X])
    return y


def rastrigin1(*X, **kwargs):
    A = kwargs.get('A', 10)
    return A*len(X) + sum([(x**2 - A * np.cos(2 * np.pi * x)) for x in X])
