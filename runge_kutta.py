from numpy import *
from matplotlib import pyplot as plt

def runge_kutta(tableau):
    m = {c: array(row) for c, row in tableau['matrix'].items()}
    b = tableau['weights']
    def rk(f, x0, xn, n, y0):
        h = (xn - x0)/n
        xs = arange(x0, xn, h)
        ys = [y0]
        for x in xs:
            ks = array([f(x0, y0)])
            for c, coefs in m.items():
                grad = zeros(len(y0))
                for i, a in enumerate(coefs):
                    grad = grad + a*ks[i]
                k = f(x + c*h, ys[-1] + h*grad)
                append(ks, [k])
            y = ys[-1] + h*b.dot(ks)
            ys.append(y)
        append(xs, xn)
        return xs, ys
    return rk

rk4_table = {
    'matrix': {
        1/3: [1/3],
        2/3: [-1/3, 1],
        1  : [1, -1, 1]
    },
    'weights': [1/8, 3/8, 3/8, 1/8]
}

rk4 = runge_kutta(rk4_table)

def func(_, y):
    return array([y[1], -y[0]])

xss, yss = rk4(func, 0, 5, 50, array([0, 1]))

plt.plot(xss, [y[0] for y in yss])
plt.plot(xss, [sin(x) for x in xss])
plt.show()