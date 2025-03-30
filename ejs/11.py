"""Programa que guarda los nombres de los alumnos y las notas que han obtenido.
Cada alumno puede tener distinta cantidad de notas.
La información se guarda en un diccionario, donde:
- Las claves son los nombres de los alumnos.
- Los valores son listas con las notas de cada alumno.

El programa realiza lo siguiente:
1. Pide el número de alumnos a introducir.
2. Para cada alumno:
   - Solicita su nombre (si el alumno ya existe, muestra un error y finaliza).
   - Pide sus notas, terminando cuando se introduce un número negativo.
3. Finalmente, muestra la lista de alumnos y la nota media obtenida por cada uno.
"""

def notas():
    alumnos = {}  # Diccionario donde se almacenará la información de los alumnos.
    
    # Solicita al usuario el número de alumnos a ingresar y lo almacena en la variable 'cantidad'.
    cantidad = int(input("Ingrese el número de alumnos: "))
    
    # Se inicia un ciclo que se repetirá 'cantidad' veces para procesar cada alumno.
    for i in range(cantidad):
        # Se solicita el nombre del alumno, mostrando el número de orden (i+1 para iniciar en 1).
        nombre = input(f"\nIngrese el nombre del alumno {i+1}: ")
        
        # Verifica si el alumno ya se ha ingresado previamente en el diccionario 'alumnos'.
        # Si es así, se muestra un mensaje de error y la función termina.
        if nombre in alumnos:
            print("Error: el alumno ya existe.")
            return
        
        # Se crea una lista vacía para almacenar las notas del alumno.
        notas = []
        
        # Se inicia un ciclo para solicitar cada nota del alumno.
        while True:
            # Solicita una nota ingresada por el usuario (se espera un número flotante).
            nota = float(input("Ingrese una nota (número negativo para terminar): "))
            
            # Si el número ingresado es negativo, se finaliza el ingreso de notas para este alumno.
            if nota < 0:
                break
            # De lo contrario, la nota válida se agrega a la lista de notas.
            notas.append(nota)
        
        # Se asocia la lista de notas obtenida al alumno mediante una clave en el diccionario 'alumnos'.
        alumnos[nombre] = notas

    # Una vez que se han ingresado todos los datos, se muestra la lista de alumnos y la nota media correspondiente a cada uno.
    print("\nLista de alumnos y su nota media:")

    # Se recorre el diccionario 'alumnos' para procesar cada par (alumno, lista de notas).
    for alumno, notas in alumnos.items():
        # Se calcula el promedio:
        # Si la lista 'notas' contiene elementos, se calcula la suma de las notas dividida por el número de notas.
        # Si la lista está vacía, se asigna un promedio de 0 para evitar la división por cero.
        promedio = sum(notas) / len(notas) if notas else 0
        # Se muestra el nombre del alumno y el promedio obtenido, formateado a dos decimales.
        print(f"{alumno}: {promedio:.2f}")

notas()

