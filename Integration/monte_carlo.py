from numpy import *
from random import uniform

def monte_carlo(f, ymin, ymax, a, b, n):
    hits = 0
    for _ in range(n):
        hits += uniform(ymin, ymax) < f(uniform(a, b))
    area = (ymax - ymin) * (b - a)
    return area * hits/n

def fun(x):
    return sqrt(4-x*x)

print(monte_carlo(fun, 0, 2, 0, 2, 1000000))