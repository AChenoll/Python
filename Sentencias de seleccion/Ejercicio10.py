'''10.Escribe un programa que a partir de información de un donante determine si
puede donar sangre. Las condiciones para donar son:
a. No se debe donar en ayunas.
b. Edad: Comprendida entre los 18 y 65 años.
c. Peso: Superior a 50kg.
d. Tensión arterial: dentro de límites adecuados para la extracción.
i. Tensión diastólica (baja): entre 50mm Hg y 100 mm Hg
ii. Tensión sistólica (alta): entre 90mm y 180mm Hg
e. Pulso (frecuencia cardiaca): entre 50 y 110 pulsaciones
f. Valores de hemoglobina:
i. En hombres: superior a 13,5 gramos por litro
ii. En mujeres: superior a 12,5 gramos por litro.
g. Plaquetas: más de 150.000 cc
h. Proteínas totales: más de 6 gr/dl.'''

print("Rellene este formulario para donar sangre: ")

ayunas=input("Viene usted en ayunas? (y/n): ")
if ayunas=='y': #Puede donar, siguiente paso
    edad=int(input("Introduzca su edad: "))
    if edad>=18 and edad<=65: #Puede donar, siguiente paso
        peso=int(input("Introduzca su peso(Kg): "))
        if peso>50:
            tenDia=int(input("Introduzca su tension arterial diastolica(mm Hg): "))
            if tenDia >=50 and tenDia<=100:
                tenSis=int(input("Introduzca su tension arterial sistolica(mm Hg): "))
                if tenSis>=90 and tenSis<=180:
                    pulso=int(input("Introduzca pulso: "))
                    if pulso>=50 and pulso<=110:
                        sexo=input("Es usted hombre(h) o mujer(m)?")
                        if sexo=='h':
                            hemoH=int(input("Introduzca su nivel de hemoglobina: "))


                    else:
                        print("No puede donar, su pulso debe estar entre 50 y 110 pulsaciones.")
                else:
                    print("No puede donar, tiene la tension arteriar sistolica fuera de rango.")
            else:
                print("No puede donar, tiene la tension arterial diastolica fuera de rango")
        else: 
            print("No puede donar, debe tener un peso mayor de 50kg.")
    else:
        print("No puede donar, tiene que tener una edad comprendida entre 18 y 65 anyos.")
else:
    print("No puede donar sangre en ayunas, vuelva otro dia ")
