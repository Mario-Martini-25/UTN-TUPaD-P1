# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. 
# Cada línea debe tener: nombre,precio,cantidad

# Se crea en la carpeta del presente programa el archivo: productos.txt con el siguiente contenido:
# lapicera,120.5,30
# regla,18.5,45
# cuaderno,152.2,150


# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea,
#  la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

with open("productos.txt", "r" ) as archivo :
    print()
    for linea in archivo:
        producto = linea.strip().split(",")
        if producto != [""]: # filtra última línea en blanco.
            print(f"Producto: {producto[0]} | Precio: ${producto[1]} | Cantidad: {producto[2]}")


# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos,
#  le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y lo agregue 
#  al archivo sin borrar el contenido existente.

def pedir_nombre_producto(): # Pide nombre del producto y valida que el dato no sea número , solo espacios o esté vacío.
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        if  nombre.isdigit() or not nombre.strip() :
            print("\n** El nombre no debe estar vacío y debe contener letras **\n")
            print("Inteante nuevamente: ", end ="")
            continue
        else:
            return nombre
    

def pedir_precio(): # valida que el el importe sea positivo y sea un decimal válido y no esté vacío.
    while True:
        precio = input("Ingrese el precio unitario del Producto: ")
        if not precio.isdigit() or not precio.strip() or float(precio) < 0 :
            print("\n** El precio debe contener solo dígitos ,no puede estar vacío y no debe ser negativo. **\n")
            print("Inteante nuevamente: ", end ="")
            continue
        else:
            return float(precio)
        

def pedir_cantidad(): # valida que el el importe sea positivo , sea un entero y no esté vacío.
    while True:
        cantidad = input("Ingrese la cantidad del Producto: ")
        if not cantidad.isdigit() or not cantidad.strip() or int(cantidad) < 0:
            print("\n** La cantidad  debe ser un número entero, no estar vacía ni ser negativa **\n")
            print("Inteante nuevamente: ", end ="")
            continue     
        else:            
            return int(cantidad)
        

def consulta_productos(): # para automatizar la consulta luego de cada actualización.

    with open("productos.txt", "r" ) as archivo :
        print()
        print("------- Listado de productos dede archivo -------")
        for linea in archivo:
            producto = linea.strip().split(",")

            if producto != [""]: # filtra última línea en blanco.
                print(f"Producto: {producto[0]} | Precio: ${producto[1]} | Cantidad: {producto[2]}")


print(f"\n** Lista de Productos **\n") #Muestra los productos
consulta_productos()
    
print("\n** Ingrese un nuevo producto **\n") #Pide los datos de un nuevo producto y los agrega al archivo productos.txt **\n")
nombre_prod = pedir_nombre_producto()
precio_prod = pedir_precio()
cantidad_prod = pedir_cantidad()
    
with open("productos.txt", "a" ) as archivo :
    archivo.write(f"{nombre_prod},{precio_prod},{cantidad_prod}\n")

print(f"\n********* Lista de Productos Actualizada *********") #Muestra nuevamente los productos actualizados.
consulta_productos()



#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en una lista
#  llamada productos, donde cada elemento sea un diccionario con claves: nombre, precio, cantidad.

def carga_archivo_a_lista_dicc(): # abre el archivo productos.txt en modo lectura y genera una lista de diccionarios con los productos.
    
    with open("productos.txt", "r" ) as archivo :
        productos = []

        for linea in archivo:
            item = linea.strip().split(",") 
            if item != [""]: # filtra última línea en blanco.
                producto = {}
                producto['nombre'] = item[0]
                producto['precio'] = float(item[1])
                producto['cantidad'] = int(item[2])
                productos.append(producto)
       
    return productos # retorna la lista de diccionarios donde cada producto es un diccionario.

def consulta_lista_dicc(productos): # esta es una consulta sobre la lista generada con la lectura del archivo.
    print("\n************** Listado de Productos ****************")
    print("_____________________________________________________")

    for producto in productos: # itera sobre cada diccionario de la lista e imprime por pantalla.
        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
        
      
productos = carga_archivo_a_lista_dicc()

print("\n*** Lista de Productos desde lista cargada ***")
consulta_lista_dicc(productos)
print()
           

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto.
# Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. 
# Si no existe, mostrar un mensaje de error.

print("\n*** Buscar producto por nombre ***\n")

def existe_producto(nombre):

    for producto in productos :
        if nombre.upper() == producto['nombre'].upper() :
            mensaje = (f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
            return mensaje
        
    mensaje = (f"\n**** El Producto {nombre} no se encuentra en el listado de Productos.  ****\n")
    return mensaje

nombre = pedir_nombre_producto()

productos = carga_archivo_a_lista_dicc()

print(existe_producto(nombre))


# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado 
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente 
# todos los productos actualizados desde la lista.

def guardar_lista_en_archivo(productos):

    with open("productos.txt", 'w') as archivo:
        
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
            

print()
consulta_lista_dicc(productos) # para visualizar lo que se va a actualizar.

guardar_lista_en_archivo(productos) # sobreescribe los datos de la lista en el txt.

consulta_productos() # para comparar el contenido del archivo txt

