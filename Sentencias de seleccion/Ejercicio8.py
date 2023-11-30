'''8. Escribe un programa que recoja un mes del año (en número) y devuelva el
número de días que tiene el mes. En caso de indicar un mes incorrecto deberá
mostrar un mensaje de error.'''

month=int(input("Introduzca mes (numero): "))

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("Tiene 31 dias.")
    case 4 | 6 | 9 | 11:
        print("Tiene 30 dias.")
    case 2:
        print("Tiene 28 dias.")
    case _:
        print("*ERROR*")