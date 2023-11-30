'''6. Escribe un programa que muestre la nota final de un alumno a partir de su
calificación numérica (valor decimal), teniendo en cuenta que:
a. Nota menor de 5 es suspenso.
b. Nota entre 5 y 6 (sin llegar) es suficiente.
c. Nota entre 6 y 7 (sin llegar) es bien.
d. Nota entre 7 y 9 (sin llegar) es notable.
e. Nota entre 9 y 10 (sin llegar) es sobresaliente.
f. Nota igual a 10 es matrícula de honor.
g. Cualquier otro valor numérico fuera de este rango es un error.'''

nota=float(input("Introduzca nota: "))

if nota < 5:
    print("Suspenso.")
elif nota >=5 and nota < 6:
    print("Suficiente.")
elif nota >=6 and nota< 7:
    print("Bien.")
elif nota >=7 and nota< 9:
    print("Notable.")
elif nota >=9 and nota< 10:
    print("Sobresaliente.")
elif nota == 10:
    print("Matricula de honor. ")