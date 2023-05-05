def MostrarMatriz(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            print(x[i][j],end=" ")
        print(" ")
    print(" ")
matriz1=[[1,4,2],[2,1,5],[4,3,1]]
matriz2=[[3,6,8],[2,6,8],[4,8,2]]
matriz=[]
for i in range(len(matriz1)):
    auxl=[]
    for j in range(len(matriz2[0])):
        aux=0
        for k in range(len(matriz1[0])):
            aux+=matriz1[i][k]*matriz2[k][j]
        auxl.append(aux)
    matriz.append(auxl)
MostrarMatriz(matriz1)
MostrarMatriz(matriz2)
MostrarMatriz(matriz)
