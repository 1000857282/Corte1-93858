import fnc_ext
def main():
    a = int(input("]Ingrese un numero:"))
    b = int(input("]Ingrese un numero:"))
    r = fnc_ext.suma(a,b)
    print(r)
    print(f"Ejecutado desde {__name__}")

if __name__=="__main__":

    main() #Invocación de la funcion_externa siempre va a tener el mismo nombre, el principal se va a llamar main


