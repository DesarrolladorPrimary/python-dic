# La función enumerate() permite iterar sobre un iterable y obtener tanto el índice como el valor.

# Ejemplo 1: Iterar sobre un diccionario y obtener el índice y la clave.
numeros = {
    "uno": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5
    }

for  num, clave in enumerate(numeros):
    print(f" Indice de las claves  {num}, {clave}")

print(" ")
print(" ")
    
# Ejemplo 2: Iterar sobre otro diccionario y obtener el índice y la clave.
nums = {
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10
}

for indice, valor in enumerate(nums):
    print(f"Indice de los valores: {indice}, {valor}")