"""
Realizar un programa que calcule el valor de IVA de un producto. (IVA=19%).
"""
pf = float(input("Ingrese el precio final del producto que compró: "))
v = (pf/(1+0.19))
IVA = pf - v
print(f" El valor IVA del producto que usted compró es de : {round(IVA,2)}") 