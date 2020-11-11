from Lagrange import lagrange

from numpy import arange, e
from matplotlib import pyplot as plt


def fun(x):
    return x * e**(-x**2/4)


def plot(xs):
    a = -10
    b = 10

    xdense = arange(a, b, .1)
    ydense = [fun(x) for x in xdense]

    ys = [fun(x) for x in xs]
    ydense2 = [lagrange(x, ys, xs) for x in xdense]

    plt.plot(xdense, ydense2)
    plt.plot(xdense, ydense)
    plt.show()
