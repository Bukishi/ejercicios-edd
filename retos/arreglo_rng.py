from array import array
import random
r=random.randint(10, 30)
v=array("i",[])
for i in range(r):
    v.append(random.randint(0, 50))
print(v)
lugar=int(input("indique el numero de el elemento que quiere: "))
while lugar <1 or lugar > r:
    print("ERROR!!, indice fuera del arreglo!")
    lugar=int(input("indique el numero de el elemento que quiere: "))
print(v[lugar-1])