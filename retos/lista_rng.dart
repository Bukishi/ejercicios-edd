import 'dart:math';
void main(List<String> args) {
  Random random= new Random();
  int numrng=random.nextInt(20)+10;
  List<int> lista=[];
  for (int i=1;i<=numrng;i++){
    lista.add(random.nextInt(10));
  }
  print("lista sin oredenar: $lista");
  lista.sort();
  print("lista ordenada: $lista");
  lista.shuffle();
  print("lista ordenada de manera aleatoria: $lista");
}