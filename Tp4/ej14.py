""""

 Se solicita crear un programa para leer direcciones de correo electrónico y verificar 
si representan una dirección válida. Por ejemplo usuario@dominio.com.ar. Para que 
una dirección sea considerada válida el nombre de usuario debe poseer solamente 
caracteres alfanuméricos, la dirección contener un solo carácter @, el dominio debe 
tener al menos un carácter y tiene que finalizar con .com o .com.ar. 
Repetir el proceso de validación hasta ingresar una cadena vacía. 
Al finalizar mostrar un listado de todos los dominios, sin repetirlos y ordenados alfabéticamente, 
recordando que las direcciones de mail no distinguen mayúsculas ni minúsculas.

"""

import re

def es_email_valido(email):
    patron = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|com\.ar)$'
    return re.match(patron, email) is not None

def obtener_dominio(email):
    return email.split('@')[1].lower()

def main():
    dominios = set()
    while True:
        email = input("Ingrese una dirección de correo electrónico (o ingrese cero para finalizar): ")
        if email == "0":
            break
        email = email.lower()
        if es_email_valido(email):
            usuario, dominio = email.split('@')
            dominios.add(dominio)
        else:
            print("Dirección de correo electrónico no válida.")
    dominios_ordenados = sorted(dominios)
    print("\nDominios únicos (ordenados):")
    for dominio in dominios_ordenados:
        print(dominio)

main()