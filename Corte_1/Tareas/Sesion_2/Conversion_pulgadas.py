"""
Realizar un programa que solicite una medida en pulgadas (decimal) y en 
pantalla imprima la respectiva conversión en milimetros.
"""

p = input("¿Quiere realizar una conversión de pulgadas a mm? :")
if p == "si":
    num = float(input("Ingrese una medida para hacer la conversión de in a mm: "))
    res = ((num * 25.4)/1)
    print(f"El número que usted ingreso equivale a: {res} mm.")
else:
    print("Gracias por su tiempo")
    
