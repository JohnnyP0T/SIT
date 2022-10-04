import math
import numpy


def frequency(data, A, fsin, k, C, N, Wd):
    c = 0
    s = []
    for i in k:
        c = c + math.pi * C * Wd * data[int(numpy.floor(i / N))]
        s.append(A * math.sin(fsin * math.pi * i * C + c))
    return s
