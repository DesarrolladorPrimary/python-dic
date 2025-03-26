"""Crear un programa en Python donde se le pregunte al usuario su nombre, su edad y su número de
documento. Todo esto deberá estar almacenado en un diccionario."""

# Inicialización de un diccionario vacío para almacenar los datos del usuario
user = {}

# Solicitar al usuario que ingrese sus datos
print(" --- Ingrese sus datos --- ")
# Solicitar el nombre del usuario y almacenarlo en el diccionario con la clave "Nombre"
user["Nombre"] = input("Ingrese su nombre: ")
print(" ")  # Espacio en blanco para mejorar la legibilidad en la consola

# Solicitar la edad del usuario y almacenarla en el diccionario con la clave "Edad"
user["Edad"] = input("Ingrese su edad: ")
print(" ")  # Espacio en blanco para mejorar la legibilidad en la consola

# Solicitar el número de documento del usuario y almacenarlo en el diccionario con la clave "Id"
user["Id"] = input("Ingrese su numero de documento: ")
print(" ")  # Espacio en blanco para mejorar la legibilidad en la consola

# Obtener los elementos del diccionario como pares clave-valor
users = user.items()

# Mostrar los datos del usuario almacenados en el diccionario
for clave, valor in users:
    print(f"{clave} : {valor}")
