class Cliente:
    def __init__(self,numero):
        self.caja=None
        self.num=numero
        self.next=None
class ListaCircular:
    def __init__(self):
        self.cajas=(1,2,3)
        self.index=0
        self.puntero=None
        for i in range(50,0,-1):
            self.nodo=Cliente(i)
            if i==50:
                self.ultimo=self.nodo
                aux=self.ultimo
            else:
                self.nodo.next=aux
            aux=self.nodo
        self.ultimo.next=aux
        self.puntero=self.ultimo.next
    def imprimir(self):
        x=self.ultimo
        y=self.ultimo.next
        while y != x:
            print(f"{y.num}",end=", ")
            y=y.next
        print(y.num)
    def sacarNumero(self):
        self.puntero.caja=self.cajas[self.index]
        aux=self.cajas[self.index]
        self.index+=1
        if self.index>2:
            self.index=0
        self.puntero=self.puntero.next
        return aux
a=ListaCircular()
on=True
x=input("desea ingresar a un cliente?[Y/N]")
while on:
    if x == "Y":
        print(f"Le toca en la caja {a.sacarNumero}")
        x=input("desea ingresar a otro cliente?[Y/N]")
    else:
        on=False
        print("adios")