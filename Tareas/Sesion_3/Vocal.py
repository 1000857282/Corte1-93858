"""
Programa que solicite al usuatio una letra del abecedario, verifique si el
caracter es una vocal o consonante.

.lower()----> convierte las mayúsculas en minúsculas
"""
letra = input("ingrese una letra del abecedario por favor: ")

# if (letra.lower() == "a"):
#     print("La letra que usted ingreso es una vocal")
# elif (letra.lower() == "e"):
#     print("La letra que usted ingreso es una vocal")
# elif (letra.lower() == "i"):
#     print("La letra que usted ingreso es una vocal")
# elif (letra.lower() == "o"):
#     print("La letra que usted ingreso es una vocal")
# elif (letra.lower() == "u"):
#     print("La letra que usted ingreso es una vocal")
# else:
#     print("La letra que usted ingreso es una consonante.")

if (letra.lower() == "a" or letra.lower()  =="e" or letra.lower()=="i" or letra.lower()=="o" or letra.lower()== "u"):
    print("La letra que usted ingreso es una vocal")
else:
    print("La letra que usted ingreso es una consonante.")

