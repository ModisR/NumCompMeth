import numpy as np
import matplotlib.pyplot as plt


def findas(m, xs_, ys_):
    js = range(m+1)
    matrix = np.array([[x**j for j in js] for x in xs_])
    coefs = np.linalg.solve(matrix.T.dot(matrix), matrix.T.dot(ys_))

    def fit(x):
        terms = [coefs[j] * x**j for j in js]
        return sum(terms)
    return fit


xs = range(1, 7)
ys = [-5.21659, 2.53152, 2.05687, 14.1135, 20.9673, 33.5652]
ft = findas(1, xs, ys)

xdense = np.arange(0, 7, .1)
ydense = [ft(x) for x in xdense]

plt.plot(xs, ys, 'ro')
plt.plot(xdense, ydense)
plt.show()
