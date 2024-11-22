"""""""""

Escribir un programa que permita dividir un archivo de texto cualquiera en partes 
que se puedan enviar por correo electrónico. El tamaño máximo de las partes se 
ingresa por teclado. Los nombres de los archivos generados deben respetar el 
nombre original con el agregado de un sufijo que indique de qué parte se trata. 
Tener en cuenta que ningún registro puede ser dividido; la partición debe efectuarse después del 
delimitador del mismo. Mostrar un mensaje de error si el proceso no 
pudiera llevarse a cabo. Recordar que no se permite cargar el archivo completo en 
memoria.

"""

def dividir_archivo(archivo_entrada, tamano_maximo):
    try:
        with open(archivo_entrada, 'r') as archivo:
            parte = 1
            tamano_actual = 0
            archivo_salida = open(f"{archivo_entrada}_parte{parte}.txt", 'w')

            for linea in archivo:
                if tamano_actual + len(linea) > tamano_maximo:
                    archivo_salida.close()
                    parte += 1
                    tamano_actual = 0
                    archivo_salida = open(f"{archivo_entrada}_parte{parte}.txt", 'w')

                archivo_salida.write(linea)
                tamano_actual += len(linea)

            archivo_salida.close()
        print("División completada.")
    except Exception as e:
        print(f"Se produjo un error: {e}")

nombre_archivo = input("Ingresa el nombre del archivo de entrada (con extensión): ")
tamano_maximo = int(input("Ingresa el tamaño máximo de las partes (en bytes): "))
dividir_archivo(nombre_archivo, tamano_maximo)
