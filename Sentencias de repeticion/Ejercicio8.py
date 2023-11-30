'''8. Escribe un programa que recoja un número y calcule si es primo'''

num=int(input("Introduzca un numero: "))

primo=True
cont=2

while primo==True and cont<num:
    if (num%cont)==0:
        primo=False
    else:
        cont+=1
else:
    if primo==True:
        print("El numero es primo.")
    else:
        print("El numero no es primo.")