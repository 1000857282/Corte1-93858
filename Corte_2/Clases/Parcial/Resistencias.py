
def resistencia(lista):
    colores = ['negro', 'cafe','rojo','naranja','amarillo', 'verde', 'azul', 'morado', 'gris', 'blanco']
    banda_1 = [0,1,2,3,4,5,6,7,8,9]
    banda_2 = [0,1,2,3,4,5,6,7,8,9]
    banda_3 = [1, 10,100,1000,10000, 100000, 1000000, 10000000, 100000000, 1000000000]
    ban1 = lista.pop(0)
    ban2 = lista.pop(0)
    ban3 = lista.pop(0)
    if banda1 in colores:
        color =  colores.index(ban1)
        num1 = banda_1[color]
    if banda2 in colores:
        color =  colores.index(ban1)
        num2 = banda_1[color]
    if banda3 in colores:
        color =  colores.index(ban1)
        num3 = banda_1[color]
    return num1, num2, num3
       
    







if __name__=='__main__':
    colores = []
    banda1= input('Ingrese el color de la primera banda: ').lower()
    banda2= input('Ingrese el color de la segunda banda: ').lower()
    banda3= input('Ingrese el color de la Tercera banda: ').lower()
    # banda1= 'negro'
    # banda2='blanco'
    # banda3 ='azul'

    colores.append(banda1)
    colores.append(banda2)
    colores.append(banda3)
    print(colores)
    resistencia(colores)