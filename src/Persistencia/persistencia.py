import sqlite3, os, dotenv
from colorama import init, Fore, Back, Style
from ..Persistencia.conectar import conexion

dotenv.load_dotenv()

DATABASE_NAME = os.getenv("DATABASE_NAME")

conectar = conexion(DATABASE_NAME)

init()

def datos():
    """
    Funcion para inicializar la base de datos y crear las tablas necesarias

    Argumentos:
        None

    Devuelve:
        None
    """
try:
        cursor = conectar.cursor()        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                usuario TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                rol TEXT DEFAULT 'Usuario' NOT NULL,
                estado INTEGER NOT NULL DEFAULT 1
                )
            
                """ )
            
            
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL,
                categoria TEXT NOT NULL,
                fecha_agregado TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                estado INTEGER NOT NULL DEFAULT 1           
                )
            
                """ )

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS menu(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                estado INTEGER NOT NULL DEFAULT 1
                )
            
                """ )
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS submenu(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                estado INTEGER NOT NULL DEFAULT 1
                )
            
                """ )
            
        print(Fore.YELLOW+"Base de datos y tablas creadas con exito"+Fore.RESET)
except sqlite3.Error as e:
        print(Fore.RED+f"Error al crear las tablas: {e}"+Fore.RESET)

        
try:
        cursor = conectar.cursor()       

        sql = ("INSERT INTO usuarios (id, nombre, usuario, email, password, rol, estado) VALUES (?,?, ?, ?, ?, ?, ?)")
        valores = [(1, 'ADMINISTRADOR', 'ADMIN', 'admin@gmail.com', 'admin123', 'admin', 1)]
        
        cursor.executemany(sql, valores)
        conectar.commit()
        
        print(Fore.YELLOW+"Datos iniciales insertados con exito"+Fore.RESET)
except sqlite3.Error as e:
        print(f"Error al insertar los datos iniciales: {e}")


try:
        cursor = conectar.cursor()
        sql = ("INSERT INTO menu (id, nombre, descripcion, estado) VALUES (?,?, ?, ?)")
        valores = [(1, 'Ingresar Producto', 'Menu principal de la aplicacion', 1),
                   (2, 'Ver productos', 'Menu de ver productos', 1),
                   (3, 'Buscar producto', 'Menu de busqueda', 1),
                   (4, 'Modificar producto', 'Menu de modificación de productos', 1),
                   (5, 'Eliminar producto', 'Menu de eliminacion de productos', 1),
                   (6, 'Gestión de usuarios', 'Gestionar usuarios', 1),
                   (7, 'Salir', 'Salir de la aplicacion', 1)
                   ]
        cursor.executemany(sql, valores)
        conectar.commit()
        
        print(Fore.YELLOW+"Datos iniciales insertados con exito"+Fore.RESET)
except sqlite3.Error as e:
        print(f"Error al insertar los datos iniciales: {e}")

try:
        cursor = conectar.cursor()
        sql = ("INSERT INTO submenu (id, nombre, descripcion, estado) VALUES (?,?, ?, ?)")
        valores = [(1, 'Ver usuarios', 'Ver los usuarios agregados', 1),
                   (2, 'Agregar usuario', 'Agregar usuario', 1),
                   (3, 'Modificar usuario', 'Menu de modificación de productos', 1),
                   (4, 'Eliminar usuario', 'Menu de eliminacion de productos', 1),
                   (5, 'Volver', 'Salir de la aplicacion', 1)
                   ]
        cursor.executemany(sql, valores)
        conectar.commit()
        
        print(Fore.YELLOW+"Datos iniciales insertados con exito"+Fore.RESET)
except sqlite3.Error as e:
        print(f"Error al insertar los datos iniciales: {e}")


def aplicacion():
        """
        Funcion para iniciar la aplicacion
        
        Argumentos:
            None
        
        Devuelve:
            None
        """
datos()
conexion(DATABASE_NAME)