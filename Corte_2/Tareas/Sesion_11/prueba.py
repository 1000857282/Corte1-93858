# Definir un diccionario con los valores del IVA para diferentes tipos de alimentos
iva_alimentos = {
    "exento": 0,
    "superreducido": 0.05,
    "reducido": 0.1,
    "normal": 0.21
}

# Leer el archivo Alimentos.txt y organizar los artículos según el valor del IVA
with open("Alimentos.txt", "r") as archivo:
    lineas = archivo.readlines()

productos = {}
for linea in lineas:
    nombre, tipo_iva = linea.strip().split(",")
    productos[nombre] = tipo_iva

# Función para calcular el valor bruto de un producto
def calcular_valor_bruto(nombre_producto, valor_neto):
    tipo_iva_producto = productos.get(nombre_producto, "normal")
    iva = iva_alimentos.get(tipo_iva_producto, 0)
    valor_base = valor_neto / (1 + iva)
    valor_iva = valor_neto - valor_base
    return valor_base, valor_iva

# Bucle principal para que el programa funcione continuamente
while True:
    producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
    
    if producto.lower() == "salir":
        break
    
    if producto in productos:
        valor_neto = float(input("Ingrese el valor neto del producto: "))
        valor_base, valor_iva = calcular_valor_bruto(producto, valor_neto)
        print(f"Valor base del producto: {valor_base:.2f}")
        print(f"Valor del IVA: {valor_iva:.2f}")
    else:
        print("Producto no encontrado en la lista. Por favor, ingrese un producto válido.")

print("¡Gracias por usar el programa!")