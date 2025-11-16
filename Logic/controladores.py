import time, sqlite3
from Logic.persistencia import *

def ingreso_usuario(usuario, password):
    try:
        conectar = sqlite3.connect("DB/productosapp.db")        
        cursor = conectar.cursor()
        sql = ("SELECT * FROM usuarios WHERE usuario=? AND password=? AND estado=1")
        valor = (usuario, password)
        cursor.execute(sql, valor)
        resultado = cursor.fetchone()
        if resultado:
            print("Ingreso exitoso")
            return True
        else:
            print("Usuario o contraseña incorrectos")
            return False
    except Exception as e:
        print(f"Error al ingresar el usuario: {e}")
        return False

def ver_usuarios():
    try:
        conectar = sqlite3.connect("DB/productosapp.db")
        cursor = conectar.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE estado=1")
        usuarios = cursor.fetchall()
        print("Usuarios activos:")
        for usuario in usuarios:
            print(f"\nIndice: {usuario[0]}\nNombre: {usuario[1]}\nUsuario: {usuario[2]}\nEmail: {usuario[3]}\nRol: {usuario[5]}")
    except Exception as e:
        print(f"Error al obtener los usuarios: {e}")
    finally:
        conectar.close()
       
       
def crear_usuario(nombre, usuario, email, password, rol):
    try:
        conectar = sqlite3.connect("DB/productosapp.db")
        cursor = conectar.cursor()
        sql = ("INSERT INTO usuarios (nombre, usuario, email, password, rol) VALUES (?, ?, ?, ?, ?)")
        valores = (nombre, usuario, email, password, rol)
        cursor.execute(sql, valores)
        conectar.commit()
        print("Usuario creado con exito")
    except Exception as e:
        print(f"Error al crear el usuario: {e}")
    finally:
        conectar.close()

def agregar_producto(nombre, precio, categoria, descripcion):
    try:
        conectar = sqlite3.connect("DB/productosapp.db")
        cursor = conectar.cursor()
        sql = ("INSERT INTO productos (nombre, precio, categoria, descripcion) VALUES (?, ?, ?, ?)")
        valores = (nombre, precio, categoria, descripcion)
        cursor.execute(sql, valores)
        conectar.commit()
        print("Producto agregado con exito")
    except Exception as e:
        print(f"Error al agregar el producto: {e}")
    finally:
        conectar.close()

def ver_productos():
    try:
        conectar = sqlite3.connect("DB/productosapp.db")
        cursor = conectar.cursor()
        cursor.execute("SELECT * FROM productos WHERE estado=1")
        productos = cursor.fetchall()
        print("Productos activos:")
        for producto in productos:
            print(f"\nIndice: {producto[0]}\nNombre: {producto[1]}\nPrecio: {producto[2]}\nCategoria: {producto[3]}\nDescripcion: {producto[4]}\nFecha Agregado: {producto[5]}")
    except Exception as e:
        print(f"Error al obtener los productos: {e}")
    finally:
        conectar.close() 
 
def buscar_producto(nombre):
    try:
        conectar = sqlite3.connect("DB/productosapp.db")
        cursor = conectar.cursor()
        sql = ("SELECT * FROM productos WHERE nombre LIKE ? AND estado=1")
        valor = (f"%{nombre}%",)
        cursor.execute(sql, valor)
        productos = cursor.fetchall()
        if productos:
            print("Productos encontrados:")
            for producto in productos:
                print(f"\nIndice: {producto[0]}\nNombre: {producto[1]}\nPrecio: {producto[2]}\nCategoria: {producto[3]}\nDescripcion: {producto[4]}\nFecha Agregado: {producto[5]}")
        else:
            print("No se encontraron productos con ese nombre.")
    except Exception as e:
        print(f"Error al buscar el producto: {e}")
    finally:
        conectar.close()

def modificar_producto(id, nombre, precio, categoria, descripcion):
    try:
        conectar = sqlite3.connect("DB/productosapp.db")
        cursor = conectar.cursor()
        sql = ("UPDATE productos SET nombre=?, precio=?, categoria=?, descripcion=? WHERE id=? AND estado=1")
        valores = (nombre, precio, categoria, descripcion, id)
        cursor.execute(sql, valores)
        conectar.commit()
        if cursor.rowcount > 0:
            print("Producto modificado con exito")
        else:
            print("No se encontró el producto con ese índice.")
    except Exception as e:
        print(f"Error al modificar el producto: {e}")
    finally:
        conectar.close()        
        
def eliminar_producto(indice):
    try:
        conectar = sqlite3.connect("DB/productosapp.db")
        cursor = conectar.cursor()
        sql = ("UPDATE productos SET estado=0 WHERE id=?")
        valor = (indice,)
        cursor.execute(sql, valor)
        conectar.commit()
        if cursor.rowcount > 0:
            print("Producto eliminado con exito")
        else:
            print("No se encontró el producto con ese índice.")
    except Exception as e:
        print(f"Error al eliminar el producto: {e}")
    finally:
        conectar.close()

def ver_menu():
    try:
        conectar = sqlite3.connect("DB/productosapp.db")
        cursor = conectar.cursor()
        cursor.execute("SELECT * FROM menu WHERE estado=1")
        menus = cursor.fetchall()
        print("Menu principal:\n")
        for menu in menus:
            time.sleep(0.4)
            print(f"{menu[0]}.- {menu[1]}")
        submenu()
    except Exception as e:
        print(f"Error al obtener el menu: {e}")
    finally:
        conectar.close()
        
def submenu():
    seleccion = input("\nSeleccione una opción del menú principal: ")
    if seleccion == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Agregar nuevo producto:\n")
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        categoria = input("Ingrese la categoría del producto: ")
        descripcion = input("Ingrese la descripción del producto: ")
        agregar_producto(nombre, precio, categoria, descripcion)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        ver_menu()
    elif seleccion == '2':
        ver_productos()
        ver_menu()  
    