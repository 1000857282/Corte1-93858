n =int(input("Ingrese la cantidad de numeros solicitados: "))
x =1; num=2#que inicie en 1
numero="1 "
while x<n:#mientras 1 sea menor al numero solicitado
    for i in range(2,num+1):#para i en un rango de 2 hasta el numero 2 
        primo = num%i#2 dividalo en 2
        if (primo==0 and num==i):#si el residuo es 0 y el numero = numero--> 2=2
            numero+=str(f" {num} ,") #concatenar palabras --> unir palabras , str --> entero a texto
            #print(num)
            num+=1#aumenteme el numero 2
            x+=1#contador aumenta
        elif (primo==0 and num!=i):
            num+=1
            break
print(numero)