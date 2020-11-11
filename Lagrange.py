from numpy import *


def pip(x, i, xs):
    xi = xs[i]
    coefs = [(x - xj) / (xi - xj) for xj in xs if xi != xj]
    return prod(coefs)


def lagrange(x, ys, xs):
    idx = range(len(ys))
    terms = [ys[i] * pip(x, i, xs) for i in idx]
    return sum(terms)
