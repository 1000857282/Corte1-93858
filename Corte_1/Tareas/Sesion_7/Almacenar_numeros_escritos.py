'''
Realice un programa que almacene diferentes números escritos por el usuario dentro de una lista hasta que se incluya 
un número negativo. muestre la lista resultante y después elimine los números duplicados, mostrando también esta 
segunda lista en pantalla.
'''

def almacenar():
    numeros = []
    num = int(input('Ingrese los números que quiere agregar a la lista y para terminar la lista escriba un número negativo: '))
    opc == 'y'
    while opc == 'y':
        if num>=0:
            numeros.append(num)
            num = int(input(' '))
        elif num<0:
            numeros.append(num)
            break
    return numeros

def num_duplicados(lista1):
    lista2 = list(set(lista1))
    return lista2


if __name__=='__main__':
    opc = str(input('Quiere generar una lista: (y/n) '))
    if opc == 'y':  
        while opc == 'y':
            lista1= almacenar()
            print(f'La lista que usted genero es: {lista1}')
            print(f'Lista sin duplicados: {num_duplicados(lista1)}')
            break
    
    else:
        print('Gracias por su tiempo, vuelva más tarde')





            