import 'dart:math';

void main() {
  List lista1 = [4, 3, 2, 2, 1];
  List lista2 = [-3, 2, 8, 0, 1];
  List multi = [];
  for (int i = 0; i < 5; i++) {
    multi.add(lista1[i] * lista2[i]);
  }
  List rand = [];
  for (int i = 0; i < 5; i++) {
    rand.add(Random().nextInt(4) - 5);
  }
  print(multi);
  multi = multi + rand;
  multi.sort((b, a) => a.compareTo(b));
  print(multi);
  print(rand);
}
