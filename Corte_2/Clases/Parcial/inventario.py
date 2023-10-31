
def crear_inventario(lista):
    con1 = lista.count('carbon')
    con2 = lista.count('madera')
    con3 = lista.count('diamante')
    diccionario = {'carbon':con1,'madera': con2, 'diamante':con3}
    print(diccionario)

def agregar_alimentos():
    lista1=['madera','hierro','carbon','madera']
    


if __name__=='__main__':
    lista= ['carbon', 'madera','madera','diamante','diamante','diamante']
    crear_inventario(lista)
