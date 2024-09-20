""""
   Un comercio de electrodomésticos necesita para su línea de cajas un programa que 
   le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan 
   dos números enteros, correspondientes al total de la compra y al dinero recibido. 
   Informar cuántos billetes de cada denominación deben ser entregados como vuelto, 
   de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes 
   de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el 
   dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta 
   de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se 
   abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1 
   billete de $200, 1 billete de $100 y 3 billetes de $10.

"""

def calcular_vuelto(compra, dinero_recibido):
    billetes = [5000, 1000, 500, 200, 100, 50, 10]
    vuelto = dinero_recibido - compra
    if vuelto < 0:
        return "Error: Dinero recibido insuficiente."
    
    resultado = {}
    for billete in billetes:
        cantidad_billetes = vuelto // billete
        if cantidad_billetes > 0:
            resultado[billete] = cantidad_billetes
            vuelto -= cantidad_billetes * billete

    if vuelto > 0:
        return "Error: No se puede entregar el cambio exacto con las denominaciones disponibles."
    
    return resultado

def main():
    while True:
        try:
            compra = int(input("Ingrese el total de la compra: "))
            dinero_recibido = int(input("Ingrese el dinero recibido: "))
            vuelto = calcular_vuelto(compra, dinero_recibido)
            if isinstance(vuelto, str):
                print(vuelto)
            else:
                print(f"Para una compra de ${compra} y un pago de ${dinero_recibido}, el vuelto es: {vuelto}")
        except ValueError:
            print("Por favor, ingrese un número válido.")
            break
main()