import numpy as np
import random
def Mostrar(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            print("{0:0.2f}".format(x[i][j]),end=" ")
        print("")
    print("")
A=np.zeros((3,3))
for i in range(len(A)):
    for j in range(len(A[0])):
        A[i][j]=random.randint(0,6)
print("La Matriz A:")
Mostrar(A)
Ainv=np.linalg.inv(A)
print("La Matriz A inversa:")
Mostrar(Ainv)
print("El resultado de A*A^-1:")
Mostrar(np.dot(A,Ainv))

