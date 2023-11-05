#-------------CLASES------------------------------- corregir
class Personas:

#------------ATRIBUTOS : CARACTERISTICAS------------
    def __init__(self):
        self.nombre = None
        self.altura = None
        self.peso = None
#-------------SETTERS : MODIFICA---------------------------

    def setNombre(self,nombre:str):
        self.nombre =nombre

    def setAltura(self,altura:int):
        self.altura = altura

    def setPeso(self,peso:int):
        self.peso = peso
        # if peso >0:
        #     self.peso = peso
        # else:
        #     self.peso = 0

#----------------GETTER : OBTIENE------------------------

    def getNombre(self):
        return self.nombre
    
    def getAltura(self):
        return self.altura
    
    def getPeso(self):
        if type(self.peso)==None:#TYPE() ME RETORNA EL TIPO DE LAVARIABLE - mirar 
        # if self.peso==0:
            return 0
        return self.peso

#--------------------METODO : IMC ------------------------
    def imc(self):
        altura = self.getAltura()
        peso = self.getPeso()
        # print(altura,peso)

        imc_valor = (self.peso)/(self.altura/100)**2 #llame al peso de usuario que ingreso
        #return (self.peso)/(self.altura/100)**2#--->para acortar
        if imc_valor < 18.5:
            return f'IMC: {imc_valor:.2f} - Por debajo.' #Retornar un string
        elif imc_valor < 24.9:
            return f'IMC: {imc_valor:.2f} - Peso Saludable.' 
        elif imc_valor < 29.9:
            return f'IMC: {imc_valor:.2f} - Peso Sobrepeso.' 
        elif imc_valor < 34.9:
            return f'IMC: {imc_valor:.2f} - Peso Obesidad I.' 
        elif imc_valor < 39.9:
            return f'IMC: {imc_valor:.2f} - Peso Obesidad II.'
        return f'IMC: {imc_valor} - Peso Obesidad III.'
        
#-----------INSTANCIANDO: CREAR USUARIO------------
def main():
    pacientes =[]
    while 1: #While 1 --> siempre verdadero
        usuario = Personas()

        # usuario.nombre = input('Nombre: ') MANERA ERRONEA
        # usuario.altura = int(input('Altura(cm): '))
        # usuario.peso = int(input('Peso(Kg): '))

        usuario.setNombre(input('Nombre: '))#METODO-- FUNCIÓN
        usuario.setAltura (int(input('Altura(cm): ')))
        usuario.setPeso (int(input('Peso(Kg): ')))

        pacientes.append(usuario)#no se utliza la lista

        print(f'Nombre: {usuario.nombre}\n'
              f'Altura: {usuario.altura} cm\n'
              f'Peso: {usuario.peso} Kg \n ')#Se le pone el punto imc()--> sin parentesis no trae nada
        print(usuario.imc())


if __name__=='__main__':
    main()