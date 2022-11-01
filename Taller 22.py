import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

xi = np.array([0, 1, 2, 3, 4])
fi = np.array([0.5, 0.1, 1, 2.1,2.4])

n = len(xi)
x = sym.Symbol('x')
polinomio = 0
divisorL = np.zeros(n, dtype = float)
for i in range(0,n,1):
    
    numerador = 1
    denominador = 1
    for j  in range(0,n,1):
        if (j!=i):
            numerador = numerador*(x-xi[j])
            denominador = denominador*(xi[i]-xi[j])
    terminoLi = numerador/denominador

    polinomio = polinomio + terminoLi*fi[i]
    divisorL[i] = denominador

polisimple = polinomio.expand()

px = sym.lambdify(x,polisimple)

muestras = 101
a = np.min(xi)
b = np.max(xi)
pxi = np.linspace(a,b,muestras)
pfi = px(pxi)

# SALIDA
print(f'Valores de fi:      {fi}')
print(f'Divisores en L(i): {divisorL}\n')
print('Polinomio de Lagrange, expresiones')
print(f'{polinomio}\n')

print('Polinomio de Lagrange: ')
print(f'{polisimple}\n')

# Gráfica
plt.plot(xi,fi,'o', label = 'Puntos')
plt.plot(pxi,pfi, label = 'Polinomio')
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title('Interpolación Lagrange')
plt.show()