import numpy as np

# INGRESO
A = np.array([[3,2,2],
              [3,1,-3],
              [1,0,-2]], dtype=float)

B = np.array([[1,2,0,4],
              [2,0,-1,-2],
              [1,1,-1,0],
              [0,4,1,0]])

# PROCEDIMIENTO
casicero = 1e-15 # Considerar como 0

def inversa(A):
    # matriz identidad
    tamano = np.shape(A)
    n = tamano[0]
    identidad = np.identity(n)

    # Matriz aumentada

    AB = np.concatenate((A,identidad),axis=1)
    AB0 = np.copy(AB)

    # Pivoteo parcial por filas
    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]

    # Para cada fila en AB
    for i in range(0,n-1,1):
        # columna desde diagonal i en adelante
        columna = abs(AB[i:,i])
        dondemax = np.argmax(columna)
        
        # dondemax no está en diagonal
        if (dondemax !=0):
            # intercambia filas
            temporal = np.copy(AB[i,:])
            AB[i,:] = AB[dondemax+i,:]
            AB[dondemax+i,:] = temporal
    AB1 = np.copy(AB)

    # eliminacion hacia adelante
    for i in range(0,n-1,1):
        pivote = AB[i,i]
        adelante = i+1
        for k in range(adelante,n,1):
            factor = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor
    AB2 = np.copy(AB)

    # elimina hacia atras
    ultfila = n-1
    ultcolumna = m-1
    for i in range(ultfila,0-1,-1):
        pivote = AB[i,i]
        atras = i-1 
        for k in range(atras,0-1,-1):
            factor = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor
        # diagonal a unos
        AB[i,:] = AB[i,:]/AB[i,i]

    inversa = np.copy(AB[:,n:])
    return inversa



print('Inversa de A: ')
print(inversa(A))

print('Inversa de B: ')
print(inversa(B))
