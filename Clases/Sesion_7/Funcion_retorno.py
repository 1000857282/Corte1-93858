
#fUNCIÓN
def suma (a,b):
    resultado = a +b 
    return resultado
# def suma (num1,num2):
#     X = num1 + num2
#     return x

#PROGRAMA MAIN
print("Inicio del progrma")
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
resultado = suma(a,b) #iNVOCA FUNCIÓN
print(resultado)