"""

Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas 
en cada una de sus plantas durante una semana. De este modo, cada columna representa 
el día de la semana y cada fila a una de sus fábricas. Ejemplo:
(Lunes) (Martes) (Miércoles) (Jueves) (Viernes) (Sábado)
0 1 2 3 4 5
(Fábrica 1) 0 23 150 20 120 25 150
(Fábrica 2) 1 40 75 80 0 80 35
( . . . ) . . . . . . . . . . . . . . . . . .
(Fábrica 
n) 3 80 80 80 80 80 80
 Se solicita:
a. Crear una matriz con datos generados al azar para N fábricas durante una 
semana, considerando que la capacidad máxima de fabricación es de 150 
unidades por día y puede suceder que en ciertos días no se fabrique ninguna. 
b. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica. 
c. Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica).
d. Cuál es el día más productivo, considerando todas las fábricas combinadas.
e. Crear una lista por comprensión que contenga la menor cantidad fabricada 
por cada fábrica.

"""

import random as rn

def generar_matriz(fabricas, dias=6):
    return [[rn.randint(0, 150) for _ in range(dias + 1)] for _ in range(fabricas)]

def total_fabricado_por_fabrica(matriz):
    return [sum(fabrica) for fabrica in matriz]

def max_produccion(matriz):
    max_produccion = 0
    fabrica_max = -1
    dia_max = -1
    for i, fabrica in enumerate(matriz):
        for j, produccion in enumerate(fabrica):
            if produccion > max_produccion:
                max_produccion = produccion
                fabrica_max = i
                dia_max = j
    return fabrica_max, dia_max, max_produccion

def dia_mas_productivo(matriz):
    dias_produccion = [sum(fabrica[dia] for fabrica in matriz) for dia in range(len(matriz[0]))]
    dia_max = max(range(len(dias_produccion)), key=lambda i: dias_produccion[i])
    return dia_max, dias_produccion[dia_max]

def menor_fabricacion(matriz):
    return [min(fabrica) for fabrica in matriz]

def main():
    N = int(input("Ingrese el número de fábricas: "))
    if N <= 0:
        print("El número de fábricas debe ser un entero positivo.")
        return

    matriz_produccion = generar_matriz(N)
    print("\nMatriz de producción (fábrica x día):")
    for i, fabrica in enumerate(matriz_produccion):
        print(f"Fábrica {i+1}: {fabrica}")

    total_fabricado = total_fabricado_por_fabrica(matriz_produccion)
    for i, total in enumerate(total_fabricado):
        print(f"Total de bicicletas fabricadas por la Fábrica {i+1}: {total}")

    fabrica, dia, produccion_max = max_produccion(matriz_produccion)
    print(f"\nLa fábrica {fabrica+1} produjo el máximo de {produccion_max} bicicletas el día {dia+1}.")

    dia_max, produccion_dia_max = dia_mas_productivo(matriz_produccion)
    print(f"\nEl día más productivo fue el día {dia_max+1} con {produccion_dia_max} bicicletas fabricadas.")

    menores_fabricaciones = menor_fabricacion(matriz_produccion)
    print(f"\nMenor cantidad fabricada por cada fábrica: {menores_fabricaciones}")

main()
