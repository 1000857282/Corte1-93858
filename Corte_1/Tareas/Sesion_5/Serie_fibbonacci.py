"""
Realizar un programa que muestre en pantalla la cantidad de dígitos solicitada por el usuario de la serie de Fibbonacci.

"""
num = int(input("Ingrese la cantidad de digitos que quiere que aparezcan en pantalla de la serie de fibonacci: "))
a = 0
b = 1
if num >1:
    print(1)
    for i in range(1,num,1):
        r = a + b
        print(r)
        a = b
        b = r
    
else:
    print("Ingrese nuevamente el número")