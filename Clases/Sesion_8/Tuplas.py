#args--->#todos lo parametros que no estan dentro de una variable
#**kwargs--> lo que yo defina como una variable

#Secuencia
def app(a,*args,**kwargs):
    print(args)
    print(kwargs)


if __name__=="__main__":
    app(1,2,3,4,5,7,9,x=1,b=2)#Parametros