import numpy as np
import matplotlib.pyplot as plt
import statistics

x1 = [1,1,2,3,1,2,3,3]
x2 = [-1,0,0,1,1,2,2,0]
y = [1.6,3,1.1,1.2,3.2,3.3,1.7,0.1]

x12 = [1,1,2,3,1,2,3,3]
for i in range(0,len(x12)):
	x12[i]=x12[i]*x12[i]

x22 = [-1,0,0,1,1,2,2,0]
for i in range(0,len(x22)):
	x22[i]=x22[i]*x22[i]

x1y = [1,1,2,3,1,2,3,3]
for i in range(0,len(x1y)):
	x1y[i]=x1y[i]*y[i]

x2y = [-1,0,0,1,1,2,2,0]
for i in range(0,len(x2y)):
	x2y[i]=x2y[i]*y[i]

x1x2= [1,1,2,3,1,2,3,3]
for i in range(0,len(x1x2)):
	x1x2[i]=x1[i]*x2[i]

#obtener a0, a1, a0 GAUSS JORDAN
n = len(x1)
x1i = sum(x1)
x2i = sum(x2)
x1i2 = sum(x12)
x1ix2i = sum(x1x2)
x2i2 = sum(x22)
yi = sum(y)
x1iyi = sum(x1y)
x2iyi = sum(x2y)
yprom = statistics.mean(y)
#matrices A y B
A = np.array([[n,x1i,x2i],
              [x1i,x1i2,x1ix2i],
              [x2i,x1ix2i,x2i2]])

B = np.array([[yi],
              [x1iyi],
              [x2iyi]])

#PROCEDIMIENTO
#evitar truncamiento en operaciones
A = np.array(A,dtype=float) 

#hacer matriz aumentada
AB = np.concatenate((A,B),axis=1)
AB0 = np.copy(AB)

#pivoteo parcial por filas
tamaño = np.shape(AB)
n = tamaño[0]
m = tamaño[1]

# Para cada fila en AB
for i in range(0,n-1,1):
    # columna desde diagonal i en adelante
    columna = abs(AB[i:,i])
    max = np.argmax(columna)
    
    # dondemax no está en diagonal
    if (max !=0):
        # intercambia filas
        temporal = np.copy(AB[i,:])
        AB[i,:] = AB[max+i,:]
        AB[max+i,:] = temporal
        
AB1 = np.copy(AB)

#eliminacion hacia adelante
for i in range(0,n-1,1):
    pivote = AB[i,i]
    adelante = i + 1
    for k in range(adelante,n,1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
AB2 = np.copy(AB)

#elimina hacia atras
ultimafila = n-1
ultimacolumna = m-1
for i in range(ultimafila,0-1,-1):
    pivote = AB[i,i]
    atras = i-1 
    for k in range(atras,0-1,-1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
    # diagonal a unos
    AB[i,:] = AB[i,:]/AB[i,i]
X = np.copy(AB[:,ultimacolumna])
X = np.transpose([X])

# SALIDA
a0 = X[0]
a1 = X[1]
a2 = X[2]
print("a0 = ", a0)
print("a1 = ", a1)
print("a2 = ", a2)

yiyprom = [1.6,3,1.1,1.2,3.2,3.3,1.7,0.1]
for i in range(0,len(yiyprom)):
	yiyprom[i]=(y[i]-yprom)**2

ya = [1.6,3,1.1,1.2,3.2,3.3,1.7,0.1]
for i in range(0,len(ya)):
	ya[i]=((y[i])-(a0)-(a1*x1[i])-(a2*x2[i]))**2

st = sum(yiyprom)
sr = sum(ya)
r = (np.sqrt((st-sr)/st))*100

print("St = [",st,"]")
print("Sr = ",sr)
print("r = ",r, "%")