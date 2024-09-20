"""""

Escribir funciones para:
a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa 
a través del teclado.
b. Recibir una lista como parámetro y devolver True si la misma contiene algún 
elemento repetido. La función no debe modificar la lista.
c. Recibir una lista como parámetro y devolver una nueva lista con los elementos 
únicos de la lista original, sin importar el orden. 
Combinar estas tres funciones en un mismo programa.

"""

import random as rn

def lista_aleatoria(n):
    lista = []
    for i in range(n):
        lista.append(rn.randint(1, 100))
    return lista

def repetidos(lista):
    for i in range(len(lista)):
        if lista[i] in lista[i + 1:]:
            return True
    return False

def elementos_unicos(lista):
    lista_unicos = []
    for elemento in lista:
        if elemento not in lista_unicos:
            lista_unicos.append(elemento)
    return lista_unicos

def main():
    try:
        n = int(input("Ingrese el valor de N: "))
        if n <= 0:
            print("Por favor, ingrese un número positivo.")
            return
            
        aleatoria = lista_aleatoria(n)
        print(f"Lista aleatoria generada: {aleatoria}") 

        if repetidos(aleatoria): 
            print("La lista contiene elementos repetidos.")
        else:
            print("La lista no contiene elementos repetidos.")

        lista_unica = elementos_unicos(aleatoria)  
        print(f"Lista con elementos únicos: {lista_unica}")

    except ValueError:
        print("Por favor, ingrese un número válido.")

main()




