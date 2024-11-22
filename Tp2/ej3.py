"""""
Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), 
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista.

"""
def lista(N):
    return [i**2 for i in range(1, N+1)]

N = int(input("Ingresa el valor de N: "))

lista_cuadrados = lista(N)

print("Los últimos 10 valores de la lista son:", lista_cuadrados[-10:])
