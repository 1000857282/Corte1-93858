
#Inserta un elemento al final de la lista
def agregar(milista):
    print(milista)
    num=int(input('Que dato desea agregar: '))
    milista.append(num)
    print(milista)

#Inserta un elemento en un índice específico
def insertar(milista):
    print(milista)
    var=int(input("Que numero desea ingresar: "))
    idx=int(input('En que posición: '))
    milista.insert(idx,var)#Posicion y valor
    print(milista)

#Borra todos los elementos de la lista
def limpiar(milista):
    print(milista)
    milista.clear()
    print(milista)

#remueve el primero que encuentre en la lista
def remover(milista): 
    print(milista)
    rem=int(input("Que número desea eliminar de la lista: "))
    milista.remove(rem)
    print(milista)

#Devuelve el valor del índice donde encuentre el valor seleccionado
def buscar(miLista):
    print(miLista)
    dato = int(input('¿Cual dato quiere buscar? '))
    pos =miLista.index(dato)
    print(f'el indice es {pos}')

#Extrae de la lista al elemento en la posición solicitada
def extraer(miLista):
    print(miLista)
    idx=int(input('¿Cual es el indice del numero que desea sacar? '))
    miLista.pop(idx)
    print(miLista)

#Determina el tamaño de la lista
def tamaño(miLista):
    print(miLista)
    n= len(miLista)
    print(f'El tamaño de la lista es de {n}')

#Devuelve el mayor y menor valor de una lista (siempre que se puedan comparar)
def comparar(miLista):
    print(miLista)
    menor = min(miLista)
    mayor = max(miLista)
    print(f'El numero menor es: {menor}')
    print(f'El numero mayor es: {mayor}')
    # print(f'El valor maximo  de la lista es: {max(milista)}')
    # print(f'El valor minimo de la lista es: {min(milista)}')

#Devuelve el número de veces que un elemento esta dentro de la lista
def contador(miLista):
    print(miLista)
    dato = int(input('¿Que numero desea revisar? '))
    con = miLista.count(dato)
    print(f'el numero {dato} esta {con} veces en la lista')

#Devuelve la suma de los elemento de una lista (siempre que se puedan sumar)
def suma(miLista):
    print(miLista)
    res = sum(miLista)
    print(f'los elementos de la lista suman {res}')

#Devuelve True si el dato solicitado pertenece a la lista 
def comprobar(miLista):
    print(miLista)
    dato = int(input('¿Que dato desea comprobar? '))
    print(dato in miLista)

#Añade una estructura de datos al final de la lista
def extender(miLista):
    print(miLista)
    b = int(input('Que dato desea ingresar en la lista: '))
    miLista.extend([b])
    print(miLista)

#Devuelve la lista ordenada ascendentemente (Siempre que sean comparables)
def ordenar_ascendente(miLista):
    print(miLista)
    lista1 = sorted(miLista)
    # lista1 = miLista.sort() --> modifica la lista oiginal por eso aparece none
    print(lista1)

#Devuelve la lista ordenada descendentemente (siempre que sean comparables)
def ordenar_descendente(miLista):
    print(miLista)
    lista2= sorted(miLista,reverse=True)
    # lista2 = miLista.reverse()
    print(lista2)
    # miLista.sort(reverse=True)--> no deja modificar la lista original porque no la lee o guard
    # print(miLista)

def sacar_duplicados(miLista):
    print(miLista)
    lista1 = list(set(miLista))
    print(lista1)

def main():
    milista=[2,4,7,8,4,5,7,8,10,2,1]                                                                                                                                                                                                                                     
    opc=''
    while opc!='exit':
        print("Seleccione una de las disguientes opciones:\n"\
            '1.Agregar\n'\
                '2.Insertar\n'\
                    '3.Limpiar\n'\
                        '4.Remover\n'\
                            '5.Buscar\n'\
                                '6.Extraer\n'\
                                    '7.Tamaño\n'\
                                        '8.Comparar\n'\
                                            '9.Contador\n'\
                                                '10.Suma\n'\
                                                    '11.Comprobar\n'\
                                                        '12.Extender\n'\
                                                            '13.Ordenar ascendentemente\n'\
                                                                '14.Ordenar descendentemente\n'\
                                                                    '15. Sacar numeros duplicados\n'\
                                                
                                )
        opc=input('=>')

        if opc == '1':
            agregar(milista)
        elif opc == '2':
            insertar(milista)
        elif opc == '3':
            limpiar(milista)
        elif opc == '4':
            remover(milista)
        elif opc == '5':
            buscar(milista)
        elif opc == '6':
            extraer(milista)
        elif opc == '7':
            tamaño(milista)
        elif opc == '8':
            comparar(milista)
        elif opc == '9':
            contador(milista)
        elif opc == '10':
            suma(milista)
        elif opc == '11':
            comprobar(milista)
        elif opc == '12':
            extender(milista)
        elif opc == '13':
            ordenar_ascendente(milista)
        elif opc == '14':
            ordenar_descendente(milista)
        elif opc == '15':
            sacar_duplicados(milista)


if __name__=='__main__':
    main()