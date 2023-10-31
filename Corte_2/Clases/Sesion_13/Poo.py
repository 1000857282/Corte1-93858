
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
    def __init__(self): #ME crea las variables
        #Self es para indicar el objeto
        self.color = None
        self.categoria = None
        self.tipo = None
        self.codigo = None
        self.nombre = None
        self.region = 'Colombia'
        #none --> no tiene ningun valor

#METODO-----------------------
    def correr(self):
        return 'Estoy corriendo'
    def volar(self):
        return 'Estoy volando'
    def quemar(self):
        return'Estoy quemando'
    def ataque(self):
        return'Estoy atacando'
    
def main():
    Pikachu = Pokemon()#aqui me importa todas las variables ya creadas para usarlas aqui
    Pikachu.nombre = 'Pikachu'
    Pikachu.color = 'Amarillo'
    Pikachu.categoria = 'Raton'
    Pikachu.tipo = 'Electrico'
    Pikachu.codigo = 25
    print(f'{Pikachu.nombre}:{Pikachu.correr()}\n'\
          f'region: {Pikachu.region}')
    #print(Pikachu.correr())
    #print(id(Pikachu))

    Charizard = Pokemon()
    Charizard.nombre = 'Charizar'
    Charizard.color = 'Naranja'
    Charizard.categoria = 'Dragon'
    Charizard.tipo = 'Fuego'
    Charizard.codigo = 6
    print(f'{Charizard.nombre}:{Charizard.volar()}\n'
         f'region: {Charizard.region}' )
    #print(Charizard.volar())
    #print(id(Charizard))

    Ninetales = Pokemon()
    Ninetales.nombre = 'Ninetales'
    Ninetales.color = 'Baige'
    Ninetales.categoria = 'Zorro'
    Ninetales.tipo = 'Fuego'
    Ninetales.codigo = 38
    Ninetales.region = 'Peruano'
    print(f'{Ninetales.nombre}:{Ninetales.quemar()}\n'\
          f'region: {Ninetales.region}')
    #print(Ninetales.quemar())
    #print(id(Ninetales))

    #no se puede copiar objeto
    Pichu = Pikachu
    print(id(Pichu))
    print(Pikachu.color)
    print(id(Ninetales))


if __name__=='__main__':
    main()