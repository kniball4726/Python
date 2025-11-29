import os, time, sqlite3, dotenv
from ..Persistencia.persistencia import conexion
from colorama import init, Fore, Back, Style

dotenv.load_dotenv()

DATABASE_NAME = os.getenv("DATABASE_NAME")

conectar = conexion(DATABASE_NAME)

init()
def ingreso_usuario(conectar, usuario, password):
    try:
        cursor = conectar.cursor()
        sql = ("SELECT * FROM usuarios WHERE usuario=? AND password=? AND estado=1")
        valor = (usuario, password)
        cursor.execute(sql, valor)
        resultado = cursor.fetchone()
        if resultado:
            return Fore.YELLOW+Style.BRIGHT+"Ingreso exitoso"+Style.RESET_ALL + Fore.RESET
        else:
            return False 
    except sqlite3.Error as e:
        print(Fore.RED+Style.BRIGHT+f"Error al ingresar el usuario: {e}"+Style.RESET_ALL + Fore.RESET)
        return False

def ver_usuarios(conectar=conexion(DATABASE_NAME)):
    try:
        cursor = conectar.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE estado=1")
        usuarios = cursor.fetchall()
        print(Fore.YELLOW+"\nUsuarios activos:"+Fore.RESET)
        for usuario in usuarios:
            print(f"\nIndice: {usuario[0]}\nNombre: {usuario[1]}\nUsuario: {usuario[2]}\nEmail: {usuario[3]}\nRol: {usuario[5]}")
    except sqlite3.Error as e:
        print(Fore.RED+"\nError al obtener los usuarios: {e}"+Fore.RESET)

       
def crear_usuario(conectar, nombre, usuario, email, password, rol):
    try:
        cursor = conectar.cursor()
        sql = ("INSERT INTO usuarios (nombre, usuario, email, password, rol) VALUES (?, ?, ?, ?, ?)")
        valores = (nombre, usuario, email, password, rol)
        cursor.execute(sql, valores)
        conectar.commit()
        print(Fore.YELLOW+"\nUsuario creado con exito"+Fore.RESET)
    except sqlite3.Error as e:
        print(Fore.RED+f"\nError al crear el usuario: {e}"+Fore.RESET)

def modificar_usuario(conectar, id, nombre, usuario, email, password, rol):
    try:
        cursor = conectar.cursor()
        sql = ("UPDATE usuarios SET nombre=?, usuario=?, email=?, password=?, rol=? WHERE id=? AND estado=1")
        valores = (nombre, usuario, email, password, rol, id)
        cursor.execute(sql, valores)
        conectar.commit()
        if cursor.rowcount > 0:
            print(Fore.YELLOW+"\nUsuario modificado con exito"+Fore.RESET)
        else:
            print(Fore.RED+"\nNo se encontró el usuario con ese índice."+Fore.RESET)
    except sqlite3.Error as e:
        print(Fore.RED+f"\nError al modificar el usuario: {e}"+Fore.RESET)


def eliminar_usuario(conectar, indice):
    try:
        cursor = conectar.cursor()
        sql = ("UPDATE usuarios SET estado=0 WHERE id=?")
        valor = (indice,)
        cursor.execute(sql, valor)
        conectar.commit()
        if cursor.rowcount > 0:
            print(Fore.YELLOW+"\nUsuario eliminado con exito"+Fore.RESET)
        else:
            print(Fore.RED+"\nNo se encontró el usuario con ese índice."+Fore.RESET)
    except sqlite3.Error as e:
        print(Fore.RED+f"\nError al eliminar el usuario: {e}"+Fore.RESET)
    

def agregar_producto(conectar, nombre, descripcion, cantidad, precio, categoria):
    try:
        cursor = conectar.cursor()
        sql = "INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)"
        valores = (nombre, descripcion, cantidad, precio, categoria)
        cursor.execute(sql, valores)
        conectar.commit()
        print(Fore.YELLOW+"\nProducto agregado con exito"+Fore.RESET)
    except sqlite3.Error as e:
        print(Fore.RED+f"\nError al agregar el producto: {e}"+Fore.RESET)


def ver_productos(conectar=conexion(DATABASE_NAME)):
    try:
        cursor = conectar.cursor()
        cursor.execute("SELECT * FROM productos WHERE estado=1")
        productos = cursor.fetchall()
        for producto in productos:
            print(f"\nIndice: {producto[0]}\nNombre: {producto[1]}\nDescripción: {producto[2]}\nCantidad: {producto[3]}\nPrecio: {producto[4]}\nCategoria: {producto[5]}\nFecha de agregado: {producto[6]}")
    except sqlite3.Error as e:
        print(Fore.RED+f"Error al obtener los productos: {e}"+Fore.RESET)
 
def buscar_producto(conectar, tipo, busqueda):
    try:
        if tipo == 1:
            cursor = conectar.cursor()
            sql = ("SELECT * FROM productos WHERE id = ? AND estado=1")
            valor = (busqueda,)
            cursor.execute(sql, valor)
            producto = cursor.fetchone()
            if producto:
                print(Fore.YELLOW+"Producto encontrado:"+Fore.RESET)
                print(f"\nIndice: {producto[0]}\nNombre: {producto[1]}\nPrecio: {producto[2]}\nCategoria: {producto[3]}\nDescripcion: {producto[4]}\nFecha Agregado: {producto[5]}")
        elif tipo == 2:
            nombre = busqueda.strip().upper()       
            cursor = conectar.cursor()
            sql = "SELECT * FROM productos WHERE nombre LIKE ? AND estado=1"
            valor = (f"%{nombre}%",)
            cursor.execute(sql, valor)
            productos = cursor.fetchall()
            if productos:
                print(Fore.YELLOW+"Productos encontrados:"+Fore.RESET)
                for producto in productos:
                    print(f"\nIndice: {producto[0]}\nNombre: {producto[1]}\nPrecio: {producto[2]}\nCategoria: {producto[3]}\nDescripcion: {producto[4]}\nFecha Agregado: {producto[5]}")
            else:
                print(Fore.RED+"\nNo se encontraron productos con ese nombre."+Fore.RESET)
        else:
            print(Fore.RED+"\nDebe proporcionar al menos un criterio de búsqueda (ID, nombre o categoría)."+Fore.RESET)
    except sqlite3.Error as e:
        print(Fore.RED+f"\nError al buscar el producto: {e}"+Fore.RESET)

        
        
        
def modificar_producto(conectar, id, nombre, precio, categoria, descripcion):
    try:
        cursor = conectar.cursor()
        sql = ("UPDATE productos SET nombre=?, precio=?, categoria=?, descripcion=? WHERE id=? AND estado=1")
        valores = (nombre, precio, categoria, descripcion, id)
        cursor.execute(sql, valores)
        conectar.commit()
        if cursor.rowcount > 0:
            print(Fore.YELLOW+"\nProducto modificado con exito"+Fore.RESET)
        else:
            print(Fore.RED+"\nNo se encontró el producto con ese índice."+Fore.RESET)
    except sqlite3.Error as e:
        print(Fore.RED+f"\nError al modificar el producto: {e}"+Fore.RESET)
        
def eliminar_producto(conectar, indice):
    try:
        cursor = conectar.cursor()
        sql = ("UPDATE productos SET estado=0 WHERE id=?")
        valor = (indice,)
        cursor.execute(sql, valor)
        conectar.commit()
        if cursor.rowcount > 0:
            print(Fore.YELLOW+"\nProducto eliminado con exito"+Fore.RESET)
        else:
            print(Fore.RED+"\nNo se encontró el producto con ese índice."+Fore.RESET)
    except sqlite3.Error as e:
        print(Fore.RED+f"Error al eliminar el producto: {e}"+Fore.RESET)
    