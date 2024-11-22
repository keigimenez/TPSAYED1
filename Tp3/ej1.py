""""

desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar 
su funcionamiento, imprimiendo la matriz luego de invocar a cada función:
a. Cargar números enteros en una matriz de N x N, ingresando los datos desde 
teclado. 
b. Ordenar en forma ascendente cada una de las filas de la matriz.
c. Intercambiar dos filas, cuyos números se reciben como parámetro.
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como 
parámetro.
g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.
h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo 
una lista con los números de las mismas.
NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera 
sea el valor ingresado.

"""

import random as rn

def cargar_matriz(N):
    return [[rn.randint(1, 100) for _ in range(N)] for _ in range(N)]

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def ordenar_filas(matriz):
    for fila in matriz:
        fila.sort()

def intercambiar_filas(matriz, f1, f2):
    matriz[f1], matriz[f2] = matriz[f2], matriz[f1]

def intercambiar_columnas(matriz, c1, c2):
    for fila in matriz:
        fila[c1], fila[c2] = fila[c2], fila[c1]

def trasponer_matriz(matriz):
    N = len(matriz)
    for i in range(N):
        for j in range(i + 1, N):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]

def promedio_fila(matriz, fila):
    return sum(matriz[fila]) / len(matriz[fila])

def porcentaje_impares_columna(matriz, columna):
    count_impares = sum(1 for fila in matriz if fila[columna] % 2 != 0)
    return (count_impares / len(matriz)) * 100

def diagonal_principal(matriz):
    N = len(matriz)
    for i in range(N):
        for j in range(N):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

def diagonal_secundaria(matriz):
    N = len(matriz)
    for i in range(N):
        for j in range(N):
            if matriz[i][j] != matriz[N - 1 - j][N - 1 - i]:
                return False
    return True

def columnas_palindromas(matriz):
    N = len(matriz)
    palindromas = []
    for c in range(N):
        if all(matriz[i][c] == matriz[N - 1 - i][c] for i in range(N)):
            palindromas.append(c)
    return palindromas

def main():
    N = int(input("Ingrese el tamaño de la matriz (N x N): "))
    matriz = cargar_matriz(N)

    print("\nMatriz cargada:")
    imprimir_matriz(matriz)

    ordenar_filas(matriz)
    print("\nMatriz después de ordenar filas:")
    imprimir_matriz(matriz)

    intercambiar_filas(matriz, 0, 1)
    print("\nMatriz después de intercambiar fila 0 y fila 1:")
    imprimir_matriz(matriz)

    intercambiar_columnas(matriz, 0, 1)
    print("\nMatriz después de intercambiar columna 0 y columna 1:")
    imprimir_matriz(matriz)

    trasponer_matriz(matriz)
    print("\nMatriz traspuesta:")
    imprimir_matriz(matriz)

    fila_promedio = int(input("\nIngrese el número de la fila para calcular su promedio: "))
    print(f"Promedio de la fila {fila_promedio}: {promedio_fila(matriz, fila_promedio)}")

    columna_impares = int(input("\nIngrese el número de la columna para calcular el porcentaje de impares: "))
    print(f"Porcentaje de elementos impares en la columna {columna_impares}: {porcentaje_impares_columna(matriz, columna_impares)}%")

    print(f"\nLa matriz es simétrica respecto a la diagonal principal: {diagonal_principal(matriz)}")
    print(f"La matriz es simétrica respecto a la diagonal secundaria: {diagonal_secundaria(matriz)}")

    palindromas = columnas_palindromas(matriz)
    print(f"Columnas palíndromas: {palindromas}")

main()