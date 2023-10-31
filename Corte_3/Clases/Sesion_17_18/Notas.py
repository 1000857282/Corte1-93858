#---------------CLASE ESTUDIANTES---------------------
class Estudiantes:
#-CONSTRUCTOR ES DONDE SE INSTANCIA EL OBJETO (CREA EL OBJETO)--
#------------ATRIBUTOS : CARACTERISTICAS----------------
    def __init__(self):
        self.__nombre = None
        self.__codigo = None
        self.__carrera = None
        self.__materia = None
        self.__notas = None

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



def main():
    usuario=Estudiantes()
    usuario.setNombre('Mariana')
    usuario.setCodigo(1000857548)
    usuario.setMateria('Programación')
    usuario.setCarrera('Mecatronica')
    usuario.setNotas(3.5)


    print(f'Nombre: {usuario.getNombre()}\n'\
          f'Codigo: {usuario.getCodigo()}\n'\
            f'Materia: {usuario.getMateria()}\n'\
                f'Carrera: {usuario.getCarrera()}\n'\
                    f'Nota: {usuario.getNotas()}\n') #Despues de llamar pongo parentesis prque es un metodo
if __name__=='__main__':
    main()