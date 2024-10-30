#Valor medio: Crear un programa que pida al usuario 10 números entre 1 y 100 y los meta en una lista o array. Nuestro programa calculará el valor medio de los números de la lista y lo mostrará al usuario.

# Inicializamos una lista vacía para almacenar los números
numeros = []

print("Introduce 10 números entre 1 y 100:")

# Pedimos al usuario que introduzca 10 números
for i in range(10):
    numero = int(input("Introduce el número " + str(i + 1) + ": "))
    
    # Verificamos si el número está fuera del rango permitido
    if numero < 1 or numero > 100:
        print("Número fuera de rango. El programa se detiene.")
        break  # Salimos del bucle si el número no está en el rango
    numeros.append(numero)

else:
    # Calculamos el valor medio de los números de la lista si todos están en el rango
    valor_medio = sum(numeros) / len(numeros)
    print("El valor medio de los números ingresados es:", round(valor_medio, 2))



"""
La función round() en Python se utiliza para redondear un número a un número específico de decimales. (no lo hemos visto pero no sabia como hacer el ejercicio sin hacer uso de esta funcion, mis disculpas.)

"""

#CREADO POR MIGUEL TORRES MARTÍNEZ 2ºB SMR ✞