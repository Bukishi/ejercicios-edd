import random
matriz1=[]
columna=int(input("ingrese la cantidad de columnas: "))
fila=int(input("ingrese la cantidad de filas: "))
for i in range(fila):
    aux=[]
    for j in range(columna):
        aux.append(random.randint(0, 5))
    matriz1.append(aux)
print(matriz1)

matriz2=[]
columna=int(input("ingrese la cantidad de columnas: "))
fila=int(input("ingrese la cantidad de filas: "))
for i in range(fila):
    aux=[]
    for j in range(columna):
        aux.append(random.randint(0, 5))
    matriz2.append(aux)
print(matriz2)

for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        matriz1[i][j]+=matriz2[i][j]
for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        print(matriz1[i][j],end='\n')
matriz3=[]
columna=int(input("ingrese la cantidad de columnas: "))
fila=int(input("ingrese la cantidad de filas: "))
for i in range(fila):
    aux=[]
    for j in range(columna):
        aux.append(random.randint(0, 5))
    matriz3.append(aux)

for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        matriz1[i][j]-=matriz3[i][j]
for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        print(matriz1[i][j],end='\n')
