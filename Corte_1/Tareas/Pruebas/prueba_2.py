class Producto:
    def init(self, nombre, precio, cantidad_disponible=0):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def obtener_info(self):
        return f"{self.nombre} - Precio: ${self.precio} - Disponibles: {self.cantidad_disponible}"

    def restar_cantidad(self, cantidad):
        if self.cantidad_disponible >= cantidad:
            self.cantidad_disponible -= cantidad
            return True
        else:
            return False

    def verificar_disponibilidad(self, cantidad):
        return self.cantidad_disponible >= cantidad


class Snack(Producto):
    def init(self, nombre, precio, tipo, cantidad_disponible=0):
        super().init(nombre, precio, cantidad_disponible)
        self.tipo = tipo

    def obtener_info(self):
        info_padre = super().obtener_info()
        return f"{info_padre} - Tipo: {self.tipo}"


class Bebida(Producto):
    def init(self, nombre, precio, tamaño, cantidad_disponible=0):
        super().init(nombre, precio, cantidad_disponible)
        self.tamaño = tamaño

    def obtener_info(self):
        info_padre = super().obtener_info()
        return f"{info_padre} - Tamaño: {self.tamaño}"


class MaquinaDispensadora:
    def init(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def realizar_venta(self, producto, cantidad):
        if producto.verificar_disponibilidad(cantidad):
            producto.restar_cantidad(cantidad)
            return producto.precio * cantidad
        else:
            return 0

    def total_ventas(self):
        return sum(producto.precio * (producto.cantidad_disponible - 1) for producto in self.productos if producto.cantidad_disponible > 0)


def main():
    # Crear productos
    snack1 = Snack("Galletas", 2.5, "Dulce", 10)
    snack2 = Snack("Papas fritas", 1.8, "Salado", 15)
    bebida1 = Bebida("Refresco", 1.0, "Pequeño", 20)
    bebida2 = Bebida("Agua", 0.8, "Grande", 12)

    # Crear máquina dispensadora
    maquina = MaquinaDispensadora()

    # Agregar productos a la máquina
    maquina.agregar_producto(snack1)
    maquina.agregar_producto(snack2)
    maquina.agregar_producto(bebida1)
    maquina.agregar_producto(bebida2)

    # Mostrar información de los productos en la máquina
    for producto in maquina.productos:
        print(producto.obtener_info())

    # Realizar una venta
    venta_total = maquina.realizar_venta(snack2, 5)
    print(f"Venta realizada. Total: ${venta_total}")

    # Mostrar información actualizada de los productos en la máquina
    for producto in maquina.productos:
        print(producto.obtener_info())

    # Mostrar total de ventas acumuladas
    print(f"Total de ventas acumuladas: ${maquina.total_ventas()}")