class Cancion:
    def __init__(self,titulo, autor):
        self.titulo = titulo
        self.artista = autor
        self.anterior=None
        self.siguiente=None
class ListaReproduccion:
    def __init__(self):
        self.primero=None
        self.ultimo=None
    def empty(self):
        return self.primero is None
    def agregarFin(self, dato):
        newnode=Cancion(dato)
        if self.empty():
            self.primero=newnode
            self.ultimo=newnode
        else:
            newnode.anterior=self.ultimo
            self.ultimo.siguiente=newnode
            self.ultimo=newnode
    def agregarIni(self,dato):
        newnode=Cancion(dato)
        if self.empty():
            self.primero=newnode
            self.ultimo=newnode
        else:
            newnode.siguiente=self.primero
            self.primero.anterior=newnode
            self.primero=newnode
    def imprimeLista(self):
        actual=self.primero
        while actual:
            print(f"cancion: {actual.titulo} , artista: {actual.artista}")
            actual=actual.siguiente
    def obtenerCabecera(self):
        return self.primero.titulo if self.primero else None
    def obtenerCola(self):
        return self.ultimo.titulo if self.ultimo else None
    def existe(self, busqueda):
        actual=self.primero
        while actual:
            if actual.titulo == busqueda or actual.artista == busqueda:
                return True
            actual=actual.siguiente
        return False
    
    def eliminar(self,busqueda):
        actual=self.primero
        while actual:
            if actual.titulo == busqueda or actual.artista == busqueda:
                if actual.anterior:
                    actual.anterior.siguiente =actual.siguiente
                else:
                    self.primero=actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior=actual.anterior
                else:
                    self.ultimo=actual.anterior
                break
            actual=actual.siguiente
