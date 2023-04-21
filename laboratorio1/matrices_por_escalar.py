import random
matriz1=[]
columna=int(input("ingrese la cantidad de columnas: "))
fila=int(input("ingrese la cantidad de filas: "))
for i in range(fila):
    aux=[]
    for j in range(columna):
        aux.append(random.randint(0, 10))
    matriz1.append(aux)
print(matriz1)
escalar=int(input("ingrese un escalar: "))
for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        matriz1[i][j]*=escalar
for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        print(matriz1[i][j],end='\n')