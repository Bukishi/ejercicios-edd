import random
def Mostrar(x):
        for i in range(len(x)):
            for j in range(len(x[0])):
                print("{0:0.2f}".format(x[i][j]),end=" ")
            print("")
        print("")

def añade(x):
    m=x
    for i in range(len(x)):
        for j in range(len(x[0])):
            m[i].append(1 if i==j else 0)
    return m

def determinante(m):
    indices = list(range(len(m)))
    det=0
     
    if len(m) == 2 and len(m[0]) == 2:
        val = m[0][0] * m[1][1] - m[1][0] * m[0][1]
        return val
 
    for y in indices: 
        aux = m 
        aux = aux[1:]
 
        for i in range(len(aux)): 
            aux[i] = aux[i][0:y] + aux[i][y+1:] 
 
        signo = (-1) ** (y % 2) 
        subdet = determinante(aux)
        det += signo * m[0][y] * subdet 
    return  det

def inversa(x):
    m=añade(x)
    for y in range(len(m)-1):
        if m[y][y]==0:
            for i in range(y+1,len(m)):
                 if m[i][y]!=0:
                    for j in range(y,len(m[0])):
                         m[y][j]+=m[i][j]
                    break
            if m[y][y]==0:return None
        for i in range(y+1,len(m)):
            r=m[i][y]/m[y][y]
            for j in range(y,len(m[0])):
                m[i][j]-=m[y][j]*r
    for i in range(len(m)):
        for j in range(i+1,len(m)):
            if m[j][j]!=0:
                r=m[i][j]/m[j][j]
                for ja in  range(j,len(m)*2):
                    m[i][ja]-=m[j][ja]*r
    for i in range(len(m)):
        r=m[i][i]
        if m[i][i] !=0:
            for j in range(len(m[0])):
                m[i][j]/=r
    for i in range(len(m)):
       m[i]=m[i][len(x):]
    return m

tamaño=random.randint(3,5)
matriz=[]
for i in range(tamaño):
    aux=[]
    for i in range(tamaño):
        aux.append(random.randint(0,5))
    matriz.append(aux)
Mostrar(matriz)
print(determinante(matriz))
if determinante(matriz)==0:
        print("no existe una matriz inversa")
else:
    Mostrar(inversa(matriz))
