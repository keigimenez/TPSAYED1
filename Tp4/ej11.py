""""

Escribir un programa que cuente cuántas veces se encuentra una subcadena dentro 
de otra cadena, sin diferenciar mayúsculas y minúsculas. Tener en cuenta que los 
caracteres de la subcadena no necesariamente deben estar en forma consecutiva 
dentro de la cadena, pero sí respetando el orden de los mismos. Ejemplo:
Cadena:
Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva 
huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.
Sub-cadena: UADE
Cantidad encontrada: 4 (Las coincidencias están resaltadas en la cadena siguiente)
Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva 
huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.

"""

def contar_subcadena(cadena, subcadena):
    cadena = cadena.lower()
    subcadena = subcadena.lower()
    
    def contar(cadena, subcadena, inicio):
        if not subcadena:
            return 1 
        if inicio >= len(cadena):
            return 0 
        count = 0
        if cadena[inicio] == subcadena[0]:
            count += contar(cadena, subcadena[1:], inicio + 1)
        count += contar(cadena, subcadena, inicio + 1)
        return count
    return contar(cadena, subcadena, 0)

def main():
    cadena = "es larga la carretera cuando uno mira atras, vas cruzando las fronteras sin darte cuenta quizas"
    subcadena = "suigeneris"
    cantidad_encontrada = contar_subcadena(cadena, subcadena)
    print(f'Cadena:\n{cadena}')
    print(f'Sub-cadena: {subcadena}')
    print(f'Cantidad encontrada: {cantidad_encontrada}')

main()