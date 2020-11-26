from numpy import *

def simpson(f, a, b, h):
    xs = arange(a, b, h)
    terms = [f(x) + 4*f(x + h/2) + f(x+h) for x in xs]
    return h * sum(terms) / 6

def func(x):
    return exp(-x*x/2)

estimate = simpson(func, -5, 5, .5)
print(estimate)
print(sqrt(2*pi))
