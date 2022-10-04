import numpy as np
import matplotlib.pyplot as plt

xn=np.array([1, 2, 3, 4, 5, 6, 7, 8])
yn=np.array([7, 5, 6, 3, 4, 2.6, 2, 0.6])

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
plt.text(9, -1.5, r'$\delta ^{18}O=-6.919+0.799*\delta ^{13}C$',
    fontsize=12)
plt.show()