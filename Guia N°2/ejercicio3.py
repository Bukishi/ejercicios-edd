class Nodo:
    def __init__(self,info):
        self.informacion=info
        self.siguiente=None
class ListaEnlazada:
    def __init__(self):
        self.primero=None
    def empty(self):
        return self.primero is None
    def añadirFin(self,dato):
        nuevo_nodo=Nodo(dato)
        if self.Empty():
            self.primero=nuevo_nodo
            return self.primero
        temporal=self.primero
        while temporal.siguiente:
            temporal=temporal.siguiente
        temporal.siguiente = nuevo_nodo
        return self.primero
    def añadirIni(self,dato):
        nuevo_nodo=Nodo(dato)
        nuevo_nodo.siguiente=self.primero
        return self.primero
    def imprime(nodo):
        while nodo:
            print(f"{nodo.informacion}")
    def imprimeLista(self):
        if self.primero is None:
            print("lista vacia")
        else:
            aux=self.primero
            while aux.siguiente:
                print(f"{aux.informacion}",end=" , ")
                aux=aux.siguiente
            print(f"{aux.informacion}")
    def eliminar(self,busqueda):
        if self.primero is None:
            return
        if self.primero.informacion==busqueda:
            self.primero=self.primero.siguiente
            return self.primero
        aux=self.primero
        while aux.siguiente:
            if aux.siguiente.informacion==busqueda:
                if aux.siguiente.siguiente:
                    aux.siguiente= aux.siguiente.siguiente
                else:
                    aux.siguiente=None
                    return aux
            aux=aux.siguiente
        return aux
    def media(self):
        if self.primero is None:
            print("lista vacia")
        else:
            aux=self.primero
            c=0
            promedio=0
            while aux.siguiente:
                promedio+=aux.informacion
                c+=1
            return promedio/c
    def desvEstandar(self):
        if self.primero is None:
            print("lista vacia")
        else:
            aux=self.primero
            med=self.media()
            c=0
            suma=0
            while aux.siguiente:
                suma+=(aux.informacion-med)**2
                c+=1
            var=suma/c
            return var**0.5
L=ListaEnlazada()
on=True
while on:
    print("1.- agregar datos a la lista")
    print("2.- Calcular la media de los datos")
    print("3.- Calcular la desviacion estandar")
    print("4.- imprimir la lista")
    print("5.- Verificar si la lista esta vacia")
    print("6.- Salir")
    x=int(input("Que desea hacer?, ingrese un numero entero para seleccionar:"))
    if x==1:
        n=float(input("Que ingrese el numero a añadir: "))
        L.añadirFin(n)
    elif x==2:
        if L.empty:
            print("lista vacia")
        else:
            print(f"la media es:{L.media}")
    elif x==3:
        if L.empty:
            print("lista vacia")
        else:
            print(f"la desviacion estandar es:{L.desvEstandar}")
    elif x==4:
        if L.empty:
            print("lista vacia")
        else:
            L.imprime()
    elif x==5:
        if L.empty:
            print("lista vacia")
        else:
            print("hay datos en la lista")
    elif x==6:
        on=False
        print("adios")