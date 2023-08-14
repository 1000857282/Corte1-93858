"""
Realizar un programa en el que se soliciten tres longitudes y con 
estos valores se determine si se puede hacer o no un triangulo. En el 
caso que se forme un triangulo, indicar si este es equilátero, isósceles  o escaleno. 
(para formar un triangulo puede usar el teorema de la desigualdad, donde la suma 
de dos lados es mayor que el otro lado)
"""
print("Por favor ingrese 3 longitudes")
a = int(input(""))
b = int(input(""))
c = int(input(""))
if a - c < b < a + c or a - b < c < a + b or b - c < a < b + c:
    if a == b and  b == c: #3 lados iguales
        print("Es un triángulo equilatero")
    elif a == b and  b!=c or b == c and  c!=a or a == c: #2 lados iguales
        print("Es un triángulo isósceles")
    elif a!= c or b!= c and b!=a: #Ningun lado igual
        print("Es un triángulo escaleno")
else:
    print("El triángulo no se puede realizar")


