class Hotel:
    def __init__(self, num_habitacion, precio_noche):
        self.num_habitacion = num_habitacion
        self.precio_noche = precio_noche
    def mostrar_info(self):
        print(f"Número de habitación: {self.num_habitacion}")
        print(f"Precio por noche: {self.precio_noche}")
# Clase Suites hereda de Hotel y agrega el atributo 'jacuzzi'
class Suites(Hotel):
    def __init__(self, num_habitacion, precio_noche, jacuzzi):
        super().__init__(num_habitacion, precio_noche)
        self.jacuzzi = jacuzzi
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tiene Jacuzzi?: {self.jacuzzi}")
        print('-' * 40)
# Clase Familiares hereda de Hotel y agrega 'capacidad_niños'
class Familiares(Hotel):
    def __init__(self, num_habitacion, precio_noche, capacidad_ninos):
        super().__init__(num_habitacion, precio_noche)
        self.capacidad_ninos = capacidad_ninos
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Capacidad para niños: {self.capacidad_ninos}")
        print('-' * 40)
# Clase Estandar hereda de Hotel y agrega 'vista'
class Estandar(Hotel):
    def __init__(self, num_habitacion, precio_noche, vista):
        super().__init__(num_habitacion, precio_noche)
        self.vista = vista
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tienen vista?: {self.vista}")
        print('-' * 40)
# Lista con diferentes tipos de habitaciones creadas
habitaciones = [
    Suites(510, 380, 'Sí'),
    Familiares(302, 220, 4),
    Estandar(95, 100, 'Sí')
]
print("Información del Sistema de Reservas de Hotel:")
print('-' * 40)
# Se recorre cada habitación para mostrar su información
for habitacion in habitaciones:
    habitacion.mostrar_info()
