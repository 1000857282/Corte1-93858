
'''
Programación orientada a objetos:

clase:
Atributos: Caracteristicas del objeto
Metodos: Acciones del objeto
Instanciacion: Invocación del objeto

Variables: minusculas
Clases: Mayuscula y segunda en mayuscula
Funciones: minuscula - segunda palabra va con raya al piso
Campos (atributos): minusculas color_persona
Metodos: Inicial en minucula y la segunda en mayuscula quemarPokemon

'''

#CONSTRUCTOR-------------------

class Pokemon():
    def __init__(self):
        #Self es para indicar el objeto
        self.color = None
        self.categoria = None
        self.tipo = None
        self.codigo = None
        self.nombre = None
        #none --> no tiene ningun valor

#METODO-----------------------
    def correr(self):
        return 'Estoy corriendo'
    def volar(self):
        return 'Estoy volando'
    def quemar(self):
        return'Estoy quemando'

def main():
    Pikachu = Pokemon()
    Pikachu.nombre = 'Pikachu'
    Pikachu.color = 'Amarillo'
    Pikachu.categoria = 'Raton'
    Pikachu.tipo = 'Electrico'
    Pikachu.codigo = 25
    print(f'{Pikachu.nombre}:{Pikachu.correr()}')
    #print(Pikachu.correr())
    #print(id(Pikachu))

    Charizard = Pokemon()
    
    Charizard.nombre = 'Charizar'
    Charizard.color = 'Naranja'
    Charizard.categoria = 'Dragon'
    Charizard.tipo = 'Fuego'
    Charizard.codigo = 6
    print(f'{Charizard.nombre}:{Charizard.volar()}')
    #print(Charizard.volar())
    #print(id(Charizard))

    Ninetales = Pokemon()
    Ninetales.nombre = 'Ninetales'
    Ninetales.color = 'Baige'
    Ninetales.categoria = 'Zorro'
    Ninetales.tipo = 'Fuego'
    Ninetales.codigo = 38
    print(f'{Ninetales.nombre}:{Ninetales.quemar()}')
    #print(Ninetales.quemar())
    #print(id(Ninetales))

    #no se puede copiar objeto
    Pichu = Pikachu
    print(id(Pichu))
    print(Pikachu.color)
    print(id(Ninetales))


if __name__=='__main__':
    main()