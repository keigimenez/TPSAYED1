""""

Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los 
elementos de la primera que sean impares. El proceso deberá realizarse utilizando 
la función filter(). Imprimir las dos listas por pantalla. 

"""

import random as rn

num = [rn.randint(1, 100) for _ in range(20)]

impares = list(filter(lambda x: x % 2 != 0, num))

def main():
    print("Lista de números aleatorios:", num)
    print("Lista de números impares:", impares)

main()
