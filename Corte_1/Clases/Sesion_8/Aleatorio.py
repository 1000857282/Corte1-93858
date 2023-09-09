#Libreria d numeros aleatorio
#dir(random)---> mirar cuantas funciones tiene y help es como funciona--> help(random.randint)

import random as r
def app():
    pal=" "
    nombre="Nicol"
    while pal != "exit":
        #x =  r.choice(nombre)#Solo aparecen las letras que estan dentro de la variable nombre y las imprime aleatorio
        x =  r.randint(100,180)#numeros aleatorios enteros-->randint
        #x =  r.uniform(100,180)--->para imprimir aleatorios decimales
        print(x)
        pal=input("para salir escriba exit:--->")

if __name__=="__main__":
    app()

