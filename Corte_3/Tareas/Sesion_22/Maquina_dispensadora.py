#--------------------CLASE-PRODCUCTO
class Producto:
    def __init__(self,nombre:str, precio:float,cantidad_disponible:int):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad_disponible = cantidad_disponible
    
    #------------METODO-SETTERS : MODIFICA-----------------
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setPrecio(self,precio):
        self.__precio = precio
    def setCantidadDisponible(self, cantidad_disponible):
        self.__cantidad_disponible = cantidad_disponible

    #------------METODO-GETTER : OBTIENE--------------------
    def getNombre(self):
        return self.__nombre
    def getPrecio(self):
        return self.__precio
    def getCantidadDisponible(self):
        return self.__cantidad_disponible
    
    #--------------METODO-SOBRE-CARGA-------------------------
    def info_producto(self):
        return (f'Producto: {self.getNombre()}\n'
        f'Precio: {self.getPrecio()}\n'
        f'Cantidad disponible: {self.getCantidadDisponible()}\n')
    
    #--------------METODOS--------------------------
        
    def restar_cantidad(self, cantidad:int): 
        if self.verificar_disponibilidad(cantidad)== True:
            if cantidad > 0 and cantidad <= self.__cantidad_disponible:
                self.__cantidad_disponible -= cantidad
                return True
            else: 
                return False


    def verificar_disponibilidad(self,cantidad):
        if self.getCantidadDisponible()>=cantidad:
            print(f'Se encuentra disponible {self.getCantidadDisponible()} de {self.getNombre()}')
            return True
        else:
            print('El producto no se encuentra disponible para la cantidad solicitada ')
        return False

#--------------------CLASE- SNACK--------------------------
class Snack(Producto):
    def __init__(self, nombre: str, precio: float, cantidad_disponible: int, tipo: str):
        super().__init__(nombre, precio, cantidad_disponible)
        self.__tipo = tipo
    
    #------------METODO-SETTERS : MODIFICA-----------------
    def setTipo(self,tipo):
        self.__tipo  = tipo

    #------------METODO-GETTER : OBTIENE--------------------
    def getTipo(self):
        return self.__tipo
    
    #-------------------SOBRECARGA-METODOS-------------------
    def info_producto(self):
        return (f'{super().info_producto()}' #super() para obtener información de la clase base
                f'Tipo: {self.getTipo()}\n')
    
#--------------------CLASE- BEBIDA--------------------------
class Bebida(Producto):
    def __init__(self, nombre: str, precio: float, cantidad_disponible: int, clase: str, tamaño:str):
        super().__init__(nombre, precio, cantidad_disponible)
        self.__clase = clase
        self.__tamaño = tamaño
    
    #------------METODO-SETTERS : MODIFICA-----------------
    def setClase(self,clase):
        self.__clase  = clase
    def setTamaño(self,tamaño):
        self.__tamaño = tamaño

    #------------METODO-GETTER : OBTIENE--------------------
    def getClase(self):
        return self.__clase
    def getTamaño(self):
        return self.__tamaño
    
    #------------------SOBRECARGA--METODOS------------------
    def info_producto(self):
        return (f'{super().info_producto()}'
                f'Clase: {self.getClase()}\n'
                f'Tamaño: {self.getTamaño()}\n')

#--------------------CLASE-DISPENSADORA---------------------

class Dispensadora:
    def __init__(self):
        self.__producto = []
        self.__total_ventas = 0

    #------------METODO-SETTERS : MODIFICA-----------------
    def setProducto(self, producto):
        self.__producto = producto
    def setTotalVentas(self, total_ventas: int):#----------------------REVISAR ERROR
        self.__total_ventas = total_ventas

    #------------METODO-GETTER : OBTIENE--------------------
    def getProducto(self):
        return self.__producto
    def getTotalVentas(self):
        return self.__total_ventas
 
    #----------------METODOS--------------------------------
    def agregar_producto(self,item: object):
        self.__producto.append(item) #ITEM--> es lo que hay en la dispensadora
        return self.__producto
        
    def realizar_venta(self, compra, cantidad:int ):
        for item in self.__producto: #Para cada item en la lista producto
            if item.getNombre() == compra.getNombre(): #Quiero verificar que el producto que quiero comprar este en el item(que es la dispensadora)
                if item.verificar_disponibilidad(cantidad) == True: 
                    item.restar_cantidad(cantidad)#Me retone True, la cantidad que me queda no porque aqui no me sirve conocerla
                    venta_total = item.getPrecio()*cantidad
                    self.setTotalVentas += venta_total #total de vnetas es 0 se le va agregar la venta total
                    print(f"Venta realizada: {cantidad} {item.getNombre()} por un total de {venta_total}.")

    def obtener_total_venta(self):
        return f'Total de ventas: {self.getTotalVentas()}'

    

def main():
    snack1 = Snack('Chocorramo', 2700, 5, 'Dulce')
    snack2 = Snack('Papas', 2000, 10, 'Salado')
    bebida1 = Bebida('Cristal', 2800, 6, 'Agua', '250ml')
    bebida2 = Bebida('Cocacola', 4000, 8, 'Gaseosa', '600ml')

    maquina = Dispensadora()
    maquina.agregar_producto(snack1)
    maquina.agregar_producto(snack2)
    maquina.agregar_producto(bebida1)
    maquina.agregar_producto(bebida2)
   

    print('\n--------------BIENVENIDOS-A-VENTAS-NICOL------------------------\n') 
    while 1:
        n = input('Elija una opcion: \n'
            f'1. Snack \n'
            f'2. Bebidas \n'
            f'Exit para salir => ').lower()
        
        if n == 'exit':
            break

        elif n == '1':
            print('\n-----------------------------------\n')
            print(f'1.{snack1.info_producto()}')
            print(f'2.{snack2.info_producto()}')
            print('\n-----------------------------------\n')

            opc = input('Quiere comprar un Sanck? (y/n) ')
            if opc == 'y':
                pro = input('Elija la opcion del snack que quiere comprar: \n'
                            f'1. {snack1.getNombre()}\n'
                            f'2. {snack2.getNombre()}\n')
                if pro == '1':
                    comp = int(input('Ingrese la cantidad del producto: '))
                    maquina.realizar_venta(snack1, comp)

                elif pro == '2':
                    comp = int(input('Ingrese la cantidad del producto: '))
                    maquina.realizar_venta(snack2, comp)
                    
                else:
                    print('Ingreso una opción invalida')
            else:
                break

        elif n == '2':
            print('\n-----------------------------------\n')
            print(f'1.{bebida1.info_producto()}')
            print(f'2.{bebida2.info_producto()}')
            print('\n-----------------------------------\n')

            opc = input('Quiere comprar un Bebida? (y/n) ')
            if opc == 'y':
                pro = input('Elija la opcion de la bebida que quiere comprar: \n'
                            f' 1. {bebida1.getNombre()}\n'
                            f' 2. {bebida2.getNombre()}\n')
                if pro == '1':
                    comp = int(input('Ingrese la cantidad del producto: '))
                    maquina.realizar_venta(bebida1, comp)

                elif pro == '2':
                    comp = int(input('Ingrese la cantidad del producto: '))
                    maquina.realizar_venta(bebida2, comp)
                    
                else:
                    print('Ingreso una opción invalida')
            else:
                break
        else:
            print('\n-----------------------------------\n')
            print('Ingreso un opción incorrecta')
            print('\n-----------------------------------\n')


if __name__=='__main__':
    main()