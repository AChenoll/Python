'''4. Escribe un programa que recoja un número y muestre un triángulo. Por
ejemplo, si se ha introducido el valor 5, se debe mostrar:
*
**
***
****
*****
'''

row=int(input("Introduzca numero de filas: "))
cont=1

for r in range(0,row,1):
    for x in range (0,cont,1):
        print("*",end="")
    else:
        print()
        cont+=1