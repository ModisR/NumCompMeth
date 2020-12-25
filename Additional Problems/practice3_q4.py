from numpy import *

B = array([
    [ 3, -1, 0],
    [-1,  3, 0],
    [ 0,  0, 6]
])
phi = pi/4
R = array([
    [ cos(phi), sin(phi), 0],
    [-sin(phi), cos(phi), 0],
    [        0,        0, 1],
])
print(R.T.dot(B).dot(R))