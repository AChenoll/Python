'''5. Escribe un programa que recoja un número por teclado y muestre los primeros
cuadrados hasta llegar al número introducido. Por ejemplo, si se ha introducido
el valor 5, se debe mostrar:
1 4 9 16 25'''

num=int(input("Introduzca un numero: "))

for i in range (1, num+1, 1):
    print(i*i, end="\t")