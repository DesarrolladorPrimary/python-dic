"""Determina si se debe declarar el impuesto de renta del próximo año basado en los ingresos mensuales.
Si los ingresos mensuales son mayores a 3.000.000:
  Se cobra 250.000 más un IVA del 18% de los ingresos mensuales.
Si los ingresos mensuales son menores o iguales a 3.000.000:
  Se cobra 200.000 más un IVA del 10% de los ingresos mensuales.
La función retorna un diccionario con el desglose del impuesto, que incluye el IVA, el impuesto fijo y el total.
"""

def calcular_impuesto(ingresos_mensuales):
    """
    Calcula y retorna el impuesto a pagar según los ingresos mensuales utilizando un diccionario para detallar el desglose.
    
        
    Retorna:
        dict: Un diccionario con el desglose del impuesto que contiene:
          - 'Ingresos': Ingresos mensuales.
          - 'IVA': El monto del IVA calculado.
          - 'ImpuestoFijo': El monto fijo a cobrar (250000 si mayores a 3000000, 200000 si menores o iguales).
          - 'TotalImpuesto': La suma del impuesto fijo y el IVA.
    """
    if ingresos_mensuales > 3000000:
        # Para ingresos mayores a 3.000.000 se calcula un IVA del 18%
        iva = 0.18 * ingresos_mensuales
        impuesto_fijo = 250000
    else:
        # Para ingresos menores o iguales a 3.000.000 se calcula un IVA del 10%
        iva = 0.10 * ingresos_mensuales
        impuesto_fijo = 200000

    # Calcula el total a pagar sumando el impuesto fijo y el IVA
    total_impuesto = impuesto_fijo + iva

    # Construye y retorna un diccionario con todo el detalle del impuesto
    return {
        "Ingresos": ingresos_mensuales,
        "IVA": iva,
        "ImpuestoFijo": impuesto_fijo,
        "TotalImpuesto": total_impuesto
    }
# Solicita al usuario sus ingresos mensuales
ingresos = float(input("Ingrese sus ingresos mensuales: "))
        # Llama a la función y almacena el resultado en un diccionario
resultado_impuesto = calcular_impuesto(ingresos)

# Muestra el desglose del impuesto de forma detallada
print("\nDesglose del impuesto:")
print(f"Ingresos mensuales: {resultado_impuesto['Ingresos']:.2f}")
print(f"IVA calculado: {resultado_impuesto['IVA']:.2f}")
print(f"Impuesto fijo: {resultado_impuesto['ImpuestoFijo']:.2f}")
print(f"Total a pagar: {resultado_impuesto['TotalImpuesto']:.2f}")
