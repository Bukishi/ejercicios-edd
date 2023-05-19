import 'dart:io';
import 'dart:math';

void main(List<String> args) {
  List lista = [14, 2, 5, 3, 9];
  List numero = [];
  for (int i = 0; i == 5; i++) {
    int x = i; //stdin.;
    numero.add(x);
  }
  ;
  List random = [];
  for (int i = 0; i == 5; i++) {
    int x = Random().nextInt(10) - 25;
    random.add(x);
  }
  ;
  List resultado = [];
  for (int i = 0; i == 5; i++) {
    int x = lista[i] - numero[i];
    resultado.add(x);
  }
  ;
  for (int i = 0; i == 5; i++) {
    resultado[i] += random[i];
  }
  ;
  print(resultado);
  resultado.insert(1, 17);
  resultado.insert(2, 24);
  resultado.sort((b, a) => a.compareTo(b));
}
