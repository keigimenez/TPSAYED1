"""""

   Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una 
   fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros 
   correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones 
   ni agregados, desarrollar programas que permitan:

   a. Sumar N días a una fecha.

   b. Calcular la cantidad de días existentes entre dos fechas cualquiera.

"""

def bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def diasymes(mes, anio):
    if mes == 2:
        return 29 if bisiesto(anio) else 28
    elif mes in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def diasiguiente(dia, mes, anio):
    if dia < diasymes(mes, anio):
        return dia + 1, mes, anio
    elif mes < 12:
        return 1, mes + 1, anio
    else:
        return 1, 1, anio + 1

def sumar_n_dias(dia, mes, anio, n):
    for _ in range(n):
        dia, mes, anio = diasiguiente(dia, mes, anio)
    return dia, mes, anio

def comparar_fechas(d1, m1, a1, d2, m2, a2):
    if a1 < a2 or (a1 == a2 and m1 < m2) or (a1 == a2 and m1 == m2 and d1 < d2):
        return -1 
    elif a1 == a2 and m1 == m2 and d1 == d2:
        return 0  
    else:
        return 1  

def dias_entre_fechas(d1, m1, a1, d2, m2, a2):
    contador = 0
    while comparar_fechas(d1, m1, a1, d2, m2, a2) != 0:
        d1, m1, a1 = diasiguiente(d1, m1, a1)
        contador += 1
    return contador

def main():
    while True:
        try:
            dia = int(input("Ingrese el dia: "))
            mes = int(input("Ingrese un mes: "))
            anio = int(input("Ingrese un año: "))
            op = int(input("Elija una opción: 1) Sumar N días 2) Calcular días entre dos fechas: "))
            
            if op == 1:
                N = int(input("Ingrese la cantidad de días a sumar: "))
                n_dia, n_mes, n_anio = sumar_n_dias(dia, mes, anio, N)
                print(f"Fecha después de sumar {N} días: {n_dia}/{n_mes}/{n_anio}")
            elif op == 2:
                dia2 = int(input("Ingrese el día de la segunda fecha: "))
                mes2 = int(input("Ingrese el mes de la segunda fecha: "))
                anio2 = int(input("Ingrese el año de la segunda fecha: "))
                dias = dias_entre_fechas(dia, mes, anio, dia2, mes2, anio2)
                print(f"Días entre {dia}/{mes}/{anio} y {dia2}/{mes2}/{anio2}: {dias}")
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
            break

main()