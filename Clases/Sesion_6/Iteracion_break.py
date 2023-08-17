# CICLO WHILE ---> BREAK
# NO TIENE DEFINIDO UN FINAL

n = int(input("Ingrese un numero: "))

i = 0
while i<n:
    i+=1
    print(i)
    if i==4:
        break #rompe el ciclo
        