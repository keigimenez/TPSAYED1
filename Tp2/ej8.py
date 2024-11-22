"""""

Utilizar la técnica de listas por comprensión para construir una lista con todos los 
números impares comprendidos entre 100 y 200.

"""

impares = [num for num in range(100, 201) if num % 2 != 0]

print(impares)