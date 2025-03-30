"""Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada
mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada
mes.
"""

def ahorro_anual():
    # Inicializa una lista para almacenar el monto ahorrado en cada uno de los 12 meses.
    ahorros_mensuales = []

    # Se recorre un ciclo desde 1 hasta 12 (inclusive) para representar cada mes del año.
    # En cada iteración se solicita al usuario el monto a depositar para el mes correspondiente.
    for mes in range(1, 13):
        ahorro = float(input(f"Ingrese el monto que desea ahorrar en el mes {mes}: "))
        # Se agrega el monto depositado en el mes actual a la lista de ahorros
        ahorros_mensuales.append(ahorro)

    # Calcula el total ahorrado al final del año sumando todos los ahorros mensuales.
    total_ahorrado = sum(ahorros_mensuales)

    # Muestra un resumen de los ahorros registrados por cada mes.
    print("\nResumen de ahorros mensuales:")
    # Se recorre la lista de ahorros utilizando enumerate para obtener tanto el índice (mes) como el valor.
    # El parámetro start=1 asegura que los meses se muestren iniciando en 1 en vez de 0.
    for mes, ahorro in enumerate(ahorros_mensuales, start=1):
        print(f"Mes {mes}: ${ahorro:.2f}")

    # Finalmente, muestra el total ahorrado al final del año, formateado a dos decimales.
    print(f"\nTotal ahorrado al final del año: ${total_ahorrado:.2f}")