import numpy as np
import os
from matplotlib import pylab, mlab, pyplot
from pylab import *
from numpy import *
from math import e

columnax = [1, 3, 5, 7, 9, 11, 13, 15]
columnay = [2.1, 3.2, 3.8, 4, 4.2, 4.4, 4.5, 4.7]


def minCuad():
    xlen = len(columnax)
    SumaY = 0
    SumaLogX = 0
    SumaLogXY = 0
    SumaLogX2 = 0

    for i in range(xlen):
        SumaLogX += columnax[i]

    for i in range(xlen):
        SumaY += columnay[i]

    product = [x * y for x, y in zip(columnax, columnay)]
    for i in range(len(product)):
        SumaLogXY += product[i]

    listx2 = []
    for x in columnax:
        listx2.append(x * x)

    for i in range(len(listx2)):
        SumaLogX2 += listx2[i]

    promy = SumaY / xlen
    promx = SumaLogX / xlen
    promxy = SumaLogXY / xlen
    promx2 = SumaLogX2 / xlen

    a1 = ((xlen * SumaLogXY) - (SumaLogX * SumaY)) / (xlen * SumaLogX2 - (SumaLogX) ** 2)
    print(f"El resultado de a1 es: {a1}")
    a0 = promy - (a1 * promx)
    print(f"El resultado de a0 es: {a0}")
    print(f"y = {a0} + {a1}x + e")


def Exp():
    xlen = len(columnax)
    LogY = np.log(columnay)
    SumaLogY = 0
    SumaLogX = 0
    SumaLogXY = 0
    SumaLogX2 = 0

    for i in range(xlen):
        SumaLogX += columnax[i]

    for i in range(xlen):
        SumaLogY += LogY[i]

    product = [x * y for x, y in zip(columnax, LogY)]
    for i in range(len(product)):
        SumaLogXY += product[i]

    listx2 = []
    for x in columnax:
        listx2.append(x * x)

    for i in range(len(listx2)):
        SumaLogX2 += listx2[i]

    promy = SumaLogY / xlen
    promx = SumaLogX / xlen
    promxy = SumaLogXY / xlen
    promx2 = SumaLogX2 / xlen

    a1 = ((xlen * SumaLogXY) - (SumaLogX * SumaLogY)) / (xlen * SumaLogX2 - (SumaLogX) ** 2)
    a0 = promy - (a1 * promx)
    α = e ** a0
    β = a1
    print(f"El resultado de α es: {α}")
    print(f"El resultado de β es: {β}")
    print(f"y = {α} * e^{β}x")


def Pot():
    xlen = len(columnax)
    LogX = np.log10(columnax)
    LogY = np.log10(columnay)
    SumaLogY = 0
    SumaLogX = 0
    SumaLogXY = 0
    SumaLogX2 = 0

    for i in range(xlen):
        SumaLogX += LogX[i]

    for i in range(xlen):
        SumaLogY += LogY[i]

    product = [x * y for x, y in zip(LogX, LogY)]
    for i in range(len(product)):
        SumaLogXY += product[i]

    listx2 = []
    for x in LogX:
        listx2.append(x * x)

    for i in range(len(listx2)):
        SumaLogX2 += listx2[i]

    promy = SumaLogY / xlen
    promx = SumaLogX / xlen
    promxy = SumaLogXY / xlen
    promx2 = SumaLogX2 / xlen

    a1 = ((xlen * SumaLogXY) - (SumaLogX * SumaLogY)) / (xlen * SumaLogX2 - (SumaLogX) ** 2)
    a0 = promy - (a1 * promx)
    α = 10 ** a0
    β = a1
    print(f"El resultado de α es: {α}")
    print(f"El resultado de β es: {β}")
    print(f"y = {α} * x^{β}")


def RazCre():
    xlen = len(columnax)
    ly = []
    lx = []
    SumaY = 0
    SumaX = 0
    SumaXY = 0
    SumaX2 = 0

    for i in range(xlen):
        lx.append(1 / columnax[i])

    for i in range(xlen):
        ly.append(1 / columnay[i])

    for i in range(xlen):
        SumaX += lx[i]

    for i in range(xlen):
        SumaY += ly[i]

    product = [x * y for x, y in zip(lx, ly)]
    for i in range(len(product)):
        SumaXY += product[i]

    listx2 = []
    for x in lx:
        listx2.append(x * x)

    for i in range(len(listx2)):
        SumaX2 += listx2[i]

    promy = SumaY / xlen
    promx = SumaX / xlen
    promxy = SumaXY / xlen
    promx2 = SumaX2 / xlen

    a1 = ((xlen * SumaXY) - (SumaX * SumaY)) / (xlen * SumaX2 - (SumaX) ** 2)
    a0 = promy - (a1 * promx)
    α = 1 / a0
    β = a1 / a0
    print(f"El resultado de α es: {α}")
    print(f"El resultado de β es: {β}")
    print(f"y = {α} * x/{β}+x")


op = int(input(
    "Escoja que programa desea utilizar: 1. Mínimos cuadrados; 2. Modelo Exponencial; 3. Ecuaciones de potencias; 4. Razones de crecimiento \n"))
if op == 1:
    minCuad()
elif op == 2:
    Exp()
elif op == 3:
    Pot()
elif op == 4:
    RazCre()
else:
    print("Ninguna opción es válida")


def f1(x):
    y = 2.5910714285714307 + (0.1589285714285712 * x)
    return y


def f2(x):
    y = 2.5892225487648797 * (e ** (0.04662267660419332 * x))
    return y


def f3(x):
    y = 2.2280241567544885 * (x ** 0.28823634828855454)
    return y


def f4(x):
    y = (4.862880988485819 * x) / (1.3399237848748946 + x)
    return y


x = arange(1, 17, 2)

p1, p2, p3, p4 = plot(x, f1(x), x, f2(x), x, f3(x), f4(x))

legend(('Regresión lineal', 'Regresión exponencial', 'Ecuación de potencias', 'Razón de cambio'),
        prop={'size': 10}, loc='lower right')

xlabel('X')
ylabel('Y')
title('La función de mejor ajuste es la ecuación de potencias')

pyplot.plot(1, 2.1, marker="o", color="blue")
pyplot.plot(3, 3.2, marker="o", color="blue")
pyplot.plot(5, 3.8, marker="o", color="blue")
pyplot.plot(7, 4, marker="o", color="blue")
pyplot.plot(9, 4.2, marker="o", color="blue")
pyplot.plot(11, 4.4, marker="o", color="blue")
pyplot.plot(13, 4.5, marker="o", color="blue")
pyplot.plot(15, 4.7, marker="o", color="blue")

show()