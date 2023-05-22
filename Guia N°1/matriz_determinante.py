import random
import numpy as np
matriz = []
for i in range(3):
    aux=[]
    for j in range(3):
        aux.append(random.randint(0,10))
    matriz.append(aux)
for i in range(3):
    print(matriz[i])
#print(np.linalg.det(matriz))
det=0
x=1
y=2
for i in range(3):
    ele=(-1)**(2+i)
    if x>2:
        x=0
    if y>2:
        y=0
    if (2+i)%2==0:
        punto=(matriz[1][x]*matriz[2][y])-(matriz[2][x]*matriz[1][y])
    else:
        punto=(matriz[1][y]*matriz[2][x])-(matriz[2][y]*matriz[1][x])
    det+=(punto*(ele*matriz[0][i]))
    x+=1
    y+=1
print(det)