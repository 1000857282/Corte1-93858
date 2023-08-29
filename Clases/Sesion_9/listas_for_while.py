"""
Listas: Son ciclicas, inician desde 0
arreglos: inician desde 1

"""
def main(cadena):

    for i in range(len(cadena)):#len -->Recorrer uno en uno los caracteres
        print(cadena[i], "valor de i: ", i)


def main2(cadena):
    for i in cadena:
        print(i)

def main3(cadena):
    i=0
    while i<len(cadena):
        print(f"{cadena[i]},valor de i: {i}" )
        i+=1 #Va aumentando en 1, contador


if __name__=="__main__":
    cadena = "Hola mundo!" #Parametro
    main(cadena)
    main2(cadena)
    main3(cadena)