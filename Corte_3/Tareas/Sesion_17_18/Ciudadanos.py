'''
Crear un programa basado en POO con las siguientes características:

1. Crear una clase "Ciudadano" que incluya los campos privados Nombre, Cédula y Edad.
2. Crear los setters y getters correspondientes a los campos, verificando que el número de cedula tenga entre 8 y 10 dígitos
 y que la edad ingresada sea un número positivo mayor que cero.
Establecer un método "mostrar" que imprima la información, por ejemplo:
Nombre: Nicolás - Edad: 28 - CC: 1289384734

Establecer un método "esMayorDeEdad" que verifique si el ciudadano es o no mayor de edad.
Realice el diagrama de clases (Representación UML)
'''
#--------------CONSTRUCTOR---------------------------
class Ciudadano():
    #------------ATRIBUTOS---------------------------
    def __init__(self,nombre:str,cedula:str,edad:int): 
        self.__nombre = nombre
        self.__cedula = cedula
        self.__edad = edad

    #------------METODO-SETTERS : MODIFICA-----------------
    def setNombre(self,nombre):
        self.__nombre = nombre
    def setCedula(self,cedula):
        self.__cedula = cedula
    def setEdad(self,edad):
        self.__edad = edad

    #------------METODO-GETTER : OBTIENE--------------------
    def getNombre(self):
        return self.__nombre
    def getCedula(self):
        return self.__cedula
    def getEdad(self):
        return self.__edad
    
    #------------METODO-- MOSTRAR--------------------------- 
    def mostrar(self):
        return f'Nombre: {self.getNombre()} - Edad: {self.getEdad()} - CC: {self.getCedula()}'
    
    #---------METODO--MAYOR-DE-EDAD-------------------------
    def mayorEdad(self):
        edad = self.getEdad()
        if edad>18:
            return f'{self.getNombre()} es mayor de edad'
        else:
            return f'{self.getNombre()} es menor de edad'
    

def main():
    while 1:
        nombre = input('Nombre: ').capitalize()
        while True:
            cedula = input('Cedula: ')
            if 8<=len(cedula)<=10:
                while True:
                    edad = int(input('Edad: '))
                    if 0<edad<101:
                        break
                    else:
                        print('Ingreso una edad invalida, ingresela de nuevo por favor. ')
                break
            else:
                print('Ingreso una cedula invalida, ingresela de nuevo por favor.')
        break
    ciudadano = Ciudadano(nombre,cedula,edad)
    print(ciudadano.mostrar())
    print(ciudadano.mayorEdad())


if __name__=='__main__':
    main()
