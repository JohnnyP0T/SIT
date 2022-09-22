import numpy
from heaviside import heaviside


def aim(
    Tc,
    T,
    tn,
    delta,
    sp,
):
    R = []
    for i in numpy.arange(0, Tc / T):
        for j in numpy.arange((i * T * 2 - tn) / (2 * delta), (((i + 1) * T * 2 - tn) / (2 * delta))):
            heaviside1 = j - (i * T * 2 - tn) / (2 * delta)
            heaviside2 = j - (i * T * 2 + tn) / (2 * delta)
            R.append(sp(i * T) * (heaviside(heaviside1) -
                                  heaviside(heaviside2)))
    return R
