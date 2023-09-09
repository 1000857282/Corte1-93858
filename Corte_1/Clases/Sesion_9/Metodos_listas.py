def agregar(milista):
    num=int(input('Que dato desea agregar: '))
    milista.append(num)
    print(milista)


def insertar(milista):
    var=int(input("Que numero desea ingresar: "))
    idx=int(input('En que posición: '))
    milista.insert(idx,var)#Posicion y valor
    print(milista)


def borrar(milista):
    milista.clear()
    print(milista)

def remover(milista): #remueve el primero que encuentre en la lista
    print(milista)
    rem=int(input("Que número desea remover: "))
    milista.remove(rem)
    print(milista)


def main():
    milista=[2,4,7,8]
    opc=''
    while opc!='exit':
        print("Seleccione una de las disguientes opciones:\n"\
            '1.Agregar\n'\
                '2.Insertar\n'\
                    '3.Borrar\n'\
                        '4.Remover\n'\
                            '5.\n'\
                                )
        opc=input('=>')

        if opc == '1':
            agregar(milista)
        elif opc == '2':
            insertar(milista)
        elif opc == '3':
            borrar(milista)
        elif opc == '4':
            remover(milista)
        elif opc == '5':
            pass


if __name__=='__main__':
    main()