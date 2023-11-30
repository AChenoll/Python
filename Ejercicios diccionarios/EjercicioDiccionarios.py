# Creo un diccionario con ejemplos de contactos y numeros de telefono
tlf=dict(
    Alex=697842601,
    Carmen=619100145,
    Jesus=666570076,
    Antonio=608220125,
    Isidro=658573415
)

# Funcion para elegir la opcion del menu
def seleccion():
    mostrarMenu()
    opcion=str(input("Seleccione una opcion: ")).lower() # Uso la funcion .lower() para pasar la letra que meta por teclado a minuscula 
    return opcion

# Cuerpo del menu
def mostrarMenu():
    print("\nMENÚ DE OPCIONES")
    print("a - Listado de teléfonos, usando el orden por defecto.") 
    print("b - Listado de teléfonos por orden alfabético.")
    print("c - Añadir un nuevo contacto")
    print("d - Modificar el teléfono de un contacto.")
    print("e - Buscar un número de teléfono")
    print("f - Eliminar un contacto.")
    print("g - Borrar el listín telefónico.")
    print("h - Salir\n")

# Metodo que muestra la lista en el orden por defecto
def defaultList():
    if len(tlf)!=0:    
        for c  in tlf.keys():
            print(c, "-", tlf[c])
    else:
        print("No tiene contactos en su agenda.")

# Metodo que muestra la lista en orden alfabético
def alphabeticList():
    if len(tlf)!=0:     
        phoneList=[]
        
        for c in tlf.keys():
            phoneList.append(c)
        
        phoneList.sort()

        for c in phoneList:
            print(c, "-", tlf[c])
    else:
        print("No tiene contactos en su agenda.")

# Metodo que inserta un nuevo contacto en la agenda, si existe, se pregunta si se quiere actualizar el contacto
def newContact():
    newName=input("Inserte nombre del nuevo contacto: ").capitalize()
    if newName not in tlf:
        newTlf=int(input("Inserte numero del nuevo contacto: "))
        tlf[newName]=newTlf
        print("Contacto añadido con exito.")
    else:
        check=input("El usuario que quiere añadir ya existe. ¿Quiere actualizar su informacion?(s/n): ").lower()
        if check == "s":
            updateTlf=int(input("Inserte nuevo numero de telefono: "))
            tlf[newName]=updateTlf
            print("Contacto añadido con exito.")
        else:
            print("Operacion cancelada.")

# Metodo que edita el numero de telefono de un contacto
def editContact():
    contact=input("Indique el contacto que quiere editar: ").capitalize()
    if contact in tlf:
        updateTlf=int(input("Inserte el nuevo numero de telefono: "))
        tlf[contact]=updateTlf
        print("Contacto editado con exito.")
    else:
        check=input("El contacto no existe. ¿Quiere crear nuevo contacto?(s/n): ").lower()
        if check == "s":
            newTlf=int(input("Inserte nuevo numero de telefono: "))
            tlf[contact]=newTlf
            print("Contacto añadido con exito.")
        else:
            print("Operacion cancelada.")

# Metodo para buscar un contacto por el numero de telefono
def search():
    contact=int(input("Indique el numero de telefono a consultar: "))
    if contact in tlf.values():
        key_list = list(tlf.keys())
        val_list = list(tlf.values())
        position = val_list.index(contact)
        print(key_list[position]," - ", contact)
    else:
        print("El contacto no existe.")

# Metodo para borrar un contacto de la agenda
def deleteContact():
    contact=input("Indique el contacto a eliminar: ").capitalize()
    if contact in tlf:
        del tlf[contact]
        print("Contacto eliminado con exito.")
    else:
        print("El contacto no existe.")

# Metodo para borrar todos los contactos de la agenda
def deleteList():
    check=input("¿Esta seguro de que quiere eliminar la lista de contactos?(s/n)").lower()
    if check == "s":
        tlf.clear()
        print("Todos los contactos han sido eliminados.")
    else:
        print("Operacion cancelada.")

# Llamo a la funcion del menu dentro de un bucle while para que se repita hasta que el usuario marque la opcion de salida
opcion="z"
opcion.lower()
while opcion!="h":
    opcion=seleccion()
    match opcion:
        case "a":
            defaultList()
        case "b":
            alphabeticList()
        case "c":
            newContact()
        case "d":
            editContact()
        case "e":
            search()
        case "f":
            deleteContact()
        case "g":
            deleteList()
        case "h":
            print("¡¡Hasta luego!!")
        case _:
            print("La opcion elegida no es correcta")
