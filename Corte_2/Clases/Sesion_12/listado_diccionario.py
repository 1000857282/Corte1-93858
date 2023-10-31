
def inscripcion():
    estudiantes = {}
    datos = {}
    
    while 1: #Siempre verdadero
        opc = input('Desea inscribir un estudiante: (y/n) ')

        if opc =='y':
            nombre = input('Nombre: ') #No hya necesidad de escribir str(input)
            edad = input('Edad: ')
            codigo = input('Codigo: ')
            genero = input('Genero: ')
            # datos['edad']= edad #los agrega los dos{'edad':'18}, igual abajo
            # datos['codigo']= codigo
            # datos['genero']= genero
            estudiantes[nombre]={'edad':edad,'codigo':codigo,'genero':genero} #Codigo mas corto
            #estudiantes[nombre]= #datos·imprime ya todos los datos dentro del diccionario, solo agrega el nombre
            print(estudiantes)

        elif opc == 'n':
            for key,value in estudiantes.items():#Items es para navegr dentro del diccionario f10
                print(f'Estudiantes: {key}')
                print(f'Edad:' ,estudiantes[key]['edad'])#Va al diciconario diccionario y  coje el indice de la edad
                print(f'Codigo:' ,estudiantes[key]['codigo'])
                print(f'Genero:' ,estudiantes[key]['genero'])
            break
        else: 
            print('Opción invalida')

def main():
    inscripcion()


if __name__=='__main__':
    main()