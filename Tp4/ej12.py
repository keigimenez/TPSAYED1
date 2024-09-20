""""

Escribir un programa para crear una lista por comprensión con los naipes de la baraja española. 
La lista debe contener cadenas de caracteres. Ejemplo: ["1 Oros", "2 
Oros"... ]. Imprimir la lista por pantalla. 

"""

def main():
    palos = ['Oros', 'Copas', 'Espadas', 'Bastos']
    numeros = range(1, 13)
    baraja = []
    for palo in palos:
        for numero in numeros:
            baraja.append(f"{numero} {palo}")
    print(baraja)

main()