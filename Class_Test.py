from numpy import *

A = [[2, 1.5, 1], [0, 1, 0], [1, 1.5, 2]]   # modify this line
# b = [sum([m**i/100 for m in range(51)]) for i in range(3)]   # modify this line
# x = linalg.solve(A, b)   # modify this line


def Last(a, N):
    def iterate(x):
        return 3.7*x*(1 - x)

    def last_impl(x0, x1, n):
        return [x0, x1] if n >= N else last_impl(x1, iterate(x1), n + 1)

    return last_impl(a, iterate(a), 2)


def Middle(f, a, b, h):
    rect_areas = [h * f(x + h/2) for x in arange(a, b, h)]
    return sum(rect_areas)

print(Middle(lambda x: 1 / (x**4 + 1), -1, 1, .1))

