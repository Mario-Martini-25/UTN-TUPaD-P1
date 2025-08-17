# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print ("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla
#  un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa 
# “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar
#  la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
print (f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y
#  lugar de residencia e imprima por pantalla una oración con los datos
#  ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”,
#  “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez,
#  tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo
#  si utilizas print(f…) para realizar la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugarResidencia = input("Ingrese su lugar de residencia: ")
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarResidencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e
#  imprima por pantalla su área y su perímetro.
print ("Cálculo de área y perímetro de un círculo de radio dado")
radio = float(input("Ingrese el radio del círculo: "))
# area del círculo = Pi * radio al cuadrado
area = 3.1416 * (radio ** 2)
# perímetro del círculo = Pi * 2 radios
perimetro = 3.1416 * 2 * radio
print (f"El área del círculo de radio {radio} es {area}")
print (f"El perímetro del círculo de radio {radio} es {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e
#  imprima por pantalla a cuántas horas equivale.
print ("Equivalencia entre segundos y horas")
segundos = int(input("Ingrese la cantidad de segundos: "))
# 1 hora equivale a 3600 segundos
horas = segundos / 3600
print (f"{segundos} segundos equivale a {horas} horas")

# 6) Crear un programa que pida al usuario un número e
#  imprima por pantalla la tabla de multiplicar de dicho número.
print (" Tabla de multiplicar de un número entero")
numero = int(input("Ingrese un número entero: "))
print (f"{numero} x 1 = {numero * 1}")
print (f"{numero} x 2 = {numero * 2}")
print (f"{numero} x 3 = {numero * 3}")
print (f"{numero} x 4 = {numero * 4}")
print (f"{numero} x 5 = {numero * 5}")
print (f"{numero} x 6 = {numero * 6}")
print (f"{numero} x 7 = {numero * 7}")
print (f"{numero} x 8 = {numero * 8}")
print (f"{numero} x 9 = {numero * 9}")
print (f"{numero} x 10 = {numero * 10}")

# 7) Crear un programa que pida al usuario dos números enteros
#  distintos del 0 y muestre por pantalla
#  el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print ("Operaciones aritméticas entre dos números enteros distintos de 0")
num1 = int(input("Ingrese el primer número entero distinto de 0 : "))
num2 = int(input("Ingrese el segundo número entero distinto de 0 : "))
print (f"El resultado de {num1} + {num2} es {num1 + num2}")
print (f"El resultado de {num1} / {num2} es {num1 / num2}")
print (f"El resultado de {num1} x {num2} es {num1 * num2}")
print (f"El resultado de {num1} - {num2} es {num1 - num2}")

# 8) Crear un programa que pida al usuario su altura y su peso e
#  imprima por pantalla su índice de masa corporal.
#  Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
# 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚 elevado al cuadrado)
print ("Cálculo de Indice de Masa Corporal")
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en Kg : "))
imc = peso / (altura ** 2)
print (f"Su Indice de masa corporal (IMC) es {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e
#  imprima por pantalla su equivalente en grados Fahrenheit.
#  Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9 / 5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
print ("Conversión de temperatura en grados Celsius a grados fahrenheit")
celcius = float(input("Ingrese una temperatura en grados Celsius: "))
fahrenheit = ( 9 / 5 * celcius ) + 32
print (f"El equivalente a {celcius} grados Celsius es {fahrenheit} grados Fahrenheit")

# 10) Crear un programa que pida al usuario 3 números e
#  imprima por pantalla el promedio de dichos números.
print ("Cálculo del promedio de 3 números.")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segudo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print (f" El promedio de los números ingresados es : {promedio}")
