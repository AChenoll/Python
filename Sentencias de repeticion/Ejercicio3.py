'''3. Escribe un programa que recoja números por teclado hasta que se introduzca
el valor cero. A continuación, debe mostrar el número de valores introducidos,
el valor mínimo introducido, el máximo, la suma de todos ellos y su media
aritmética (todos los cálculos sin contar el cero)'''

num=-1
cont=0
min=47000000
max=0
sum=0

while num!=0:
    num=int(input("Introduzca un numero positivo (0 para salir): "))
    if num!=0:
        cont+=1

    if num<min and num!=0:
        min=num

    if num>max:
        max=num

    sum+=num

else:
    print("Numero de valores introducidos: ", cont)
    print("Minimo: ", min)
    print("Maximo: ", max)
    print("Suma: ", sum)
    print("Media: ", (sum/cont))