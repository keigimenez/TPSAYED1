"""""

Eliminar de una lista de números enteros aquellos valores que se encuentren en 
una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista 
resultante. La función debe modificar la lista original sin crear una copia modificada.

"""

import random as rn

def eliminar_valores(lista_original, valores_a_eliminar):
    for valor in valores_a_eliminar:
        while valor in lista_original:
            lista_original.remove(valor)

def main():
    num = int(input("Ingrese un tamaño para la lista original: "))
    lista_original = [rn.randint(1, 20) for _ in range(num)]
    num_eliminar = int(input("Ingrese un valor específico a eliminar: "))
    valores_a_eliminar = [rn.randint(1, 20) for _ in range(5)]
    valores_a_eliminar.append(num_eliminar) 
    print("Lista original:", lista_original)
    print("Lista de valores a eliminar (incluyendo el valor ingresado):", valores_a_eliminar)
    eliminar_valores(lista_original, valores_a_eliminar)
    print("Lista resultante:", lista_original)

main()
