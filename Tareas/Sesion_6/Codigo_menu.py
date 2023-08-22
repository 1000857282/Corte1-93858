print("Seleccione el código que desea ejecutar: \n", \
      "1.Código para  mostrar los divisores positivos del número que ingreso. \n",\
        "2.Código para saber el producto entre dos números enteros realizando sumas sucesivas.\n", \
            "3.Código para saber la serie de Fibbonacci.")

opcion= int(input("Ingrese la opción del código que desea ejecutar: "))

if opcion==1:
    
    num = int(input("Ingrese un número para saber los divisores positivos del número:"))
    r = 0

    if num!=0:
        for i in range(1,num+1,1):
            r = num % i
            if r==0:
                print(f"El número {i} es divisible por {num} ")    
    else:
        print("Ningún número es divisible entre cero, ingrese otro número por favor.")

elif opcion==2:
    
    num1= int(input("Ingrese un número:"))
    num2=int(input("Ingrese otro número: "))
    r = 0 
    if num1>1 and num2>1 or num1<1 and num2>1:##############
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

elif opcion==3 :
    
    num = int(input("Ingrese la cantidad de digitos que quiere que aparezcan en pantalla de la serie de fibonacci: "))
    a = 0
    b = 1
    if num >1:
        print(1)
        for i in range(1,num,1):
            r = a + b
            print(r)
            a = b
            b = r
    else:
        print("Ingrese nuevamente el número")

print("Gracias por su tiempo! 7u7")
    
    
    
    
