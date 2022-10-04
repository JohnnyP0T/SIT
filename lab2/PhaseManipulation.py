import math
import numpy


def phase(data, A, fsin, k, C, N):
    s = []
    for i in k:
        s.append(A * math.sin(fsin * math.pi * i * C + data[int(numpy.floor(i / N))] * (math.pi / 2)))
    return s
