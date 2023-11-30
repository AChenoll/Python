def esPalindromo(cadena):
    cadenaSinEspacios=cadena.replace(' ','')
    cadenaReves=cadenaSinEspacios[::-1]

    if cadenaSinEspacios==cadenaReves:
        return True
    else:
        return False

def esPalindromoIgnoreCase(cadena):
    cadena=cadena.lower()
    cadenaSinEspacios=cadena.replace(' ','')
    cadenaReves=cadenaSinEspacios[::-1]

    if cadenaSinEspacios==cadenaReves:
        return True
    else:
        return False
    


cadena=input("Inserte un texto: ")

opcion=" "
fin=False
while opcion !="s" or opcion!="n" and fin==False:
    opcion=input("Desea tener en cuenta mayousculas y minusculas? (s/n)")
    opcion=opcion.lower()
    match opcion:
        case "s":
            if esPalindromo(cadena):
                print("'", cadena, "' es palindromo")
            else:
                print("'", cadena, "' no es palindromo")
            fin=True

        case "n":    
            if esPalindromoIgnoreCase(cadena):
                print("'", cadena, "' es palindromo")
            else:
                print("'", cadena, "' no es palindromo")
            fin=True
        
        case _:
            print("Opcion incorrecta")

