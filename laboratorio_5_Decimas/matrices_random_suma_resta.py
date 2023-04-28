def MostrarMatriz(x):
    for i in range(fila):
        for j in range(columna):
            print(x[i][j],end=" ")
        print(" ")
    print(" ")
def Matriz(x):
    for i in range(fila):
        aux=[]
        for j in range(columna):
            aux.append(random.randint(0, 5))
        x.append(aux)
    return x
def Resta(x,y):
    m=[]
    m=Matriz(m)
    for i in range(fila):
        for j in range(columna):
            m[i][j]=x[i][j]-y[i][j]
    return m
def Suma(x,y):
    m=[]
    m=Matriz(m)
    for i in range(fila):
        for j in range(columna):
            m[i][j]=x[i][j]+y[i][j]
    return m
import random
m1=[]
m2=[]
columna=int(input("ingrese la cantidad de columnas: "))
fila=int(input("ingrese la cantidad de filas: "))
m1=Matriz(m1)
m2=Matriz(m2)
MostrarMatriz(m1)
MostrarMatriz(m2)
MostrarMatriz(Suma(m1,m2))
MostrarMatriz(Resta(m1,m2))