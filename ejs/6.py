"""Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las
palabras español e inglés separadas por dos puntos, y cada par: separados por comas. El programa
debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español
y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario
debe dejarla sin traducir."""

# Inicialización de un diccionario vacío para almacenar las traducciones
tradu = {}

# Bucle para permitir al usuario agregar palabras al diccionario
while True:
    print(" ")
    # Solicitar al usuario que ingrese una palabra en español y su traducción al inglés
    word = input("Ingrese las palabras de la siguiente manera (Español:Ingles). Escriba 0 si desea terminar: ")
    
    # Preguntar al usuario si desea terminar
    if word == "0":
        break
    
    # Dividir la entrada en dos partes: palabra en español y palabra en inglés
    español, ingles = word.split(":")
        # Agregar la palabra en español como clave y su traducción al inglés como valor al diccionario
    tradu[español.strip()] = ingles.strip()

print("\nDiccionario de traducciones creado con éxito.\n")

# Solicitar al usuario una frase en español para traducir
frase = input("Ingrese una frase en español para traducir: ")

# Dividir la frase en palabras y traducir palabra por palabra
palabras = frase.split()
traduccion = []

for palabra in palabras:
    # Si la palabra está en el diccionario, traducirla; de lo contrario, dejarla igual
    if palabra in tradu:
        traduccion.append(tradu[palabra])
    else:
        traduccion.append(palabra)

# Mostrar la frase traducida
print("\nFrase traducida:")
print(" ".join(traduccion))



