""""

Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se 
ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de carga. Se solicita:
a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe 
aparecer una sola vez en el informe.
b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus 
ingresos. Mostrar los registros de entrada al club antes y después de 
eliminarlo. Informar cuántos ingresos se eliminaron

"""
def registro_ingresos(ingresos):
    while True:
        numero_socio = input("Ingrese el número de socio (5 dígitos) o 0 para finalizar: ")
        if numero_socio == "0":
            break
        if numero_socio in ingresos:
            ingresos[numero_socio] += 1
        else:
            ingresos[numero_socio] = 1
    return ingresos

def mostrar_ingresos(ingresos):
    print("\nRegistros de ingresos:")
    for socio, cantidad in ingresos.items():
        print(f"Socio {socio}: {cantidad} ingresos")

def eliminar_socio(ingresos, socio_baja):
    if socio_baja in ingresos:
        eliminados = ingresos.pop(socio_baja)
        print(f"\nSe eliminaron {eliminados} ingresos del socio {socio_baja}.")
    else:
        print(f"\nEl socio {socio_baja} no tiene registros.")
    return eliminados if socio_baja in ingresos else 0

def menu():
    ingresos = {}
    while True:
        print("\nMenú:")
        print("1. Registrar ingresos")
        print("2. Mostrar ingresos")
        print("3. Eliminar socio")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ingresos = registro_ingresos(ingresos)
        elif opcion == "2":
            mostrar_ingresos(ingresos)
        elif opcion == "3":
            socio_baja = input("Ingrese el número de socio que se dio de baja: ")
            eliminados = eliminar_socio(ingresos, socio_baja)
            print(f"\nTotal de ingresos eliminados: {eliminados}")
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

menu()
