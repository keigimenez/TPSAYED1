""""""""""

e dispone de tres formatos diferentes de archivos de texto en los que se almacenan datos de empleados, 
detallados más abajo. Desarrollar un programa para cada 
uno de los formatos suministrados, que permitan leer cada uno de los archivos y 
grabar los datos obtenidos en otro archivo de texto con formato CSV.
Archivo 1: Los campos tienen longitud fija con un espacio de separación 
entre ellos.
(Regla) 1 2 3 4 5 6 
012345678901234567890123456789012345678901234567890123456789012
Pérez Juan 20080211 Corrientes 348 
González Ana M 20080115 Juan de Garay 1111 3er piso dto A
Archivo 2: Todos los campos de este archivo están precedidos por un 
número de dos dígitos que indica la longitud del campo a leer.
10Pérez Juan082008021114Corrientes 348
14González Ana M082008011533Juan de Garay 1111 3er piso dto A
NOTAS:
· Los espacios que se encuentren al final de las cadenas en el formato 1 deberán 
ser eliminados.
· El formato 2 debe generalizarse para que soporte registros con cualquier cantidad de campos.

"""

import csv

def leer_formato1(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, 'r') as archivo:
            lineas = archivo.readlines()

        with open(archivo_salida, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(['Apellido', 'Nombre', 'Fecha', 'Direccion'])

            for linea in lineas:
                apellido = linea[0:10].strip()
                nombre = linea[10:20].strip()
                fecha = linea[20:28].strip()
                direccion = linea[28:].strip()
                escritor_csv.writerow([apellido, nombre, fecha, direccion])

        print("Datos del archivo 1 grabados correctamente en formato CSV.")
    except Exception as e:
        print(f"Se produjo un error: {e}")


def leer_formato2(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, 'r') as archivo:
            lineas = archivo.readlines()

        with open(archivo_salida, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(['Apellido', 'Nombre', 'Fecha', 'Direccion'])

            for linea in lineas:
                i = 0
                campos = []
                while i < len(linea):
                    longitud = int(linea[i:i+2])
                    i += 2
                    campo = linea[i:i+longitud].strip()
                    campos.append(campo)
                    i += longitud
                escritor_csv.writerow(campos)

        print("Datos del archivo 2 grabados correctamente en formato CSV.")
    except Exception as e:
        print(f"Se produjo un error: {e}")


leer_formato2('archivo2.txt', 'salida2.csv')
leer_formato1('archivo1.txt', 'salida1.csv')
