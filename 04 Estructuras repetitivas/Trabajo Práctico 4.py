# Trabajo Práctico 4
# Estructuras repetitivas

#Ejercicio 1
# Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# Se utiliza un bucle for pues se conocen la cantidad de iteraciones a realizar.
for i in range(101): # la variable i tomará valores desde 0 a 100
    print(i)


#Ejercicio 2
# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

# se utilizará un bucle While porque no sabemos la cantidad de iteraciones necesrias.

divisor = 1 # se define el valor desde dónde iniciará el divisor (irá multiplicandose por 10)
cant_digitos = 0 # se irá incrementando en el ciclo while o si es 0, en el if else.

numero = int(input("Ingrese un número entero: ")) # solicita ingresar el número

if numero != 0:

    parte_entera = int(numero / divisor) # se obtiene la parte entera de la división 

    while parte_entera != 0: # se repite este ciclo hasta que la parte entera de la div. sea 0
        cant_digitos += 1 # en cada repetición aumenta este contador indicando la cantidad de cifras.
        divisor *= 10 # se incrementa el valor del divisor ( potencia de 10 )
        parte_entera = int(numero / divisor) 

else:
    cant_digitos = 1 # como el número ingresado fue 0 se actualiza  a 1 la cantidad de dígitos y sale.

print(f"El número  {numero} contiene {cant_digitos} dígitos.")


#Ejercicio 3
# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# se solicita ingresar los números
primer_num = int(input("Ingerese el primer número: "))
segundo_num = int(input("Ingrese el segundo número: "))

while primer_num == segundo_num: # se valida la entrada del segundo número
    print("\nEl segundo número no debe ser igual al primero.\n ")
    segundo_num = int(input("Ingrese nuevamente un segundo número: "))

if primer_num < segundo_num: # se ordenan los números según su valor para obtener el rango
    inicio = primer_num
    final = segundo_num
else:
    inicio = segundo_num
    final = primer_num

suma = 0

for i in range(inicio+1, final): # se suma 1 al inicio para excluirlo y el final ya está excluído.
    suma += i

print(f"\nLa suma de los enteros comprendidos entre {inicio} y {final}, sin incluir a estos, es {suma}.\n")


#Ejercicio 4
# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el
# usuario ingrese un 0.

print("\nEste programa suma los números ingresados\n")
# Se inicializan el totalizador y el contador para poder trabajarlos dentro del bucle while
sumatoria = 0
contador = 0
# Se hace la primer pregunta fuera del bucle para poder validar
numero = int(input("Ingrese un número para ser sumado, (0 para terminar): "))

while numero != 0: # se repite hasta que el usuario ingrese un 0
    sumatoria += numero
    numero = int(input("Ingrese otro número para ser sumado, (0 para terminar): "))
    contador += 1

print(f"La sumatoria de los {contador} números ingresados es {sumatoria}")

#Ejercicio 5
# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9.
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# se importa random para obtener el número aleatorio
import random
numero_aleatorio = random.randint(0, 9)

print("\nEste juego consiste en adivinar un número entre 0 y 9\n")
cant_intentos = 1
numero = int(input(f"Ingresa el número (intento nº{cant_intentos}):  "))
# se valida luego del primer intento
while numero != numero_aleatorio:
    if numero < 0 or numero > 9: # si el número está fuera del rango se informa al usuario
        print("\nRecordá que el número debe estar entre 0 y 9\n")
    cant_intentos += 1 # se actualiza la cantidad de intentos y se vuelve a solicitar otro num.
    numero = int(input(f"Ingresa el número (intento nº{cant_intentos}):  "))

print(f"\nAcertaste el número en {cant_intentos} intentos.\n")


#Ejercicio 6
# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100,-1,-1): # se define el rango desde 100 a -1 ,que no está incluido, y paso negativo.
    if i % 2 == 0: # se evalúa en cada iteración si el valor de i es par. 
        print(i)


# Ejercicio 7
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero = int(input("Ingrese un número entero positivo: "))

while numero <= 0: # se valida la entrada de un número entero positivo
    print("\nEl número solicitado debe ser un entero mayor que 0")
    numero = int(input("Ingrese un número entero positivo: "))

suma = 0 # se inicializa el totalizador
for i in range(0, numero+1): # se define el rango.
    suma += i

print(f"La suma de los enteros entre 0 y {numero} es {suma}.")


#Ejercicio 8
# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cant_numeros = 100 # cambiando el valor de esta variable se puede controlar con otros valores.
cant_pares = 0
cant_impares = 0
cant_positivos = 0
cant_negativos = 0
print(f"\nEste programa pide ingresar {cant_numeros} números enteros y cuenta los positivos, negativos, pares e impares.")

for i in range(cant_numeros):
    numero = int(input("Ingrese un número entero : "))
    
    if numero % 2 == 0: # en este condicional se definen la cantidad de pares e impares
        cant_pares += 1
    else:
        cant_impares += 1
    
    if numero > 0: # en este otro condicional se definen la cantidad de positivos y negativos
        cant_positivos +=1
    elif numero < 0:
        cant_negativos += 1
    
print(f"\nEn los {cant_numeros} números ingresados: ")
print(f"{cant_pares} son números pares y {cant_impares} son impares,")
print(f" además, {cant_positivos} son números positivos y {cant_negativos} son negativos.\n")

#Ejercicio 9
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

cant_numeros = 10 # cambiando el valor de esta variable se puede controlar con otros valores.

print(f"\nEste programa pide ingresar {cant_numeros} números enteros y obtiene la media de los mismos.")

suma = 0

for i in range(cant_numeros):
    numero = int(input("Ingrese un número entero : "))
    suma += numero

print(f"La media de los {cant_numeros} números ingresados es {suma / cant_numeros}")



#Ejercicio 10
# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

print("\nEste programa invierte los dígitos de un número ingresado.")

# se reutiliza el algoritmo del ejercicio 2 para hallar la cantidad de dígitos del número

divisor = 1 # se define el valor desde dónde iniciará el divisor (irá multiplicandose por 10)
cant_digitos = 0 # se irá incrementando en el ciclo while o si es 0, en el if else.

numero = int(input("Ingrese un número entero: ")) # solicita ingresar el número

if numero != 0:

    parte_entera = int(numero / divisor) # se obtiene la parte entera de la división 

    while parte_entera != 0: # se repite este ciclo hasta que la parte entera de la div. sea 0
        cant_digitos += 1 # en cada repetición aumenta este contador indicando la cantidad de cifras.
        divisor *= 10 # se incrementa el valor del divisor ( potencia de 10 )
        parte_entera = int(numero / divisor) 

else:
    cant_digitos = 1 # como el número ingresado fue 0 se actualiza  a 1 la cantidad de dígitos y sale.

# Se utiliza la cantidad de dígitos del número ingresado para determinar la potencia
# a la que debemos elevar cada posición en un bucle for.


suma_nuevo_num = 0 # Esta variable almacenará la suma de cada iteración del bucle hasta llegar al nuevo num.
resto_num = numero # Esta variable almacenará el resto del número original luego de restar 
n = 0

# se define el rango en forma decreciente para obtener el valor de las unidades partiendo del mas significativo
# y así sucesivamente hasta llegar a la última posición.
for i in range(cant_digitos,0,-1): 
    valor_pos = int(resto_num / 10 ** (i-1)) # es el valor obtenido para la posición más relevante.
    suma_nuevo_num += valor_pos * 10 ** n # Se va obteniendo el valor del nuevo número sumando el valor
    # significativo anterior por la potencia de 10 correspondiente (comenzando de n=0 para las unidades).
    resto_num -= valor_pos * (10 ** (i-1)) # se obtiene el resto del número para seguir iterando.
    n += 1 # se actualiza la potencia por la que se multiplica el siguiente valor de posición 

print(f"El número invertido corespondiente a {numero} es {suma_nuevo_num}")
