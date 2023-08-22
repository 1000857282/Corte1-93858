n =int(input("Ingrese la cantidad de numeros solicitados: "))
x =1; num=2
numero="1 "
while x<n:
    for i in range(2,num+1):
        primo = num%i
        if (primo==0 and num==i):
            numero+=str(f" {num} ,") #concatenar palabras --> unir palabras , str --> entero a texto
            #print(num)
            num+=1
            x+=1
        elif (primo==0 and num!=i):
            num+=1
            break
print(numero)