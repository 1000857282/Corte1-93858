def resistencia(colores):
    bandas=['negro','cafe','rojo','naranja','amarillo'
    ,'verde','azul','morado','gris','blanco']

    b1=bandas.index(colores[0])
    b2=bandas.index(colores[1])
    b3=bandas.index(colores[2])
    r=(b1*10+b2)*(10**b3)

    if r//(10**9)>=1:
        print(f'Resultado: {r/10**9} Giga-ohms')
    elif r//(10**6)>=1:
        print(f'Resultado: {r/10**6} Mega-ohms')
    elif r//(10**3)>=1:
        print(f'Resultado: {r/10**3} Kilo-ohms')
    else:
        print(f'Resultado: {r} ohms')

if __name__=="__main__":
    colores=[]
    for i in range(3):
        colores.append(input(f'Color {i}:'))
    print(colores)
    resistencia(colores)