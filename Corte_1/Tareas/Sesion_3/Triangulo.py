"""
Realizar un programa en el que se soliciten tres longitudes y con 
estos valores se determine si se puede hacer o no un triangulo. En el 
caso que se forme un triangulo, indicar si este es equilátero, isósceles  o escaleno. 
(para formar un triangulo puede usar el teorema de la desigualdad, donde la suma 
de dos lados es mayor que el otro lado)
"""

print("Por favor ingrese 3 longitudes")
a = int(input("longitud 1: "))
b = int(input("longitud 2: "))
c = int(input("longitud 3: "))
if a + c > b and a + b > c and c + b > a:
    if a == b == c: #3 lados iguales
        print("Es un triángulo equilatero")
    elif a == b or b == c or a == c: #2 lados iguales
            print("Es un triángulo isósceles")
    else:
            print("Es un triángulo escaleno")
else:
    print("El triángulo no se puede realizar")