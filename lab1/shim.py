import numpy
from heaviside import heaviside


def shim(
    Tc,
    T,
    delta,
    sp,
    MAX,
    A,
):
    k = 0
    R = []
    for i in numpy.arange(0, Tc / T):
        tn = (sp(i * T) / (MAX)) * T
        for j in numpy.arange(((i * T * 2) - tn) / (2 * delta), (((i + 1) * (T * 2)) - tn) / (2 * delta)):
            R.append(A * (heaviside(j - ((i * T * 2 - tn) / (2 * delta))) - heaviside(
                j - ((i * T * 2 + tn) / (2 * delta)))))
    return R
