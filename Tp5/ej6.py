"""""""""""

El método index permite buscar un elemento dentro de una lista, devolviendo la 
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se 
produce una excepción de tipo ValueError. Desarrollar un programa que cargue 
una lista con números enteros ingresados a través del teclado (terminando con -1) 
y permita que el usuario ingrese el valor de algunos elementos para visualizar la 
posición que ocupan, utilizando el método index. Si el número no pertenece a la 
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el 
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.

"""

def cargar_lista():
    lista = []
    print("Ingresa números enteros para cargar la lista (termina con -1):")
    while True:
        try:
            numero = int(input("Número: "))
            if numero == -1:
                break
            lista.append(numero)
        except ValueError:
            print("Por favor, ingresa un número entero válido.")
    return lista

def buscar_elementos(lista):
    errores = 0
    while errores < 3:
        try:
            numero = int(input("Ingresa el número a buscar en la lista: "))
            posicion = lista.index(numero)
            print(f"El número {numero} se encuentra en la posición {posicion}.")
        except ValueError:
            errores += 1
            print(f"Error: el número no se encuentra en la lista. (Errores: {errores}/3)")
        if errores == 3:
            print("Se alcanzó el límite de errores. Proceso terminado.")
            break

lista_numeros = cargar_lista()
print("Lista cargada:", lista_numeros)
buscar_elementos(lista_numeros)
