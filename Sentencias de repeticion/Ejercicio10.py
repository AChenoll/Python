'''10.Escribe un programa que recoja un número y muestre un triángulo formado por
secuencias decrecientes de números impares. Por ejemplo, si se introduce el
5 se debe mostrar:
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1 '''

num=int(input("Introduzca un numero: "))
cont=1
text=""

for i in range(1, num+2+1,2):
    text+=str(i)
    print(text[::-1])
