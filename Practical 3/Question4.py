from numpy import *
from matplotlib import pyplot as plt

h = .5
def heun(f, x0, y0, x1):
    ys = [y0]
    for x in arange(x0, x1 - h, h):
        y = ys[-1]
        k0 = f(x, y)
        k1 = f(x + h/2, y + k0*h/2)
        ys.append(y + h * k1)
    return ys

def fun(_, y):
    A = array([[0, 1], [0, -1]])
    return A.dot(y)

def exact(x):
    return 1 - exp(-x)

xs = arange(0, 5, h)
y_estimate = [y[0] for y in heun(fun, 0, array([0, 1]), 5)]
x_dense = arange(0, 5, .1)
y_exact = [exact(x) for x in x_dense]

plt.plot(xs, y_estimate)
plt.plot(x_dense, y_exact)
plt.show()
