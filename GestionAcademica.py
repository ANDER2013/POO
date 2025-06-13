class Universidad:
    def __init__(self, nombre, id, correo):
        self.nombre = nombre
        self.id = id
        self.correo = correo
    def mostrarInfo(self):
        print(f"Nombre: {self.nombre}")
        print(f"ID: {self.id}")
        print(f"Correo: {self.correo}")
# Clase Estudiante hereda de Universidad y agrega 'carrera' y 'promedio'
class Estudiante(Universidad):
    def __init__(self, nombre, id, correo, carrera, promedio):
        super().__init__(nombre, id, correo)
        self.carrera = carrera
        self.promedio = promedio
    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Carrera: {self.carrera}")
        print(f"Promedio: {self.promedio}")
# Clase Docente hereda de Universidad y agrega 'materia'
class Docente(Universidad):
    def __init__(self, nombre, id, correo, materia):
        super().__init__(nombre, id, correo)
        self.materia = materia
    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Materia que imparte: {self.materia}")
# Clase Administrativo hereda de Universidad y agrega 'departamento'
class Administrativo(Universidad):
    def __init__(self, nombre, id, correo, departamento):
        super().__init__(nombre, id, correo)
        self.departamento = departamento
    def mostrarInfo(self):
        super().mostrarInfo()
        print(f"Departamento: {self.departamento}")
# Se crean objetos para cada tipo de miembro de la universidad
Estudiante1 = Estudiante("Carla", "EST123", "carla@utpl.edu.ec", "Medicina", 9.2)
docente1 = Docente("Ramiro", "MGI321", "ramirez@utpl.edu.ec", "POO")
admin1 = Administrativo("Marco", "ADM789", "marco@utpl.edu.ec", "Ingenierías")
# Lista que almacena todos los miembros
miembros = [Estudiante1, docente1, admin1]
# Se recorre la lista mostrando la información completa de cada persona
for persona in miembros:
    print("-" * 30)
    persona.mostrarInfo()
