n=int(input('Cual es la cantidad de primos que desea generar: '))

primos='1 '
numeros=1
i=2
while numeros<n:
    for j in range(2,i+1,1):
        x=i%j
        if (x==0) and (i==j):
            primos+=str(f'{i} ')
            numeros+=1
        elif (x==0 and i!=0):
            break
    i+=1
print(primos)