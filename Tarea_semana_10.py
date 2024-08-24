# Semana 9
# Tarea: Sistema de Gestión de Inventarios

# Ingresar los atributos del producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Atributos del producto
        self._id_producto = id_producto  # ID único del producto
        self._nombre = nombre  # Nombre del producto
        self._cantidad = cantidad  # Cantidad en inventario
        self._precio = precio  # Precio del producto

    # funciones para leer y escribir cada atributo
    def get_id_producto(self):
        return self._id_producto

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_cantidad(self):
        return self._cantidad

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        self._precio = precio

    # Maneras de mostrar la información del producto
    def mostrar_info(self):
        return f"ID: {self._id_producto}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: {self._precio}"



# Inventario
class Inventario:
    def __init__(self):
        # Crear lista para almacenar los productos
        self.productos = []

    # Formas de añadir o eliminar productos

    def añadir_producto(self, producto):
        # Verificar que el ID del producto sea único antes de añadirlo
        for p in self.productos:
            if p.get_id_producto() == producto.get_id_producto():
                print("Error: Ya existe un producto con ese ID.") # código de error
                return
        self.productos.append(producto)
        print("Producto añadido con éxito.") # código exitoso

    def eliminar_producto(self, id_producto):
        # Eliminar producto por ID
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado con éxito.") # código exitoso
                return
        print("Error: Producto no encontrado.") # código de error

    # Formas de modificar el inventario

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Actualizar cantidad o precio de un producto por ID
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("Producto actualizado con éxito.") # código exitoso
                return
        print("Error: Producto no encontrado.") # código de error

    def buscar_producto(self, nombre):
        # Buscar productos por nombre (puede haber nombres similares)
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for p in resultados:
                print(p.mostrar_info())
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        # Mostrar todos los productos en el inventario
        if self.productos:
            for p in self.productos:
                print(p.mostrar_info())
        else:
            print("El inventario está vacío.")




# Impresión en pantalla
# Menu de opciones

def menu():
    inventario = Inventario()

    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto")
        print("4. Buscar producto(s) por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (o presione Enter para no cambiarla): ")
            precio = input("Ingrese el nuevo precio (o presione Enter para no cambiarlo): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_todos()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()


# Universidad Estatal Amazónica
# Andrés Ponce M.
