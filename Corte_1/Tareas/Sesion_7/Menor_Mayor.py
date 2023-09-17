'''
Realice un programa que genere 15 números aleatorios y los almacene dentro de una lista. 
Posteriormente ordene dichos elementos de menor a mayor.

'''

from random import randint as r



def aleatorio():
    numeros_generados = 0
    lista1 = []
    while numeros_generados<15:
        num_aleatorio = r(1,100)
        lista1.append(num_aleatorio)
        # print(lista)
        numeros_generados += 1
    return(lista1)

def ordenar_ascendente():
    lista2 = aleatorio()
    lista3 = sorted(lista2)
    return lista2,lista3

if __name__=="__main__":
    p1= str(input('Quiere generar 15 numeros  aleatorios dentro de una lista? (y/n) '))
    if p1 == 'y':
       lista = ordenar_ascendente()
       lista1 = print(f'La lista original es: {lista[0]}')
       lista2 = print(f'Ordenada de menor a mayor queda: {lista[1]}')
       print('Gracias por su tiempo')

    else:
        print('Gracias por su tiempo, intentelo más tarde si gusta')
    