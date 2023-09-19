
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
            datos['edad']= edad
            datos['codigo']= codigo
            datos['genero']= genero
            estudiantes[nombre]= datos
            print(estudiantes)

        elif opc == 'n':
            for key,value in estudiantes.items():#Items es para navegr dentro del diccionario f10
                print(f'Estudiantes: {key}')
                print(estudiantes[key]['edad'])#Va al diciconario diccionario y  coje el indice de la edad
            break
        else: 
            print('Opción invalida')

#MIARA CODIGOOOOOOOOOOOOOOOOOO
def main():
    inscripcion()


if __name__=='__main__':
    main()