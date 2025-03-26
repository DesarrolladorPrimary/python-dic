"""Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en
un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en
<dirección> y su número de teléfono es <teléfono>."""

# Crear un diccionario vacío para almacenar los datos del usuario
datosU = {}

# Solicitar los datos al usuario y almacenarlos en el diccionario
# Se solicita el nombre del usuario y se guarda con la clave "Nombre"
datosU["Nombre"] = input("Ingrese su nombre: ")
print(" ")  # Espacio en blanco para mejorar la legibilidad en la consola

# Se solicita la edad del usuario, se convierte a entero y se guarda con la clave "Edad"
datosU["Edad"] = int(input("Ingrese su edad: "))
print(" ")  # Espacio en blanco para mejorar la legibilidad en la consola

# Se solicita la dirección del usuario y se guarda con la clave "Dirección"
datosU["Dirección"] = input("Ingrese su dirección: ")
print(" ")  # Espacio en blanco para mejorar la legibilidad en la consola

# Se solicita el número de teléfono del usuario y se guarda con la clave "Teléfono"
datosU["Teléfono"] = input("Ingrese su número de teléfono: ")
print(" ")  # Espacio en blanco para mejorar la legibilidad en la consola

# Mostrar el mensaje con los datos almacenados en el diccionario
# Se utiliza una cadena formateada (f-string) para mostrar los datos de manera clara
print(f"{datosU['Nombre']} tiene {datosU['Edad']} años, vive en {datosU['Dirección']} y su número de teléfono es {datosU['Teléfono']}.")