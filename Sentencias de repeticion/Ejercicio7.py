'''7. Escribe un programa que recoja una cadena de texto por teclado y una letra a
buscar. Luego debe buscar dicha letra por la cadena y al finalizar debe indicar
el número de veces que se repite la letra en el texto.'''

cad=input("Introduzca cadena de caracteres: ").lower()

let=input("Introduzca letra a buscar: ").lower()

#Cambio la cadena y el caracter a lowercase para que cuente tanto mayusculas como minusculas

count=0

for x in cad:
    if x==let:
        count+=1
else:
    print("Numero de veces del caracter '", let, "': ", count)

