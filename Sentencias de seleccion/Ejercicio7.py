'''7. Escribe un programa que recoja la hora del día y devuelva un saludo, según
las siguientes reglas:
INTERVALO DE HORAS SALUDO
[7,12) Buenos días
[12, 20) Buenas tardes
En otro caso Buenas noches'''

hour=int(input("Introduzca hora del dia: "))

if hour>=7 and hour<12:
    print("Buenos dias.")
elif hour >=12 and hour<20:
    print("Buenas tardes.")
else:
    print("Buenas noches.")