import math
import random


def nois(x):
    MIN = 2
    MAX = 5
    xres = x.copy()
    for i in range(MIN + math.floor(random.uniform(0, int(MAX - MIN + 1)))):
        ri = math.floor(random.uniform(0,len(x)))
        xres[ri] = int(not bool(x[ri]))
    return xres