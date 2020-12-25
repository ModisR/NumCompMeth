from numpy import *
from matplotlib.pyplot import *

def func(x):
    x0, x1 = x
    return array([x0 + 2*x1**2 - 1, 3*x1**2 + x1**3 - 1])

def H(x):
    x0, x1 = x
    return array([[1, 4*x1], [6*x0, 3*x1**2]])


n = 500
xs = [array([1, 1])]
js = range(n)

for j in js:
    xj = xs[-1]
    x = xj - linalg.inv(H(xj)).dot(func(xj))
    xs = append(xs, [x], axis=0)

js = append(js, n)
plot(js, xs)
show()