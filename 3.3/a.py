# Uso del método items() en Python.
# El método items() devuelve una vista de los pares clave-valor de un diccionario.

# Ejemplo 1: Usar items() con un bucle for para iterar sobre un diccionario.
animal = {
    "Especie": "Perro",
    "Raza": "Pastor Aleman",
    "Color": "Oscuro",
    "Edad": "5 anios"
}

# Imprimir el diccionario completo.
print(f"Diccionario: {animal}\n\n")

# Obtener una vista de los pares clave-valor del diccionario.
valors = animal.items()

# Iterar sobre los pares clave-valor y mostrarlos.
for clave, valor in valors:
    print(f"Valores del diccionario: {clave} : {valor}")

print(" ")
print(" ")

# Ejemplo 2: Usar items() para convertir un diccionario en una vista de tuplas.
programacion = {
    "Web": "JS",
    "IA": "Python",
    "App": "Kotlin"
}

# Obtener una vista de tuplas (clave, valor) del diccionario.
Dtupla = programacion.items()

# Imprimir la vista de tuplas.
print(f"Diccionario Tupla: {Dtupla}")