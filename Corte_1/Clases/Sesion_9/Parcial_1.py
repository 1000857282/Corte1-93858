import random as r

def repartir(cartas):
        cartas= ['A',2,3,4,5,6,7,8,9,'J','Q']
        x =  r.randint(cartas)
        cartas.append(x)
        print(cartas)


def inicio_programa():
    cartas=[]
    p1 = str(input("Desea iniciar el juego?: (y/n) "))
    if p1 == 'y':
        repartir(cartas)

        #pal=''
        #while pal!='exit':   
        p2 = str(input("Desea pedir una carta?: (y/n) "))
        if p2 == 'y':
             repartir(cartas)
             print(cartas)
             
            
        elif p2 == 'n':
             pass
             
        #pal=input("para salir escriba exit:--->")

        


    elif p1=='n':
        print("Gracias por jugar")

    else:
        print('opcion invalida')





if __name__=='__main__':
    inicio_programa()
