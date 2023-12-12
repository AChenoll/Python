# Ejercicio 1
class Persona():
    def __init__(self, nombre='Periquito', apellidos='De Los Palotes', dni='11111111A', edad=33):
        self.nombre=nombre
        self.apellidos=apellidos
        self.dni=dni
        self.edad=edad

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter 
    def nombre(self, newNombre):
        self.nombre=newNombre
    
    @property
    def apellidos(self):
        return self.apellidos
    
    @apellidos.setter
    def apellidos(self, newApellidos):
        self.apellidos=newApellidos
        
    @property
    def dni(self):
        return self.dni

    @dni.setter
    def dni(self, newDni):
        self.dni=newDni

    
    @property
    def edad(self):
        return self.edad

    @edad.setter
    def edad(self, newEdad):
        if newEdad > 0:
            self.edad=newEdad
        else:
            print('La edad tiene que ser un numero positivo mayor que 0')

    # Metodo para mostrar los datos de una persona
    def mostrar(self):
        return 'Nombre: ', self.nombre,', apellidos: ', self.apellidos, ', edad: ', self.edad, ', DNI: ', self.dni
    
    # Metodo que indica si una persona es mayor de edad
    def mayorDeEdad(self):
        if self.edad >= 18:
            return self.nombre, ' es mayor de edad.'
        else:
            return self.nombre, ' no es mayor de edad.'

# Ejercicio 2
class Cuenta():
    def __init__(self, titular, cantidad=0):
        self.titular=titular
        self.cantidad=cantidad

    @property
    def titular(self):
        return self.titular
    
    @titular.setter
    def titular(self, newTitular):
        self.titular=newTitular

    @property
    def cantidad(self):
        return self.cantidad
    
    @cantidad.setter
    def __cantidad(self,newCantidad):
        self.cantidad=newCantidad
        
    # Metodo para ingresar dinero en la cuenta
    def ingresar(self, ingCantidad):
        if ingCantidad > 0:
            Cuenta.__cantidad(ingCantidad)
        else:
            print('La cantidad a ingresar debe ser positiva.')

    # Metodo para retirar dinero de la cuenta
    def retirar(self, retCantidad):
        if retCantidad > 0:
            Cuenta.__cantidad(-retCantidad)
        else:
            print('La cantidad a retirar debe ser positivo.')

    # Metodo para mostrar todos los datos de la cuenta
    def mostrar(self):
        print ('Titular: ', self.titular, ', saldo: ', self.cantidad)

# Ejercicio 3
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion=bonificacion

    def mostrar(self):
        super().mostrar()
        print(', bonificacion: ', self.bonificacion, '%')