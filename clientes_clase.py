#La idea general es hace un clase para agregar nuesvo clientes 
#Se tomara cuenta datos ncesario como
###Nombre
###Direccion
###Telefono
###Edad
###Correo
class Cliente:
    def __init__(self,nombre,edad,direccion):
        self.nombre = nombre
        self.edad  = edad
        self.direccion = direccion
    
    def get_cliente(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nDireccion: {self.direccion}")
    
   

class Producto:
    def __init__(self,id,nombre,precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio
    
    def get_producto(self):
        print(f"id: {self.id}\nNombre: {self.nombre}\nPrecio: {self.precio}")

class Ventas:
    def __init__(self,cliente):
        self.cliente = cliente
        self.producto = []
    
    def agrega_producto(self,producto):
        self.producto.append(producto)
    
    def total_venta(self):
        return sum(p.precio for p in self.producto)
    
    def resumen(self):
        print(f"Cliente\nNombre: {self.cliente.nombre}")
        print("Productos")
        for produc in self.producto:
            print(f"- {produc.nombre}: {produc.precio}")
        print(f"Total: {self.total_venta()}")

list_clientes = []
list_clientes.append(Cliente("Marco",21,"Copalera"))
list_clientes.append(Cliente("Perla",23,"Tabachin"))

def mostrar_clientes():
    for cliente in list_clientes:
        print(cliente.get_cliente())

def buscar_clientes(nombre_buscar):
    for clientes in list_clientes:
        if clientes.nombre.lower() == nombre_buscar.lower():
            return clientes
    return None

list_productos = []
list_productos.append(Producto(1,"Sabritas",25))
list_productos.append(Producto(2,"Coca-Cola",31))
list_productos.append(Producto(3,"Galletas",10))
list_productos.append(Producto(4,"Dulces",5))

def mostrar_producto():
    for producto in list_productos:
        print(producto.get_producto())
        
def buscar_producto(nom_producto):
    for producto in list_productos:
        if producto.nombre.lower() == nom_producto.lower():
            return producto
    return None

ventas_gen = []

def agregar_venta_producto(venta):
    venta_proceso = venta
    while True:
        print("Menu secundaro para agregar un prodcuto")
        print("1.-Agregar Producto\n2.-Lista de Producto\n3.-Terminar")
        opcion = input("Selecciona una opcion: ")
        if opcion == "1":
            producto_agregar = buscar_producto(input("Nombre del producto: "))
            if producto_agregar:
                venta_proceso.agrega_producto(producto_agregar)
                print(f"Producto: {producto_agregar.nombre}")
            else:
                print("Producto no encontrado")
        elif opcion == "2":
            mostrar_producto()
        elif opcion == "3":
            break
        else:
            print("Opcion no valida")     
        
    
    return venta_proceso

def agregar_venta_cliente():
    while True:       
        opcion = 0 
        nom_client = input("¿Nombre del cliente?")
        cliente = buscar_clientes(nom_client)
        if cliente:
            return cliente
        else:
            print("Cliente no encontrado")
            print("1.-Finalizar\n2.-Seguir Buscando")
            opcion = int(input("Seleccione una opcion: "))
            
        if opcion == 1:
            return None

def agregar_venta():
         
    opcion = 0   
    
    cliente = agregar_venta_cliente()
    if cliente:
        while True:
            print(f"Cliente encontrado {cliente.nombre}")
            venta_proceso = Ventas(cliente)
            venta_proceso = agregar_venta_producto(venta_proceso)
            print("Compra Realizada")
            venta_proceso.resumen()
            print("¿Desa finalizar la compra?")
            print("1.-Finalizar Correctamente\n2.-Cancelar")
            opcion = int(input("Seleccione una opcion: "))
            if opcion == 1:
                ventas_gen.append(venta_proceso)
                print("Compra finalizada")
                break
            else:
                print("Compra Cancelada")
                break           
        
    else:
        print("Cancelacion")
            
         
            
        

while True:
    print("Caja registradora")
    print("1.-Agregar Venta\n2.-Ver clientes\n3.-Ver Productos\n4.-Salir")
    opcion = input("Selecciona una opcion: ")
    if opcion == "1":
        agregar_venta()
        print("\n\n") 
    elif opcion == "2":
        mostrar_clientes() 
        print("\n\n") 
    elif opcion == "3":
        mostrar_producto()   
        print("\n\n") 
    elif opcion == "4":
        break
    else:
        print("Opcion no valida") 
        
        