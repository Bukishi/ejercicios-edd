import numpy as np 
filas=int(input("ingrese la cantidad de filas: "))
columnas=int(input("ingrese la cantidad de columnas: "))
m1=np.empty((filas,columnas),int)
m2=np.empty((filas,columnas),int)
for i in range(filas):
    for j in range(columnas):
        m1[i][j]=int(input (f"ingrese un valor entero para la matriz 1 en la posicion en la fila:{i+1}, columna: {j+1}: "))
for i in range(filas):
    for j in range(columnas):
        m2[i][j]=int(input (f"ingrese un valor entero para la matriz 2 en la posicion en la fila:{i+1}, columna: {j+1}: "))
def Suma(x,y):
    m=np.add(x,y)
    return m
def Resta(x,y):
    m=np.subtract(x,y)
    return m
def MostrarMatriz(x):
    for i in range(filas):
        for j in range(columnas):
            print(x[i][j],end=" ")
        print(" ")
    print(" ")
MostrarMatriz(m1)
MostrarMatriz(m2)
MostrarMatriz(Suma(m1,m2))
MostrarMatriz(Resta(m1,m2))
