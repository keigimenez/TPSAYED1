""""

 Desarrollar un programa que permita realizar reservas en una sala de cine de N 
filas con M butacas por cada fila. Desarrollar las siguientes funciones y utilizarlas 
en un mismo programa:
mostrar_butacas: Mostrará por pantalla el estado de cada una de las butacas 
del cine. Esta función deberá ser invocada antes de que se realice la reserva, y 
se volverá a invocar luego de la misma con los estados actualizados.
reservar: Deberá recibir una matriz y la butaca seleccionada, y actualizará la 
sala en caso de estar disponible dicha butaca. La función devolverá True/False 
si logró o no reservar la butaca.
cargar_sala: Recibirá una matriz como parámetro y la cargará con valores 
aleatorios para simular una sala con butacas ya reservadas.
butacas_libres: Recibirá como parámetro la matriz y retornará cuántas butacas desocupadas hay en la sala.
butacas_contiguas: Buscará la secuencia más larga de butacas libres contiguas en una misma fila y
devolverá las coordenadas de inicio de la misma. 

"""

import random as rn

def mostrar_butacas(sala):
    for fila in sala:
        print(' '.join(fila))

def reservar(sala, fila, butaca):
    if sala[fila][butaca] == 'Libre':
        sala[fila][butaca] = 'Reservado' 
        return True
    return False

def cargar_sala(n, m):
    sala = [['Libre' if rn.random() < 0.8 else 'Reservado' for _ in range(m)] for _ in range(n)]
    return sala

def butacas_libres(sala):
    libres = 0
    for fila in sala:
        libres += fila.count('Libre')
    return libres

def butacas_contiguas(sala):
    coordenadas = []
    for i, fila in enumerate(sala):
        count = 0
        for j in range(len(fila)):
            if fila[j] == 'Libre':
                count += 1
                if count == 1:
                    inicio = j
            else:
                if count > 1:
                    coordenadas.append((i, inicio))
                count = 0
        if count > 1:  # Para el caso de que la fila termine con butacas libres
            coordenadas.append((i, inicio))
    return coordenadas

def main():
    N = int(input("Ingrese el número de filas: "))
    M = int(input("Ingrese el número de butacas por fila: "))
    sala = cargar_sala(N, M)
    
    print("Estado inicial de las butacas:")
    mostrar_butacas(sala)
    while True:
        try:
            fila_reserva = int(input(f"Ingrese el número de fila para la reserva (1 a {N}): ")) - 1
            butaca_reserva = int(input(f"Ingrese el número de butaca para la reserva (1 a {M}): ")) - 1

            if fila_reserva < 0 or fila_reserva >= N or butaca_reserva < 0 or butaca_reserva >= M:
                print("Número de fila o butaca inválido. Intente de nuevo.")
                continue

            if reservar(sala, fila_reserva, butaca_reserva):
                print(f"Reserva exitosa en la fila {fila_reserva + 1}, butaca {butaca_reserva + 1}")
            else:
                print(f"No se pudo reservar la fila {fila_reserva + 1}, butaca {butaca_reserva + 1} (ya está reservada).")
            break  
        except ValueError:
            print("ingrese numeros enteros...")

    print("Estado actualizado de las butacas:")
    mostrar_butacas(sala)
    
    libres = butacas_libres(sala)
    print(f"Número de butacas libres: {libres}")

    coordenadas_contiguas = butacas_contiguas(sala)
    if coordenadas_contiguas:
        print(f"La secuencia más larga de butacas libres comienza en la fila {coordenadas_contiguas[0][0] + 1}, butaca {coordenadas_contiguas[0][1] + 1}")
    else:
        print("No hay secuencias de butacas libres contiguas.")

main()
