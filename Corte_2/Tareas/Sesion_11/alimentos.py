
def main_read1():
    f = open('Alimentos.txt','r')
    documento = f.read() #Read lee todo
    f.close()
    print(documento)




if __name__=='__main__':
    main_read1()