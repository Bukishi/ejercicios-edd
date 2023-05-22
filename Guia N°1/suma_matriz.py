import random
def Mostrar(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            print((x[i][j]),end=" ")
        print("")
    print("")
def sumaFila(x):
    m=None
    print("la suma de las filas es: ",end=" ")
    for i in range(len(x)):
        aux=0
        for j in range(len(x[0])):
            aux+=x[i][j]
        print(aux,end="  ")
        if m==None or aux < m:
            m=aux
    print("")
    return print(f"y la suma de las filas mas altas es: {m}")

def sumaColu(x):
    M=None
    print("la suma de las columnas es: ",end=" ")
    for i in range(len(x[0])):
        aux=0
        for j in range(len(x)):
            aux+=x[j][i]
        print(aux,end="  ")
        if M==None or aux > M:
            M=aux
    print("")
    return print(f"y la suma de las columnas mas altas es: {M}")
M=[]
for i in range(5):
    aux=[]
    for j in range(5):
        aux.append(random.randint(0,10))
    M.append(aux)
Mostrar(M)
sumaColu(M)
sumaFila(M)