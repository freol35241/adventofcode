import numpy as np

input = 265149

def findLayer(num):
    sqrt = np.sqrt(num)
    res = int(sqrt)
    
    if res%2 == 0:
        res -= 1
        
    return res+2

def findSidePos(num, side):
    return (num-(side-2)**2)%(side-1)


def solve1(num):
    side = findLayer(num)
    sidePos = findSidePos(num, side)
    return side//2 + np.abs(sidePos-(side//2))


print(solve1(input))
