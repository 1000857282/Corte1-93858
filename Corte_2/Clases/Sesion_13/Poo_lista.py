'''Programación orientada a objetos:

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
#Proceso-------------------
    def ataquePokemon(self):
        return 'Estoy atacando'


def main():
    pokemones = []
    while 1:#Siempre verdadero y se sale con un break
        pokemon = Pokemon()
        pokemon.nombre= input('Nombre del pokemnon: ')
        pokemon.categoria = input('Categoria del pokemon: ')
        pokemon.color = input('Color del pokemon: ')
        pokemon.tipo = input('Tipo del pokemon: ')
        pokemon.codigo = input('Codigo del pokemon: ')
        pokemones.append(pokemon)

        opc = input('Desea inscribir ottro pokemon (y/n): ')
        if opc== 'n':
            break
        elif opc!= 'y':
            print('Opcion invalida')
        print(pokemones)

    print('\n-------LISTA DE POKEMONES---------')
    for i in pokemones:
        print(f'Nombre: {i.nombre}\n'
              f'Tipo:{i.tipo}\n'
              f'Codigo: {i.codigo}\n'
               f'Ataca!!...{i.ataquePokemon()}\n' 
               '-------------------------') #I es el primero objeto de la lista de pokemones



if __name__=='__main__':
    main()