from numpy import *
from matplotlib import pyplot as plt

a = -2
h = .2
def Integrator(f, x):
    xs = arange(a, x, h)
    dx = h
    if x < a:
        xs = arange(x, a, h)
        dx *= -1
    terms = [f(x + h/2) for x in xs]
    return dx * sum(terms)

def func(x):
    return x*x


xdense = arange(-4, 4, .04)
ys1 = [Integrator(func, x) for x in xdense]
ys2 = [(x**3 + 8) / 3 for x in xdense]

plt.plot(xdense, ys1)
plt.plot(xdense, ys2)
plt.show()