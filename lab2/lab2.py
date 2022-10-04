from turtle import color
import matplotlib.pyplot as plt
import math
import numpy
import PhaseManipulation
import FrequencyModulation
import PhaseDemodulator
import FrequencyDemodulator
import random
from scipy.fft import fft


#Входные данные

#Наш варик !!!
data = [0, 1, 1, 1, 1, 1, 0, 1]
Pd = 0.39
Fd = 0.37

#Пример
# data = [0, 1, 0, 1, 1, 1, 0, 1]
# Pd = 0.3
# Fd = 0.35

dataLng = len(data)
N = 2**7
fsin = 10**3
Wd = 10**3
Td = math.pi/2
K = N * dataLng
k = numpy.arange(0, K)
Tsign = dataLng / K
C = Tsign / fsin
A = 1
t = numpy.arange(0, Tsign - C, C)

noliki = [-1] * 128
adinichki = [1] * 128
final = []
for l in data:
    if l == 0:
        final.extend(noliki)
    else:
        final.extend(adinichki)

ok = []
for i in k:
    ok.append(A * math.sin(fsin*math.pi*i*C))

s = PhaseManipulation.phase(data,A,fsin,k,C,N)

plt.figure()

plt.subplot(411)
plt.plot(ok, 'r--')
plt.plot(s)
plt.plot(final, alpha=0.5)

plt.title('Фазовая манипуляция')
plt.grid(True)

plt.subplot(412)
s = fft(s)
plt.plot(abs(s)[:100])
plt.title('Спектр фазовой манипуляции')
plt.grid(True)

#____________________________________________________________
s = FrequencyModulation.frequency(data, A, fsin, k, C, N, Wd)

plt.subplot(413)
plt.plot(ok, 'r--')
plt.plot(s)
plt.plot(final, alpha=0.5)
plt.title('Частотная манипуляция')
plt.grid(True)

plt.subplot(414)
s = fft(s)
plt.plot(abs(s)[:100])
plt.title('Спектр частотной манипуляции')
plt.grid(True)
plt.show()

#____________________________________________________________
plt.figure('2')

s = PhaseManipulation.phase(data,A,fsin,k,C,N)

L1 = [A * math.sin(fsin*math.pi*i*C) for i in k]
L2 = [A * math.cos(fsin*math.pi*i*C) for i in k]

sb1 = PhaseDemodulator.pd(s,L1,K,N,Pd)
sb2 = PhaseDemodulator.pd(s,L2,K,N,Pd)

plt.subplot(511)
plt.step([i for i in range(dataLng)], sb1[1], where='post')
plt.title('Демодулированный сигнал')
plt.grid(True)

plt.subplot(512)
plt.step([i for i in range(dataLng)], sb2[1], where='post')
plt.title('Демодулированный сигнал')
plt.grid(True)


ss = [i + random.uniform(0,0.5) - random.uniform(0,0.5) for i in s]
sb1 = PhaseDemodulator.pd(ss,L1,K,N,Pd)
sb2 = PhaseDemodulator.pd(ss,L2,K,N,Pd)

s = PhaseManipulation.phase(data,A,fsin,k,C,N)
plt.subplot(513)
plt.plot(ok, 'r--')
plt.plot(s)
plt.plot(ss)
plt.plot(final, alpha=0.5)

plt.title('Фазовая манипуляция с помехами')
plt.grid(True)

plt.subplot(514)
plt.step([i for i in range(dataLng)], sb1[1], where='post')
plt.title('Демодулированный сигнал с помехами')
plt.grid(True)

plt.subplot(515)
plt.step([i for i in range(dataLng)], sb2[1], where='post')
plt.title('Демодулированный сигнал с помехами')
plt.grid(True)


plt.show()
#____________________________________________________________

s = FrequencyModulation.frequency(data, A, fsin, k, C, N, Wd)

sb = FrequencyDemodulator.fd(s, K, N, Fd)
plt.figure('3')
plt.subplot(411)
plt.plot(s)
plt.plot(final, alpha=0.5)
plt.title('Частотная манипуляция')
plt.grid(True)

plt.subplot(412)
plt.step([i for i in range(dataLng)], sb[1], where='post')
plt.title('Демодулированный сигнал')
plt.grid(True)

ss = [i + random.uniform(0,0.5) - random.uniform(0,0.5) for i in s]

plt.figure('3')
plt.subplot(413)
plt.plot(ss)
plt.plot(final, alpha=0.5)
plt.title('Частотная манипуляция с помехами')
plt.grid(True)

sb = FrequencyDemodulator.fd(ss,K,N,Fd)
plt.subplot(414)
plt.step([i for i in range(dataLng)], sb[1], where='post')
plt.title('Демодулированный сигнал с помехами')
plt.grid(True)




plt.show()