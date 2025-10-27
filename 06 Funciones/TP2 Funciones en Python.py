# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo():
    print ("Hola Mundo!")

imprimir_hola_mundo()


# 2) Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    # Imprime un saludo con el nombre con que se llama a la función
    return (f"Hola {nombre}!")

nombre_usuario = input("Ingrese su nombre: ")

saludo_a_imprimir = saludar_usuario(nombre_usuario)
print(saludo_a_imprimir)


# 3) Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
# los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    # Imprime en una línea una presentación personal con los datos ingresados.
    print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugarResidencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, lugarResidencia)


# 4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
# como parámetro y devuelva el área del círculo. calcular_perimetro_
# circulo(radio) que reciba el radio como parámetro y devuelva
# el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
# funciones para mostrar los resultados.

from math import pi

# area del círculo = Pi * radio al cuadrado
def calcular_area_circulo(radio):
    area = round(pi * (radio ** 2), 2 )
    return area

# perímetro del círculo = Pi * 2 radios
def calcular_perimetro_circulo(radio):
    perimetro = round(pi * 2 * radio, 2)
    return perimetro

print ("Cálculo de área y perímetro de un círculo de radio dado")

radio = float(input("Ingrese el radio del círculo: "))

print (f"El área del círculo de radio {radio} es {calcular_area_circulo(radio)}")
print (f"El perímetro del círculo de radio {radio} es {calcular_perimetro_circulo(radio)}")


# 5) Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función.

def segundos_a_horas(segundos):
    # 1 hora equivale a 3600 segundos
    horas = round(segundos / 3600, 2)
    return horas

print ("Equivalencia entre segundos y horas")
segundos = int(input("Ingrese la cantidad de segundos: "))

print (f"{segundos} segundos equivale a {segundos_a_horas(segundos)} horas")


# 6) Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    # Genera una tabla de multiplicar del 1 al 10 por el número ingresado
    for i in range(1,11):
        print(f"{numero} X {i} = {numero * i}")

print (" Tabla de multiplicar de un número entero")
numero = int(input("Ingrese un número entero: "))

tabla_multiplicar(numero)


# 7) Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
# de forma clara.

def operaciones_basicas(a, b):
    # Genera una tupla con las 4 opreraciones básicas. Validar entrada distinta de 0 para "b".
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

print ("Operaciones aritméticas entre dos números enteros distintos de 0")
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero distinto de 0 : "))

resultados_operaciones_basicas = operaciones_basicas(num1, num2)

print (f"El resultado de {num1} + {num2} es {resultados_operaciones_basicas[0]}")
print (f"El resultado de {num1} - {num2} es {resultados_operaciones_basicas[1]}")
print (f"El resultado de {num1} x {num2} es {resultados_operaciones_basicas[2]}")
print (f"El resultado de {num1} / {num2} es {round(resultados_operaciones_basicas[3],2)}")


# 8) Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
# para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    # Ingresando el peso en Kg y la atura en m.
    imc = peso / (altura ** 2)
    return imc

print ("Cálculo de Indice de Masa Corporal")
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en Kg : "))

print (f"Su Indice de masa corporal (IMC) es {round(calcular_imc(peso, altura),2)}")


# 9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    # 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9 / 5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
    fahrenheit = ( 9 / 5 * celsius ) + 32
    return fahrenheit

print ("Conversión de temperatura en grados Celsius a grados fahrenheit")
celsius = float(input("Ingrese una temperatura en grados Celsius: "))

print (f"El equivalente a {celsius} ºC es {celsius_a_fahrenheit(celsius)} grados Fahrenheit")


# 10) Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(num1, num2, num3):
    promedio = (num1 + num2 + num3) / 3
    return promedio

print ("Cálculo del promedio de 3 números.")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segudo número: "))
num3 = float(input("Ingrese el tercer número: "))

print (f" El promedio de los números ingresados es : {calcular_promedio(num1, num2, num3)}")
