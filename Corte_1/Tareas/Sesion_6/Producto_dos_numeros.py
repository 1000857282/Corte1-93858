"""
Realizar un programa que muestre el producto entre dos números enteros (negativos o positivos), realizando sumas sucesivas.

"""
num1= int(input("Ingrese un número:"))
num2=int(input("Ingrese otro número: "))
r = 0 
# Códifo base
# for i in range(0,num2,1):
#     r = r + num1
#     print(f"{r-num1} + {num1} = {r}")

# print(f"El producto entre {num1} y {num2} es {r}")


if num1>1 and num2>1 or num1<1 and num2>1:#No pude hacer la otra condicion si num2<1 and num1>1
    for i in range(0,num2,1):
        r = r + num1
        print(f"{r-num1} + {num1} = {r}")
# elif num1<1 and num2<1:
else: 
    for i in range(num2,0,1):
        r = r + num1#Aqui la pongo negativo y el resultado me queda postivo y el r*(-1) se borra
        print(f"({r-num1}) + ({num1}) = {r*(-1)}")

    r=r*(-1)

print(f"El producto entre {num1} y {num2} es {r}")

