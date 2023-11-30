'''4. Escribe un programa que recoja dividendo y divisor, y realice su división
siempre que el divisor sea distinto de cero.'''

dividendo=int(input("Introduzca el dividendo: "))
divisor=int(input("Introduzca el divisor: "))

if divisor != 0:
    print("Resultado: ", round(dividendo/divisor,2))
else:
    print("No se puede dividir por cero.")