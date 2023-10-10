'''
Realizar un ejercicio donde se calcule el IMC de las siguientes 4 personas, cuyos valores se ven en la tabla. 
El sistema debe mostrar según el valor de IMC obtenido para cada uno de las personas indicando su correspondiente escala. 
'''

class Personas:
    def _init_(self):

        #Atributos constructor
        self.nombre = None
        self.altura = None
        self.peso = None

        #Metodo
    def Indice(self):
        IMC = self.peso/((self.altura/100)**2) #Aqui se hace la conversion de centimetros a metros

        #Condición
        if IMC <= 18.5:
            return str("Por debajo")
        elif IMC <=24.9:
            return str("Saludable")
        elif IMC <=29.9:
            #print(IMC) Imprime IMC
            return str("Sobre peso")
        elif IMC <=34.9:
            return str("Obesidad I")
        elif IMC <=39.9:
            return str("Obesidad II")
        else:
            return str("Obesidad III")
            

#instancia es la creacion del objeto
def main():
    estudiante1 = Personas() #Se llma a la clase y se crea los siguientes atributos
    estudiante1.nombre = "Pedro Caceres"
    estudiante1.altura = 188
    estudiante1.peso = 97


    estudiante2 = Personas()
    estudiante2.nombre = "Maria Perez"
    estudiante2.altura = 160
    estudiante2.peso = 47


    estudiante3 = Personas()
    estudiante3.nombre = "Julian Domingues"
    estudiante3.altura = 158
    estudiante3.peso = 58

    estudiante4 = Personas()
    estudiante4.nombre = "Jessica fuentes"
    estudiante4.altura = 170
    estudiante4.peso = 73

    print(f"Estudiante: {estudiante1.nombre} resultado: {estudiante1.Indice()}")
    print(f"Estudiante: {estudiante2.nombre} resultado: {estudiante2.Indice()}")
    print(f"Estudiante: {estudiante3.nombre} resultado: {estudiante3.Indice()}")
    print(f"Estudiante: {estudiante4.nombre} resultado: {estudiante4.Indice()}")


if __name__== "__main__":
    main()                  