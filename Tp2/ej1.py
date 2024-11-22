"""""

Desarrollar cada una de las siguientes funciones y escribir un programa que permita 
verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:
a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos
 también será un número al azar de dos dígitos.
b. Calcular y devolver el producto de todos los elementos de la lista anterior.
c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar 
se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar 
listas auxiliares.
d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas 
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].

"""

import random as rn

def cargar_lista_aleatoria():
    cantidad_elementos = rn.randint(10, 99) 
    lista = [rn.randint(10, 80) for _ in range(cantidad_elementos)]
    return lista

def calcular_producto(lista):
    producto = 1
    for numero in lista:
        producto *= numero
    return producto

def eliminar_apariciones(lista, valor):
    while valor in lista:
        lista.remove(valor)

def es_capicua(lista):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda < derecha:
        if lista[izquierda] != lista[derecha]:
            return False
        izquierda += 1
        derecha -= 1
    return True

def main():
    while True:
        try:
            lista_numeros = cargar_lista_aleatoria()
            print("Lista cargada:", lista_numeros)

            producto = calcular_producto(lista_numeros)
            print("Producto de los elementos:", producto)

            valor_a_eliminar = int(input("Ingrese el valor a eliminar de la lista (o -1 para salir): "))
            if valor_a_eliminar == -1:
                print("Saliendo...")
                break
            eliminar_apariciones(lista_numeros, valor_a_eliminar)
            print("Lista después de eliminar", valor_a_eliminar, ":", lista_numeros)

            capicua = es_capicua(lista_numeros)
            print("La lista es capicúa:", capicua)

        except ValueError:
            print("Por favor, ingrese un número válido.")

main()