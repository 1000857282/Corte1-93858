'''
Realice un programa para calcular el valor bruto de un producto alimenticio según la última reforma tributaria 
del IVA de la canasta familiar del año 2023.
Primero se debe leer el archivo Alimentos.txt, para organizar cada uno de los artículos según el valor del IVA. 
El usuario ingresará un producto del listado, junto con el valor neto del mercado actual, entonces el programa 
retornará el valor base del producto y el valor del iva discriminados.
El programa funcionará continuamente hasta que el usuario escriba "salir"

'''

from prettytable import PrettyTable

def abrir_documento():
    f = open('Alimentos.txt','r')
    documento = f.readlines() #Read lee todo
    f.close()
    #print(documento)#----> imprime todo en una sola lista, no hay listas internas
    lista = []
    for dato in documento: #Coge cada dato del documento
        lista.append(dato.rstrip('\n').split(','))#Me agrega cada linea en una lista aparte (quite la linea de salto y separemelos por comas)
    doc_ordenado = sorted(lista, key=lambda x: x[2])#lamba es una funcion anonima que oma un argumento x y devuelve x[1], que es el valor en la segunda posición de la lista x. y sorted la organiza
    return doc_ordenado

def imprimir_tabla():
    tabla = PrettyTable()#crear tabla
    tabla.field_names = lista[56]  #La ultima lista es la cabecera porque ya se organizo
    for fila in lista[0:56]:# Agregar las filas a la tabla
        tabla.add_row(fila)
    print(tabla)

def buscar_producto():
    lista = abrir_documento()
    encontrado = False
    for fila in lista:
        if pro in fila:
            encontrado = True
            break
        else:
            encontrado = False
    return encontrado


def calcular_iva(producto):
    lista = abrir_documento()
    for fila in lista:
        if producto in fila:
            iva = float(fila[2])
            val= int(input('Ingrese el valor del producto sin puntos ni comas por favor: '))
            vsi = round(val / (1 + iva),2)
            # valor_iva = val - vsi otra forma de hacerlo
            valor_iva = round(vsi*iva,2)
            print(f'El valor base del producto {producto}, es: {vsi}')
            print(f'El valor del IVA es: {valor_iva}')
        else:
            continue


if __name__=='__main__':
    lista = abrir_documento()
    imprimir_tabla()
    while True:
        pro = input('Ingrese el producto que compró ó escriba "salir" para terminar:\n').capitalize()
        if pro == 'Salir':
            break
        else:
            encontrado = buscar_producto()
            if encontrado == True:
                calcular_iva(pro) 
            elif encontrado == False:
                    print('El alimento ingresado no está en el menú o catálogo de alimentos.')
                    



