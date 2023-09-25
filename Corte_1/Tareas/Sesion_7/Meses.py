'''
Realice un programa que solicite al usuario el nombre de un mes del año, posteriormente debe entregar como 
resultado el número de días que tiene el mes, junto con los festivos correspondientes. (ej: Marzo ==> 20, día de San José). 

'''
def meses_del_año(mes):
    meses = ['enero', 'febrero', 'marzo','abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'novimebre', 'diciembre']
    dias_del_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31  ]
 
    if mes in meses:
        mes1 = meses.index(mes)#saqueme el indice del mes que escribio el usuario y luego metalo en la otra lista para hubicar los dias
        #print(mes1)
        dias_del_mes1 = dias_del_mes[mes1]
        #print(dias_del_mes1)
        #enero = dias_festivos[0:2]
        return dias_del_mes1


def festivos(mes):
    festivos = ['1, Año nuevo\n 9, Día de los Reyes Magos', '20, Día de San José', '2, Domingo de Ramos\n 6, Jueves Santo\n 7, Viernes Santo\n 9, Domingo de Resurrección', \
                '1, Dia del trabajo\n 22, Día de la Ascensión', '12, Corpus Christie\n 19, Sagrado Corazón', \
                    '3, San Pedro y San Pablo\n 20, Dia de la independencia', '7, Batalla de boyaca\n 21, Asunción de la Virgen María', '16, Día de la Raza',\
                        '6, Día de Todos los Santos\n 13, Independencia de Cartagena', '8, Inmaculada Concepción\n 25, Navidad' ]

    if mes == 'enero':
        enero = festivos.pop(0)
        return enero
    elif mes == 'febrero':
        febrero = 'Ninguno'
        return febrero
    elif mes == 'marzo':
        marzo = festivos.pop(1)
        return marzo
    elif mes == 'abril':
        abril = festivos.pop(2)
        return abril
    elif mes == 'mayo':
        mayo = festivos.pop(3)
        return mayo
    elif mes == 'junio':
        junio = festivos.pop(4)
        return junio
    elif mes == 'julio':#
        julio = festivos.pop(5)
        return julio
    elif mes == 'agosto':
        agosto = festivos.pop(6)
        return agosto
    elif mes == 'octubre':
        octubre = festivos.pop(7)
        return octubre
    elif mes == 'noviembre':
        noviembre = festivos.pop(8)
        return noviembre
    elif mes == 'diciembre':
        diciembre = festivos.pop(9)
        return diciembre



if __name__=='__main__':
    opc = ' '
    while opc != 'exit': 
        mes = str(input('Ingrese un mes del año para saber el numero de dias y sus festivos correspondientes: ').lower())
        dias_del_mes = meses_del_año(mes)
        festivos_del_mes = festivos(mes)
        mes = mes.capitalize()
        print(f'{mes} tiene {dias_del_mes} dias, festivos ==> \n {festivos_del_mes}')
        print('Exit para salir ')
        opc=input('=>')
        
   