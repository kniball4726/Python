import sqlite3, os
from colorama import Fore, Style, init, Back


init()

def conexion(db_name):
    
    conectar = None
    
    if not os.path.exists("src/db"):
            os.makedirs("src/db")
    try:
        conectar = sqlite3.connect(db_name)
        print(Fore.YELLOW+f"Conexion establecida {db_name} con exito"+Fore.RESET)
        
    except sqlite3.Error as e:
        print(Fore.RED+f"no se ha establecido la conexion, error {e}"+Fore.RESET)
        
    return conectar
