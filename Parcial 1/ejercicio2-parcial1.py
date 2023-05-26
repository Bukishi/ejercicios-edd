import random
import numpy as np

def mostrarmatriz(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            print(x[i][j],end=" ")
        print("")
    print("")

def genmatriz(a,b):
    m=[]
    for i in range(3):
        aux=[]
        for j in range(3):
            n=random.randint(a,b)
            aux.append(n)
        m.append(aux)
    return m

def genmatriz2(a,b):
    m=[]
    for i in range(3):
        aux=[]
        for j in range(3):
            n=random.randint(a,b)-11
            aux.append(n)
        m.append(aux)
    return m
    
A=genmatriz(1, 10)
print("Matriz A: ")
mostrarmatriz(A)
B=genmatriz(11, 30)
print("Matriz B: ")
mostrarmatriz(B)
C=genmatriz2(1, 10)
print("Matriz C: ")
mostrarmatriz(C)
print("Matriz (A+B)*C: ")
aux=np.add(A,B)
mostrarmatriz(np.dot(aux,C))
print("Matriz A*C + B*C: ")
aux=np.dot(A,C)
mostrarmatriz(np.add(aux,np.dot(B,C)))

