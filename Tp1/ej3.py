"""""
  una persona desea llevar el control de los gastos realizados al viajar en el subterráneo 
  dentro de un mes. Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes 
  (detalladas en la tabla de abajo) se solicita desarrollar una función que reciba como parámetro la cantidad 
  de viajes realizados en un determinado mes y devuelva el total gastado en viajes. 
  Realizar también un programa para verificar el comportamiento de la función.

"""

def control_gasto(viaje):
    tarifa_maxima = 125
    total = 0
    if viaje <= 20:
        total = viaje * tarifa_maxima
    elif viaje <= 30:
        total = 20 * tarifa_maxima + (viaje - 20) * tarifa_maxima * 0.8
    elif viaje <= 40:
        total = 20 * tarifa_maxima + 10 * tarifa_maxima * 0.8 + (viaje - 30) * tarifa_maxima * 0.7
    else:
        total = 20 * tarifa_maxima + 10 * tarifa_maxima * 0.8 + 10 * tarifa_maxima * 0.7 + (viaje - 40) * tarifa_maxima * 0.6
    return total

def main():
    while True:
        try:
            viajes = int(input("Ingrese la cantidad de viajes que realizó este mes: "))
            total = control_gasto(viajes)
            print(f"El total de gasto al mes es de: ${total}")
        except ValueError:
            print("Por favor, ingrese un número válido.")
            break

main()