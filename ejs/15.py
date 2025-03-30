"""Realizar un algoritmo el cual sume los ingresos de una empresa mensualmente, teniendo en cuenta
que se debe saber de qué son las ganancias y se debe pedir al usuario de cuánto dinero total se
obtuvo de esa ganancia. Al final se deberá saber si las ganancias actuales son mayores a las ganancias
del año pasado, en cuyo caso se imprime en pantalla que se obtuvieron más ganancias y se calcula la
diferencia; si son menores, se imprime el faltante para alcanzar las ganancias del año pasado.

GANANCIAS: Pedir al usuario que ingrese las ganancias del año pasado.
"""

def main():
    # Solicita al usuario las ganancias del año pasado.
    ganancias_pasadas = float(input("Ingrese las ganancias del año pasado: "))

    # Solicita la cantidad de ingresos (o fuentes de ganancia mensual) que se desean ingresar.
    cantidad_ingresos = int(input("Ingrese la cantidad de ingresos (ganancias) mensuales: "))

    # Inicializa el total de ganancias del año actual en 0.
    total_actual = 0

    # Lista para almacenar el detalle de cada ingreso en forma de diccionario.
    ingresos_detalle = []

    # Se recorre un ciclo para obtener el detalle de cada ingreso.
    for i in range(cantidad_ingresos):
        print(f"\nIngreso {i+1}:")
        # Solicita la descripción de la ganancia (por ejemplo, "ventas", "servicios", etc.)
        descripcion = input("Ingrese la descripción de la ganancia: ")
        # Solicita el monto obtenido para dicha ganancia.
        monto = float(input("Ingrese el monto obtenido: "))

        # Agrega el ingreso actual como un diccionario a la lista de ingresos.
        ingresos_detalle.append({
            "descripcion": descripcion,
            "monto": monto
        })

        # Acumula el monto para obtener el total de ganancias actuales.
        total_actual += monto

    # Muestra el detalle de cada ingreso.
    print("\nDetalle de ingresos:")
    for ingreso in ingresos_detalle:
        print(f"Ganancia por {ingreso['descripcion']}: ${ingreso['monto']:.2f}")

    # Muestra el total de ganancias acumuladas del año actual.
    print(f"\nTotal de ganancias del año actual: ${total_actual:.2f}")

    # Compara las ganancias actuales con las del año pasado y muestra el resultado.
    if total_actual > ganancias_pasadas:
        diferencia = total_actual - ganancias_pasadas
        print(f"\nSe obtuvieron más ganancias que el año pasado por un monto de: ${diferencia:.2f}")
    elif total_actual < ganancias_pasadas:
        diferencia = ganancias_pasadas - total_actual
        print(f"\nFaltan ${diferencia:.2f} de ganancias para alcanzar las del año pasado.")
    else:
        print("\nLas ganancias del año actual son iguales a las del año pasado.")

main()


