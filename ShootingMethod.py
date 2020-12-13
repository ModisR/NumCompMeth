from numpy import *
from lib.runge_kutta import rk, heun
from lib.root_finding import secant_rule

a=0
b=1
alpha=1
beta=0

def f(_, y):
    return array([[0, 1], [-1, 0]]).dot(y)

def G(u):
    _, ys = rk(heun)(f, a, b, 2000, array([alpha, u]))
    return ys[-1][0] - beta

print(secant_rule(G, 0, 2, .000001))