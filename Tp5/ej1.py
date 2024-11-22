""""""""""

Desarrollar una función para ingresar a través del teclado un número natural. La 
función rechazará cualquier ingreso inválido de datos utilizando excepciones y 
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese 
número sea entero y que sea mayor que 0, mostrando un mensaje con la razón 
exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea 
correcto. Escribir también un programa que permita probar el correcto funcionamiento de la misma.

"""

import os

def limpiar_pantalla():
    """Limpia la pantalla de la terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def num_natural():
    while True:
        try:
            limpiar_pantalla()
            entrada = input("Ingrese un número natural: ")
            numero = int(entrada)
            if numero <= 0:
                raise ValueError("El número debe ser mayor que 0.")
            print(f"se ingreso el numero: {entrada}")
            return 
        except ValueError as e:
            print(f"Error: {e}. Intente de nuevo.")
        except Exception as e:
            print(f"Error inesperado: {e}. Intente de nuevo.")
    return

num_natural()
