import matplotlib.pyplot as plt
import math
import numpy
import random
import CodeLab
import Nois
import DifferenceBoolList
import GetPackage



N = 128
k = 8
i = range(0,N)
x = []
for index in i:
    x.append(math.floor(random.uniform(0, 2)))

code = CodeLab.code(x,k)

plt.figure()

plt.subplot(511)
plt.step([i for i in range(N)], x, where='post')
plt.title('Исходный случайный сигнал')
plt.grid(True)


plt.subplot(512)
plt.step([i for i in range(len(code))], code, where='post')
plt.title('Сформированный сигнал')
plt.grid(True)

#Сформированый сигнал с помехами
codeNois = Nois.nois(code)

dif = DifferenceBoolList.difference(code, codeNois)
plt.subplot(513)
plt.step([i for i in range(len(dif))], dif, where='post')
plt.title('Разница между переданным и принятым сигналом')
plt.grid(True)

dif = DifferenceBoolList.difference(GetPackage.getInformationPackage(code), 
                                    GetPackage.getInformationPackage(codeNois))
plt.subplot(514)
plt.step([i for i in range(len(dif))], dif, where='post')
plt.title('Разница между информационными посылками')
plt.grid(True)

dif = DifferenceBoolList.difference(GetPackage.getVerificationPackage(code), 
                                    GetPackage.getVerificationPackage(codeNois))
plt.subplot(515)
plt.step([i for i in range(len(dif))], dif, where='post')
plt.title('Разница между проверочными посылками')
plt.grid(True)

#plt.show()
#___________________________________________________________________________________________________

plt.figure()

codeReceived = CodeLab.code(GetPackage.getInformationPackage(codeNois), k)

dif = DifferenceBoolList.differenceRec(GetPackage.getVerificationPackage(codeNois), 
                                    GetPackage.getVerificationPackage(codeReceived))

plt.subplot(511)
plt.step([i for i in range(len(dif))], dif, where='post')
plt.title('Разность между контрольной и проверочной посылкой')
plt.grid(True)

decode = CodeLab.deCode(GetPackage.getInformationPackage(codeNois),
                        dif,
                        k)

plt.subplot(512)
plt.step([i for i in range(len(decode))], decode, where='post')
plt.title('Восстановленная информационная посылка')
plt.grid(True)

dif = DifferenceBoolList.difference(decode, x)
plt.subplot(513)
plt.step([i for i in range(len(dif))], dif, where='post')
plt.title('Разница между исходной и восстановленной информационной посылкой')
plt.grid(True)


plt.show()