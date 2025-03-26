"""Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe
preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar.
Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato.

Lista de la compra ----- Precio
Artículo 1 Precio Artículo 1
Artículo 2 Precio Artículo 1
... ...
Total"""

# Inicialización de un diccionario vacío para almacenar los productos y sus precios
cesta = {}

# Bucle infinito para permitir al usuario agregar productos a la cesta
while True:
    # Preguntar al usuario si desea terminar
    desi = input("Desea terminar: ")
    print("  \n")  # Espacio en blanco para mejorar la legibilidad en la consola

    # Si el usuario responde "si", se rompe el bucle
    if desi.lower() == "si":
        break

    # Solicitar el nombre del producto
    Art = input("Ingrese el nombre del producto: ")
    # Solicitar el precio del producto y convertirlo a entero
    Pre = int(input("Ingrese el precio del producto: "))
    # Agregar el producto y su precio al diccionario
    cesta[Art] = Pre

# Obtener los elementos del diccionario como pares clave-valor
valors = cesta.items()

# Mostrar la lista de la compra
print("Lista de la compra ----- Precio")
for clave, valor in valors:
    # Mostrar cada producto y su precio
    print(f"   {clave}        -----> {valor}")

# Calcular y mostrar el coste total de la compra
total = sum(cesta.values())
print(f"\nTotal: {total}")