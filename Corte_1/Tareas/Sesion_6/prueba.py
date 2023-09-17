def calcular_divisores(numero):
    divisores = []
    for i in range(1, numero): #En un rango de 1 a dos 
        if numero % i == 0:
            divisores.append(i)
    return divisores


def es_numero_perfecto(numero):
    divisores = calcular_divisores(numero)
    suma_divisores = sum(divisores)
    return suma_divisores == numero # si la suma es igual al numero que se indico = 2 --> verdadero siga a while o falso termine

def encontrar_numeros_perfectos(cantidad):
    numeros_perfectos_encontrados = 0 #un contador de 0 a la cantidad
    numero = 2 #Me dice desde donde inicie
    while numeros_perfectos_encontrados < cantidad: 
        if es_numero_perfecto(numero):#Si la suma de la lista es igual al numero de i 
            print(f"Numero perfecto #{numeros_perfectos_encontrados + 1}: {numero}")
            numeros_perfectos_encontrados += 1 #Contador de los numeros encontrados
        numero += 1 #Aumente el numero en 1 (2+1=3)

cantidad = int(input("Ingrese la cantidad de números perfectos que desea encontrar: "))

encontrar_numeros_perfectos(cantidad)





