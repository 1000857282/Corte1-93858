
print("Seleccione el código que desea realizar: \n", \
      "1.Código para cálcular el precio a pagar por el servicio a parqueadero. \n",\
        "2.Código para saber el tipo de triángulo.\n", \
            "3.Código para saber si la letra es vocal o consonante.")

opcion= int(input("Ingrese la opción del código que desea ejecutar: "))

if opcion == 1:

    Horas= int(input("Ingrese las horas que permanecio su vehículo en el estacionamiento: "))
    minutos = int(input("Ingrese los minutos:   "))

    if minutos<=60:
        hora=Horas*60
        total_minutos= hora+minutos #525
        cobro_sin_IVA = round(139 * total_minutos,-2) #73000
        cobro_con_IVA = round(cobro_sin_IVA*1.19,-2)
        descriminante_IVA = round(cobro_con_IVA - cobro_sin_IVA,-2)
        print( f"El valor total a pagar es de: {round(cobro_con_IVA)}\n",\
                f"Valor discriminante del IVA: {round(descriminante_IVA)} \n"\
                f"El valor por tiempo: {round(cobro_sin_IVA)}")
        
    elif minutos>60:
        print("los minutos que usted ingreso es mayor o igual al equivalente de 1 hora, ingrese los datos nuevamente")

elif opcion == 2: 
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
    

elif opcion == 3: 
    letra = input("ingrese una letra del abecedario por favor: ")

    if (letra.lower() == "a" or letra.lower()  =="e" or letra.lower()=="i" or letra.lower()=="o" or letra.lower()== "u"):
        print("La letra que usted ingreso es una vocal")
    else:
        print("La letra que usted ingreso es una consonante.")

else:
     print("La opción que usted ingreso es incorrecta, ingresela nuevamente.")

