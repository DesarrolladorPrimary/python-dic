# Función zip()

# Ejercicio 1: Crear un diccionario a partir de dos listas

# Inicializar dos listas de la misma longitud
claves = ["nombre", "edad", "ciudad"]
valores = ["Juan", 25, "Madrid"]

# Crear un diccionario usando zip()
# La función dict() convierte un iterable de pares clave-valor (como el resultado de zip()) en un diccionario.
diccionario = dict(zip(claves, valores))

print(diccionario)  # {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid'}




#Ejercicio 2: Crear un diccionario a partir de dos listas de diferente longitud
# Inicializar dos listas de diferente longitud
claves = ["nombre", "edad", "ciudad"]
valores = ["Juan", 25, "Madrid", "España"]
# Crear un diccionario usando zip()
diccionario = dict(zip(claves, valores))
# El resultado es un diccionario con solo dos elementos, ya que zip() se detiene cuando se agota la lista más corta.
print(diccionario)  # {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid'}