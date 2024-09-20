"""""

 Escribir una función que reciba una lista como parámetro y devuelva True si la lista 
está ordenada en forma ascendente o False en caso contrario. Por ejemplo, 
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar 
además un programa para verificar el comportamiento de la función.

"""

import random as rn

def ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
        return True

def main():
    num = int(input("Ingrese un valor: "))
    lista_numeros = [rn.randint(1, 20) for _ in range(10)]
    letras = ['a', 'b', 'c', 'd', 'e', 'f']
    lista_letras = [letras[rn.randint(0, len(letras) - 1)] for _ in range(10)]

    print("Lista de números:", lista_numeros)
    print("¿Está ordenada la lista de números?:", ordenada(lista_numeros))

    print("Lista de letras:", lista_letras)
    print("¿Está ordenada la lista de letras?:", ordenada(lista_letras))

    return ordenada(lista_numeros), ordenada(lista_letras) 

main()
