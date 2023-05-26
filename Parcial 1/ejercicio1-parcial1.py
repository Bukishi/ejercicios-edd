import numpy as np 
import random

def mostrarmatriz(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            print((x[i][j]),end=" ")
        print("")
    print("")

def genmatriz():
    m=[]
    for i in range(4):
        aux=[]
        for j in range(4):
            n=random.randint(0, 10)
            aux.append(n)
        m.append(aux)
    return m

def mult3(x):
    r2=np.dot(x, x)
    r3=np.dot(r2,x)
    return r3

def inv(x):
    a=np.linalg.det(x)
    if a==0:
        print("no existe inversa")
        return x
    else:
        i=np.linalg.inv(x)
        return i

A=genmatriz()
B=genmatriz()
C=genmatriz()

print("Matriz A:")
mostrarmatriz(A)
print("Matriz B:")
mostrarmatriz(B)
print("Matriz C:")
mostrarmatriz(C)
print("Matriz (A³ * B⁻¹ * C) + (A³)⁻¹")
a3=mult3(A)
#mostrarmatriz(a3)
#mostrarmatriz(inv(B))
aux1=np.dot(a3,inv(B))
resultado=np.dot(aux1, C)
resultado=np.add(resultado,inv(a3))
mostrarmatriz(resultado)