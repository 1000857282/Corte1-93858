def crear_inventario(lista):
    inventario={}
    for elemento in lista:
        if elemento not in inventario:
            inventario[elemento]=1
        else:
            inventario[elemento]+=1
    #print(inventario)
    return inventario

def agregar_inventario(inv,lista):
    nuevo=crear_inventario(lista)
    for elemento in nuevo:
        if elemento not in inv:
            inv[elemento]=nuevo[elemento]
        else:
            inv[elemento]+=nuevo[elemento]
    #print(inv)

def reducir_inventario(inv,lista):
    nuevo=crear_inventario(lista)
    for elemento in nuevo:
        if elemento not in inv:
            inv[elemento]=nuevo[elemento]
        else:
            lote=inv[elemento]-nuevo[elemento]
            if lote < 0:
                inv[elemento]=0
                continue
            inv[elemento]=lote
    #print(inv)

def borrado_inventario(inv,item):
    if item in inv:
        del inv[item]
        print(inv)
    else:
        print(inv)

if __name__=="__main__":
    crear_inventario(['carbon','madera','madera','diamante','diamante','diamante'])
    agregar_inventario({'madera':1},['madera','hierro','carbon','madera'])
    reducir_inventario({'carbon':2,'hierro':3,'diamante':0},['diamante','carbon','hierro','hierro'])
    borrado_inventario({'carbon':2,'madera':1,'diamante':2},'diamante')