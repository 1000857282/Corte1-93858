def selec_producto():
    f=open("Alimentos.txt","rt")
    a = f.readlines()
    f.close
    lista = []
    for dato in a:
        lista.append(dato.rstrip("\n").split(","))
    print(lista)

def metodo():
    l = []

    with open('Alimentos.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split(',')
            l.append(parts[1].lower())

    while True:
        a = input("Ingrese el nombre del producto que compró o escriba 'salir' para terminar:\n").lower()

        if a == 'salir':
            break

        if a in l:
            pc = float(input(f"Ingrese el valor que le cobraron por el producto '{a}':\n"))
            index = l.index(a)
            iva = float(lines[index].split(',')[2])
            vsi = pc / (1 + iva)
            vaiva = pc - vsi
            print(f'El costo del alimento {a} es: {vsi}')
            print(f'El valor del IVA es: {vaiva}')
        else:
            print('El alimento ingresado no está en el menú o catálogo de alimentos.')

    
if __name__ == '__main__':
    selec_producto()
    metodo()
