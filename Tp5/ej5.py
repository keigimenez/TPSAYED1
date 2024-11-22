"""""""""

La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del 
módulo math. Escribir un programa que utilice esta función para calcular la raíz 
cuadrada de un número cualquiera ingresado a través del teclado. El programa 
debe utilizar manejo de excepciones para evitar errores si se ingresa un número 
negativo.

"""

import math

def calcular_raiz():
    try:
        num = float(input("Ingresa un número: "))
        if num < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        raiz_cuadrada = math.sqrt(num)
        print(f"La raíz cuadrada de {num} es {raiz_cuadrada}")
    except ValueError as e:
        print(f"Error: {e}")

calcular_raiz()
