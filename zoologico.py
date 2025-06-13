class Animal:
    def __init__(self, nombre, edad, tipoAlimentacion):
        self.nombre = nombre
        self.edad = edad
        self.tipoAlimentacion = tipoAlimentacion

    def mostrarInfo(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Tipo de Alimentación: {self.tipoAlimentacion}")

    def comportamiento(self):
        print("Este animal tiene un comportamiento normal.")        

# Clase Ave hereda de Animal y redefine el comportamiento
class Ave(Animal):
    def comportamiento(self):
        print(f"{self.nombre} está volando.")

# Clase Mamifero hereda de Animal y redefine el comportamiento
class Mamifero(Animal):
    def comportamiento(self):
        print(f"{self.nombre} está caminando.")

# Clase Reptil hereda de Animal y redefine el comportamiento
class Reptil(Animal):
    def comportamiento(self):
        print(f"{self.nombre} está reptando.")

# Se crean objetos de cada tipo de animal
loro = Ave("Loro", 2, "Herbívoro")
tigre = Mamifero("Tigre", 5, "Carnívoro")
iguana = Reptil("Iguana", 3, "Omnívoro")

# Se recorren los animales mostrando su información y comportamiento
for animal in [loro, tigre, iguana]:
    animal.mostrarInfo()
    animal.comportamiento()
    print("-" * 30)
