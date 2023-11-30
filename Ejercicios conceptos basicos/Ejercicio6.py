'''6. Escribe un programa que recoja las notas de las tres evaluaciones de un
alumno. A continuación debe calcular y mostrar la nota final, teniendo en
cuenta que la primera evaluación cuenta un 20% de la nota final, la segunda
evaluación un 35% y la tercera evaluación un 45%.'''

ev1=float(input("Nota del primer trimestre: "))
ev2=float(input("Nota del segundo trimestre: "))
ev3=float(input("Nota del tercer trimestre: "))

final=(ev1*0.2)+(ev2*0.35)+(ev3*0.45)

print("Nota final: ", round(final,2))