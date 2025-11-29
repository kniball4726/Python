import os, time, dotenv, sqlite3
from colorama import init, Fore, Back , Style
from ..Persistencia.conectar import conexion
from ..Controllers.controladores import *

dotenv.load_dotenv()

DATABASE_NAME = os.getenv("DATABASE_NAME")

conectar = conexion(DATABASE_NAME)

init()
def ingreso(conectar=conexion(DATABASE_NAME)):
    """
    Funcion para el ingreso de usuarios al sistema
    
    Args:
        conectar: Conexion a la base de datos
    
    Returns:
        None
    """

    try:
      os.system('cls' if os.name == 'nt' else 'clear')
      print(Fore.YELLOW + Style.BRIGHT+ "Bienvenido al sistema de gestión de productos\n" + Style.RESET_ALL + Fore.RESET)
      usuario = input("Ingrese su usuario: ").strip().upper()
      password = input("Ingrese su contraseña: ").strip()
    
      if ingreso_usuario(conectar, usuario, password):
        print(Fore.YELLOW + "Ingreso exitoso\n"+Fore.RESET)
        print(Fore.YELLOW+"Cargando el sistema..."+Fore.RESET)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        ver_menu(conectar)
      else:
        print(Fore.RED + "Usuario o contraseña incorrectos\n"+Fore.RESET)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        ingreso(conectar)
    except sqlite3.Error as e:
      print(Fore.RED + f"Error durante el ingreso: {e}"+Fore.RESET)
    
    
def ver_menu(conectar=conexion(DATABASE_NAME)):
    """
    Funcion para mostrar el menu principal del sistema
    Args:
        conectar: Conexion a la base de datos
        Returns:
            None
    """    
    
    try:
        cursor = conectar.cursor()
        cursor.execute("SELECT * FROM menu WHERE estado=1")
        menus = cursor.fetchall()
        print(Fore.YELLOW+Style.BRIGHT+"Menu principal:\n"+Fore.RESET+Style.RESET_ALL)
        for menu in menus:
            time.sleep(0.4)
            print(f"{menu[0]}.- {menu[1]}")
        submenu(conectar)
    except sqlite3.Error as e:
        print(Fore.RED+f"Error al obtener el menu: {e}"+Fore.RESET)
        
def submenu(conectar=conexion(DATABASE_NAME)):
    """
    Funcion para manejar las opciones del menu principal
    Args:
        conectar: Conexion a la base de datos
        Returns:
            None
    """
    seleccion = input(Fore.YELLOW+Style.BRIGHT+"\nSeleccione una opción del menú principal: "+ Fore.RESET+Style.RESET_ALL)
    try:
        if seleccion == '1':    
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.YELLOW+"Agregar nuevo producto:\n"+Fore.RESET)
            nombre = input("Ingrese el nombre del producto: ").strip().upper()
            descripcion = input("Ingrese la descripción del producto: ").strip()
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            categoria = input("Ingrese la categoría del producto: ").strip().upper()
           
            if len(nombre) <= 0 or precio < 0.00 or len(categoria) <= 0 or cantidad < 0:
                print(Fore.RED + "\nError: Todos los campos son obligatorios y el precio debe ser mayor a cero."+Fore.RESET)
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_menu(conectar)
            else:
                agregar_producto(conectar, nombre, descripcion, cantidad, precio, categoria, )
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_menu(conectar)
                
        elif seleccion == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.YELLOW+"Ver productos:\n"+Fore.RESET)
            ver_productos(conectar)
            input(Fore.YELLOW+"\nPresione Enter para volver al menú principal..."+Fore.RESET)
            os.system('cls' if os.name == 'nt' else 'clear')
            ver_menu(conectar)
        elif seleccion == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.YELLOW+"Buscar producto (Seleccione criterio):\n"+Fore.RESET)
            print("1.- Id\n2.- Nombre\n3.- Volver al menú principal ")
            menu_buscar = input(Fore.YELLOW+Style.BRIGHT+"\nIngrese su opción: "+Fore.RESET+Style.RESET_ALL)
            if menu_buscar == '1':
                termino_busqueda = int(input(Fore.YELLOW+"\nIngrese el ID del producto a buscar: "+Fore.RESET))
                buscar_producto(conectar, 1, termino_busqueda)
                input(Fore.YELLOW+"\nPresione Enter para volver al menú principal..."+Fore.RESET)
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_menu(conectar)
            elif menu_buscar == '2':
                termino_busqueda = input(Fore.YELLOW+"\nIngrese el nombre del producto a buscar: "+Fore.RESET).strip()
                buscar_producto(conectar, 2, termino_busqueda)
                input(Fore.YELLOW+"\nPresione Enter para volver al menú principal..."+Fore.RESET)
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_menu(conectar)
            elif menu_buscar == '3':    
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_menu(conectar)
            else:
                print(Fore.RED + "\nError: Opción no válida."+Fore.RESET)
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_menu(conectar)
                
        elif seleccion == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.YELLOW+"Modificar producto:\n"+Fore.RESET)
            id_producto = int(input("Ingrese el ID del producto a modificar: "))
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ").strip().upper()
            nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
            nueva_categoria = input("Ingrese la nueva categoría del producto: ").strip().upper()
            nueva_descripcion = input("Ingrese la nueva descripción del producto: ").strip()
            
            if len(nuevo_nombre)<=0 or nuevo_precio <= 0 or len(nueva_categoria)<= 0:
                print(Fore.RED + "Error: Todos los campos son obligatorios y el precio debe ser mayor a cero."+Fore.RESET)
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_menu(conectar)
            else:                
                modificar_producto(conectar, id_producto, nuevo_nombre, nuevo_precio, nueva_categoria, nueva_descripcion)
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_menu(conectar)
        elif seleccion == '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.YELLOW+"Eliminar producto:\n"+Fore.RESET)
            id_producto = int(input("Ingrese el ID del producto a eliminar: "))
            if not id_producto or id_producto is None:
                print(Fore.RED + "Error: El ID del producto es obligatorio." + Fore.RESET)
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_menu(conectar)
            else:
                eliminar_producto(conectar, id_producto)
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_menu(conectar)
        elif seleccion == '6':
            try:
                os.system('cls' if os.name == 'nt' else 'clear')
                cursor = conectar.cursor()
                cursor.execute("SELECT * FROM submenu WHERE estado=1")
                submenu = cursor.fetchall()
                print(Fore.YELLOW+Style.BRIGHT+"Menu de usuarios:\n"+Fore.RESET+Style.RESET_ALL)
                for submenus in submenu:
                    time.sleep(0.4)
                    print(f"{submenus[0]}.- {submenus[1]}")
                submenu_usuarios(conectar)
            except sqlite3.Error as e:
                    print(Fore.RED+f"Error al obtener el menu: {e}"+Fore.RESET)
        elif seleccion == '7':
            print(Fore.YELLOW + "Saliendo del sistema..."+Fore.RESET)
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.YELLOW + Style.BRIGHT+ "Gregory Rodriguez © 2025\nDNI 95777596\nGracias por usar la aplicación."+Fore.RESET+Style.RESET_ALL)
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print(Fore.RED+"Opción no válida. Intente de nuevo."+Fore.RESET)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            ver_menu(conectar)
    except sqlite3.Error as e:
        print(Fore.RED + f"Error al procesar la selección del menú: {e}"+Fore.RESET)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        ver_menu(conectar)  
    
def submenu_usuarios(conectar=conexion(DATABASE_NAME)):
    """
    Funcion para manejar las opciones del submenú de usuarios
    
    Args:
        conectar: Conexion a la base de datos
        
        Returns:
            None
    """
    
    opcion_usuario = input(Fore.YELLOW+Style.BRIGHT+"\nSeleccione una opción del menú principal: "+ Fore.RESET+Style.RESET_ALL)
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        if opcion_usuario == '1':
            ver_usuarios(conectar)
            input(Fore.YELLOW+"\nPresione Enter para volver al menú principal..."+Fore.RESET)
        elif opcion_usuario == '2':
            print(Fore.YELLOW+"Agregar nuevo usuario:\n"+Fore.RESET)
            nombre = input("Ingrese el nombre completo: ").strip().upper()
            usuario = input("Ingrese el nombre de usuario: ").strip().upper()
            email = input("Ingrese el email: ").strip().lower()
            password = input("Ingrese la contraseña: ").strip()
            rol = input("Ingrese el rol (admin/user): ").strip().lower()
            
            if len(nombre)<= 0 or len(usuario)<= 0 or len(email)<= 0 or len(password)<= 0 or len(rol)<= 0:
                print(Fore.RED + "Error: Todos los campos son obligatorios."+Fore.RESET)
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_menu(conectar)
            else:
                crear_usuario(conectar, nombre, usuario, email, password, rol)
                time.sleep(2)
        
        elif opcion_usuario == '3':
            print(Fore.YELLOW+"Modificar usuario:\n"+Fore.RESET)
            id_usuario = int(input("Ingrese el ID del usuario a modificar: ")).strip()
            nuevo_nombre = input("Ingrese el nuevo nombre completo: ").strip().upper()
            nuevo_usuario = input("Ingrese el nuevo nombre de usuario: ").strip().upper()
            nuevo_email = input("Ingrese el nuevo email: ").strip().lower()
            nuevo_password = input("Ingrese la nueva contraseña: ").strip()
            nuevo_rol = input("Ingrese el nuevo rol (admin/user): ").strip().lower()
            
            if len(nuevo_nombre)<= 0 or len(nuevo_usuario)<= 0 or len(nuevo_email)<= 0 or len(nuevo_password)<= 0 or len(nuevo_rol)<= 0:
                print(Fore.RED + "Error: Todos los campos son obligatorios."+Fore.RESET)
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_menu(conectar)
            else:
                modificar_usuario(conectar, id_usuario, nuevo_nombre, nuevo_usuario, nuevo_email, nuevo_password, nuevo_rol)
                time.sleep(2)
        
        elif opcion_usuario == '4':
            print(Fore.YELLOW+"Eliminar usuario:\n"+Fore.RESET)
            id_usuario = int(input("Ingrese el ID del usuario a eliminar: ")).strip()
            if not id_usuario or id_usuario <= 0 or id_usuario == "" or id_usuario is None:
                print(Fore.RED + "Error: El ID del usuario es obligatorio." + Fore.RESET)
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_menu(conectar)
            else:
                eliminar_usuario(conectar, id_usuario)
                time.sleep(2)
        else:
            print(Fore.RED+"\nOpción no válida. Volviendo al menú principal..."+Fore.RESET)
            time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        ver_menu(conectar)
    except sqlite3.Error as e:
        print(Fore.RED+f"Error durante la operación del submenú de usuarios: {e}"+Fore.RESET)
       