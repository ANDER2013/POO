class Producto:
    def __init__(self, nombre, marca, precio):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
    def calcularPrecio(self):
        iva = 0.15  # IVA del 15%
        return self.precio * (1 + iva)
    def mostrarInfo(self):
        print(f"Producto: {self.nombre}")
        print(f"Marca: {self.marca}")
        print(f"Precio sin IVA: ${self.precio:.2f}")
# Clase Televisor hereda de Producto y agrega atributo 'tamaño'
class Televisor(Producto):
    def __init__(self, nombre, marca, precio, tamaño):
        super().__init__(nombre, marca, precio)
        self.tamaño = tamaño  # Nuevo atributo exclusivo
    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Tamaño: {self.tamaño} pulgadas")
# Clase Telefono hereda de Producto y agrega atributo 'sim'
class Telefono(Producto):
    def __init__(self, nombre, marca, precio, sim):
        super().__init__(nombre, marca, precio)
        self.sim = sim  # Nuevo atributo exclusivo
    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Número de SIM: {self.sim}")
# Clase Laptop hereda de Producto y agrega atributo 'ram'
class Laptop(Producto):
    def __init__(self, nombre, marca, precio, ram):
        super().__init__(nombre, marca, precio)
        self.ram = ram  # Nuevo atributo exclusivo
    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Memoria RAM: {self.ram} GB")
# Se crean objetos de cada clase hija con sus respectivos atributos
tv = Televisor("TELEVISOR", "LG", 550, 55)
celular = Telefono("CELULAR", "SAMSUNG", 200, 2)
laptop = Laptop("LAPTOP", "ASUS", 700, 8)
# Lista con los productos creados
productos = [tv, celular, laptop]
# Se recorre la lista y se muestra la información de cada producto con su precio con IVA
for producto in productos:
    print("-" * 30)
    producto.mostrarInfo()
    print(f"Precio con IVA: ${producto.calcularPrecio():.2f}")
