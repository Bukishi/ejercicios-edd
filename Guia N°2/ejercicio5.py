class Nodo:
    def __init__(self,nom,info):
        self.nombre=nom
        self.cargo=info
        self.sub=[]
class Arbol:
    def __init__(self) -> None:
        self.head=None
        self.jerarquia=["CEO","Gerente","Desarrollador"]
    def addEmp(self,nombre,i):
        nuevoNodo=Nodo(nombre,self.jerarquia[i])# se le entrega el nombre de el empleado y un entero representando su cargo en la empresa
        if self.head is None:
            self.head=nuevoNodo
        else:
            n=self.jerarquia.index(nuevoNodo)
            if self.jerarquia.index(self.head)>n:
                aux=self.head
                self.head=nuevoNodo
                self.head.sub.append(aux)
            elif self.jerarquia.index(self.head.sub[0].cargo)>n:
                    self.head.sub[0].sub.append(nuevoNodo)
            else:
                self.head.sub.append(nuevoNodo)
    def delEmp(self,nombre):
        aux=self.head
        if aux.nombre==nombre:
            aux.sub[1].sub.append(aux.sub[0].sub)
            self.head=aux.sub[0]
        else:
            for i in aux.sub:
                if i.nombre==nombre:
                    aux2=i
            if len(aux2.sub)==0:
                i=aux.sub.index(aux2)
                aux.sub.pop(i)
            else:
                aux.sub.append(aux2.sub)
                i=aux.sub.index(aux2)
                aux.sub.pop(i)
    def impArbol(self,nodo):
        if nodo:
            print(f"nombre:{nodo.nombre}, cargo: {nodo.cargo}",end=" ")
            if len(nodo.sub)!=0:
                print("subordinados")
                for i in nodo.sub:
                    self.impArbol(i)
            else:pass
    def buscar(self,nombre,nodo):
        if nodo.nombre==nombre:
            print(f"cargo:{nodo.cargo}, subordinados: {nodo.sub}")
        else:
            for i in nodo.sub:
                self.buscar(i)
    def buscarJefe(self,nombre,nodo):
        if nombre in nodo.sub:
            print(f"jefe directo:{nodo.nombre}, cargo:{nodo.cargo}")