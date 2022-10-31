import math
from signal import signal
import numpy
import codelab
import matplotlib.pyplot as plt
from scipy.fft import fft


modulate = lambda sd, t, w: sd(t)*math.sin(w*t)
# Наш вариант
s1 = lambda t: (1 - math.sin(t)) / 2
s2 = lambda t: (1 + math.sin(t)) / (2 + math.sin(t))
lam = 0.01
lamT = 0.12
T = 4
w1 = 30
lamw = 15
w2 = w1+2*lamw


# Вариант из методички.
# s1 = lambda t: 1 + math.sin(t * math.sin(t))
# s2 = lambda t: 1 + math.cos(t * math.sin(t))
# lam = 0.01
# lamT = 0.1
# T = 6
# w1 = 20
# lamw = 15
# w2 = w1+2*lamw


sig1 = [s1(counter) for counter in numpy.arange(0, T, lam)]
sig2 = [s2(counter) for counter in numpy.arange(0, T, lam)]

plt.figure()

plt.subplot(411)
plt.plot(sig1)
plt.title('Исходные сигналы')
plt.grid(True)

plt.subplot(412)
plt.plot(sig2)
plt.grid(True)

modsig1 = [modulate(s1,counter, w1) for counter in numpy.arange(0, T, lam)]
modsig2 = [modulate(s2,counter, w2) for counter in numpy.arange(0, T, lam)]


plt.subplot(413)
plt.plot(modsig1)
plt.plot([ -i for i in sig1 ], alpha=0.5, color='r')
plt.plot(sig1, alpha=0.5, color='r')
plt.title('Модулированные сигналы')
plt.grid(True)

plt.subplot(414)
plt.plot(modsig2)
plt.plot([ -i for i in sig2 ], alpha=0.5, color='r')
plt.plot(sig2, alpha=0.5, color='r')
plt.grid(True)

plt.figure()

plt.subplot(511)
plt.stem([abs(i) for i in fft(modsig1)][:100], linefmt='blue', markerfmt='none', basefmt='blue' )
plt.title('Спектры модулированных сигналов')
plt.grid(True)

plt.subplot(512)
plt.stem([abs(i) for i in fft(modsig2)][:100], linefmt='blue', markerfmt='none', basefmt='blue' )
plt.grid(True)


#modulate1 = lambda s1, s2, t, w1, w2, w3, w4: ((s1(t))*math.sin(w1*t) + (s2(t)*math.sin(w2*t)))
modulate1 = lambda s1, s2, t, w1, w2: ((s1(t) * math.sin(w1*t)) + (s2(t) * math.sin(w2*t)))
modsumsig = [modulate1(s1, s2, counter, w1, w2) for counter in numpy.arange(0, T, lam)]


plt.subplot(513)
plt.plot(modsumsig)
plt.title('Суммарный сигнал')
plt.grid(True)

plt.subplot(514)
plt.stem([abs(i) for i in fft(modsumsig)][:100], linefmt='blue', markerfmt='none', basefmt='blue' )
plt.title('Спектр суммарного сигнала')
plt.grid(True)

plt.subplot(515)
plt.stem([abs(i) for i in fft(modsig1)][:30] + [abs(i) for i in fft(modsig2)][30:100], linefmt='blue', markerfmt='none', basefmt='blue')
plt.title('Сумма спекторов')
plt.grid(True) 

plt.figure()


decompositionsig1 = codelab.fdecomposition(modsumsig, T, w1, lamw, lam)
decompositionsig2 = codelab.fdecomposition(modsumsig, T, w2, lamw, lam)

plt.subplot(411)
plt.plot(decompositionsig1)
plt.plot([ -i for i in sig1 ], alpha=0.5, color='r')
plt.plot(sig1, alpha=0.5, color='r')
plt.title('Разделенные сигналы')
plt.grid(True)

plt.subplot(412)
plt.plot(decompositionsig2)
plt.plot([ -i for i in sig2 ], alpha=0.5, color='r')
plt.plot(sig2, alpha=0.5, color='r')
plt.grid(True)

plt.subplot(413)
plt.plot(codelab.demodulate(decompositionsig1.real, lam, T), color='black')
#plt.plot([ -i for i in sig1 ], alpha=0.5, color='r')
plt.plot(sig1, alpha=0.5, color='r')
plt.title('Демодулированные сигналы')
plt.grid(True)

plt.subplot(414)
plt.plot(codelab.demodulate(decompositionsig2.real, lam, T), color='black')
#plt.plot([ -i for i in sig2 ], alpha=0.5, color='r')
plt.plot(sig2, alpha=0.5, color='r')
plt.grid(True)


plt.figure()

sumsigfunc = lambda t, lamt, s: s[math.floor(t/lamt) % 2](t)
sumsig = [sumsigfunc(counter, lamT, [s1,s2]) for counter in numpy.arange(0, T, lam)]

plt.subplot(411)
plt.plot(sumsig)
plt.title('Суммарный сигнал')
plt.grid(True)

plt.subplot(412)
plt.stem([abs(i) for i in fft(sumsig)][30:300], linefmt='blue', markerfmt='none', basefmt='blue' )
plt.title('Спектр суммарного сигнала')
plt.grid(True)

plt.subplot(413)
plt.plot(codelab.tdecomposition(sumsig,T,lamT,lam,2,0))
plt.plot(sig1, alpha=0.5, color='r')
plt.title('Модулированные сигналы')
plt.grid(True)

plt.subplot(414)
plt.plot(codelab.tdecomposition(sumsig,T,lamT,lam,2,1))
plt.plot(sig2, alpha=0.5, color='r')
plt.grid(True)

plt.figure()

sumsigfunc = lambda t, lamt, s: s[math.floor(t/lamt) % 2](t)
sumsig = [sumsigfunc(counter, lam, [s1,s2]) for counter in numpy.arange(0, T, lam)]

plt.subplot(511)
plt.plot(sumsig)
plt.title('Суммарный сигнал, без высокочастотных составляющих')
plt.grid(True)

plt.subplot(512)
plt.plot(codelab.tdecomposition(sumsig,T,lamT,lam,2,0))
plt.title('Принятые сигналы')
plt.grid(True)

plt.subplot(513)
plt.plot(codelab.tdecomposition(sumsig,T,lamT,lam,2,1))
plt.grid(True)

signal1 = codelab.tdecomposition(sumsig,T,lamT,lam,2,0)
signal2 = codelab.tdecomposition(sumsig,T,lamT,lam,2,1)

decompositionsig1 = codelab.filtr(signal1, T, 0.00000000001, lamw, lam)
decompositionsig2 = codelab.filtr(signal2, T, 0.00000000001, lamw, lam)
plt.subplot(514)
plt.plot(decompositionsig1)
#plt.plot(sig1, alpha=0.5, color='r')
plt.title('Принятые сигналы, пропущенные через фильтр низких частот')
plt.grid(True)

plt.subplot(515)
plt.plot(decompositionsig2)
#plt.plot(sig2, alpha=0.5, color='r')
plt.grid(True)

plt.show()
