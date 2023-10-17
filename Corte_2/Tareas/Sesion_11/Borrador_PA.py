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
    documento = ['CODIGO,DESCRIPCION,TARIFA IVA LEY VIGENTE\n', '1110100,Arroz,0\n', '1110200,Harina de maiz y otras harinas,0.05\n', '1110300,Pastas alimenticias,0.05\n', '1110400,Cereales preparados,0.19\n']

    # f = open('Alimentos.txt','r')
    # documento = f.readlines() #Read lee todo
    # f.close()
    # print(documento)#----> imprime todo en una sola lista, no hay listas internas

    #----------ORAGANIZAR--DOCUEMNTO-------
    doc_ordenado = sorted(documento, key=lambda x: x[3])#lamba es una funcion anonima que oma un argumento x y devuelve x[1], que es el valor en la segunda posición de la lista x. y sorted la organiza
    # print(doc_ordenado)
    lista = []
    for dato in doc_ordenado: #Coge cada dato del documento
        lista.append(dato.rstrip('\n').split(','))#Me agrega cada linea en una lista aparte (quite la linea de salto y separemelos por comas)
    #print(lista)#Imprime una sola lista sin salto de linea
  
    #----------Opciones para organizar e imprimir-------------------
    # for sublista in lista:
    #     print( sublista) imprime las sublista con salto de linea
    # for fila in lista:
    #     for celda in fila:
    #         print(celda, end="\t")  # Usar "\t" para separar las celdas con una pestaña--> imprime sin listas
    #     print()  # Saltar a una nueva línea para la siguiente fila
    #-----------------------------------------------------------------

    tabla = PrettyTable()#crear tabla
    tabla.field_names = lista[4]  #La ultima lista es la cabecera porque ya se organizo
    for fila in lista[0:4]:# Agregar las filas a la tabla
        tabla.add_row(fila)
    print(tabla)

    # lista_2 = [cadena.lower() for cadena in fila]
    print(lista)
    return lista

def calcular_iva(producto):
    lista = abrir_documento()
    for fila in lista:
        buscar = fila.index(producto)
    val= int(input('Ingrese el valor del producto: '))
    iva = float(fila[buscar].split(',')[2])
    vsi = val / (1 + iva)
    valor_iva = val - vsi
    print(f'El costo del alimento {producto} es: {vsi}')
    print(f'El valor del IVA es: {valor_iva}')
    



if __name__=='__main__':
    lista = abrir_documento()
    while True: 
        pro = input('Ingrese el producto que compró ó escriba "salir" para terminar:\n').capitalize()#--> Volver minuscula
        for fila in lista:
            buscar = fila.index(pro)
            if pro in fila:
                calcular_iva(pro)
        if pro not in lista:
            print('El alimento ingresado no está en el menú o catálogo de alimentos.')
        elif pro == 'salir':
            break

