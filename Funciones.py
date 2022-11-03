from Estructura import Cuenta

cuenta = Cuenta()

def mostrarSaldo():
    print("Su saldo es de: ", cuenta.Saldo)

def deposito(monto):
    cuenta.Saldo += monto

def retiro(monto):
    cuenta.Saldo -= monto
    

