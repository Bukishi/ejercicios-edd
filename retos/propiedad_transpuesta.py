def MostrarMatriz(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            print(x[i][j],end=" ")
        print(" ")
    print(" ")
def Transpose(x):
    m=[]
    for i in range(len(x)):
        auxl=[]
        aux=0
        for j in range(len(x[0])):
            aux=x[j][i]
            auxl.append(aux)
            aux=0
        m.append(auxl)
    return m
def Suma(x,y):
    m=[]
    for i in range(len(x)):
        auxl=[]
        aux=0
        for j in range(len(x[0])):
            aux=x[i][j]+y[i][j]
            auxl.append(aux)
            aux=0
        m.append(auxl)
    return m
A=[[1,4,2],[2,1,5],[4,3,1]]
B=[[3,6,8],[2,6,8],[4,8,2]]
At=[]
Bt=[]
At=Transpose(A)
Bt=Transpose(B)
print("la matriz A:")
MostrarMatriz(A)
print("la matriz At: ")
MostrarMatriz(At)
print("la matriz At+Bt:")
MostrarMatriz(Suma(At,Bt))
S=Suma(A, B)
print("la matriz A+B: ")
MostrarMatriz(S)
print("la matriz (A+B)t: ")
MostrarMatriz(Transpose(S))