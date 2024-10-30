#Valor medio 2: Crear un programa que genere 200 números aleatorios entre 1 y 100 y los meta en una lista o array. Nuestro programa calculará el valor medio de los números de la lista y lo mostrará al usuario 


import random  # Importar la librería random para generar números aleatorios

# Pedir al usuario el número de aleatorios que quiere generar
cantidad = int(input("¿Cuántos números aleatorios quieres generar? "))  # Convertir la entrada a un número entero

# Pedir al usuario el rango mínimo y máximo
minimo = int(input("Introduce el valor mínimo (debe ser al menos 1): "))  # Convertir la entrada a un número entero
maximo = int(input("Introduce el valor máximo (debe ser como máximo 100): "))  # Convertir la entrada a un número entero

# Verificar si el rango es válido
if minimo < 1 or maximo > 100:
    print("Error: El valor mínimo debe ser al menos 1 y el valor máximo debe ser como máximo 100.")
else:
    numeros = []  # Crear una lista vacía para almacenar los números aleatorios

    # Bucle que se repite según la cantidad especificada por el usuario
    for _ in range(cantidad):
        numero = random.randint(minimo, maximo)  # Generar un número aleatorio dentro del rango
        numeros.append(numero)  # Agregar el número generado a la lista

    suma = 0  # Inicializar la variable suma en 0 para acumular los números



    # Bucle para sumar todos los números en la lista
    for numero in numeros:
        suma += numero  # Sumar cada número a la variable suma

    # Calcular el valor medio dividiendo la suma entre la cantidad de números
    valor_medio = suma / len(numeros)  # len(numeros) devuelve el número de elementos en la lista

    # Mostrar el valor medio calculado al usuario
    print("El valor medio es:", valor_medio)  # Imprimir el resultado




"""
EN EL BUCLE FOR hago uso de "_" esto lo he aprendido de tutoriales en youtube, esto se hace para indicar que no utilizaremos la varible del bucle. Podria haber puesto cualquier otro nombre a la varible pero me ha gustado la práctica del "_"


"""

#CREADO POR MIGUEL TORRES MARTÍNEZ 2ºB SMR ✞