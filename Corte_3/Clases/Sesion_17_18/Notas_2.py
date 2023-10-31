#---------------CLASE ESTUDIANTES---------------------
class Estudiantes:
#-CONSTRUCTOR ES DONDE SE INSTANCIA EL OBJETO (CREA EL OBJETO)--
#------------ATRIBUTOS : CARACTERISTICAS----------------
    def __init__(self,nombre:str,codigo:int,carrera:str,materia:str,notas:float): #Datos al constructor como parametros
        self.__nombre = nombre
        self.__codigo = codigo
        self.__carrera = carrera
        self.__materia = materia
        self.__notas = notas

#------------METODO-SETTERS : MODIFICA---------------------------
    def setNombre(self,nombre:str):
        self.__nombre = nombre

    def setCodigo(self,codigo:int):
        self.__codigo = codigo

    def setCarrera(self,carrera:str):
        self.__carrera = carrera

    def setMateria(self,materia: str):
        self.__materia = materia

    def setNotas(self,notas: float):
        self.__notas = notas
        if 0<notas<5:
            self.__notas = notas

#--------------METODO--GETTER : OBTIENE------------------------
    def getNombre(self):
        return self.__nombre

    def getCodigo(self):
        return self.__codigo

    def getCarrera(self):
        return self.__carrera 

    def getMateria(self):
        return self.__materia

    def getNotas(self):
        return self.__notas

#---------------METODO PROMEDIO--------------------------
    def __promedio(self): #No se puede ver a menos de que se haga una invocaciñon dentro de la clase, que es la función de abajo
        n = self.getNotas()
        return round(sum(n)/len(n),2)
    
    def getPromedio(self):
        average  = self.__promedio()
        if average<3:
            return f'El Estudiante {self.getNombre()} reprobo la materia con : {average}'
        return f'El Estudiante {self.getNombre()} aprobo la materia con : {average}'


def main():
    # usuario=Estudiantes()
    # usuario.setNombre('Mariana')
    # usuario.setCodigo(1000857548)
    # usuario.setMateria('Programación')
    # usuario.setCarrera('Mecatronica')
    # usuario.setNotas(3.5)
    while 1:
        universidad = []
        nota =[]
        nombre = input('Nombre: ')
        codigo = int(input('Codigo: '))
        materia = input('Materias: ')
        carrera = input('Carrera: ')
        numero_notas = int(input('Cantidad de notas:'))
        x = 1
        while x<numero_notas+1:
            notas = float(input(f'Nota {x}: '))
            if 0<=notas<=5:
                nota.append(notas)
                x+=1
            else:
                print('Ingreso una nota invalida: ')
            
        usuario = Estudiantes(nombre,codigo, materia, carrera, nota)
        universidad.append(usuario)



        print(f'Nombre: {usuario.getNombre()}\n'\
            f'Codigo: {usuario.getCodigo()}\n'\
                f'Materia: {usuario.getMateria()}\n'\
                    f'Carrera: {usuario.getCarrera()}\n'\
                        f'Nota: {usuario.getNotas()}\n'\
                            f'=> {usuario.getPromedio()}') #Despues de llamar pongo parentesis prque es un metodo
if __name__=='__main__':
    main()
    #informacion de todo el ciudadanoy si es mayor o menor