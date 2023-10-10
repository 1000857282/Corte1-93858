'''
Realice un programa para calcular el valor bruto de un producto alimenticio según la última reforma tributaria 
del IVA de la canasta familiar del año 2023.
Primero se debe leer el archivo Alimentos.txt, para organizar cada uno de los artículos según el valor del IVA. 
El usuario ingresará un producto del listado, junto con el valor neto del mercado actual, entonces el programa 
retornará el valor base del producto y el valor del iva discriminados.
El programa funcionará continuamente hasta que el usuario escriba "salir"

'''

def abrir_documento():
    f = open('Alimentos.txt','r')
    documento = f.readlines() #Read lee todo
    f.close()
    #print(documento)----> imprime todo en una sola lista, no hay listas internas
    #------ORAGANIZAR--DOCUEMNTO-------
    lista = []
    for dato in documento: #Coge cada dato del documento
        #print(dato.rstrip('\n').split(','))#quite la linea de salto y separemelos por comas
        lista.append(dato.rstrip('\n').split(','))#Me agrega cada liena en una lista aparte
    for sublista in lista:
        print( sublista)
    #print(lista)-->Imprime una sola lista sin salto de linea
    for line in line:
        
    return lista

def buscador():
    pass



if __name__=='__main__':
    lista = abrir_documento()
    while True: 
        pro = input('Ingrese un producto para conocer el valor base de su producto, junto con el valor del iva discriminado:').lower()#--> Volver minuscula
        
        if pro in lista:
            val= int(input('Ingrese el valor del producto: '))
            buscar = lista.index(pro)
            iva = 
        elif pro== 'salir':
            break
            

