lista=[]

cadena=-1

while cadena!="":
    cadena=input("Inserte un texto (cadena vacia para salir): ")

    if cadena != "":
        lista.append(cadena)

print(lista)

lista.sort()

print(lista)

lista.sort(reverse=True)

print(lista)
