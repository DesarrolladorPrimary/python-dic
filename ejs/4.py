"""Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso
{'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada
asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de 
las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número 
total de créditos del curso."""

# Diccionario que almacena las asignaturas y sus créditos
asig = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

# Obtener los elementos del diccionario como pares clave-valor
materia = asig.items()

# Inicializar el contador para el total de créditos
TC = 0

# Recorrer cada asignatura y sus créditos
for clave, valor in materia:
    # Mostrar los créditos de cada asignatura
    print(f"La asignatura {clave} tiene {valor} créditos \n")
    # Sumar los créditos al total
    TC = valor + TC

# Espacio en blanco para mejorar la legibilidad
print(" ")

# Mostrar el total de créditos del curso
print(f"Total de créditos: {TC} ")