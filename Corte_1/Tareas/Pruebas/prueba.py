class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def obtener_informacion(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"

    def restar_cantidad(self, cantidad_a_restar):
        if cantidad_a_restar>0 and cantidad_a_restar<= self.cantidad:
            self.cantidad -= cantidad_a_restar
            return True
        else:
            print("Error: No hay suficiente cantidad disponible.")
            return False

    def verificar_disponibilidad(self, cantidad_solicitada):
        return cantidad_solicitada <= self.cantidad


class Snack(Producto):
    def __init__(self, nombre, precio, cantidad, tipo):
        super().__init__(nombre, precio, cantidad)
        self.tipo = tipo

    def obtener_informacion(self):
        return f"{super().obtener_informacion()}, Tipo: {self.tipo}"


class Bebida(Producto):
    def __init__(self, nombre, precio, cantidad, marca, tamaño):
        super().__init__(nombre, precio, cantidad)
        self.marca = marca
        self.tamaño = tamaño

    def obtener_informacion(self):
        return f"{super().obtener_informacion()}, Marca: {self.marca}, Tamaño: {self.tamaño}"


class MaquinaDispensadora:
    def __init__(self):
        self.productos = []  # Lista para almacenar objetos Producto
        self.total_ventas = 0

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado a la máquina.")

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.verificar_disponibilidad(cantidad):
                    venta_total = cantidad * producto.precio
                    producto.restar_cantidad(cantidad)
                    self.total_ventas += venta_total
                    print(f"Venta realizada: {cantidad} {producto.nombre} por un total de {venta_total}.")

    def obtener_total_ventas(self):
        return f"Total de ventas: {self.total_ventas}"


# Ejemplo de uso:

snack1 = Snack('Galletas', 2.5, 10, 'Salado')
bebida1 = Bebida('Refresco', 1.75, 20, 'Coca-Cola', '500ml')

maquina = MaquinaDispensadora()
maquina.agregar_producto(snack1)
maquina.agregar_producto(bebida1)

maquina.realizar_venta('Galletas', 3)
maquina.realizar_venta('Refresco', 2)

print(snack1.obtener_informacion())
print(bebida1.obtener_informacion())
print(maquina.obtener_total_ventas())