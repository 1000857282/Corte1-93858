#Funcion recursiva
#no se uitliza necesariamente el for
#Doblar y desdoblar
#Factorial

def factorial (x):
    if x > 0:
        fac = x*factorial(x-1) #5 factorial de (5-1) ---> me llama la función
        print(fac)
    else:
        return 1 #Le digo queme retorne 1 porque 1 * 0 = 0 y me sale error
    return fac


def main():
    num = int(input('Ingrese un número: '))
    resultado = factorial(num)
    print(f'El resultado es : {resultado}')

if __name__=='__main__':
    main()