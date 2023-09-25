

def main_read1():
    f = open('matrizAsignacion.txt','rt')#rt---> r= read y t = texto --> leer texto   ABRIR EL ARCHIVO
    documento = f.read() #Read lee todo
    f.close()
    print(documento)

def main_read2():
    f = open('matrizAsignacion.txt','rt')#rt---> r= read y t = texto --> leer texto
    documento = f.readline().rstrip('\n').split(',') #REadline solo lee la primera linea , el split hace una lista
    while documento != [""]: #Si dejo espacio entre las comillas va a esperar un espacio y me va a imprimir un espacio
        print(documento)
        #input('Presione enter')   si lo comento imprime con espacio 
        documento = f.readline().rstrip('\n').split(',')
    f.close()
'''
RSTRIP
txt="banana,,,,ssqqqww..." #rstrip quita todo lo que no necesita, quita los bordes
x = txt.rstrip(".")
rstrip recorta --> desde lo ultimo; strip--> corta desde el incio y el final no importa el orden

SPLIT --> Separa numeros o caracteres por lo que yo le diga en un lista
txt = "Hello, mi name is Nicol"
X = TXT.SPLIT(",") -->separemelo por comas
['Hello', ' mi name is Nicol']
'''    
def suma(lista):
    salida = ""
    for dato in lista:
        resultado  = int(dato[0])+int(dato[1])+int(dato[3])
        salida+=(str(resultado) + ('\n'))
        return salida
        print(resultado)

def main_read3():
    f = open('matrizAsignacion.txt','rt')#abrir documento
    documento = f.readlines() #Readlines me crea una lista y en una lista tengo qeu coger dato por dato
    f.close()#Lo abro lo leo y lo cierro
    lista = []
    for dato in documento: #Coge cada dato del documento
        #print(dato.rstrip('\n').split(','))#quite la linea de salto y separemelos por comas
        lista.append(dato.rstrip('\n').split(','))
    print(lista)
        #suma(lista)
    a = suma(lista)
    print(a)

    print(documento)

if __name__=='__main__':
    main_read1()
    main_read2()
    main_read3()
    