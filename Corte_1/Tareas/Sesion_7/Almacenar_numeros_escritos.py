'''
Realice un programa que almacene diferentes números escritos por el usuario dentro de una lista hasta que se incluya 
un número negativo. muestre la lista resultante y después elimine los números duplicados, mostrando también esta 
segunda lista en pantalla.
'''
def alamacenar():
        num = int(input('Ingrese el numero que quiere agregar a la lista:'))
        numeros = []
        if num > 0:
            numeros.append(num)
        elif num < 0:
             numeros.append(num)
             breakpoint
        return numeros

if __name__=="__main__":
    opc = str(input('Quiere agregar un numero a una lista: (y/n) '))
    if opc == 'y':  
        while opc == 'y':
            #p1= int(input('Ingrese los números que quiere agregar a la lista y para terminar la lista escriba un número negativo:  '))
                lista = print(alamacenar())
                print(lista)
                opc = str(input('Quiere agregar otro numero?: (y/n) '))
                if opc == 'y':
                    lista.append(alamacenar())

                elif opc == 'n':
                    print('Gracias por su tiempo, vuelva más tarde')
                else: 
                    print('Opcion invalida')
    elif opc == 'n':
         print('Gracias por su tiempo, vuelva más tarde')
    else: 
         print('Opcion invalida')
         
            