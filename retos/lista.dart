import 'dart:io';
void main(List<String> args) {
  print("ingrese la cantidad de elementos en la lista: ");
  int cuenta= int.parse(stdin.readLineSync()!);
  while(cuenta<1){
    print("Error, ingrese un mayor a 1: ");
    cuenta= int.parse(stdin.readLineSync()!);
    }
  List<int> numeros = [];
  for (int i = 1; i <= cuenta; i++) {
    print("ingrese: ");
    int e= int.parse(stdin.readLineSync()!);
    numeros.add(e);
    }
  print(numeros);
  int aux=0;
  for (int i = 0; i < numeros.length; i++) {
    aux+=numeros[i];
  }
  print(aux);
}