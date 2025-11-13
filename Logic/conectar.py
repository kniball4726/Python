import sqlite3

conectar = None


def crear_database():
    try:
        conectar = sqlite3.connect("db/usuarios.db")
        cursor = conectar.cursor()
        
        cursor.execute("""
        CREATE TABLE usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        
            """ )
        
    except Exception as e:
        print(f"no se ha establecido la conexion, error {e}")
    finally:
        conectar.close()

crear_database()