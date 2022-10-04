import numpy


def pd(s, L, K, N, Pd):
    b = [[i for i in range(0, int(K / N))],
         [i for i in range(0, int(K / N))]]
    for i in numpy.arange(0, K / N):
        t = 0
        for k in numpy.arange(N * i, N * (i + 1)):
            if abs(s[int(k)] - L[int(k)]) > Pd:
                t = t + 1
            b[0][int(i)] = t
            b[1][int(i)] = 1 if t > 25 else 0
    return b
