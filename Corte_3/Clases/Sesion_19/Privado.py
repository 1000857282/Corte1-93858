#--------------SUPER CLASE DEPORTISTAS----------------
class Deportista():
    def __init__(self,nombre:str,edad:int,documento:str):
        self.__nombre = nombre
        self.__documento = documento
        self.__edad = edad

    #------------METODO-SETTERS : MODIFICA---------------------------
    def setNombre(self,nombre:str):
        self.__nombre = nombre
    def setDocumento(self,documento:str):
        self.__documento
    def setEdad(self, edad:int):
        self.__edad

    #--------------METODO--GETTER : OBTIENE------------------------
    def getNombre(self):
        return self.__nombre
    def getDocumento(self):
        return self.__documento
    def getEdad(self):
        return self.__edad
    
    #---------------SOBRECARGA-------------------------------
    def presentacion(self):
        return f'{self.getNombre()} es un gran deportista'

    
#------------CLASE DEPORTISTA DE TENIS--------------------
class Tenistas(Deportista):
    def __init__(self,nombre:str, edad: int, documento:str,\
                  games: int, sets:int):
        super().__init__(nombre,edad,documento)
        self.__games = games
        self.__sets = sets

    #------------METODO-SETTERS : MODIFICA---------------------
    def setGames(self, games:int):
        self.__games = games
    def setSets(self, sets:int):
        self.__sets = sets

    #--------------METODO--GETTER : OBTIENE--------------------
    def getGames(self):
        return self.__games
    def getSets(self):
        return self.__sets
    
    #-------------METODO---------------------------------------
    def ace(self):
        return f'El jugador {self.getNombre()} ha ganado {self.getGames()} games'
    #def presentacion(self):
    #   return f'{self.getNombre()} es un gran tenista'


    #------------CLASE DEPORTISTA DE FUTBOL--------------------
class Futbolista(Deportista):
    def __init__(self,nombre:str,documento:str,edad:int,\
                 goles:int, equipo:str):
           super().__init__(nombre, edad,documento)
           self.__goles = goles
           self.equipo = equipo
    #--------------Setters------------------------
    def setGoles(self,goles:int):
        self.__goles=goles
    def setEquipo(self,equipo:str):
        self.equipo = equipo

    #-------------Getters--------------------------

    def getGoles(self):
        return self.__goles
    def getEquipo(self):
        return self.equipo
    

    #-------------Metodo------------------------------
    def anotar(self):
        return f'el jugador{self.getNombre()} ha anotado {self.getGoles()} goles'
    def presentacion(self):
        return f'{self.getNombre()} es un gran futbolista'



def main():
    inscrito = Futbolista('Falcao Garcia',35,'1000585',34, 'Seleccion Colombia')
    print(f'Nombre: {inscrito.getNombre()}\n'\
          f'Edad: {inscrito.getEdad()}\n'\
            f'Documento: {inscrito.getDocumento()}\n'\
                f'#Goles: {inscrito.getGoles()}\n'\
                f'Equipo: {inscrito.getEquipo()}\n')

    print(inscrito.anotar())
    print(inscrito.presentacion())

    print('\n----------------------------------------')
    inscrito2= Tenistas('Roger Federer',43,'546541',4,12)
    print(f'Nombre: {inscrito2.getNombre()}\n'\
          f'Edad: {inscrito2.getEdad()}\n',\
            f'Documento: {inscrito2.getDocumento()}\n',\
                f'#Games: {inscrito2.getGames()}\n',\
                f'#sets: {inscrito2.getSets()}\n')
    
    print(inscrito2.ace())
    print(inscrito2.presentacion())
    print('\n------------------------------------')
    inscrito3=Deportista('Magnus Carlsen',32,'2387623')
    print(inscrito3.presentacion())





if __name__=='__main__':
    main()


