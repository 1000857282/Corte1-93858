"""
Realizar un programa que dado un número por el usuario, muestre los divisores positivos de ese número,
en el caso que el número sea cero,indicar un mensaje "Ningún número es divisible entre cero".

"""
num = int(input("Ingrese un número para saber los divisores positivos del número:"))
r = 0

if num!=0:
    for i in range(1,num+1,1):
        r = num % i
        if r==0:
            print(f"El número {i} es divisible por {num} ")    
else:
    print("Ningún número es divisible entre cero, ingrese otro número por favor.")