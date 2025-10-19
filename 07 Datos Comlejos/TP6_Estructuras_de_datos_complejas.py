# 1) Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
# Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)


# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#  desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#  desarrollado en el punto anterior, crear una lista que contenga únicamente las 
# frutas sin los precios.

frutas = list(precios_frutas.keys())

print(frutas)


# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

print("\nEste programa le pedirá 5 nombres y sus respectivos números telefónicos")
print("luego podrá consultar los números telefónicos, introduciendo el nombre.\n")

def pedir_nombre(): # Pide nombre y valida que el dato no sea número , solo espacios o esté vacía.
    while True:
        nombre = input("Ingrese el nombre del contacto: ")
        if  nombre.isdigit() or not nombre.strip() :
            print("\n** El nombre no debe estar vacío y debe contener letras **\n")
            continue
        else:
            return nombre
    

def pedir_num_tel(): # valida que el número telefónico sean solo dígitos y que sean 10
    while True:
        num_tel = input("Ingrese el número telefónico (10 dígitos) del contacto: ")
        if not num_tel.isdigit() or num_tel == "" or len(num_tel) != 10 :
            print("\n** El número telefónico no debe estar vacío y debe contener 10 dígitos **\n")
            continue
        else:
            return num_tel
    

def validar_contacto_existente(nombre): # valida que el nombre corresponda con una clave del diccionario y
                                        # en ese caso retorna el par clave, valor como tupla. o la tupla 0, 0 en caso negativo.
    
    for clave, val in numeros_telefónicos.items():

        if clave.upper() == nombre.upper():
            return clave, val
    return 0, 0


numeros_telefónicos = {}

contactos_a_ingresar = 5

while contactos_a_ingresar > 0: 
    
    nombre = pedir_nombre()

    contacto, telefono = validar_contacto_existente(nombre) # obtiene el par clave, valor si el nombre ya existe o 0,0 si no

    if contacto != 0:
        # Informa que el contacto ya existe , muestra el contacto correspondiente y repite el ciclo.
        print(f"\n** El contacto {contacto} ya existe con el número de teléfono : {telefono}.**")
        continue

    num_tel = pedir_num_tel()
    numeros_telefónicos[nombre] = num_tel

    print(f"\n*** Se ha ingresado el contacto '{nombre} tel: {numeros_telefónicos[nombre]}' ***\n")
    contactos_a_ingresar -= 1

# Luego de ingresados los contactos se realiza una consulta

print(f"\nPara consultar un número telefónico, ", end="")

nombre_consulta = pedir_nombre()
contacto, telefono = validar_contacto_existente(nombre_consulta) # se valida la existencia y se recupera el par Clave , Valor.

if contacto != 0:
    print(f"\nEl número telefónico de {contacto} es {telefono}")
else:
    print(f"\n*** El contacto {nombre_consulta} no existe.***")


# 5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

def pedir_frase(): # valida que no sean números y que no esté vacia o solo espacios.
    while True:
        frase = input("Ingrese una frase: ")
        if  frase.isdigit() or not frase.strip() :
            print("\n** La frase no debe estar vacía y debe contener letras **\n")
            continue
        else:
            return frase

frase = pedir_frase()

lista_palabras = frase.split() # se convierte la frase en una lista de palabras.

palabras_unicas = set(lista_palabras) # se genera un conjunto de palabras no repetidas.

contador_palabras = {}

for palabra in palabras_unicas: # 
    contador_palabras[palabra] = lista_palabras.count(palabra) # se genera un diccionario con clave = palabras únicas 
                                                               #y la cantidad de apariciones en la lista de palabras.
print(f"Palabras_únicas : {palabras_unicas}")
print(f"Recueno: {contador_palabras}")


# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#  Luego, mostrá el promedio de cada alumno.

def pedir_nombre_alumno(): # valida que el nombre del alumno no sea número , solo espacios o esté vacio.
    while True:
        nombre = input("Ingrese el nombre del alumno: ")
        if  nombre.isdigit() or not nombre.strip() :
            print("\n** El nombre no debe estar vacío y debe contener letras **\n")
            continue
        else:
            return nombre


def existe_alumno(alumnos, alumno): # valida que el nombre exista en la lista de claves del diccionario ( ambos por parámetro).
        
    for nombre in alumnos.keys():

        if nombre.upper() == alumno.upper(): # para que no importen las mayúsculas o minúnsculas.
            return True
    return False    


def pedir_notas_alumno(cantidad): # pide la cantidad de notas solicitadas por parámetro y valida que sean valores entre 0 y 10
    notas = []                    
    contador = 0
    while contador < cantidad:
        nota = (input(f"ingresar nota {contador + 1}: "))
        if nota.isdigit and int(nota) <= 10:
            notas.append(int(nota))
            contador += 1
        else:
            print(f"La nota debe ser un dígito entre 0 y 10 ")
            continue
    return tuple(notas) # se genera un tupla a partir de la lista de notas

def promedio(notas):
    return round(sum(notas) / len(notas), 2)

alumnos = {}
cantidad_alumnos = 3
contador = 0

while contador < cantidad_alumnos:
    print()
    
    alumno = pedir_nombre_alumno()
    if not existe_alumno(alumnos,alumno): # si el alumno ingresado no existe aun en el diccionario se piden las notas y se agrega.
        notas = pedir_notas_alumno(3)
        alumnos[alumno] = notas
        contador +=1
    else:     # si existe el alumno en el diccionario se vuelve a pedir un nuevo ingreso sin actualizar el contador.
        print(f" ** El alumno {alumno} ya se cargó")
        continue
       

for alumno, notas  in alumnos.items():
    print(f"\nEl promedio del alumno {alumno} es: {promedio(notas)}")

print()


# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {1, 2, 4, 8, 9, 12, 13, 14, 15 }
parcial2 = {1, 4, 7, 9, 10, 11, 12, 13, 15}

# estudiantes que aprobaron ambos parciales = Intersección de los conjuntos parcial1 y parcial2
print(f"Los estudiantes que aprobaron ambos parciales son : {parcial1 & parcial2}")

# estudiantes que aprobaron solo un parcial = diferencia simétrica de los conjuntos parcial1 y parcial2
print(f"Los estudiantes que aprobaron ambos parciales son : {parcial1 ^ parcial2}")

# estudiantes que aprobaron al menos un parcial = unión de los conjuntos parcial1 y parcial2
print(f"Los estudiantes que aprobaron ambos parciales son : {parcial1 | parcial2}")


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe


def existe_producto(producto):
    return producto in productos


def agregar_unidades(producto, cantidad):
    productos[producto] += cantidad
    print(f"\nSe han agregado {cantidad} unidades al Producto {producto}, su Stock actual es {productos[producto]}")


def agregar_producto(producto):
    productos[producto] = 0
    print(f"\nSe ha dado de alta el Producto {producto} con Stock {productos[producto]}")


def consultar_stock(producto):
    return productos[producto]


def ingresar_cantidad(producto): # valida que la cantidad ingresada sea un número y mayor que 0
    while True:
        cantidad = input(f"Ingrese cantidad de unidades a agregar al stock del producto {producto}:  ")
        if cantidad.isdigit() and int(cantidad) > 0:
            return int(cantidad)
        else:
            print(f"El valor ingresado {cantidad} no es válido. Ingese un valor numérico entero positivo")    
            continue


def opcion_s_n(): # valida la opción de si o no para evaluarla directamente como boolena
     
    while True:

        opcion = input("Ingrese una opción:  ( S / N ): ")
        
        if opcion == "S" or opcion == "s":
            return True
        elif opcion == "N" or opcion == "n":
            return False
        else:
            print("la opción ingresada no es válida. Ingrese S o N")
            continue


# diccionario con 3 productos iniciales
productos = {
    'martillo' : 50,
    'pala' : 80,
    'serrucho' : 100
}

print("\n****  Consulta y actualización de Stock  ****\n")

producto = input(f"\nIngrese el producto a consultar: ").strip().lower()

if existe_producto(producto): # llama a la funsion y si existe muestra el stock.
    print(f"\nEl stock del producto {producto} es : {consultar_stock(producto)} .")
    
    print(f"\nDesea agregar unidades al stock de {producto} ?:") # como existe , pregunta si quiere agragar unidades.
    
    if opcion_s_n(): # LLama a la función de validación de opción , si responde que no sale del sistema.
        cantidad = ingresar_cantidad(producto)
        agregar_unidades(producto, cantidad)
        
else:
    print(f"\nEl producto {producto} no existe ") # como el producto no existe ...
    
    print(f"\nDesea dar de alta {producto} en el stock ?") # pregunta si lo quiere dar de alta...
    
    if opcion_s_n():
        agregar_producto(producto) # si la respuesta es positiva se da de alta con stock 0. 
        
        print(f"\nDesea agregar unidades al stock de {producto} ?:") # pregunta si quiere actualizar el stock
        
        if opcion_s_n():
            cantidad = ingresar_cantidad(producto)  # si la respuesta es positiva actualiza y sale del sitema.
            agregar_unidades(producto, cantidad)


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

dias_semana = ['lunes', 'martes', 'miércoloes', 'jueves', 'viernes', 'sábado', 'domingo'] # Lista para validar los días.

def ingresar_dia_consulta(): # valida el ingreso de los días en la consulta
    
    while True:
        
        dia = input("Ingrese el día de la semana: ").strip().lower()
        
        if dia in dias_semana:
            return dia
        else:
            print("no ha ingresado un valor válido para día de la semana")
            print("Intente de nuevo...")
            continue


# Diccionario agenda

agenda = {
    ('lunes', '10:30') : 'Presentación Informe Semanal',
    ('martes' , '15:00') : 'Reunión de Trabajo',
    ('miercoles', '12:00') : 'Almuerzo de Trabajo',
    ('jueves', '18:00') : 'Practica',
    ('viernes', '19:00') : 'Cierre de Semana',
 }


print("********************************")
print("\n****   Consultar Agenda   ****\n")
print("********************************")

dia_consulta = ingresar_dia_consulta() # se asigna a la variable el valor devuelto por la validación

for key in agenda.keys(): # se itera sobre la lista de tuplas clave
    if key[0] == dia_consulta: # se obtiene el "día" correpondiente al elemento del diccionario...
        print(f"{dia_consulta} , {key[1]} -  evento:  {agenda[key]}") # se configura el registro a mostrar por pantalla
print()   


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.

paises = {
    'Argentina':'Buenos Aires',
    'Chile': 'Santiago',
    'Paraguay' :'Asunción',
    'Uruguay': 'Montevideo'
}

paises_traspuesto = {}

for clave, valor in paises.items(): # iterando sobre el diccionario y obteniendo el par de valores clave , valor con el método items 
    paises_traspuesto[valor] = clave # se va formando el nuevo diccionario con los valores invertidos.

print(paises_traspuesto)