def esPalindromo(cadena):
    cadena=cadena.lower()
    cadenaSinEspacios=cadena.replace(' ','')
    cadenaReves=cadenaSinEspacios[::-1]

    if cadenaSinEspacios==cadenaReves:
        return True
    else:
        return False


cadena=input("Inserte una cadena: ")

if esPalindromo(cadena):
    print("'", cadena, "' es palindromo")
else:
    print("'", cadena, "' no es palindromo")

