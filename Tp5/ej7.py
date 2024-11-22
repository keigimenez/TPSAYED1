"""""""""

Escribir un programa que juegue con el usuario a adivinar un número. El programa 
debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para 
eso, cada vez que se introduce un valor se muestra un mensaje indicando si el número que tiene que 
adivinar es mayor o menor que el ingresado. Cuando consiga 
adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar 
el número. Si el usuario introduce algo que no sea un número se mostrará un 
mensaje en pantalla y se lo contará como un intento más

"""

import random as rn

def adivinar_numero():
    num_secreto = rn.randint(1, 500)
    intentos = 0

    while True:
        try:
            intento = int(input("Adivina el número (entre 1 y 500): "))
            intentos += 1
            if intento < num_secreto:
                print("El número secreto es mayor.")
            elif intento > num_secreto:
                print("El número secreto es menor.")
            else:
                print(f"¡Felicidades! Adivinaste el número {num_secreto} en {intentos} intentos.")
                break
        except ValueError:
            intentos += 1
            print("Entrada no válida. Por favor, ingresa un número.")

adivinar_numero()
