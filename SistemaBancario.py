class Cuentas:
    def __init__(self, num_cuenta, saldo):
        self.num_cuenta = num_cuenta
        self.saldo = saldo
    def mostrar_info(self):
        print(f"Número de Cuenta: {self.num_cuenta}")
        print(f"Saldo: {self.saldo}")
# Clase Corriente hereda de Cuentas y agrega el atributo 'sobregiro'
class Corriente(Cuentas):
    def __init__(self, num_cuenta, saldo, sobregiro):
        super().__init__(num_cuenta, saldo)
        self.sobregiro = sobregiro
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Sobregiros: {self.sobregiro}")
        print('-' * 30)
# Clase Ahorro hereda de Cuentas y agrega 'tasa_interes'
class Ahorro(Cuentas):
    def __init__(self, num_cuenta, saldo, tasa_interes):
        super().__init__(num_cuenta, saldo)
        self.tasa_interes = tasa_interes
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tasa de interés: {self.tasa_interes}")
        print('-' * 30)
# Clase Inversion hereda de Cuentas y agrega 'rendimiento'
class Inversion(Cuentas):
    def __init__(self, num_cuenta, saldo, rendimiento):
        super().__init__(num_cuenta, saldo)
        self.rendimiento = rendimiento
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Rendimiento: {self.rendimiento}")
        print('-' * 30)
# Lista con distintos tipos de cuentas
banco = [
    Corriente(2901482942, 200000, 500),
    Ahorro(2485029420, 5430000, '10%'),
    Inversion(5293502395, 99999999, 210000)
]
# Muestra información de todas las cuentas en el sistema bancario
print("Información del Sistema Bancario:")
print('-' * 30)
for cuenta in banco:
    cuenta.mostrar_info()
