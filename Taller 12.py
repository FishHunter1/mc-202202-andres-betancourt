from math import factorial
from math import e
xi=0.55
xi_1=0.555
h=0.005
valor_ant = 0
operacion = 0
for i in range(16):
    if i % 2 ==0:
        operacion+= (e**(-xi)/factorial(i))*h**i
    else:
        operacion -= (e**(-xi)/factorial(i)*h**i)

    ea=abs((operacion-valor_ant)/operacion)*100
    valor_ant=operacion
    print("orden",i)
    print("Resultado",operacion)
    print("error",ea,"%")
    