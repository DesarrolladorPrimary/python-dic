"""Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes
se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro
diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde
preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al
usuario por una opción del siguiente menú:
✓ Añadir cliente,
✓ Eliminar cliente,
✓ Mostrar cliente,
✓ Listar todos los clientes,
✓ Listar clientes preferentes,
✓ Terminar."""

# Inicialización de la base de datos de clientes
clientes = {}

# Bucle principal para gestionar las operaciones
while True:
    # Mostrar el menú de opciones
    print("\nMenú de opciones:")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")
    
    # Solicitar la opción al usuario
    opcion = int(input("Seleccione una opción: "))
    
    # Opción 1: Añadir cliente
    if opcion == 1:
        # Solicitar los datos del cliente
        nif = input("Ingrese el NIF del cliente: ")
        nombre = input("Ingrese el nombre del cliente: ")
        direccion = input("Ingrese la dirección del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")
        correo = input("Ingrese el correo del cliente: ")
        preferente = input("¿Es cliente preferente? (si/no): ").lower() == "si"
        
        # Crear un diccionario con los datos del cliente
        cliente = {
            "nombre": nombre,
            "dirección": direccion,
            "teléfono": telefono,
            "correo": correo,
            "preferente": preferente
        }
        
        # Añadir el cliente a la base de datos
        clientes[nif] = cliente
        print("Cliente añadido con éxito.")

    # Opción 2: Eliminar cliente
    elif opcion == 2:
        # Solicitar el NIF del cliente a eliminar
        nif = input("Ingrese el NIF del cliente a eliminar: ")
        # Verificar si el cliente existe y eliminarlo
        if nif in clientes:
            del clientes[nif]
            print("Cliente eliminado con éxito.")
        else:
            print("El cliente no existe.")

    # Opción 3: Mostrar cliente
    elif opcion == 3:
        # Solicitar el NIF del cliente a mostrar
        nif = input("Ingrese el NIF del cliente a mostrar: ")
        # Verificar si el cliente existe y mostrar sus datos
        if nif in clientes:
            cliente = clientes[nif]
            print(f"Datos del cliente (NIF: {nif}):")
            for clave, valor in cliente.items():
                print(f"{clave.capitalize()}: {valor}")
        else:
            print("El cliente no existe.")

    # Opción 4: Listar todos los clientes
    elif opcion == 4:
        print("Lista de todos los clientes:")
        for nif, cliente in clientes.items():
            print(f"NIF: {nif}, Nombre: {cliente['nombre']}")

    # Opción 5: Listar clientes preferentes
    elif opcion == 5:
        print("Lista de clientes preferentes:")
        for nif, cliente in clientes.items():
            if cliente["preferente"]:
                print(f"NIF: {nif}, Nombre: {cliente['nombre']}")

    # Opción 6: Terminar
    elif opcion == 6:
        print("Saliendo del programa...")
        break

    # Opción inválida
    else:
        print("Opción no válida. Intente de nuevo.")