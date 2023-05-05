import 'dart:io';
import "dart:math";
void main(List<String> args) {
  print("ingrese la cantidad de elementos en la lista: ");
  int cuenta= int.parse(stdin.readLineSync()!);
  while(cuenta<1){
    print("Error, ingrese un mayor a 1: ");
    cuenta= int.parse(stdin.readLineSync()!);
    }
  List<int> numeros = [];
  for (int i = 1; i <= cuenta; i++) {
    print("ingrese numero entero positivo: ");
    int n= int.parse(stdin.readLineSync()!);
    while(n<1){
      print("Error, ingrese un mayor a 0: ");
      n= int.parse(stdin.readLineSync()!);
    }
    numeros.add(n);
    }
  print("lista: $numeros");
  numeros.sort();
  print("lista ordenada de forma ascendente: $numeros");
  numeros.sort((b,a)=>a.compareTo(b));
  print("lista ordenada de forma descendente: $numeros");
    int m=100000;
    int M=0;
  for (int i =0;i<numeros.length;i++){
    m=min(m,numeros[i]);
    M=max(M,numeros[i]);
  }
  print("el numero mayor de la lista es $M y el menor $m");
}