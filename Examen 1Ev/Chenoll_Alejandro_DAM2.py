""" 
INSTRUCCIONES

1. El examen consiste en completar este menú de opciones. Se trata de utilizar
   un diccionario para almacenar las cervezas consumidas por los alumnos de una clase. 
   La clave del diccionario es el nombre del alumno (en mayúsculas), el valor es
   una lista con las cervezas consumidas en cada quedada de la clase.
   
2. En cada función que debes realizar se añade un comentario donde se 
   explica lo que tienes que hacer. Para ayudarte a encontrarlo,
   comienza con el texto TO-DO.

3. Puedes añadir cuantas funciones estimes oportunas para hacer el ejercicio. 

4. En el ejercicio se piden por teclado consumiciones de cerveza, que se representan como
   números enteros. Cuando se pida un número por teclado el programa debe repetir
   la operación hasta que sea un valor correcto (es decir, un número entero mayor o igual que cero) 

¡SUERTE!
"""

""" 
TO-DO: Completa esta función devolviendo tu nombre completo y grupo 
"""
def nombreAlumno():
    return "alejandro chenoll gonzalez - dam2"

def menu():
    print("EJERCICIO DE", nombreAlumno().upper())
    print("(PATROCINADO POR CERVEZAS VICTORIA)")
    print("a) Borrar todos los datos de la clase (1 PUNTO)")
    print("b) Añadir consumiciones de un alumno (1.5 PUNTOS)")
    print("c) Listar consumiciones de la clase (2.5 PUNTOS)")
    print("d) Buscar al más bebedor de la clase (3.5 PUNTOS)")
    print("e) Eliminar alumno (1.5 PUNTOS)")
    print("\nz) Salir")

""" 
TO-DO: esta función borra todos los datos del diccionario. 
Antes de borrar debe mostrar el texto: 
"ADVERTENCIA. Se perderán todos los datos. ¿Desea continuar (S/N)?: "
Para confirmar el borrado el usuario debe introducir S (tanto minúscula como mayúscula).
Cualquier otra respuesta se considera que no confirma el borrado. 
Si se confirma la operación, se borra el diccionario.
"""
def borrarClase():
    borrar=input("ADVERTENCIA. Se perderán todos los datos. ¿Desea continuar (S/N)?: ").upper()
    if borrar == 'S':
        clase.clear()
        print('Se han borrado todos los datos.')
    elif borrar =='N':
        print("Operacion cancelada.")
    elif borrar != 'S' and borrar!='N':
        print("Opcion incorrecta. Operacion cancelada.")

""" 
TO-DO: esta función debe pedir por teclado el nombre del alumno y las cervezas que se 
ha tomado (número entero igual o mayor que cero).
Si el alumno ya existe en el diccionario: añade la consumición a su lista de consumiciones.
    Ejemplo: se añade ALUMNO1:3 y existe en el dicionario ALUMNO1:[2,0]. El resultado debe 
    ser ALUMNO1:[2,0,3] 
Si el alumno no existe en el diccionario: crea una nueva entrada para el nuevo alumno.
    Ejemplo: se añade ALUMNO1:3 y no existe en el dicionario. El resultado debe 
    ser ALUMNO1:[3]
"""
def nuevaConsumicion():
    alumno=input('Nombre del alumno: ').upper()
    if alumno not in clase:
        print(alumno, 'no existe en la clase, se va a crear una entrada nueva.')
        cervezas=-1
        while cervezas < 0:
            check=input('Inserte numero de cervezas consumidas: ').isnumeric() # Hago esto para comprobar que se inserta un numero
            if check:    
                cervezas=int(check)
                if cervezas >= 0:
                    lilstaCervezas=[]
                    lilstaCervezas.append(cervezas) # Hago esto para insertarle como dato al alumno una lista, no un numero
                    clase[alumno]=lilstaCervezas
                    print('Alumno creado con exito.')
            else:
                print('Error, la cantidad de cervezas no puede ser menor que cero.')

    else:
        cervezas=-1
        while cervezas<0:
            check=input('Inserte numero de cervezas consumidas: ').isnumeric()
            if check:    
                cervezas=int(check)
                if cervezas >= 0:
                    clase[alumno].append(cervezas)
                    print('Lista de cervezas del alumno actualizada.')
            else:
                print('Error, debe insertar un numero positivo.')
        

""" 
TO-DO: esta función debe listar las consumiciones de la clase y la media  
en orden alfabético.

Si el dicionario está vacío: debe mostrar el texto "No hay datos"
Si el diccionario tiene datos: debe mostrar la información con el siguiente formato
Ejemplo: diccionario con esta información
    "ALUMNO1": [3, 3, 2],
    "ALUMNO2": [1, 2, 0, 1],
    "ALUMNO3": [4, 5]
El listado se mostrará así:

Alumno: ALUMNO1 Consumiciones: [3, 3, 2] Media: 2.66
Alumno: ALUMNO2 Consumiciones: [1, 2, 0, 1] Media: 1.0
Alumno: ALUMNO3 Consumiciones: [4, 5] Media: 4.5

NOTA: no es necesario dar formato a la media, que salgan los decimales
que sean necesarios.

PISTA: dada una lista l, la función sum(l) devuelve la suma de todos sus elementos.
"""
def listarClase():
    if len(clase)!=0:    
        for c  in clase.keys():
            print("Alumno:", c, "Consumiciones:", clase[c], "Media:", (sum(clase[c])/len(clase[c])))
    else:
        print("No se encuentran datos.")

""" 
TO-DO: esta función debe buscar el alumno de la clase con más consumiciones
en un día y en total.
Si el dicionario está vacío: debe mostrar el texto "No hay datos"
Si el diccionario tiene datos: debe buscar al alumno con más consumiciones en un día y 
en total, y mostrar sus nombres (pueden ser el mismo o distintos).
En caso de que haya más de un alumno con el máximo de cervezas se muestra el primer nombre encontrado.
 
Ejemplo: diccionario con esta información
    "ALUMNO1": [3, 3, 2],
    "ALUMNO2": [1, 2, 0, 1],
    "ALUMNO3": [1, 5]

Deberá mostrar este mensaje:
El mayor bebedor en un día es ALUMNO3 que se bebió 5 cervezas.
El mayor bebedor en total es ALUMNO1 que ha consumido ya 8 cervezas.

PISTA: dada una lista l, la función sum(l) devuelve la suma de todos sus elementos.
PISTA: dada una lista l, la función max(l) devuelve el valor máximo.
"""
def buscarMayorBebedorClase():
    if len(clase)!=0:  
        maxBebedor=0
        nombreMaxBebedor=''
        maxTotalBebedor=0
        nombreMaxTotalBebedor=''  
        for c  in clase.keys():
            if max(clase[c])>maxBebedor:
                maxBebedor=max(clase[c])
                nombreMaxBebedor=c
        
            if sum(clase[c])>maxTotalBebedor:
                maxTotalBebedor=sum(clase[c])
                nombreMaxTotalBebedor=c
    
        print('El mayor bebedor en un día es', nombreMaxBebedor, 'que se bebió ', maxBebedor, ' cervezas.')
        print('El mayor bebedor en total es', nombreMaxTotalBebedor, 'que ha consumido ya ', maxTotalBebedor, ' cervezas.')
    else:
        print("No se encuentran datos.")

"""
TO-DO: esta función borra un alumno de la clase.
Debe pedir por teclado el nombre del alumno.
Si el alumno ya existe en el diccionario: antes de borrar debe confirmar la operación 
(S/N, pudiendo insertar tanto minúscula como mayúscula). Si se confirma la operación, se elimina
el alumno del diccionario.
Si el alumno no existe en el diccionario: debe mostrarse el mensaje "El alumno <nombre> no existe".
"""
def eliminarAlumno():
    borrar=input("Indique el alumno a borrar: ").upper()
    if borrar in clase:
        confirmar=input('Esta seguro que quiere borrar el alumno? (S/N): ').upper()
        if confirmar == 'S':
            del clase[borrar]
            print("El alumno ha sido borrado.")
        else:
            print("Operacion cancelada.")
    else:
        print("El alumno no existe. Operacion cancelada.")

    
def leerOpcion():
    opcion = input("\nIntroduzca la opción que desea realizar: ").upper()
    return opcion

def ejecutarOpcion(opcion):
    seguir = True

    match opcion:
        case "A":
            borrarClase()
        case "B":
            nuevaConsumicion()
        case "C":
            listarClase()
        case "D":
            buscarMayorBebedorClase()
        case "E":
            eliminarAlumno()
        case "Z":   # Fin de programa
            seguir = False
        case _:
            print("Opción errónea")
    
    # Sólo se va a poner la espera de teclado si no hay que finalizar
    if seguir:
        x = input("\n\nPulse una tecla para continuar...")
    
    return seguir

""" 
Comienzo del programa
"""

# Variable donde se guardan los datos iniciales de prueba del programa
clase = {
    "ALUMNO1": [3, 3, 2],
    "ALUMNO2": [1, 2, 0, 1],
    "ALUMNO3": [4, 5]
}

seguir = True
while seguir:
    menu()
    seguir = ejecutarOpcion(leerOpcion())
else:
    print("Que pases un buen día")
     
    
