#1) Crear una lista con las notas de 10 estudiantes.
#•Mostrar la lista completa.
#•Calcular y mostrar el promedio.
#•Indicar la nota más alta y la más baja.

notas = [6, 8, 5, 7, 9, 3, 10, 7, 6, 4]
for nota in notas:
    print(nota, end = " ")
print()

suma = 0
for nota in notas:
    suma += nota
print(f"El promedio de las notas de la lista es: {suma / len(notas)}")

mayor_nota = notas[0]
menor_nota = notas[0]
for nota in notas:
    if nota > mayor_nota:
        mayor_nota = nota
    elif nota < menor_nota:
        menor_nota = nota
print(f"La nota más alta de la lista es: {mayor_nota}")
print(f"La nota más baja de la lista es: {menor_nota}")


#2) Pedir al usuario que cargue 5 productos en una lista.
#•Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#•Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []

for i in range(5):
    producto = input(f"Ingrese el producto {i+1}: ")
    productos.append(producto)

lista_ordenada = sorted(productos)
print("La lista ordenada de los productos es:")
for producto in lista_ordenada:
    print(producto, end = "  ")
print()

producto_a_eliminar = input("Ingrese el producto que desea eliminar: ")

if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar) 
else:
    print("El producto ingresado no está en la lista.")

print("La lista resultante es:")
for producto in productos:
    print(producto, end = "  ")
print()


# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.

import random
numeros_aleatorios = [random.randint(1, 100) for i in range(15)]

pares =[]
impares = []
for num in numeros_aleatorios:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"\nEn la lista generada hay: \n {len(pares)} números pares y {len(impares)} impares.")


# 4) Dada una lista con valores repetidos:
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

datos_sin_repetir = []

for dato in datos:
    if dato not in datos_sin_repetir:
        datos_sin_repetir.append(dato)

print("La lista sin valores repetidos es:")
for dato in datos_sin_repetir:
    print(dato, end = "  ")


# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada.

presentes = ["Juan", "Pedro", "María", "Lorena", "Fabián", "Jorge", "Ana", "Luisa"]

print("La lista de los estudiantes presentes es:" )
for estudiante in presentes:
    print(estudiante)
print()

opcion = input("Desea agregar o eliminar un estudiante a esta lista? (ingrese A o E) : ")

if opcion.upper() == "A":
    nuevo_estudiante = input("Ingrese el nuevo estudiante: ")
    presentes.append(nuevo_estudiante)
elif opcion.upper() == "E":
    estudiante_a_eliminar = input("Ingrese el estudiante a eliminar: ")
    presentes.remove(estudiante_a_eliminar)
else:
    print("No ingresó una opción válida")

print("\nLa lista de los estudiantes presentes es:" )
for estudiante in presentes:
    print(estudiante)
print()


# 6) Dada una lista con 7 números, rotar todos los elementos una posición 
# hacia la derecha (el último pasa a ser el primero).

numeros = [1, 2, 3, 4, 5, 6, 7]
print(f"La lista original es: {numeros}")

numeros_reordenados = []

numeros_reordenados.append (numeros[-1]) # se toma el último elemento y se agrega como primer elemento de la nueva lista.

for numero in numeros[:-1]: # se define el rango de iteración hasta el último elemnto sin incluirlo.
    numeros_reordenados.append(numero)

print(f"La lista rotada es: {numeros_reordenados}")


# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# •Calcular el promedio de las mínimas y el de las máximas.
# •Mostrar en qué día se registró la mayor amplitud térmica.

temperaturas = [
    [8, 18], # día 1
    [-1, 16], # día 2
    [8, 19], # día 3
    [9, 20], # día 4
    [10, 21], # día 5
    [9, 21], # día 6
    [11, 21] # día 7
]

suma_max = 0
suma_min = 0
mayor_amplitud = 0
dia_mayor_amplitud = ""

for d in range(len(temperaturas)):
    suma_min += temperaturas[d][0]
    suma_max += temperaturas[d][1]
    amplitud = temperaturas[d][1] - temperaturas[d][0]
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = d+1 # se suma 1 para corregir el orden del elemento respecto del indice de su posición.

promedio_min = round(suma_min/len(temperaturas), 2)
promedio_max = round(suma_max/len(temperaturas), 2)

print()
print(f"El promedio de las temperaturas mínimas de la semana es: {promedio_min}ºC")
print(f"El promedio de las temperaturas máximas es : {promedio_max}ºC")
print(f"La mayor amplitud térmica fue de {mayor_amplitud}ºC y se registró en el día : {dia_mayor_amplitud}")
print()


# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# •Mostrar el promedio de cada estudiante.
# •Mostrar el promedio de cada materia.

# matriz de 5 x 3. estudiantes filas, materias columnas
notas_por_estudiante =[
    [8, 7, 9],
    [6, 5, 6],
    [4, 8, 9],
    [7, 9, 10],
    [3, 6, 10]
]

# para calcular el promedio de cada estudiante
for estudiante in notas_por_estudiante: 
    suma_estudiante = 0
    cant_materias = 0
    for materia in estudiante:
        suma_estudiante += materia
        cant_materias += 1
    print(f"El promedio del estudiante {notas_por_estudiante.index(estudiante)+1} es: {suma_estudiante/cant_materias:.2f}")
print()

# para calcular el promedio de cada materia,
for materia in range(len(notas_por_estudiante[0])): # se obtiene la cantidad de materias con la longitud de la primera fila.
    suma_materia = 0
    cant_estudiantes = 0
    for estudiante in notas_por_estudiante:
        suma_materia += estudiante[materia]
        cant_estudiantes += 1
    print(f"El promedio de la materia {materia + 1} es: {suma_materia/cant_estudiantes:.2f}")
print()


# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#•Inicializarlo con guiones "-" representando casillas vacías.
#•Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#•Mostrar el tablero después de cada jugada.

tablero = []

for filas in range(3):
    fila= [] 
    tablero.append(fila) # se agrega una lista vacía a la lista tablero
    for columna in range(3):
        tablero[filas].append("-") # se agregan 3 elementos "-" por cada fila.
  

for filas in tablero:
    for columnas in filas:
        print(columnas, end=" " )
    print()
 
turno_Jugador = "X"
cant_jugadas = 0

while cant_jugadas < 9: # Limite de jugadas para llenar el tablero

    fila_jugada = (int(input("Ingrese la fila de la jugada (1 a 3 ): ")) -1)
    while fila_jugada < 0 or fila_jugada > 2:
        fila_jugada = (int(input("La fila de la jugada debe ser entre (1 a 3 ): ")) - 1 )# se resta 1 para manejar indice

    columna_jugada = (int(input("Ingrese la columna de la jugada (1 a 3 ): ")) - 1) # se resta 1 para manejar indice
    while columna_jugada < 0 or columna_jugada > 2:
        columna_jugada = (int(input("La columna de la jugada debe ser entre (1 a 3 ): ")) - 1)

    if tablero[fila_jugada][columna_jugada] == "-": 
        cant_jugadas += 1  # validada la entrada se actualiza el contador de jugadas.
        if turno_Jugador == "X":
            tablero[fila_jugada][columna_jugada] = "X" # se evalua el estado anterior de jugador y se actualiza para la próxima jugada.
            turno_Jugador = "O"
        else:
            tablero[fila_jugada][columna_jugada] = "O" # se evalua el estado anterior de jugador y se actualiza para la próxima jugada.
            turno_Jugador = "X"

        print()
        for filas in tablero:
            for columnas in filas:
                print(columnas, end=" " )
            print()
        print()
      
    else:
        print("Esa casilla ya está ocupada. Intenta nuevamente") 


# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# •Mostrar el total vendido por cada producto.
# •Mostrar el día con mayores ventas totales.
# •Indicar cuál fue el producto más vendido en la semana.

ventas =[
    [100, 200, 300, 400, 200, 300, 150] # 7 días (columnas) , 4 productos (filas)
    [200, 350, 450, 500, 700, 200, 100]
    [150, 250, 300, 600, 250, 100, 350]
    [400, 350, 700, 800, 900, 100, 250]
]

for producto in ventas:
    total_producto = 0
    for dia in producto:
        total_producto += producto
    print(f"El total de las ventas del producto {producto+1} fueron: {total_producto}")


mayor_venta = 0
dia_mayor_venta = 0

for dia in range(len(ventas[0])): # se obtiene la cantidad de días con la longitud de la primera fila.
    venta_dia = 0
    for producto in range(len(ventas)):
        venta_día += ventas[producto][dia]
        if venta_día > mayor_venta:
            mayor_venta = venta_dia
            dia_mayor_venta = dia+1
        
    print(f"La mayor venta del productos {mayor_venta} fue el día {dia_mayor_venta}")
print()


mayor_venta_producto = 0
prod_mas_vendido = 0

for producto in ventas:
    total_producto = 0
    for dia in producto:
        total_producto += dia # se calcula el total de la venta en la semana
    if total_producto > mayor_venta_producto: # se valora con los anteriores
        mayor_venta_producto = total_producto
        prod_mas_vendido = ventas.index(producto) # se obtiene la posición del producto mas vendido
print()
print(f"El producto más vendido en la semana fue {prod_mas_vendido+1} con {mayor_venta_producto} ventas")
print()
