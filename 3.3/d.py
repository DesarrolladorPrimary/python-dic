# Función reversed()

# Ejercicio 1: Invertir un diccionario.
# Inicializar un diccionario.
# Este diccionario contiene diferentes tipos de pasteles como claves y su cantidad como valores.
pasteles = {
    "manzana": 5,
    "fresa": 7,
    "chocolate": 3,
    "vainilla": 8
}

# Invertir el diccionario usando reversed().
# La función reversed() invierte el orden de los elementos del diccionario.
# dict(reversed(pasteles.items())) convierte el resultado en un diccionario nuevamente.
invertido = dict(reversed(pasteles.items()))
print(invertido)

# Ejercicio 2: Invertir un diccionario con valores duplicados.
# Inicializar un diccionario con valores duplicados.
# Este diccionario contiene cupones como claves y los sabores de los pasteles como valores.
cupones = {
    "cupon1": "fresa",
    "cupon2": "chocolate",
    "cupon3": "fresa",
    "cupon4": "vainilla"
}

# Invertir el diccionario usando reversed().
# La función reversed() invierte el orden de los elementos del diccionario.
# dict(reversed(cupones.items())) convierte el resultado en un diccionario nuevamente.
invertido = dict(reversed(cupones.items()))
print(invertido)