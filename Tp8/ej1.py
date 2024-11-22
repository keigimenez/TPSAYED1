"""""""""""""""

Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios, y luego escribir un programa que las vincule:
a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha 
válida.
b. Sumar N días a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al 
segundo se considerará que el primero corresponde al día anterior. En ningún 
caso la diferencia en horas puede superar las 24 horas.

"""
from datetime import datetime, timedelta

def ingresar_fecha():
    while True:
        fecha_str = input("Ingresa una fecha (dd/mm/aaaa): ")
        try:
            dia, mes, año = map(int, fecha_str.split('/'))
            if mes < 1 or mes > 12 or dia < 1 or dia > 31:
                print("Fecha inválida. El día o el mes son incorrectos.")
                continue

            if mes in [4, 6, 9, 11] and dia > 30:
                print("Fecha inválida. El mes seleccionado no tiene más de 30 días.")
                continue
            elif mes == 2:
                if (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)) and dia > 29:
                    print("Fecha inválida. Febrero en un año bisiesto solo tiene 29 días.")
                    continue
                elif dia > 28:
                    print("Fecha inválida. Febrero solo tiene 28 días en años no bisiestos.")
                    continue

            return (dia, mes, año)
        except ValueError:
            print("Formato incorrecto. Asegúrate de ingresar la fecha en el formato dd/mm/aaaa.")

def sumar_dias(fecha, n_dias):
    dia, mes, año = fecha
    fecha_obj = datetime(año, mes, dia)
    nueva_fecha = fecha_obj + timedelta(days=n_dias)
    return (nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)

def ingresar_horario():
    while True:
        horario_str = input("Ingresa un horario (hh:mm): ")
        try:
            horas, minutos = map(int, horario_str.split(':'))
            if 0 <= horas < 24 and 0 <= minutos < 60:
                return (horas, minutos)
            else:
                print("Hora o minutos fuera de rango. Asegúrate de ingresar un horario válido.")
        except ValueError:
            print("Formato incorrecto. Asegúrate de ingresar el horario en el formato hh:mm.")

def diferencia_horarios(hora1, hora2):
    h1, m1 = hora1
    h2, m2 = hora2
    minutos_hora1 = h1 * 60 + m1
    minutos_hora2 = h2 * 60 + m2
    if minutos_hora1 < minutos_hora2:
        minutos_hora1 += 24 * 60  
    diferencia = minutos_hora1 - minutos_hora2
    horas = diferencia // 60
    minutos = diferencia % 60
    return (horas, minutos)


def main():
    fecha = ingresar_fecha()
    print(f"Fecha ingresada: {fecha[0]}/{fecha[1]}/{fecha[2]}")
    n_dias = int(input("¿Cuántos días deseas sumar a la fecha? "))
    nueva_fecha = sumar_dias(fecha, n_dias)
    print(f"Fecha después de sumar {n_dias} días: {nueva_fecha[0]}/{nueva_fecha[1]}/{nueva_fecha[2]}")
    horario = ingresar_horario()
    print(f"Horario ingresado: {horario[0]:02d}:{horario[1]:02d}")
    print("Ingresa el segundo horario:")
    horario2 = ingresar_horario()
    print(f"Segundo horario ingresado: {horario2[0]:02d}:{horario2[1]:02d}")
    diferencia = diferencia_horarios(horario, horario2)
    print(f"Diferencia entre los horarios: {diferencia[0]} horas y {diferencia[1]} minutos")

main()
