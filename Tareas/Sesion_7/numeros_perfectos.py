'''
Utilizando el programa que determina cuales son los divisores de un número, imprima la cantidad de números perfectos solicitados por el usuario (máximo 10). (Un número perfecto es aquel cuya 
suma de divisores menos el número original, coinciden con dicho número)

'''

def divisor_numero(num):
    num = int(input("Ingrese un número para saber los divisores positivos del número:"))
    r = 0
    if num!=0:
        for i in range(1,num+1,1): 
            r = num % i
            if r==0:
                return(i)
                #print(f"El número {i} es divisible por {num} ")    
    else:
        print("Ningún número es divisible entre cero, ingrese otro número por favor.")
    
def numeros_perfectos():
    --------------------------------------------------------------------------------------------------------------------------------------------------------
    
#Main
p1= str(input('Quiere saber cuales son los divisores de un número y/n' ))

if p1== 'y':
    p2 = int(input('Cuantos números perfectos desea saber?: '))
    
