# Trabajo Práctico 3
# Estructuras condicionales

#Ejercicio 1
# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#  deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# Se solicita al usurio ingresar su edad y se asigna dicho valor a la variable "edad_usuario"
edad_usuario = int(input("Ingrese su edad: "))
# se realiza la comparación : si el usuario tiene 18 años cumplidos o más
if edad_usuario >= 18:
    # si dicha comparación es Verdadera se imprime por pantalla el mensaje:
    print("Es mayor de edad")
# Haya sido Verdadera o falsa la comparación Termina el programa


#Ejercicio 2
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, 
# deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario 
# deberá mostrar el mensaje “Desaprobado”.

# Se solicita al usurio ingresar su nota y se asigna dicho valor a la variable "nota_usuario"
nota_usuario = float(input("Ingrese su nota: "))
# se realiza la comparación
if nota_usuario >= 6:
    # si es verdadera se imprime el siguiente mensaje por pantalla:
    print("Aprobado")
else:
    # si es falsa se imprime este otro mensaje:
    print("Desaprobado")


#Ejercicio 3
#Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par,
# imprimir por pantalla el mensaje "Ha ingresado un número par"; en caso contrario, 
# imprimir por pantalla "Por favor, ingrese un número par". 
# Nota: investigar el uso del operador de módulo (%) en Python 
# para evaluar si un número es par o impar.

numero = int(input("Ingrese un número par: "))
# Para saber si un número es par se divide por 2 y su resto debe ser 0
if numero % 2 == 0:
    print(" Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


#Ejercicio 4
# Escribir un programa que solicite al usuario su edad e imprima por pantalla 
# a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

edad_usuario = int(input("Ingrese su edad: "))
# Se asume que la edad ingresada es un número positivo
if edad_usuario < 12:
    print("Pertenece a la categoría : Niño/a")
# Siendo falsa la condición anterior se sabe que la edad es mayor o igual a 12
elif edad_usuario < 18:
    print("Pertenece a la categoría : Adolescente")
# Siendo falsa la condición anterior se sabe que la edad es mayor o igual a 18
elif edad_usuario < 30:
    print("Pertenece a la categoría : Adulto/a joven")
# Siendo falsa la condición anterior se sabe que la edad es mayor o igual a 30
else:
    print("Pertenece a la categoría : Adulto/a")


#Ejercicio 5
# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada,
# imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario,
# imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos
# que tiene un iterable tal como una lista o un string.

contrasenia = input("Ingrese una contraseña de entre 8 y 14 caracteres : ")
# Con la función len() se obtiene la longitud de una cadena
longitud_contrasenia = len(contrasenia)
# Se compara la longitud obtenida con el rango solicitado por medio de una expresión lógica
if longitud_contrasenia >= 8 and longitud_contrasenia <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#Ejercicio 6
# escribir un programa que tome la lista numeros_aleatorios,
# calcule su moda, su mediana y su media y las compare para determinar 
# si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Nota: crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.

# se importa random para obtener la lista y se parametriza para un rango de 50
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# del paquete statistics se importan mode, median y mean
from statistics import mode, median, mean 
# Se calculan los valores de los parámetros solicitados para la lista generada
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
# de acuerdo a los valores de dichos parámetros se determina el sego de los datos
if media > mediana and mediana > moda:
    print("En la lista de los 50 números aleatorios generada hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("En la lista de los 50 números aleatorios generada hay sesgo negativo")
else:
    print("En la lista de los 50 números aleatorios generada no hay sesgo")


##Ejercicio 7
# Escribir un programa que solicite una frase o palabra al usuario. 
# Si el string ingresado termina con vocal, añadir un signo de exclamación al final
# e imprimir el string resultante por pantalla; en caso contrario, dejar el string
#  tal cual lo ingresó el usuario e imprimirlo por pantalla.

# se solcita ingresar la palabra o frase
frase = input("Ingrese una palabra o frase: ")
# se obtiene en último carácter de la candena ingresada y se pasa a Mayúsculas para
# minimizar las condiciones y validar también las vocales minúsculas.
ultimo_caracter = frase[-1].upper()
# se evalua si el último carácter es una vocal y si es así, se modifica la cadena agregando "!"
if ultimo_caracter == "A" or ultimo_caracter == "E" or ultimo_caracter == "I" or ultimo_caracter == "O" or ultimo_caracter == "U":
    frase = frase + "!"
# se iprime por pantalla la frase modificada o sin modificar según el condicional anterior
print (frase)


# Ejercicio 8
# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#  dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada
# por el usuario e imprimir el resultado por pantalla. 
# Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir
# entre mayúsculas y minúsculas.

# Se solicita ingresar el nombre
nombre = input("Ingrese su nombe: ")
# se imprime por pantalla el menú de opciones
print ("Menú de Opciones:")
print ("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print ("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print ("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
# se solicita al usuario que ingrese la opción
opcion = int(input("Ingrese una de las opciones anteriores 1 , 2 o 3 : "))
# se evalua la opción y se actúa según el caso:
if opcion == 1:
    nombre = nombre.upper()
    print (nombre)
elif opcion == 2:
    nombre = nombre.lower()
    print (nombre)
elif opcion == 3:
    nombre = nombre.title()
    print (nombre)
else:
    print ("La opción ingresada es incorrecta")


#Ejercicio 9
#Escribir un programa que pida al usuario la magnitud de un terremoto, 
# clasifique la magnitud en una de las siguientes categorías según 
# la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# se solicita al usuario ingresar la magnitud del terremoto
magnitud = float(input("Ingrese la magnitud del terremoto: "))
# se asigna cada categoría a una variable con el mismo nombre
muy_leve = "Muy leve (imperceptible)"
leve = "Leve (ligeramente perceptible)"
moderado = "Moderado (sentido por personas, pero generalmente no causa daños)"
fuerte = "Fuerte (puede causar daños en estructuras débiles)"
muy_fuerte = "Muy Fuerte (puede causar daños significativos)"
extremo = "Extremo (puede causar graves daños a gran escala)"
# se evalúa la magnitud y se clasifica en categoría según la escala de Richter.
if magnitud < 3:
    categoria = muy_leve
elif magnitud < 4:
    categoria = leve
elif magnitud < 5:
    categoria = moderado
elif magnitud < 6:
    categoria = fuerte
elif magnitud < 7:
    categoria = muy_fuerte
else:
    categoria = extremo
# se informa por pantalla el resultado de la categorización 
print (f"Según la escala de Richter el terremoto es {categoria} .")


# Ejercio 10
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S),
# qué mes del año es y qué día es. El programa deberá utilizar esa información para
# imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

# se solicita ingresar los datos al usuario.
emisferio = input ("Ingrese el emisferio en el que se encuentra (N / S) : ")
mes = input ("Ingrese qué mes del año es: ")
dia = int(input ("Ingrese qué día es: "))
# se convierte emiferio a mayúsculas para poder evaluar también si se ingresa en minúscula.
# según los datos de la tabla informada los meses están expresados en letras.
# asumimos que serán ingresados correctamente. Solo se convierte el texto a minúsculas para la evaluación.
emisferio = emisferio.upper()
mes = mes.lower()
# según los datos ingresados se determina el orden de la estación del año con el valor verdadero de una variable booleana.
primera_estacion = (mes == "diciembre" and dia >= 21) or (mes == "enero") or (mes == "febrero") or (mes == "marzo" and dia <= 20)
segunda_estacion = (mes == "marzo" and dia >= 21) or (mes == "abril") or (mes == "mayo") or (mes == "junio" and dia <= 20)
tercera_estacion = (mes == "junio" and dia >= 21) or (mes == "julio") or (mes == "agosto") or (mes == "septiembre" and dia <= 20)
cuarta_estacion = (mes == "septiembre" and dia >= 21) or (mes == "octubre") or (mes == "noviembre") or (mes == "diciembre" and dia <= 20)
# se evalúa el hemisferio . Se asume que se ingresó N o S
if emisferio == "N":
    if primera_estacion:
        estacion = "Invierno"
    elif segunda_estacion:
        estacion = "Primavera"
    elif tercera_estacion:
        estacion = "Verano"
    else:
        estacion = "Otoño"
else:
    if primera_estacion:
        estacion = "Verano"
    elif segunda_estacion:
        estacion = "Otoño"
    elif tercera_estacion:
        estacion = "Invierno"
    else:
        estacion = "Primavera"

print (f"Usted se encuentra en {estacion}")
