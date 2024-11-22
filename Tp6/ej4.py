"""""""""

Desarrollar un programa para eliminar todos los comentarios de un programa escrito en lenguaje Python.
 Tener en cuenta que los comentarios comienzan con el 
signo # (siempre que éste no se encuentre encerrado entre comillas simples o dobles) y 
que también se considera comentario a las cadenas de documentación 
(docstrings).

"""

import re

def eliminar_comentarios(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, 'r') as archivo:
            codigo = archivo.read()
        codigo_sin_docstrings = re.sub(r'("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\')', '', codigo)
        codigo_sin_comentarios = re.sub(r'#.*', '', codigo_sin_docstrings)
        with open(archivo_salida, 'w') as archivo:
            archivo.write(codigo_sin_comentarios)
        print("Comentarios eliminados correctamente.")
    except Exception as e:
        print(f"Se produjo un error: {e}")

nombre_archivo_entrada = input("Ingresa el nombre del archivo de entrada (con extensión): ")
nombre_archivo_salida = input("Ingresa el nombre del archivo de salida (con extensión): ")
eliminar_comentarios(nombre_archivo_entrada, nombre_archivo_salida)
