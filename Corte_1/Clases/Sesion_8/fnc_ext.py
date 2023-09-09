def suma(a,b):
    x=a+b
    print(f"Ejecutado desde {__name__}")

    return x

if __name__=="__main__": #Si el nombre es main ejecuta lo de abajo , si es funcion externa ejecuta hasta la linea 7

    print(suma(20,40)) 

