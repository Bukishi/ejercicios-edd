import 'dart:math';

void main() {
  List lista1 = [];
  List lista2 = [];
  List lista3 = [];
  List promedios = [];
  for (int i = 0; i < 7; i++) {
    lista1.add(Random().nextInt(70) + 30);
    lista2.add(Random().nextInt(70) + 30);
    lista3.add(Random().nextInt(70) + 30);
  }
  List listadelistas = [lista1, lista2, lista3];
  for (int i = 0; i < 3; i++) {
    int aux = 0;
    for (int j = 0; j < 7; j++) {
      int x = listadelistas[i][j];
      aux += x;
    }
    double aux2 = aux / listadelistas[i].length;
    promedios.add(aux2);
  }
  print(lista1);
  print(lista2);
  print(lista3);
  print(promedios);
}
