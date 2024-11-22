"""""""""""""""

Todo programa Python es susceptible de ser interrumpido mediante la pulsación de 
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar 
un programa para imprimir los números enteros entre 1 y 100000, y que solicite 
confirmación al usuario antes de detenerse cuando se presione Ctrl-C.

"""

def imprimir_numeros():
    try:
        for i in range(1, 100001):
            print(i)
    except KeyboardInterrupt:
        try:
            respuesta = input("\n¿Deseas detener el programa? (s/n): ")
            if respuesta.lower() == 's':
                print("Programa detenido.")
                return
            else:
                imprimir_numeros()
        except KeyboardInterrupt:
            print("\nPrograma detenido forzosamente.")
            return

imprimir_numeros()
