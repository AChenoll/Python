'''6. Escribe un programa que recoja un número de filas y columnas, y muestre una
tabla con tantas filas y columnas como indicadas, numerando las celdas de
izquierda a derecha y de arriba abajo. Por ejemplo, si se introducen 2 filas y 3
columnas, se debe mostrar:
1 2 3
4 5 6
'''
row=int(input("Numero de filas: "))
col=int(input("Numero de columans: "))
cont=1

for x in range (0, row, 1):
    for y in range (0, col, 1):
        print(cont, end="\t")
        cont+=1
    else:
        print()