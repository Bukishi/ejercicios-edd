import "dart:io";
import "dart:math";

void main(List<String> args) {
  List primera = [];
  List segunda = [];
  for (int i = 0; i < 10; i++) {
    primera.add(Random().nextInt(10) + 10);
    segunda.add(Random().nextInt(10) + 10);
  }
  List tercera = [];
  for (int i = 1; i < 6; i++) {
    print("ingrese termino $i: ");
    int n = int.parse(stdin.readLineSync()!);
    tercera.add(n);
  }
  print("Primera lista: $primera");
  print("Segunda lista: $segunda");
  print("Tercera lista: $tercera");
  List lista = [];
  lista = primera + segunda + tercera;
  print("Todas las listas concatenadas:");
  print(lista);
  int largo = lista.length;
  //print(largo);
  num aux = 0;
  for (int i = 0; i < largo; i++) {
    aux += lista[i];
  }
  aux /= largo;
  print("promedio de la lista: $aux");
  lista.sort((a, b) => a.compareTo(b));
  print("La lista ordenada:");
  print(lista);
}
