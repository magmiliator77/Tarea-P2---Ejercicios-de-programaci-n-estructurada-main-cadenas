#Invertir una frase: Escribir un programa que pida al usuario que introduzca una frase y muestre por pantalla la frase invertida. Dar la posibilidad de volver a ejecutar el programa de nuevo.

while True:
    # Solicita al usuario que introduzca una frase
    frase = input("Introduce una frase: ")

    # Variable para almacenar la frase invertida
    frase_invertida = ""

    # Recorre cada carácter de la frase y los agrega al inicio de frase_invertida
    for caracter in frase:
        frase_invertida = caracter + frase_invertida

    # Muestra la frase invertida
    print("La frase invertida es:", frase_invertida)

    # Pregunta al usuario si quiere volver a invertir otra frase
    repetir = input("¿Quieres invertir otra frase? (s/n): ").lower()

    # Si el usuario responde algo diferente de 's', el bucle se detiene
    if repetir != 's':
        break

"""
Inicialmente, frase_invertida está vacía: "".

Primer carácter ("H"): Al agregar "H" al inicio de frase_invertida, esta se convierte en "H"

Segundo carácter ("o"): Al agregar "o" al inicio de "H", frase_invertida se convierte en "oH"

Tercer carácter ("l"): Al agregar "l" al inicio de "oH", frase_invertida ahora es "loH"

Cuarto carácter ("a"): Al agregar "a" al inicio de "loH", finalmente obtenemos "aloH"

"""


#CREADO POR MIGUEL TORRES MARTÍNEZ 2ºB SMR ✞