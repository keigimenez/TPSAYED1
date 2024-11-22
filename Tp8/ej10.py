""""""""""

 Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario 
y una lista de claves. La función debe eliminar del diccionario todas las claves 
contenidas en la lista, devolviendo el diccionario modificado y un número entero 
que represente la cantidad de claves eliminadas. Desarrollar también un programa 
para verificar su comportamiento

"""

def eliminarclaves(diccionario, lista_claves):
    claves_eliminadas = 0
    for clave in lista_claves:
        if clave in diccionario:
            del diccionario[clave]
            claves_eliminadas += 1
    return diccionario, claves_eliminadas

def main():
    diccionario = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }
    lista_claves = ['b', 'd', 'e']
    diccionario_modificado, cantidad_eliminadas = eliminarclaves(diccionario, lista_claves)
    print(f"Diccionario modificado: {diccionario_modificado}")
    print(f"Cantidad de claves eliminadas: {cantidad_eliminadas}")

main()
