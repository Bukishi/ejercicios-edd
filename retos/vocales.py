palabra=input("ingrese una palabra: ")
a,e,i,o,u=0,0,0,0,0
for k in palabra:
    if "a" ==k :
        a+=1
    if "e" ==k:
        e+=1
    if "i" ==k:
        i+=1
    if "o" ==k:
        o+=1
    if "u" ==k:
        u+=1
print (f"a: {a}, e: {e}, i: {i}, o: {o}, u: {u}")