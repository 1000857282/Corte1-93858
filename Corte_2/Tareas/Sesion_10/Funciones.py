'''
Realice un programa donde permita crear una lista de 10 números aleatorios entre 1 y 50 
(todos números enteros), después cree tres funciones donde se reciba la lista como parámetro 
para:
mayor()-Función que imprima número mayor de la lista (no puede usar el metodo de max)
mínimo()- Función que imprimaa el número menor de la lista (no puede usar el metodo min)
primos()- Función que imprima los números de la lista que son primos

'''
from random import randint as r

def lista():
    lista = []
    for i in range(10):
        lista.append(r(1,50))
    print(lista)
    return lista

def mayor(lista):
    mayor = 0
    for numero in lista:
        if numero > mayor:
            mayor = numero          
    return mayor

def menor(lista):
    menor = mayor
    for numero in lista:
        if numero < menor:
            menor = numero
    return menor


def primos(lista):
    lista_primos = []
    for numero in lista:
        for i in range(2,numero+1):#Que inicie en dos y que vayya hasta el numero de la lista
            primo = numero%i #residuo
            if (primo==0 and numero == i): # si el residuo es cero y igual al numero que esta en i agregue
                lista_primos.append(numero)
            elif (primo==0 and numero != i):
                break

    return lista_primos


if __name__=='__main__':
    
    lista = lista()
    mayor = mayor(lista)
    menor = menor(lista)
    print(f'El numero mayor de la lista es : {mayor}')
    print(f'El menor de la lista es: {menor}')
    primos = primos(lista)
    print(primos)

