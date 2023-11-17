'''
Continúe el ejercicio de la tarea anterior con las siguientes características:

Cree tres clases heredadas de la clase "Ciudadano", basadas en tres profesiones, que incluyan mínimo 2 campos propios cada una.
Cree por lo menos un método único para cada clase heredada, que tenga relación con cada una de las profesiones seleccionadas.
En una de las tres clases heredadas, sobrecargue un método
'''

#--------------CONSTRUCTOR----------------------------------
class Ciudadano():
    #------------ATRIBUTOS---------------------------
    def __init__(self,nombre:str,cedula:str,edad:int,profesion:str): 
        self.__nombre = nombre
        self.__cedula = cedula
        self.__edad = edad
        self.profesion = profesion

    #------------METODO-SETTERS : MODIFICA-----------------
    def setNombre(self,nombre):
        self.__nombre = nombre
    def setCedula(self,cedula):
        self.__cedula = cedula
    def setEdad(self,edad):
        self.__edad = edad
    def setProfesion(self,profesion):
        self.profesion = profesion

    #------------METODO-GETTER : OBTIENE--------------------
    def getNombre(self):
        return self.__nombre
    def getCedula(self):
        return self.__cedula
    def getEdad(self):
        return self.__edad
    def getProfesion(self):
        return self.profesion
    
    #------------METODO-- MOSTRAR--------------------------- 
    def mostrar(self):
        return f'Nombre: {self.getNombre()} - Edad: {self.getEdad()} - CC: {self.getCedula()} - Profesión: {self.getProfesion()} '
    
    #--------SOBRECARGA: -METODO--SALUDO-------------------------
    def saludo(self):
        return f'Hola soy {self.getNombre()} y soy {self.getProfesion().lower()}, en que te puedo ayudar?'

        
#-----------------CLASE-ENFERMERA---------------------------
class Enfermera(Ciudadano):
    def __init__(self, nombre: str, cedula: str, edad: int, profesion:str, pacientes:int, turno:str):
        super().__init__(nombre, cedula, edad, profesion)
        self.pacientes = pacientes
        self.turno = turno

    #------------METODO-SETTERS : MODIFICA------------------
    def setPacientes(self,pacientes):
        self.pacientes = pacientes
    def setTurno(self,turno):
        self.turno = turno

    #--------------METODO--GETTER : OBTIENE-----------------
    def getPacientes(self):
        return self.pacientes
    def getTurno(self):
        return self.turno
    
    ##-------------METODO--ENFERMERA------------------------
    def signos_vitales(self,paciente):
        return f'El paciente {paciente} se encuentran en buenas condiciones'
    
    #-------------SOBRECARGA--------------------------------
    def saludo(self):
        return f'Hola soy {self.getNombre()}, en que te puedo ayudar?'

#-----------------CLASE-MECÁNICO----------------------------
class Mecanico(Ciudadano):
    def __init__(self, nombre: str, cedula: str, edad: int, profesion:str, nivel:str, ordenes:int):
        super().__init__(nombre, cedula, edad, profesion)
        self.nivel = nivel
        self.ordenes = ordenes
    
    #------------METODO-SETTERS : MODIFICA------------------
    def setNivel(self,nivel):
        self.nivel = nivel
    def setOrdenes(self,ordenes):
        self.ordenes = ordenes

    #--------------METODO--GETTER : OBTIENE-----------------
    def getNivel(self):
        return self.nivel
    def getOrdenes(self):
        return self.ordenes
    
    ##-------------METODO--MECANICO-------------------------
    def diagnostico_vehiculo(self):
        return f'Su vehiculo esta para cambio de aceite 7n7'
    
#-----------------CLASE-CANTANTE----------------------------
class Cantante(Ciudadano):
    def __init__(self, nombre: str, cedula: str, edad: int, profesion:str, genero_musical:str, canciones:int):
        super().__init__(nombre, cedula, edad, profesion)
        self.genero_musical  = genero_musical
        self.canciones = canciones

    #------------METODO-SETTERS : MODIFICA------------------
    def setGeneroMusical(self,genero_musical):
        self.genero_musical = genero_musical
    def setCanciones(self,canciones):
        self.canciones = canciones

    #--------------METODO--GETTER : OBTIENE-----------------
    def getGeneroMusical(self):
        return self.genero_musical
    def getCanciones(self):
        return self.canciones
    
    #------------------METODO-CANTANTE----------------------
    def albumes(self):
        return f'La música es vida, escucha mi nuevo album!!'
    #-------------SOBRECARGA--------------------------------
    def saludo(self):
        return f'Hola soy {self.getNombre()}, en que te puedo ayudar?'


def main():
    print('\n------------------------------------')
    ciudadano1 = Enfermera('Elizabeth','1000585', 27, 'Enfermera', 8,'Mañana')
    
    print(f'Nombre: {ciudadano1.getNombre()}\n'\
          f'Edad: {ciudadano1.getEdad()}\n'\
            f'Cedula: {ciudadano1.getCedula()}\n'\
            f'Profesión: {ciudadano1.getProfesion()}\n'\
            f'Pacientes por dia: {ciudadano1.getPacientes()}\n'\
            f'Turno: {ciudadano1.getTurno()}\n')
    print(ciudadano1.signos_vitales('Sebastián Gomez'))
    print(ciudadano1.saludo())

    print('\n----------------------------------------')
    ciudadano2= Mecanico('Gustavo','1000827614', 31,'Mecánico', 'B', 12)
    print(f'Nombre: {ciudadano2.getNombre()}\n'\
          f'Edad: {ciudadano2.getEdad()}\n'\
            f'Cedula: {ciudadano2.getCedula()}\n'\
            f'Profesión: {ciudadano2.getProfesion()}\n'\
            f'Nivel: {ciudadano2.getNivel()}\n'\
            f'Ordenes por dia: {ciudadano2.getOrdenes()}\n')
    
    print(ciudadano2.diagnostico_vehiculo())
    print(ciudadano2.saludo())

    print('\n------------------------------------')
    ciudadano3 = Cantante('Kenia Os','2387623', 25, 'Cantante','Pop', 20)
    print(f'Nombre: {ciudadano3.getNombre()}\n'\
        f'Edad: {ciudadano3.getEdad()}\n'\
        f'Cedula: {ciudadano3.getCedula()}\n'\
        f'Profesión: {ciudadano3.getProfesion()}\n'\
        f'Genero musical: {ciudadano3.getGeneroMusical()}\n'\
        f'Canciones: {ciudadano3.getCanciones()}\n')

    print(ciudadano3.albumes())
    print(ciudadano3.saludo())
    print(ciudadano3.mostrar())#Llama la sobrecarga


if __name__=='__main__':
    main()
