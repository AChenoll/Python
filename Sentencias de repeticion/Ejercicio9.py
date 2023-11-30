'''9. Escribe un programa que recoja un número impar. Debe asegurarse de que
sea impar, en caso de no serlo debe descartarlo y pedirlo de nuevo. Una vez
tenga el número impar debe mostrar una pirámide de asteriscos cuya base es
igual al número introducido. Por ejemplo, si se introduce el valor 7 se debe
mostrar:
   *
  ***
 *****
******* <- base de la pirámide (7 asteriscos)'''

base=int(input("Introduzca ancho de base (impar): "))
cont=1
contBlank=base

if base%2!=0:
    for r in range(0,base,2):
        for y in range(0,contBlank,2):
            print(" ", end="")
        else:    
            contBlank=contBlank-2

        for x in range (0,cont,1):
            print("*",end="")
        
        print()
        cont+=2
        

        
else:
    print("El numero de filas no es impar. ")