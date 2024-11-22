"""""""""""

Desarrollar una función que devuelva una cadena de caracteres con el nombre del 
mes cuyo número se recibe como parámetro. Los nombres de los meses deberán 
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función. 
Devolver una cadena vacía si el número de mes es inválido. La detección de meses 
inválidos deberá realizarse a través de excepciones.

"""

def nombre_mes(numero_mes):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    try:
        if 1 <= numero_mes <= 12:
            return meses[numero_mes - 1]
        else:
            raise ValueError("Número de mes inválido")
    except ValueError:
        return ""

def ingresar_mes():
    try:
        numero_mes_ingresado = int(input("Ingresa el número del mes (1-12): "))
        nombre_mes_resultado = nombre_mes(numero_mes_ingresado)
        if nombre_mes_resultado:
            print(f"El nombre del mes es: {nombre_mes_resultado}")
        else:
            print("Número de mes inválido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

ingresar_mes()
