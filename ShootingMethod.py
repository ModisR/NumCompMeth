from numpy import *
import matplotlib.pyplot as plt

from lib.runge_kutta import rk, heun
from lib.root_finding import secant

a = 0
b = 6
alpha = 1
beta = 0

def f(_, y):
    return array([y[1], -y[0]])

def G(u):
    _, ys = rk(heun)(f, a, b, 2000, array([alpha, u]))
    return ys[-1][0] - beta

u_ = secant(G, 0, 1, .000001)
xs, ys_ = rk(heun)(f, a, b, 2000, array([alpha, u_]))
plt.plot(xs, [y[0] for y in ys_])
plt.show()
