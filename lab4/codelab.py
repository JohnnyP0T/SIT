import math
from numbers import Real
import numpy
from scipy.fft import fft
import scipy
from scipy.fft import ifft
import scipy.signal as signal


def fcomposition(t, s):
    R = 0
    for i in range(len(s)):
        F = s[i]
        R = R + F(t)
    return R

def demodulate(p, lam, T):
    h = signal.hilbert(p)
    h = numpy.abs(h)
    return h

def fdecomposition(sms, T, w, lamw, lam):
    smds = []
    for i in numpy.arange(T/lam):
        smds.append(sms[int(i)] * lam)
    spectr = fft(smds)
    R = []
    K = len(spectr)
    for i in range(K):
        if( ( abs( ((2*math.pi*i) / T) - w) ) <= lamw ) or ( abs( ((2*math.pi*(K + 1 - i)) / T) - w ) <= lamw ):
            R.append(spectr[i])
        else:
            R.append(0)
    R = ifft(R)
    for i in range(len(R)):
        R[i] = (R[i].real)*100
    return R

def filtr(sms, T, w, lamw, lam):
    smds = []
    for i in numpy.arange(T/lam):
        smds.append(sms[int(i)] * lam)
    spectr = fft(smds)
    R = []
    K = len(spectr)
    for i in range(K):
        if( ( abs( ((2*math.pi*i) / T) - w) ) <= lamw ) or ( abs( ((2*math.pi*(K + 1 - i)) / T) - w ) <= lamw ):
            R.append(spectr[i])
        else:
            R.append(0)
    R = ifft(R)
    for i in range(len(R)):
        R[i] = (R[i].real)
    return R

def tdecomposition(s, T, lamT, lam, c, n):
    k = 0
    KX = []
    KY = []
    for i in numpy.arange(T/lam):
        if math.floor((i*lam)/(lamT)) % c == n:
            KX.append(i*lam)
            KY.append(s[int(i)]*lam)
            k = k + 1
    R = []
    for i in numpy.arange(T/lam):
        R.append(numpy.interp( int(i)*lam, KX, KY ) * 100)
    return R

