import matplotlib.pyplot as plt
import math
import aim
import shim
import numpy
from scipy.fft import fft

t = []
i = 0
while i <= 4:
    t.append(i)
    i = i + 0.001

y = []
for i in t:
    y.append((1 - math.sin(i))/2)

sp = lambda t: (1 - math.sin(t))/2
s = aim.aim(
    Tc=4,
    delta=0.001,
    T=1 / 5,
    sp=sp,
    tn=1 / 12,
)
plt.figure()
plt.subplot(411)
plt.plot(numpy.arange(0, 4, 4 / len(s)), s)
plt.plot(t, y)
plt.title('График входного сигнала и АИМ сигнала')
plt.grid(True)
s = aim.aim(
    Tc=4,
    delta=0.001,
    T=1 / 5,
    sp=sp,
    tn=1 / 12,
)

plt.subplot(412)
s = fft(s)
plt.plot(abs(s)[:500])
plt.title('Спектр АИМ сигнала')
plt.grid(True)

plt.subplot(413)
s = shim.shim(
    Tc=4,
    delta=0.001,
    T=1 / 5,
    sp=sp,
    A=1,
    MAX=1,
)
plt.plot(numpy.arange(0, 4, 4 / len(s)), s)
plt.plot(t, y)
plt.title('График входного сигнала и ШИМ сигнала')
plt.grid(True)

plt.subplot(414)
s = shim.shim(
    Tc=4,
    delta=0.001,
    T=1 / 5,
    sp=sp,
    A=1,
    MAX=1,
)
s = fft(s)
plt.plot(abs(s)[:500])
plt.title('Спектр ШИМ сигнала')
plt.grid(True)

plt.show()
