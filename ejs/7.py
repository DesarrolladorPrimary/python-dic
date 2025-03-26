"""Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se
almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor
el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura,
pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de
factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el
número de factura y se eliminará del diccionario. Después de cada operación el programa debe
mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro."""

# Inicialización de un diccionario vacío para almacenar las facturas
# La clave será el número de factura y el valor será el coste de la factura
facturas = {}

# Bucle principal para gestionar las operaciones
while True:
    # Mostrar el menú de opciones al usuario
    desi = int(input("Que desea realizar \n1.Añadir factura \n2.Pagar factura \n3.Ver facturas \n4.Salir \n~: "))
    
    # Opción 1: Añadir una nueva factura
    if desi == 1:
        # Solicitar el número de la factura
        factU = int(input("Ingrese el numero de la factura: "))
        print(" ")
        # Solicitar el valor de la factura
        valorF = int(input("Ingrese el valor de la factura: "))
        print(" ")
        # Añadir la factura al diccionario
        facturas[factU] = valorF

    # Opción 2: Pagar una factura existente
    elif desi == 2:
        # Solicitar el número de la factura a eliminar
        eli = int(input("Ingrese el numero de la factura que desea eliminar: "))
        print(" ")
        # Verificar si la factura existe antes de eliminarla
        if eli in facturas:
            del facturas[eli]
        else:
            print("La factura no existe.")

    # Opción 3: Ver todas las facturas
    elif desi == 3:
        # Mostrar las facturas pendientes
        print(f"Facturas pendientes: {facturas}")
        print(" ")
        # Calcular y mostrar el total pendiente de cobro
        total_pendiente = sum(facturas.values())
        print(f"Total pendiente de cobro: {total_pendiente}")
        print(" ")

    # Opción 4: Salir del programa
    else: 
        break