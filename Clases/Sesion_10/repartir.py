# import random as r
# def repartir():
#     pass
import random as r

p1 = str(input("Desea iniciar el juego?: (y/n) "))
if p1 == 'y':
    cartas: [ ]
    x =  r.randint(1,9)
    cartas.append(x)
    print(cartas)