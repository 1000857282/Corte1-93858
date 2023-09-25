import random

# Función para crear una matriz de 5x10 con números aleatorios entre 1 y 100
def crear_matriz(filas, columnas):
    matriz = []
    for _ in range(filas):
        fila = [random.randint(1, 100) for _ in range(columnas)]
        matriz.append(fila)
    return matriz

# Función para imprimir una matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Función para encontrar el número más alto y más bajo con sus posiciones
def encontrar_extremos(matriz):
    maximo = matriz[0][0]
    minimo = matriz[0][0]
    pos_max = (0, 0)
    pos_min = (0, 0)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maximo:
                maximo = matriz[i][j]
                pos_max = (i, j)
            elif matriz[i][j] < minimo:
                minimo = matriz[i][j]
                pos_min = (i, j)

    return maximo, pos_max, minimo, pos_min

# Función para organizar la matriz de mayor a menor
def organizar_matriz(matriz):
    matriz_flatten = [elemento for fila in matriz for elemento in fila]#Coge cada elemento y lo guarda en una lista nueva
    matriz_flatten.sort(reverse=True)#la orgamiza

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = matriz_flatten.pop(0)

# Crear la matriz
matriz = crear_matriz(3, 2)

# Imprimir la matriz original
print("Matriz original:")
imprimir_matriz(matriz)

# Encontrar el número más alto y más bajo con sus posiciones
maximo, pos_max, minimo, pos_min = encontrar_extremos(matriz)

print(f"\nNúmero más alto: {maximo}, posición: {pos_max}")
print(f"Número más bajo: {minimo}, posición: {pos_min}")

# Organizar la matriz de mayor a menor
organizar_matriz(matriz)

# Imprimir la matriz ordenada
print("\nMatriz ordenada de mayor a menor:")
imprimir_matriz(matriz)