"""10. En una escuela se necesita un programa el cual gestione la cantidad de personas que entran a cuyo
salón, teniendo en cuenta que se debe que tener la información personal de cada estudiante y de
los profesores, así mismo, se debe tener un registro del número del salón al cual se le valla a hacer
la gestión y que al final se muestre en pantalla."""

def main():
    # Diccionario principal para almacenar la información de la escuela
    escuela = {}

    # Se solicita el número del salón
    salon = input("Ingrese el número del salón: ")
    escuela['salon'] = salon

    # Se solicita la cantidad de personas que ingresarán
    cantidad = int(input("Ingrese la cantidad de personas que ingresarán: "))
    escuela['cantidad_personas'] = cantidad

    # Lista para almacenar los diccionarios con los datos de cada persona
    personas = []

    # Se inicia un ciclo que se repetirá 'cantidad' veces, donde 'cantidad' es el número de personas a ingresar.
    for i in range(cantidad):
        # Imprime un encabezado indicando el número de la persona (se usa i+1 para empezar en 1 en lugar de 0)
        print(f"\nDatos de la persona {i+1}:")

        # Solicita al usuario el nombre de la persona
        nombre = input("Ingrese el nombre: ")

        # Se solicita la edad y se convierte a entero para poder utilizarla posteriormente en operaciones numéricas si fuese necesario
        edad = int(input("Ingrese la edad: "))

        # Pide el rol de la persona, siendo este 'estudiante' o 'profesor'
        rol = input("Ingrese el rol (estudiante/profesor): ")

        # Crea un diccionario con la información recogida para la persona
        persona = {
            'nombre': nombre,  # Almacena el nombre ingresado
            'edad': edad,      # Almacena la edad convertida a entero
            'rol': rol         # Almacena el rol ingresado
        }
        # Agrega el diccionario de la persona a la lista 'personas'
        personas.append(persona)
    
    # Una vez finalizado el ingreso de datos, se agrega la lista 'personas' al diccionario principal 'escuela'
    escuela['personas'] = personas

    # Se inicia la impresión de la información consolidada
    print("\nInformación registrada:")
    # Muestra el número del salón introducido previamente por el usuario
    print(f"Número de salón: {escuela['salon']}")
    # Muestra la cantidad total de personas que se registraron
    print(f"Cantidad de personas: {escuela['cantidad_personas']}")

    # Se itera sobre cada diccionario (cada persona) en la lista de personas, utilizando enumerate para obtener
    # tanto el índice (empezando en 1) como los datos de la persona.
    for idx, persona in enumerate(escuela['personas'], start=1):
        # Imprime el encabezado de la persona con su número de orden
        print(f"\nPersona {idx}:")
        # Imprime el nombre almacenado en el diccionario de la persona
        print(f"  Nombre: {persona['nombre']}")
        # Imprime la edad almacenada en el diccionario de la persona
        print(f"  Edad: {persona['edad']}")
        # Imprime el rol (estudiante/profesor) almacenado en el diccionario de la persona
        print(f"  Rol: {persona['rol']}")

main()

