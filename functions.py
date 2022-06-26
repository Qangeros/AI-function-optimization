import numpy as np

def eggholder(x1, x2):
    a = np.sqrt(np.fabs(x2 + x1 / 2 + 47))
    b = np.sqrt(np.fabs(x1 - (x2 + 47)))
    return -(x2 + 47) * np.sin(a) - x1 * np.sin(b)


def rastrigin(*X, **kwargs):
    A = kwargs.get('A', 10)
    return A*len(X) + sum([(x**2 - A * np.cos(2 * np.pi * x)) for x in X])
