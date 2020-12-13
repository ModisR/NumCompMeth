from numpy import *

def rk(iterate):
    def runge_kutta(f, x0, xn, n, y0):
        h = (xn - x0)/n
        xs = arange(x0, xn, h)
        ys = [y0]
        for x in xs:
            ys.append(iterate(f, x, ys[-1], h))
        xs = append(xs, xn)
        return xs, ys
    return runge_kutta

def euler(f, x, y, h):
    k0 = h * f(x, y)
    return y + h * k0

def heun(f, x, y, h):
    k0 = h * f(x, y)
    k1 = h * f(x+h, y + k0)
    return y + (k0 + k1)/2

def rk4(f, x, y, h):
    k0 = h * f(x, y)
    k1 = h * f(x+h/2, y + k0/2)
    k2 = h * f(x+h/2, y + k1/2)
    k3 = h * f(x+h, y + k2)
    return y + (k0 + 2*(k1 + k2) + k3)/6