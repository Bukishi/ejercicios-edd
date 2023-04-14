nombre=[]
rut=[]
for i in range(5):
    a=input("nombre: ")
    b=input("rut: ")
    nombre.append(a)
    rut.append(b)
print(nombre,rut)
nombre.sort()
rut.sort()
print(nombre,rut)