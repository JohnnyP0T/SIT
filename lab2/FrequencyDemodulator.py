import math
import numpy


def fd(s, K, N, Fd):
    b = [[i for i in range(0, int(K/N))],
             [i for i in range(0, int(K/N))]]
    for i in range(0, int(K/N)):
        t = 0
        state = 0
        for k in range(N*i, N*(i+1)):
            newState = getNewState(s[k], Fd)

            t = t + 1 if newState != 0 and (state == 0 or newState != state) else t
            state = newState if newState != 0 else state
        b[0][i] = t
        b[1][i] = 1 if t > 1 else 0
    return b


def getNewState(sk,Fd):
    if sk > Fd:
        return 1
    elif sk < -Fd:
        return -1
    else:
        return 0