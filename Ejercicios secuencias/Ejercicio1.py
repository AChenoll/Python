lista=[]

numero=-1

while numero!=0:
    numero=int(input("Inserte un numero (0 para salir): "))

    if numero != 0:
        lista.append(numero)

print(lista)

lista.sort()

print(lista)

lista.sort(reverse=True)

print(lista)
