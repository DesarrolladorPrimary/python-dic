#Función reversed()

# Ejercicio 1: Invertir un diccionario
# Inicializar un diccionario
pasteles = {
    "manzana": 5,
    "fresa": 7,
    "chocolate": 3,
    "vainilla": 8
}

# Invertir el diccionario usando reversed()
invertido = dict(reversed(pasteles.items()))
#Se invierte el orden de los elementos del diccionario
print(invertido)  



# Ejercicio 2: Invertir un diccionario con valores duplicados
# Inicializar un diccionario con valores duplicados

cupones = {
    "cupon1": "fresa",
    "cupon2": "chocolate",
    "cupon3": "fresa",
    "cupon4": "vainilla"
}

# Invertir el diccionario usando reversed()
#Se invierte el orden de los elementos del diccionario
invertido = dict(reversed(cupones.items()))
print(invertido)