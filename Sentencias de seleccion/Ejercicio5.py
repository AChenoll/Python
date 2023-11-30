'''5. Escribe un programa que calcule el precio de entrada a un museo a partir de
la edad del visitante, teniendo en cuenta que:
a. Menores de 5 años entran gratis.
b. Niños entre 5 años y 18 (sin llegar a los 18) pagan 3€.
c. Mayores de edad hasta los 65 (sin llegar a los 65) pagan 6€.
d. Jubilados entran gratis.'''

age=int(input("Introduzca edad: "))

if age<0 or age>120:
    print("Edad incorrecta. ")
elif age>=5 and age<18:
    print("Entrada 3€ ")
elif age>=18 and age<65:
    print("Entrada 6€. ")
elif age>=65 and age<120:
    print("Entrada gratis. ")
