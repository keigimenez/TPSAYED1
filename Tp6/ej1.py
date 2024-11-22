""""""""""

Escribir un programa que lea un archivo de texto conteniendo un conjunto de apellidos y nombres en
 formato "Apellido, Nombre" 
y guarde en el archivo ARMENIA.TXT los registros de aquellas personas cuyo apellido
termina con la cade na "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en ESPAÑA.TXT los 
terminados en "EZ". Descartar el resto. Ejemplo: Arslanian, Gustavo –> ARMENIA.TXT Rossini,
Giuseppe –> ITALIA.TXT Pérez, Juan –> ESPAÑA.TXT Smith, John –> descartar El archivo puede ser creado 
mediante el Block de Notas o el cualquier otro editor.

"""


def clasificar_apellidos(archivo_entrada):
    try:
        with open(archivo_entrada, 'r') as archivo:
            lineas = archivo.readlines()

        with open('ARMENIA.TXT', 'w') as armenia, \
             open('ITALIA.TXT', 'w') as italia, \
             open('ESPAÑA.TXT', 'w') as espana:
            
            for linea in lineas:
                apellido, nombre = linea.strip().split(', ')
                if apellido[-3:] == 'IAN':
                    armenia.write(linea + '\n')
                elif apellido[-3:] == 'INI':
                    italia.write(linea + '\n')
                elif apellido[-2:] == 'EZ':
                    espana.write(linea + '\n')
                else:
                    continue

        print("Clasificación completada.")
    except Exception as e:
        print(f"Se produjo un error: {e}")

nombre_archivo = input("Ingresa el nombre y apellido: ")
clasificar_apellidos(nombre_archivo)
