from numpy import abs

def newton_raphson(f, df, x0, e):
    def iterate(x):
        return x - f(x)/df(x)
    x1 = iterate(x0)
    while abs(x1 - x0) >= e:
        x0, x1 = x1, iterate(x1)
    return x1

def secant_rule(f, x0, x1, e):
    while abs(x1 - x0) >= e:
        x0, x1 = x1, x1 - f(x1) * (x1 - x0)/(f(x1) - f(x0))
    return x1

def bisection_rule(f, x0, x1, e):
    while abs(x1 - x0) >= e:
        x2 = (x0 + x1)/2
        x0, x1 = (x0, x2) if f(x1)*f(x2) > 0 else (x2, x1)
    return x1