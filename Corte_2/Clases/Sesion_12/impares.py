#Funcion rescursiva
#sumar los numeros naturales impares
#Doblar y desdoblar
#no se uitliza necesariamente el for
def impar(n):
    if n == 0: 
        return 1
    else:
        num = (2*n+1)+impar(n-1)
        return num

    # if n>0:
    #     num = (2*n+1)+impar(n-1)
    #     return
    # else:
    #     return 1



def main():
    num = int(input('Ingrese un número: '))
    resultado = impar(num)
    print(f'El resultado es : {resultado}')

if __name__=='__main__':
    main()