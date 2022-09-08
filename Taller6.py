import math
n=float(input("Escriba un numero en Radianes \n"))
es=(0.5*pow(10,-8))*100
interacion=1
pot=2
val=1
signo=-1

while n > es:
    if signo==-1:
        operacion=round((valor+pow(n,pot)) / math.factorial(pot),8)
        val=float(operacion)
        print(f'Interacion # {interacion}')
        interacion +=1
        pot +=2
        signo *=-1
    else:
        operacion=round((valor-pow(n,pot)) / math.factorial(pot),8)
        val=float(operacion)
        print(f"Interacion # {interacion}")
        interacion +=1
        pot +=2
        signo *=-1
    print(f'El valor del coseno es:{valor}')
