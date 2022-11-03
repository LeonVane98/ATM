import Funciones as transac
from Estructura import Cuenta

cuenta = Cuenta()
codigo = '0241'
numTarjeta = '125521'

def retirar():
    print("Retirar saldo")
    monto = int(input("Ingrese el monto a retirar: "))
    if (monto %100 != 0):
        print("El retiro debe ser en multiplos de 100")
    if(monto > cuenta.Saldo):
        print("No posee suficientes fondos...")
        transac.mostrarSaldo()
    else:
        transac.retiro(monto)
        transac.mostrarSaldo()

def depositar():
    print("Depositar saldo")
    monto = int(input("Ingrese el monto a depositar: "))
    if (monto %100 !=0):
        print("El retiro debe ser en multiplos de 100")
    else:
        transac.deposito(monto)
        transac.mostrarSaldo()
    
def menu():
    numero = input("Ingrese su numero de tarjeta: ")
    clave = input("Ingrese su clave: ")
    if (clave == codigo and numero == numTarjeta):
        print("""Seleccione su opcion:
        ************
        1. Ver saldo
        2. Depositar
        3. Retirar
        4. Salir
        ************
        """)
        while True:
            try:
                opcion = int(input("Seleccione una opcion: "))
            except: 
                print("Opcion invalida...")
                continue
            else:
                if opcion == 1:
                    transac.mostrarSaldo()
                elif opcion == 2:
                    depositar()
                elif opcion == 3:
                    retirar()
                elif opcion == 4:
                    print("Hasta la vista, baby...")
                    break
    else:
        print("Clave equivocada, intente de nuevo")
        menu()  
menu()


    
