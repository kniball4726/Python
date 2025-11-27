import sqlite3
import os
from src.Logic.logica import ingreso

conectar = None

def conexion():
    try:
        if not os.path.exists("src/db"):
            os.makedirs("src/db")
            
        conectar = sqlite3.connect("src/db/productos.db")
        print("Conexion establecida")
        
    except sqlite3.Error as e:
        print(f"no se ha establecido la conexion, error {e}")
    return conectar

def crear_tablas():
    try:
        conectar = sqlite3.connect("src/db/productos.db")
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
                precio REAL NOT NULL,
                categoria TEXT NOT NULL,
                descripcion TEXT,
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
            
        print("Base de datos y tablas creadas con exito")
    except sqlite3.Error as e:
        print(f"Error al crear las tablas: {e}")
    finally:
        conectar.close() 
        
def datos_iniciales():
    try:
        conectar = sqlite3.connect("src/db/productos.db")
        cursor = conectar.cursor()       

        sql = ("INSERT INTO usuarios (id, nombre, usuario, email, password, rol, estado) VALUES (?,?, ?, ?, ?, ?, ?)")
        valores = [(1, 'ADMINISTRADOR', 'ADMIN', 'admin@gmail.com', 'admin123', 'admin', 1)]
        
        cursor.executemany(sql, valores)
        conectar.commit()
        
        print("Datos iniciales insertados con exito")
    except sqlite3.Error as e:
        print(f"Error al insertar los datos iniciales: {e}")
    finally:
        conectar.close()

def datos_menu():
    try:
        conectar = sqlite3.connect("src/db/productos.db")
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
        
        print("Datos iniciales insertados con exito")
    except sqlite3.Error as e:
        print(f"Error al insertar los datos iniciales: {e}")
    finally:
        conectar.close()


def aplicacion():
    conexion()
    crear_tablas()
    datos_iniciales()
    datos_menu()
    ingreso()