# Función sorted()

# La función sorted() se utiliza para ordenar los elementos de un iterable.

# Ejercicio 1: Ordenar un diccionario de números.

desordenado = {
    "One": 2, 
    "Two": 4, 
    "three": 3, 
    "Four": 1, 
    "Five": 0
    }
# Ordenar los valores del diccionario en orden ascendente.
ordendo = sorted(desordenado.values())
# Imprimir los valores ordenados.
print(f" Valores del diccionario ordenados: {ordendo}")  # [0, 1, 2, 3, 4]



#Ejercicio 2: Ordenar un diccionario de cadenas.

desordenado = {
    "b": "1", 
    "c": "2", 
    "a": "3", 
    "d": "4"
    }


# Ordenar las claves del diccionario en orden ascendente.
ordenado = sorted(desordenado.keys())
# Imprimir las claves ordenadas.
print(f"Claves del diccionario ordenadas: {ordenado}")  # ['a', 'b', 'c', 'd']