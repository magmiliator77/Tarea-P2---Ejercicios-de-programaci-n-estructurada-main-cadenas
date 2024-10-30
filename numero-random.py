"""
Este ejercicio lo he hecho para practicar y por el chiste, está basado en el programa de Telecinco Pasapalabra. En concreto en la ultima fase de este donde tienes que adivinar una palabra relacionada con un tema. 

¿¿¿Seras capaz de ganar a los Mosos de Arousa???
(Son los protagonistas del programa, llevan sin perder mucho tiempo y siguen todavía en pie)

"""

import random  # Importar la librería random para generar números aleatorios

# Lista de palabras
palabras = ["manzana", "naranja", "plátano", "fresa", "kiwi"]

# Elegir una palabra aleatoria de la lista
palabra = random.choice(palabras)  # Seleccionar una palabra al azar

print("¡Bienvenido a Pasapalabra!")
print("Adivina cual es la letra de hoy, relacionada con frutas.")

# Bucle para permitir al usuario adivinar una letra
letra = input("Introduce una letra: ").lower()  # Pedir al usuario que introduzca una letra

# Verificar si la letra está en la palabra
if letra in palabra:
    print("¡Correcto! La letra era:", palabra)
    print("Has ganado Pasapalabra!! eres un fiera")
else:
    print("Incorrecto. La palabra era:", palabra)
    print("No pasa nada, otro dia mas que gana los mosos de escuadra, pero te llevas el juego de pasa palabra!!")


#CREADO POR MIGUEL TORRES MARTÍNEZ 2ºB SMR ✞
