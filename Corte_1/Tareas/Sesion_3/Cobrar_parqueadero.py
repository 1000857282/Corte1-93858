"""
Realice un programa para cobrar el tiempo de parqueo en un 
estacionamiento, donde se cobra $139 el minuto. mostrar el valor 
total, discriminando el IVA, aproximando a la cifra de $50 siguiente. 
"""

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
    
    
# elif minutos > 60:
#     min = minutos-60
#     hora = minutos - min
#     if hora == 60:
#         Horas+=1
#         h=Horas*60
#     total_minutos= h+minutos #525
#     cobro_sin_IVA = round(139 * total_minutos,-2) #73000
#     cobro_con_IVA = round(cobro_sin_IVA*1.19,-2)
#     descriminante_IVA = round(cobro_con_IVA - cobro_sin_IVA,-2)
#     print( f"El valor total a pagar es de: {round(cobro_con_IVA)}\n",\
#             f"Valor discriminante del IVA: {round(descriminante_IVA)} \n"\
#             f"El valor por tiempo: {round(cobro_sin_IVA)}")
else:
    print("Por favor ingrese los datos correctamente")


