def relaxation(init, sx, sy, a=1, b=1):
    res = init[:]
    for x in range(1, sx - 1):
        for y in range(1, sy - 1):
            res[x,y] = (a*(init[x-1,y] + init[x+1,y]) + b*(init[x,y-1] + init[x,y+1])) / (2*(a+b))
    return res