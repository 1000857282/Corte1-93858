"""
Realizar un programa en el que se soliciten tres longitudes y con 
estos valores se determine si se puede hacer o no un triangulo. En el 
caso que se forme un triangulo, indicar si este es equilátero, isósceles  o escaleno. 
(para formar un triangulo puede usar el teorema de la desigualdad, donde la suma 
de dos lados es mayor que el otro lado)
"""
print("Seleccione una opción:\n", \
      "1. Realizar un triangulo equilatero\n",\
        "2. Realizar un triangulo isósceles\n", \
            "3.Realizar un triangulo escaleno")

tri = input("Ingrese el nombre del triángulo:")
print("Por favor ingrese 3 longitudes")
a = int(input(""))
b = int(input(""))
c = int(input(""))
if a - c < b < a + c or a - b < c < a + b or b - c < a < b + c:
    if (tri.lower()=="equilatero"):
        if a == b and  b == c: #3 lados iguales
            print("Es un triángulo equilatero")
        else: 
            print("Con los datos ingresados no se puede hacer un triangulo equilatero")

    if (tri.lower()=="isosceles"):
        if a == b and  b!=c or b == c and  c!=a or a == c: #2 lados iguales
            print("Es un triángulo isósceles")
        else:
            print("Con los datos ingresados no se puede hacer un triangulo isósceles")

    if (tri.lower()=="escaleno"):    #Error
        if a!= c or b!= c or a!=b: #Ningun lado iguales
            print("Es un triángulo escaleno")
        else: 
            print("Con los datos ingresados no se puede hacer un triangulo escaleno")
else:
    print("El triángulo no se puede realizar")


