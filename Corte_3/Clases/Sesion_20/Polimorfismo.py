'''
Polimorfismo: muchas formas---> Secentra en las facultades que pueden tener los metodos, se puede tener un metodo que se puede transformar en diferentes formas
 un metodo que puede tener varias formas (lso animales se pueden comunir pero en difrerentes formas) hya algo parecido a la sobrecarga que es saludo
'''

class Ciudadano:
    def __init__(self, nombre:str, idioma:str,):
        self.__nombre = nombre
        self.__idioma = idioma

    #----------Setters-----------------------
    def setIdioma(self,idioma:str):
        self.__idioma =idioma 

    def setNombre(self,nombre:str):
        self.__nombre = nombre

    #----------Getter------------------------
    def getIdioma(self):
        return self.__idioma
    
    def getNombre(self):
        return





class Colombiano:
    def __init__(self,idioma:str, nombre:str, cc:str):
        super().__init__(idioma,nombre)#Supper( --> llama a la super clase)
        self.__cc = cc

    def setCC(self, cc:str):
        self.__cc = cc

    def getCC(self):
        return self.__cc
    
    #---------Sobre carga---------------------
    def saludo(self):
        return f'Qiubo parce!'
            

class Ingles(Ciudadano):
    def __init__(self, nombre: str, idioma: str, id:str):
        super().__init__(nombre, idioma)
        self.__id = id
    
    def setId(self, id:str):
        self.__id = id
    
    def getId(self):
        return self.__id
    
    #----------Sobre Carga------------------------
    def saludo(self):
        return f'Hello my Friend!'


class Chino(Ciudadano):
    def __init__(self, nombre: str, idioma: str, sfz:str):
        super().__init__(nombre, idioma)
        self.__sfz = sfz

    def setSfz(self, sfz:str):
        self.__sfz = sfz

    def getSfz(self):
        return self.__sfz
    #-------Sobre Carga--------------
    def saludo(self):
        return f'Hola en Chino!!!'
    
#--------------Metodo Polimorfismo------------------
def darSaludo(objeto):
    return objeto.saludo() #invoca ala ciudadano y al saludo y retorna un string
    
def main():
    ciudadano1 = Ciudadano('Frances','Carla Bruni')
    ciudadano2 = Colombiano('Español', 'Radamel Garcia','254488558')
    ciudadano3 = Ingles('Ingles', 'David Beckman','S45488')
    ciudadano4 = Chino('Mandarin','Shang longh', 'CH48456')
    ciudadanos = [ciudadano1, ciudadano2, ciudadano3, ciudadano4]

    print('------------Ptresentación----------------')
    for persona in ciudadanos:
        print(f'Ciudadano: {persona.getNombre()}, idioma:{persona.getIdioma()}')
        print(f'{persona.getnombre()} dice: '+ darSaludo(persona)+'\n')#funcion estapor fuera, que se lleva como parametro el objeto
        
    # print(f'Ciudadano: {ciudadano1.getNombre()}, idioma:{ciudadano1.getIdioma()}')
    # print(ciudadano2.saludo())
    # print(darSaludo(ciudadano1))
#Vn = VB/1.19 ---> calcular el iva


if __name__ == '__main__':
    main()