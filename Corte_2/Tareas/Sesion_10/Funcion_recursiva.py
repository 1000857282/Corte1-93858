'''
Escribir una funcion recursiva que encuentre el mayor elemento de una lista.
'''
from random import randint as r

def crear_lista():
    lista = []
    for i in range (16):
        lista.append(r(1,28))
    return lista


def encontrar_mayor(lista,index):
    tamaño = len(lista)
    if tamaño != 1:
        numero1 = lista[index]
        numero2 = lista[index+1]

        if  numero1 > numero2:
            lista.remove(numero2) 
            mayor = numero1 #guardeme el numero mayor 
            encontrar_mayor(lista,index)#llame a la funcion apra que realice el mismo procedimiento pero con ls lista ya actualizada
   
        else:
            mayor = numero2
            lista.remove(numero1)
            encontrar_mayor(lista,index)

    elif tamaño == 1:
        print('fin')
    return lista   


if __name__=='__main__':

    lista = crear_lista()
    print(lista)
    mayor = encontrar_mayor(lista,0)
    mayorfinal= mayor.pop(0)#saca la unica posicion que esta en la lista del numero existente
    print(f'El numero mayor de la lista es: {mayorfinal}')


''' Una forma más facil pero confusa ---> Revisar'''

# from random import randint as r

# def crear_lista():
#     lista = []
#     for i in range (16):
#         lista.append(r(1,28))
#     return lista


# def encontrar_mayor(lista,index,mayor): #numero mayor al anterior
#     if index != len(lista):#Si el indice es diferente del tamaño de la lista
#         numero = lista[index] #numero sera la primera posicion
#         if  numero > mayor: #mayor = 0
#             mayor = numero
#             encontrar_mayor(lista, index+1,mayor) #se llama la funcion nuevamente pero se le aumento el indice
#             return mayor
#         else:
#             encontrar_mayor(lista, index+1,mayor)


# if __name__=='__main__':

#     lista = crear_lista()
#     print(lista)
#     lista = sorted(lista, reverse=True)
#     mayor = encontrar_mayor(lista,0,0)
#     print(f'El numero mayor de la lista es: {mayor}')