'''
Utilizando el programa que determina cuales son los divisores de un número, imprima la cantidad de números perfectos solicitados 
por el usuario (máximo 10). (Un número perfecto es aquel cuya 
suma de divisores menos el número original, coinciden con dicho número) (6, 28, 496, 8.128 )

'''

def divisor_numero(num):
    divisores = []
    r = 0
    for i in range(1,num): #para i en un rango de 1 hasta el numero contador, aumente de 1 en 1
        r = num % i
        if r==0:
            divisores.append(i) #agregelo a la lista
    return divisores 
    # print(divisores)

    
def numeros_perfectos(num_2):
    divisores = divisor_numero(num_2) #redefino la variable, guardo la respuesta de la funcion de divisor_numero en una nueva llamada divisores
    suma = sum(divisores) #suma los numeros dentro de la lista
    return suma
    
    
#Main
p1= str(input('Quiere saber cuales son los divisores de un número y/n: ' ))

if p1== 'y':
    p2 = int(input('Cuantos números perfectos desea saber?: '))
    contador_numeros_encontrados = 0
    numero = 2 #Inicie desde 2 la suma

    while contador_numeros_encontrados<p2:
        
        if numeros_perfectos(numero)==numero:
            contador_numeros_encontrados+=1
            print(f'Los numeros perfectos son: #{contador_numeros_encontrados+1}: {numero}' )
        numero+=1 

else:
    print('Gracias, vuelva más tarde')
    
