r = int(input("Ingrese un radio: "))
h = int(input("Ingrese un altura: "))

if r>0 and h>0:
    volumen = 3.1416*r**2*h
    print(f"El volumen del cilindro es:{volumen}")