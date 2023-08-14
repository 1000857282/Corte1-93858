"""
Realice un programa que solicite a un estudiante su nota y retorne el mensaje "aprobó" si obtuvo
 una nota superior o igual a 3, en caso contrario indique "reprobó".

 \n salto de linea al momento de imprimir
 \ salto en el codigo
"""


print("Seleccione una opción:\n", \
      "1. Calcula el área de un circulo\n",\
        "2. Calcula el área de un rectángulo\n", \
            "3.Calcula el área de un triángulo")

fig = input("Ingrese el nombre de la figura:")
A="NAN"
if (fig.lower()=="circulo"):
    r = int(input("Ingrese el valor del radio: "))
    A = 3.1416*r**2
elif (fig.lower()=="rectangulo"):
    b = int(input("ingrese el valor de la base:"))
    h = int(input("ingrese el valor de la base:"))
    A = b*h
elif (fig.lower()=="triangulo"):
    b = int(input("ingrese el valor de la base:"))
    h = int(input("ingrese el valor de la base:"))
    A = b*h/2
else:
    print("Ingreso una opción invalida")
print(f"El valor del área es: {A}")