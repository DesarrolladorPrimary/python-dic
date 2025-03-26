"""Escribe un programa Python que pida un número por teclado y que cree un diccionario cuyas claves
sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves."""

# Inicialización de un diccionario vacío
# Este diccionario almacenará las claves (números) y sus valores (cuadrados)
dicc = {}

# Solicitar al usuario un número entero
# Este número definirá el rango de claves en el diccionario
num = int(input("Ingrese un numero: "))

# Bucle para generar las claves y valores del diccionario
# Itera desde 1 hasta el número ingresado por el usuario (inclusive)
for i in range(1, num + 1):
    # Asignar al diccionario la clave `i` y como valor el cuadrado de `i`
    dicc[i] = i ** 2

# Imprimir el diccionario resultante
# Muestra las claves y sus valores (cuadrados) en formato de diccionario
print(dicc)