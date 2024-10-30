#: Crear un programa que pida al usuario su nombre y sus apellidos (todo en la misma frase). Independientemente de como escriba esos datos, debemos mostrar como salida el nombre y los apellidos con la primara letra de cada uno en mayúscula y el resto en minúscula con un mensaje informativo del tipo "Tu nombre escrito correctamente es: ...". Dar la posibilidad de

while True:
    # Solicita al usuario que introduzca su nombre y apellidos
    nombreyApellidos = str(input("Introduce tu nombre y tus apellidos --> "))

    # Variable donde se almacenará el nombre con el formato correcto
    nombreCorrecto = ""

    # Divide el nombre completo en palabras y las procesa una por una
    for palabra in nombreyApellidos.split():
        # Formatea cada palabra: primera letra en mayúscula y el resto en minúscula
        nombreCorrecto += palabra[0].upper() + palabra[1:].lower() + " "

    # Muestra el nombre completo con el formato correcto, eliminando el último espacio extra
    print("Tu nombre escrito correctamente es", nombreCorrecto.strip())

    # Pregunta al usuario si quiere volver a ingresar otro nombre
    repetir = input("¿Quieres volver a comprobar tu nombre? (s/n) -->")
    
    # Si el usuario responde algo diferente de 's', el bucle se detiene
    if repetir != 's':
        break


#CREADO POR MIGUEL TORRES MARTÍNEZ 2ºB SMR ✞