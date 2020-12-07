from numpy import *
from scipy import integrate

# vector map - applies f to every element of xs
# and returns numpy-compatible vector
def vmap(f, xs):
    return array([f(x) for x in xs])

def nodes_and_coefs(weight, a, b, n):
    def get_h(k):
        return integrate.quad(lambda x: weight(x) * x ** k, a, b)[0]
    ks = range(n+1)
    hs = vmap(get_h, range(2*n+2))
    # find xi
    B = [hs[k:k+n+1] for k in ks]
    u = -hs[n+1:]
    cs = append(linalg.solve(B, u), [1])
    xs = roots(cs[::-1]).real
    # find Ai
    B = [[xs[i]**k for i in ks] for k in ks]
    u = hs[:n+1]
    As = linalg.solve(B, u)
    return xs, As

def gauss(f, As, xs):
    return sum(As.dot(vmap(f, xs)))

x_, A_ = nodes_and_coefs(lambda x: exp(-x*x), -1, 1, 6)
print(gauss(exp, A_, x_))