'''3. Escribe un programa que lea tres números y que muestre los números mayor
y menor.'''

num1=int(input("Escriba un numero: "))
num2=int(input("Escriba otro numero: "))
num3=int(input("Escriba otro numero: "))

menor= num1 if num1 < num2 else num2
menor= menor if menor<num3 else num3

print("El numero menor es: ", menor)