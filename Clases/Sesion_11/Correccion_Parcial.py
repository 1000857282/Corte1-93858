from random import choice as c

def repartir(deck):
    return c(deck)

def valor(card):
    jack=['J', 'Q','K']

    if card in jack: #si   la carta esta en jack
        card = 10
    elif card == 'A':
        card = 11
    else:
        card = int(card)
    return card

def conteo(mano):
    cartas = []
    for i in range(len(mano)):
        cartas.append(valor(mano[i]))
    print(cartas)
    #sum(cartas) pasa abajo
    print(f'Conteo: {sum(cartas)}')


def inicio():
    mano = []
    mano.append(repartir()) #para pedir numeros 
    mano.append(repartir())
    print(mano)
    conteo(mano)

    opc = 'y'
    while opc == 'y':
        opc= print('Quiere otra carta? : (y/n)')
        if opc == 'y':
            mano.append(repartir())
            print(mano)
        elif opc == 'n':
            break
        else:
            print('Opcion invalida')
            opc = 'y' #Refrescar la opcion y 
    # card = repartir()
    # v_card = valor(card)
    # print(v_card)


    # deck= 'A23456789JQK'
    # card = repartir(deck)
    # print(card)
    # card = repartir(deck)
    # print(card)



if __name__=='__main__':
    inicio()


