# CICLO wHILE ---> CONTINUE
# NO TIENE DEFINIDO UN FINAL

n = int(input("Ingrese un numero: "))
i = 0
while i<n:
    i+=1 #siempre va dentro del while
    
    if i==4:
        continue #Omite el 4 porque le dice que se omita el print(i) osea que no lo imprima---> puede hacerse un bloque infinito 
    print(i)


    #PASS---> completa el codigo o evita que salga error, lleno el vacío que hay 
