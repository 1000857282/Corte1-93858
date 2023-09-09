'''Clase 12---> Sesion_10
'''

from random import randint as r

def main(filas,columnas):
    matriz = []
    for i in range(filas): #en un rango de filas
        matriz.append([]) #agrege una fila
        for j in range(columnas):
            matriz[i].append(r(1,10))#subindice cero [i] agregue , llamar la funcion de aleatorio de 1 a 10
        print(matriz[i]) #imprime la matriz de filas jutno con la subcolumna que genero anteriormente

    #print(matriz) #imprime las filas lado a lado
    return matriz #retorna para guardarla e imprimirla

  
def escalar(matriz): #primero entra en la fila y luego en la columna
    esc=int(input('Ingrese un número para escalar la matriz: '))
    for i in matriz: #for i in range (len(matriz)): #vaya de 0 hasta el numero de filas
        for j in range(len[i]):#lea el tamaño de i #for j in range(len(matriz[i])): #vaya de cero hasta el numero de columnas en especifico
            i[j]*=esc #matriz[i][j]*= esc #miltiplicar por el escalar --> forma mas corta que esc*matriz[i][j]
        print(i) #print(matriz[i]) --> imprime la lista


if __name__=='__main__':
    filas = int(input('Ingrese el numero de filas: '))
    columnas = int(input('Ingrese el numero de columnas: '))
    print('--------ORIGINAL---------')
    matriz = main (filas,columnas)
    print('--------ESCALAR----------')
    escalar(matriz)

   # a[0].index(5) ---> buscar en la fila cero el numero 5 , me bota la posicion

   #m = [3 5 9]
   #for i in range(len(m))---> cuanta la lista desde i = 0,1,2 --> fila en este caso solo coge la lista
   #for i in m --> lee elemento por elemento  porque coge todo la matriz i = 3 ,5 ,9