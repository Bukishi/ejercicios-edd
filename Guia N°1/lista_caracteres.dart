void main() {
  List lista = ["a", 2, 0, "b", 8, "c"];
  for (int i = 0; i < lista.length; i++) {
    if (lista[i].runtimeType == int) {
      print(lista[i]);
    }
  }
}
