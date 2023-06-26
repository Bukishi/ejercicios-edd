class Cola:
    def __init__(self):
        self.cola=[]
    def empty(self):
        return len(self.cola)==0
    def add(self,x):
        self.cola.append(x)
    def pop(self):
        if self.empty():
            raise ValueError("la cola esta vacia")
        else:
            return self.cola.pop(0)
    def size(self):
        return len(self.cola)
    def show(self):
        if self.empty():
            raise ValueError("la cola esta vacia")
        else:
            for i in self.cola:
                print(i,end=", ")
class Pila:
    def __init__(self):
        self.top=None
        self.stack=[]
    def Empty(self):
        return len(self.stack)==0
    def push(self,item):
        self.top=item
        self.stack.append(item)
        return self.top
    def pop(self):
        if not self.Empty():
            self.stack.pop()
            self.top = self.stack[-1]
            return self.top
    def size(self):
        return len(self.stack)
    def __str__(self):
        return str(self.stack)
    def show(self):
        if self.Empty():
            raise ValueError("la pila esta vacia")
        else:
            for i in self.stack:
                print(i,end=", ")
class Almacen:
    def __init__(self):
        self.pila=Pila()
        self.despacho=Cola()
    def addprod(self, x):
        self.pila.push(x)
    def desp(self):
        if self.despacho.empty():
            print("la cola de despacho esta vacia")
        else:
            print(f"se entrego el producto: {self.despacho.pop}")
    def pilaADesp(self):
        if self.pila.Empty():
            print("no hay nada en la pila")
        else:
            self.despacho.add(self.pila.pop())
    def pilaVacia(self):
        if self.pila.Empty():
            print("la pila de productos esta vacia")
        else:
            print("hay productos en la pila")
    def colaVacia(self):
        if self.despacho.empty():
            print("la cola de despacho esta vacia")
        else:
            print("hay productos en la cola de despacho")
    def impRecibidos(self):
        self.pila.show()
    def impDesp(self):
        self.despacho.show()
    def totalProductos(self):
        print(f"hay {self.despacho.size()+self.pila.size()} productos en el almacen")
A=Almacen()
on=True
while on:
    print("1.- agregar productos al almacen")
    print("2.- Despachar Productos")
    print("3.- mostrar productos recibidos en el almacen")
    print("4.- mostrar productos para despacho")
    print("5.- mostrar la cantidad total de productos en el almacen")
    print("6.- mover de la pila al despacho")
    print("7.- Salir")
    x=int(input("Que desea hacer?, ingrese un numero entero para seleccionar:"))
    if x==1:
        n=input("Que ingrese el nombre del producto a añadir: ")
        A.addprod(n)
    elif x==2:
        A.desp()
    elif x==3:
        A.impRecibidos()
    elif x==4:
        A.impDesp()
    elif x==5:
        A.totalProductos()
    elif x==6:
        A.pilaADesp()
    elif x==7:
        on=False
        print("adios")