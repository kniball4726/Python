import sqlite3, os
from colorama import Fore, Style, init, Back


init()

def conexion(db_name):
    """
    Funcion para conectar a la base de datos SQLite
   
    Argumentos:
        db_name: Nombre de la base de datos SQLite
        
    Devuelve:
        Conexion a la base de datos SQLite
            
    """
    
    conectar = None
    
    if not os.path.exists("src/db"):
            os.makedirs("src/db")
    try:
        conectar = sqlite3.connect(db_name, timeout=20)
        print(Fore.YELLOW+f"Conexion establecida {db_name} con exito"+Fore.RESET)
        
    except sqlite3.Error as e:
        print(Fore.RED+f"no se ha establecido la conexion, error {e}"+Fore.RESET)
  
    return conectar
