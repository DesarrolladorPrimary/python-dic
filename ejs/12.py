"""Realizar un algoritmo que pregunte el nombre de la persona y la edad, y que muestre la fecha de nacimiento
de dicha persona (calculado a partir del año actual y la edad ingresada).
Se permite ingresar datos de varias personas.
"""

from datetime import datetime

def age_time():
    # Lista para almacenar la información de cada persona
    personas = []

    # Solicita al usuario el número de personas que se desean ingresar.
    cantidad = int(input("¿Cuántas personas desea ingresar? "))

    # Se recorre un ciclo para cada persona
    for i in range(cantidad):
        # Crea un diccionario temporal para almacenar los datos de la persona actual
        persona = {}
        persona["Nombre"] = input("Ingrese su nombre: ")
        persona["Edad"] = int(input("Ingrese su edad: "))
        print(" ")

        # Obtiene el año actual
        current_year = datetime.now().year
        # Calcula el año de nacimiento restando la edad al año actual
        persona["Año de nacimiento"] = current_year - persona["Edad"]

        # Agrega el diccionario con los datos de la persona a la lista de personas
        personas.append(persona)

    # Después de ingresar los datos se muestra la información para cada persona
    print("\nInformación de las personas ingresadas:")
    for persona in personas:
        print(f"Nombre: {persona['Nombre']}, Edad: {persona['Edad']}, Año de nacimiento: {persona['Año de nacimiento']}")

age_time()