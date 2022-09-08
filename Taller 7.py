import math
from math import factorial

es = 0.5 *  10**-8 * 100
ea = 100
num = 0.85
potencia = 1
valor = 1
iteraciones = 1
e = 1
while ea >= es:
  op = (pow(num,potencia)/factorial(valor))
  e += op
  e2 = 1/e
  iteraciones += 1
  ea = abs(((e2-ea)/e2)*100)
  valor += 1
  potencia += 1
  #iteracion 2
  op = (pow(num,potencia)/factorial(valor))
  e += op
  e3 = 1/e
  iteraciones += 1
  ea = abs(((e3-e2)/e2)*100)
  valor += 1
  potencia += 1
else:
  print("El valor estimado es de: ", e2)
  print("El error aproximado porcentual es de: ", ea, "%")
  print("El numero de iteraciones fue: ", iteraciones)
  
  
#Segundo punto
es4 = 0.5 *  10**-8 * 100
ea4 = 100

num4 = 0.85
potencia4 = 1
valor4 = 1
iteraciones4 = 1
e4 = 1
while ea4 >= es4:
  op4 = (pow(num4,potencia4)/factorial(valor4))
  e4 -= op4
  iteraciones4 += 1
  ea4 = abs(((e4-ea4)/e4)*100)
  valor4 += 1
  potencia4 += 1
  #iteracion 2
  op6 = (pow(num4,potencia4)/factorial(valor4))
  e6 = e4 + op6
  iteraciones4 += 1
  ea4 = abs(((e6-e4)/e6)*100)
  valor4 += 1
  potencia4 += 1
else:
  print("valor estimado: ", e4)
  print("error aproximado porcentual: ", ea4, "%")
  print("iteraciones: ", iteraciones4)