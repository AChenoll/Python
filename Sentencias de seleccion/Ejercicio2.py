'''2. Escribe un programa que recoja un número por teclado y muestre el día de la
semana que es (1 = Lunes, 2 = Martes…). En caso de introducir un número
incorrecto, mostrará el mensaje “Día de la semana incorrecto”.'''

day=int(input("Introduzca el dia de la semana (numero): "))

match day:
    case 1:
        print("Lunes")
    case 2:
        print("Martes.")
    case 3:
        print("Miercoles.")
    case 4:
        print("Jueves.")
    case 5:
        print("Viernes.")
    case 6:
        print("Sabado.")
    case 7:
        print("Domingo.")
    case _:
        print("Error")