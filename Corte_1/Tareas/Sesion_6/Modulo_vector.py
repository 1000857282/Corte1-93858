'''Realice un programa que calcule el módulo de un vector, 
junto con sus componentes rectangulares. (Debe solicitar las coordenadas de origen y fin del vector) 
'''

from math import sqrt as raizc
 

def componentes(x1,x2,y1,y2):
    comp_x = x2 - x1
    comp_y = y2 - y1 
    #comp_z = 124----> Ejemplo
    return comp_x ,comp_y #comp_z ---> lo retorna como una Tupla



def modulo_vector(x,y):
    modulo = raizc(x**2 + y**2)
    return modulo 

#MAIN:

p1 = str(input('Quiere saber el modulo de un vector y sus componentes rectangulares? : y/n '))
if p1 == 'y':
    x1= int(input('Ingrese la coordenada de x en el punto de origen: '))
    x2 = int(input('Ingrese la coordenada de x en el punto final: '))
    y1= int(input('Ingrese la coordenada de y en el punto de origen: '))
    y2 = int(input('Ingrese la coordenada de y en el punto final: '))

    if x2>x1 and y2>y1:
        r_1 = componentes(x1,x2,y1,y2)
        print(r_1)
        x = r_1[0]
        y = r_1[1]
        print(x)
        print(y)
        print(f'Las componentes rectangulares del vector son:  ({r_1})')
        calcular_modulo = modulo_vector(x,y)
        print(f'El módulo del vector es: {round(calcular_modulo,2)}')

    else:
        print("El punto final tiene que ser mayor que el punto de origen")
else:
    print('Gracias, vuelva más tarde')

#no funciona para (0,0) y (0,3) arreglarlo