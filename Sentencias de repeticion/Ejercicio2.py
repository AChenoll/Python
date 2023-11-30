'''2. Escribe un programa que recoja un número y calcule su factorial.'''

num=int(input("Introduzca un numero: "))
fact=1

for i in range(num,1,-1):
    fact=fact*i
else:
    print(fact)