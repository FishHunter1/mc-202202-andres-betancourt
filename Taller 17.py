import numpy as np
import matplotlib.pyplot as plt

xn=np.array([1, 2, 3, 4, 5, 6])
yn=np.array([4.5 , 6 , 9 , 12 , 17 , 24])

def menu():
    print("[1] Minimo cuadrado")
    print("[2] Exponencial")

def minimo_cuadrado():
    n=len(xn)
    Sum_x=sum(xn)
    Sum_y=sum(yn)
    Sum_xx=sum(xn**2)
    Sum_xy=sum(xn*yn)

    print(Sum_x, Sum_y, Sum_xx, Sum_xy) 

    a_0=(Sum_xx*Sum_y-Sum_xy*Sum_x)/(n*Sum_xx-Sum_x**2)
    a_1=(n*Sum_xy-Sum_x*Sum_y)/(n*Sum_xx-Sum_x**2)
    print(a_0, a_1)

    x=np.linspace(7, 12, 2)
    y=a_0+a_1*x

    plt.figure(1)
    plt.scatter(xn, yn, color='r')
    plt.grid(linestyle='dotted')
    plt.plot(x, y, color='b')
    plt.title(r'$\delta ^{13}C$ vs $\delta ^{18}O$', fontsize=20)
    plt.xlabel(r'$\delta ^{13}C$', fontsize=16)
    plt.ylabel(r'$\delta ^{18}O$', fontsize=16)
    plt.xlim(7, 12)
    plt.show()

def exponencial():
    log_a = np.log(xn)
    log_b = np.log(yn)

    coefficients = np.polyfit(xn, log_b, 1)
    print(coefficients)

    c = np.exp(1.17) * np.exp(0.06*xn)
    plt.plot(xn, yn, "o")
    plt.plot(xn, c)
    plt.figure(1)
    plt.scatter(xn, yn, color='r')
    plt.grid(linestyle='dotted')
    plt.plot(xn, yn, color='b')
    plt.title(r'$\delta ^{13}C$ vs $\delta ^{18}O$', fontsize=20)
    plt.xlabel(r'$\delta ^{13}C$', fontsize=16)
    plt.ylabel(r'$\delta ^{18}O$', fontsize=16)
    plt.xlim(7, 12)
    plt.show()



menu()
option = int(input("Ingresa tu opcion: "))
 
while option != 0:
    if option == 1:
        minimo_cuadrado()
        break
    elif option == 2:
        exponencial()
        break
    else:
        print("Opcion invalida")
        break
