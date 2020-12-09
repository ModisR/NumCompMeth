from numpy import *
from random import uniform

def monte_carlo(f, ymin, ymax, a, b, N):
    n = 0
    for _ in range(N):
        n += uniform(ymin, ymax) < f(uniform(a, b))
    area = (ymax - ymin) * (b - a)
    p = n / N
    # error estimate
    print(area * sqrt(p*(1-p)/N))
    return p * area

def fun(x):
    return sqrt(4-x*x)

print(monte_carlo(fun, 0, 2, 0, 2, 1000000))