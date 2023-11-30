
import math
import random

# Funcion para elegir la opcion del menu
def seleccion():
    mostrarMenu()
    opcion=str(input("Seleccione una opcion: ")).lower() #uso la funcion .lower() para pasar la letra que meta por teclado a minuscula 
    return opcion

# Cuerpo del menu
def mostrarMenu():
    print("\nMENÚ DE OPCIONES")
    print("a - Mostrar un rombo.") 
    print("b - Adivinar un número.")
    print("c - Resolver una ecuación de segundo grado.")
    print("d - Tabla de números.")
    print("e - Cálculo del número factorial de un número.")
    print("f - Cálculo de un número de la sucesión de Fibonacci.")
    print("g - Tabla de multiplicar.")
    print("h - Salir\n")

# Funcion que dado el ancho imprime por pantalla un rombo
def rombo():
    base=int(input("Introduzca ancho de base (impar): "))

    if base%2!=0:
        for i in range(-base + 1, base, 2):
            print(" " * abs(i // 2) + "*" * (base - abs(i)))
                        
    else:
        print("El numero de filas no es impar. ")
        rombo()

# Funcion para adivinar un numero entre 1 y 100
def adivinar():
    print("Adivine un numero entre 1 y 100")
    numAd=random.randint(1,100)
    num=-1
    while num!=numAd:
        num=int(input("Introduzca numero: "))
        if num<numAd:
            print("Has fallado, el numero es mayor que ", num)
        elif num>numAd:
            print("Has fallado, el numero es menor que ", num)
        else:
            print("¡¡Felicidades, has acertado el numero!!")

# Ecuacion que devuelve (si existen) las soluciones a una ecuacion de segundo grado
def ecuacion():
    print("Vamos a resolver una ecuacion de segundo grado. (ax^2+bx+c=0)")
    print("Introduzca los coeficientes:")
    a=int(input("a: "))
    b=int(input("b: "))
    c=int(input("c: "))

    raiz =  b * b - 4 * a * c

    if raiz < 0: # comprobamos si no existen soluciones reales
        print(f'La ecuación no tiene soluciones reales.')
    else:
        raiz = math.sqrt(raiz)                               # calculamos la raíz
        x_1 = (-b + raiz) / (2 * a)                     # calculamos una primera solución
        if raiz != 0:                                   # comprobamos si hay otra solución
            x_2 = (-b - raiz) / (2 * a)                 # calculamos la segunda solución
            print(f'Las soluciones son {x_1} y {x_2}.') # mostramos las dos soluciones
        else:
            print(f'La única solución es x = {x_1}') # mostramos la única solución

# Fucnion que dado un numero de filas y columnas devuelve una tabla de numeros aleatorios
def tablaNumeros():
    row=int(input("Numero de filas: "))
    col=int(input("Numero de columans: "))

    for x in range (0, row, 1):
        for y in range (0, col, 1):
            print(random.randint(0,99), end="\t")
        else:
            print()

# Funcion que calcula el factorial de un numero
def factorial():
    num=-1
    while num<0:
        num=int(input("Introduzca un numero para calcular su factorial: (Positivo)"))
    
    return math.factorial(num)

# Funcion que imprime por pantalla los numeros de la sucesion de Fibonacci
def fibonacci():
    n=int(input("Indique la posicion a mostrar de la secuencia de Fibonacci: "))
    primero=0
    segundo=1
    sum=0
    cont=0
    print("Posicion ", n, " de la Secuencia de Fibonacci: " ,end="")
    # El contador no puede ser mayor que n.
    while(cont<=n):    
        cont+=1
        primero=segundo
        segundo=sum
        sum=primero+segundo	

    print(sum)

# Funcion que imprime la tabla de multiplicar de un numero
def tablaMultiplicar():
    num=int(input("Dime un numero del 1 al 10 para mostrar su tabla de multiplicar: "))
    if num in range(1,10):
        for x in range(1,10):
            print(x, " * ", num, " = ", x*num)
    else:
        print("Fuera de rango.")
        tablaMultiplicar()

# Llamo a la funcion del menu dentro de un bucle while para que se repita hasta que el usuario marque la opcion de salida
opcion="z"
while opcion!="h":
    opcion=seleccion()
    print(opcion)
    match opcion:
        case "a":
            rombo()
        case "b":
            adivinar()
        case "c":
            ecuacion()
        case "d":
            tablaNumeros()
        case "e":
            factorial()
        case "f":
            fibonacci()
        case "g":
            tablaMultiplicar()
        case "h":
            print("¡¡Hasta luego!!")
        case _:
            print("La opcion elegida no es correcta")
