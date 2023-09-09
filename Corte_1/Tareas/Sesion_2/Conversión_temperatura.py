"""
Solicite una temperatura en escala Fº (decimal) y en
pantalla muestre el equivalente en Cº.
"""

F = float(input("Ingrese una temperatura en grados Fº para saber su equivalente en Cº: "))
res = ((F-32)/1.8)
print(f"La temperatura que usted ingreso en Fº equivale a {round(res,2)} Cº.")