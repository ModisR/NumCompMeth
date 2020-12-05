from numpy import *
import pylab as plt

def trap(f, a, b, n):
    h = (b-a)/n
    fs = [f(x) + f(x+h) for x in arange(a, b, h)]
    return h/2 * sum(fs)

def simpson(f, a, b, n):
    h = (b-a)/n
    fs = [f(x) + 4*f(x+h/2) + f(x+h) for x in arange(a, b, h)]
    return h/6 * sum(fs)

def fun(x):
    return 2./(x*x+1)

xdense = arange(0, 5, .1)
errors = [-log(abs(simpson(fun, -1, 1, 10**x) - pi)/log(10)) for x in xdense]
plt.plot(xdense, errors)
plt.show()
