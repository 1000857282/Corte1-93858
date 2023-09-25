'''
Realice un programa donde se cree una matriz de 5x10, después se imprima en pantalla la matriz creada, 
indicando cuál es el número más alto y más bajo dentro de la lista, incluyendo su respectiva posición.
Finalmente se organice la matriz del número mayor al menor, empezando desde la posición [0,0].
'''

from random import randint as r
def main(a,b):
    matriz = []
    for i in range(a): #en un rango de filas
        matriz.append([]) #agrege una fila
        for j in range(b):
            matriz[i].append(r(1,100))#subindice cero [i] agregue , llamar la funcion de aleatorio de 1 a 100
        print(matriz[i]) #imprime la matriz de filas jutno con la subcolumna que genero anteriormente
    #print(matriz) #imprime las filas lado a lado
    return matriz #retorna para guardarla e imprimirla

def max_min(matriz):
    minimo = matriz[0][0]
    pos_min = (0, 0)
    maximo = matriz[0][0]
    pos_max = (0, 0)
    for i in range(len(matriz)): #Para un rango de la primera fila
        for j in range(len(matriz[i])):#Para un rango de la posicion 0 de la fila 1-->0
            if matriz[i][j] < minimo: #Si la matriz en la primera posicion (0,0) es menor al minimo.
                minimo = matriz[i][j]#En minimo guardeme el numero de la posicion segun i y j
                pos_min = (i, j)#Muestre la posicion de i y j
            elif matriz[i][j] > maximo:
                maximo = matriz[i][j]
                pos_max = (i, j)
    return minimo,maximo,pos_min,pos_max 


# def max_min_fila(matriz):
#     for fila in matriz:
#         mayor = max(fila)
#         menor = min(fila)
#     return mayor, menor

def organizar(matriz):
    lista_matriz = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            lista_matriz.append(matriz[i][j])#cada elemento de la matriz me va a agragar en una lista
            lista_matriz.sort(reverse=True)#la lista se organiza
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = lista_matriz.pop(0)
        print(matriz[i])

if __name__=='__main__':

    print('--------MATRIZ CREADA---------')
    matriz = main(5,10)
    minimo,maximo,pos_min,pos_max = max_min(matriz) #Debe ir en el orden de como se retorno o sino se hace un mierdero 7u7
    # mayor, menor = max_min_fila(matriz)
    print(f"\nNúmero más alto: {maximo}, posición: {pos_max}")
    print(f"Número más bajo: {minimo}, posición: {pos_min}")

    for num_fila, fila in enumerate(matriz, start=1):# i --> fila
        mayor = max(fila)
        pos1 = fila.index(mayor)
        print(f'\nEl numero mayor de la fila {num_fila} es: {mayor} , y su posición es: {pos1}')
        menor = min(fila)
        pos2 = fila.index(menor)
        print(f'El numero menor de la fila {num_fila} es: {menor} , y su posición es: {pos2}')
    print('\n-------MATRIZ_ORGANIZADA-------')
    organizar(matriz)
    max_min(matriz)
    minimo,maximo,pos_min,pos_max = max_min(matriz)
    print(f"\nNúmero más alto: {maximo}, posición: {pos_max}")
    print(f"Número más bajo: {minimo}, posición: {pos_min}")

    
  


