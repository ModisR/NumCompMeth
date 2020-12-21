from numpy import abs
from lib.differentiation import dh4

def newton(f, x0, e=0):
    def iterate(x):
        return x - f(x)/dh4(f, x)
    x1 = iterate(x0)
    while abs(x1 - x0) > e:
        x0, x1 = x1, iterate(x1)
    return x1

def secant(f, x0, x1, e=0):
    while abs(x1 - x0) > e:
        x0, x1 = x1, x1 - f(x1) * (x1 - x0)/(f(x1) - f(x0))
    return x1

def bisection(f, x0, x1, e=0):
    while abs(x1 - x0) > e:
        x2 = (x0 + x1)/2
        x0, x1 = (x0, x2) if f(x1)*f(x2) > 0 else (x2, x1)
    return x1