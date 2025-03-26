# Este script demuestra el uso del método items() en Python.
# El método items() devuelve una vista de los pares clave-valor de un diccionario.

# Ejemplo 1: Usar items() con un bucle for para iterar sobre un diccionario.
animal = {
    "Especie":"Perro",
    "Raza": "Pastor Aleman",
    "Color":"Oscuro",
    "Edad": "5 anios"
}

print (f"Diccionario: {animal}\n\n")

valors = animal.items()

for clave, valor in valors:
    print(f"Valores del dicccionario: {clave} : {valor}")

print(" ")
print(" ")

# Ejemplo 2: Usar items() para convertir un diccionario en una vista de tuplas.
programacion = {
    "Web": "JS",
    "IA" : "Python",
    "App": "Kotlin"
}

Dtupla = programacion.items()
print(f"Diccionario Tupla: {Dtupla}")