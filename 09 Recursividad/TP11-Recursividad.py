# 1) Crea una función recursiva que calcule el factorial de un número. 
# Luego, utiliza esa función para calcular y mostrar en pantalla el factorial
#  de todos los números enteros entre 1 y el número que indique el usuario

def factorial(n):

    if n == 0 or n == 1: 
        return 1
    else:
        return n*factorial(n-1) 
    
numero = int(input("Ingrese un número entero: "))

for num in range(1, numero+1):
    print(f"\nEl factorial de {num} es : {factorial(num)}")


# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def serie_fibonacci(posicion):

    if posicion == 0: # casos base
        return 0
    elif posicion == 1:
        return 1
    else:
        return serie_fibonacci(posicion-1)+serie_fibonacci(posicion-2) # llamada recursiva a dos instancias de la función.
    
posicion = int(input("Ingrese un número entero: "))

for pos in range(posicion+1):
    print(f"\nEl valor de Fibonacci para la posición {pos} es : {serie_fibonacci(pos) }")


# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
# utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia(base,exponente):

    if exponente == 0:  # caso base
        return 1
    else:
        return base * potencia(base,exponente-1) # llamada resursiva con el exponente disminuido en 1

base = int(input("Ingrese un número entero para la base: "))
exponente = int(input("Ingrese un número entero para el exponente: "))

print(f"\nLa potencia de {base} elevado a la {exponente} es {potencia(base, exponente)}")


# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal
#  y devuelva su representación en binario como una cadena de texto.

def en_binario(num):

    if num == 0:
        return "" # en el caso base, si el cociente es 0 entonces ya tenemos todos los restos que me forman el binario. por eso la cadena vacía.
    else:
        return en_binario(num // 2) + str( num % 2) # llamada recursiva, se pasa como argumento el cociente entero y se concatena el resto.

decimal = int(input("Ingrese un número entero positivo para convertir a binario: "))
print(f"\nAl número {decimal} en base 10 le corresponte el número {en_binario(decimal)} en base 2.")


# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto 
# sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos: La solución debe ser recursiva. / No se debe usar [::-1]  ni la función reversed().

def es_palindromo(palabra):

    if len(palabra) <=1 : # caso base cuando la cadena tiene uno o ningún elemento.
        return True
    
    if palabra[0] != palabra[-1]:
        return False
    
    return es_palindromo(palabra[1:-1]) # llamada recursiva - se reduce la cadena quitando los extremos.

print(f"\n El resultado a si la palabra 'arenera' es un palíndormo es: {es_palindromo("arenera")}.")
print(f"\n El resultado a si la palabra 'radar' es un palíndormo es: {es_palindromo("radar")}.")
print(f"\n El resultado a si la palabra 'programa' es un palíndormo es: {es_palindromo("programa")}.")


# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
# número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones: No se puede convertir el número a string. Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos: suma_digitos(1234) → 10 (1 + 2 + 3 + 4) suma_digitos(9) → 9 suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):

    if n < 10:  # caso base . el número es de un solo dígito
        return n
    else:
        return (n % 10) + suma_digitos (n // 10) # llamada recursiva . se va reduciendo el número en un dígito.
    
n = int(input("Ingrese un número entero positivo para sumar sus dígitos: "))
print(f"\nLa suma de los dígitos de {n} es:  {suma_digitos(n)}.")
    

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques,
#  en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo
#  y devuelva el total de bloques que necesita para construir toda la pirámide.
# Ejemplos: contar_bloques(1) → 1 (1) contar_bloques(2) → 3 (2 + 1) contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):

    if n == 1: # caso base. queda un solo bloque
        return n
    else:
        return n + contar_bloques(n-1) # llamada recursiva . se va reduciendo la cantidad de bloques en 1.
    
n = int(input("Ingrese un número entero positivo para indicar la cantidad de bloques de la base: "))
print(f"\nLa cantidad de bloques necesarios para construir una pirámide de base {n} es:  {contar_bloques(n)}.")


# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo
#  (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
# Ejemplos: contar_digito(12233421, 2) → 3 contar_digito(5555, 5) → 4 contar_digito(123456, 7) → 0

def contar_digito(numero, digito):

    if numero < 10: # caso base. el número tiene un solo dígito.

        if numero == digito: # compara el número con el dígito buscado y retorna 1 si son iguales , 0 si no.
            return 1
        else:
            return 0
    
    unidades = numero % 10 # para obtener el último dígito para comparar con el dígito buscado.
    num_sin_unidades = numero // 10 # para obtener el nuevo número reducido para la llamada recursiva.

    if unidades == digito:
        return 1 + contar_digito(num_sin_unidades, digito) # llamada recursiva sumando 1 si hay conicidencia . 
    else:
        return contar_digito(num_sin_unidades, digito) # llamada recursiva sin actualizar contador si no hay conicidencia . 
    

numero = int(input("Ingrese un número entero positivo para contar la ocurrencia de un dígito en él: "))

while True:

    digito = int(input("Ingrese un dígito para contar su ocurrencia dentro del número ingresado: "))

    if digito >= 0 and digito < 10:
        print(f"\nEl dígito {digito} se encuentra  {contar_digito(numero, digito)} veces en {numero}.")
        break
    else:
        continue

