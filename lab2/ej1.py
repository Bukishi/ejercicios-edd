import numpy as np 
import random
def mostrar(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            print(x[i][j],end=" ")
        print("")
    print("")
filas=columnas=random.randint(2, 5)
m1=[]
m2=[]
for i in range(filas):
    aux=[]
    for j in range(columnas):
        n=float(input(f"ingrese un numero para fila {i+1} y columna {j+1} de la matriz 1: "))
        aux.append(n)
    m1.append(aux)
for i in range(filas):
    aux=[]
    for j in range(columnas):
        n=float(input(f"ingrese un numero para fila {i+1} y columna {j+1} de la matriz 2: "))
        aux.append(n)
    m2.append(aux)
m3=[]
for i in range(filas):
    aux=[]
    for j in range(columnas):
        n=m1[i][j]-m2[i][j]
        aux.append(n)
    m3.append(aux)
f=int(input("ingrese el numero de filas: "))
c=int(input("ingrese el numero de columnas: "))
while f != len(m3[0]):
    f=int(input("Error,ingrese el numero de filas aceptable: "))
m4=[]
for i in range(f):
    aux=[]
    for j in range(c):
        n=float(input(f"ingrese un numero para fila {i+1} y columna {j+1} de la matriz 3: "))
        aux.append(n)
    m4.append(aux)
m5=np.dot(m3, m4)
A,B=m1,m2
print("Matriz A")
mostrar(A)
print("Matriz B")
mostrar(B)
AB=np.dot(A,B)
print("la matriz A*B")
mostrar(AB)
print("la matriz A^t y B^t:")
At=np.transpose(A)
print("")
Bt=np.transpose(B)
print("matriz (A*B)^t")
mostrar(np.transpose(AB))
print("matriz A^t*B^t")
mostrar(np.dot(At,Bt))