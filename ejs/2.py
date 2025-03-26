"""Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al
usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos
de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello."""

# Diccionario con los precios de las frutas
# Cada clave representa el nombre de una fruta y su valor asociado es el precio por kilo
frutas = {
    "Platano": 1.35,
    "Manzana": 0.80,
    "Pera": 0.85,
    "Naranja": 0.70
}

# Solicitar el nombre de la fruta al usuario
# Se utiliza el método .capitalize() para asegurar que la primera letra sea mayúscula
frut = input("Ingrese el nombre de la fruta: ").capitalize()
print(" ")  # Espacio en blanco para mejorar la legibilidad en la consola

# Solicitar el número de kilos
# Se convierte la entrada del usuario a un entero para realizar cálculos
kil = int(input("Ingrese el número de kilos: "))
print(" ")  # Espacio en blanco para mejorar la legibilidad en la consola

# Verificar si la fruta está en el diccionario
if frut in frutas:
    # Si la fruta está en el diccionario, se calcula el precio total
    valor = kil * frutas[frut]
    # Mostrar el precio total con dos decimales
    print(f"{kil} kilos de {frut} cuestan ${valor:.2f}")
else:
    # Si la fruta no está en el diccionario, se muestra un mensaje de error
    print("Fruta no encontrada")