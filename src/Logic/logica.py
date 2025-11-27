import os, time
from colorama import init, Fore, Back 
from src.Controllers.controladores import *
from src.Persistencia.persistencia import *

init()
def ingreso():
  try:
    init()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.YELLOW + Style.BRIGHT+ "Bienvenido al sistema de gestión de productos\n" + Style.RESET_ALL + Fore.RESET)
    usuario = input("Ingrese su usuario: ").strip().upper()
    password = input("Ingrese su contraseña: ").strip()
    
    if ingreso_usuario(usuario, password):
      print(Fore.YELLOW + "Ingreso exitoso\n"+Fore.RESET)
      print(Fore.YELLOW+"Cargando el sistema..."+Fore.RESET)
      time.sleep(1)
      os.system('cls' if os.name == 'nt' else 'clear')
      ver_menu()
    else:
      print(Fore.RED + "Usuario o contraseña incorrectos\n"+Fore.RESET)
      time.sleep(2)
      os.system('cls' if os.name == 'nt' else 'clear')
      ingreso()
  except Exception as e:
    print(Fore.RED + f"Error durante el ingreso: {e}"+Fore.RESET)

  
def ver_menu():
    try:
        conectar = sqlite3.connect("src/db/productos.db")
        cursor = conectar.cursor()
        cursor.execute("SELECT * FROM menu WHERE estado=1")
        menus = cursor.fetchall()
        print(Fore.YELLOW+Style.BRIGHT+"Menu principal:\n"+Fore.RESET+Style.RESET_ALL)
        for menu in menus:
            time.sleep(0.4)
            print(f"{menu[0]}.- {menu[1]}")
        submenu()
    except sqlite3.Error as e:
        print(Fore.RED+f"Error al obtener el menu: {e}"+Fore.RESET)
    finally:
        conectar.close()
        
def submenu():
    seleccion = input(Fore.YELLOW+Style.BRIGHT+"\nSeleccione una opción del menú principal: "+ Fore.RESET+Style.RESET_ALL)
    try:
        init()
        if seleccion == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.YELLOW+"Agregar nuevo producto:\n"+Fore.RESET)
            nombre = input("Ingrese el nombre del producto: ").strip().upper()
            precio = float(input("Ingrese el precio del producto: "))
            categoria = input("Ingrese la categoría del producto: ").strip().upper()
            descripcion = input("Ingrese la descripción del producto: ").strip()
            if nombre == "" or precio <= 0 or categoria == "":
                print(Fore.RED + "\nError: Todos los campos son obligatorios y el precio debe ser mayor a cero."+Fore.RESET)
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_menu()
            else:
                agregar_producto(nombre, precio, categoria, descripcion)
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_menu()
                
        elif seleccion == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.YELLOW+"Ver productos:\n"+Fore.RESET)
            ver_productos()
            input(Fore.YELLOW+"\nPresione Enter para volver al menú principal..."+Fore.RESET)
            os.system('cls' if os.name == 'nt' else 'clear')
            ver_menu()
        elif seleccion == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.YELLOW+"Buscar producto:\n"+Fore.RESET)
            termino_busqueda = input("Ingrese el nombre del producto a buscar: ")
            buscar_producto(termino_busqueda)
            input(Fore.YELLOW+"\nPresione Enter para volver al menú principal..."+Fore.RESET)
            os.system('cls' if os.name == 'nt' else 'clear')
            ver_menu()
        elif seleccion == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.YELLOW+"Modificar producto:\n"+Fore.RESET)
            id_producto = int(input("Ingrese el ID del producto a modificar: ")).strip()
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ").strip().upper()
            nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
            nueva_categoria = input("Ingrese la nueva categoría del producto: ").strip().upper()
            nueva_descripcion = input("Ingrese la nueva descripción del producto: ").strip()
            
            if nuevo_nombre == "" or nuevo_precio <= 0 or nueva_categoria == "":
                print(Fore.RED + "Error: Todos los campos son obligatorios y el precio debe ser mayor a cero."+Fore.RESET)
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_menu()
            else:                
                modificar_producto(id_producto, nuevo_nombre, nuevo_precio, nueva_categoria, nueva_descripcion)
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_menu()
        elif seleccion == '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.YELLOW+"Eliminar producto:\n"+Fore.RESET)
            id_producto = int(input("Ingrese el ID del producto a eliminar: ")).strip()
            if not id_producto or id_producto <= 0 or id_producto == "" or id_producto is None:
                print(Fore.RED + "Error: El ID del producto es obligatorio." + Fore.RESET)
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_menu()
            else:
                eliminar_producto(id_producto)
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_menu()
        elif seleccion == '6':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.YELLOW+"Gestión de usuarios:\n"+Fore.RESET)
            menu_usuarios = ["1.- Ver usuarios", "2.- Agregar usuario", "3.- Modificar usuario", "4.- Eliminar usuario"]
            for item in menu_usuarios:
                print(item)
                time.sleep(0.4)
            opcion_usuario = input(Fore.YELLOW+Style.BRIGHT+"\nSeleccione una opción del menú de usuarios: "+Fore.RESET+Style.RESET_ALL)
            
            os.system('cls' if os.name == 'nt' else 'clear')
            if opcion_usuario == '1':
                ver_usuarios()
                input(Fore.YELLOW+"\nPresione Enter para volver al menú principal..."+Fore.RESET)
            elif opcion_usuario == '2':
                print(Fore.YELLOW+"Agregar nuevo usuario:\n"+Fore.RESET)
                nombre = input("Ingrese el nombre completo: ").strip().upper()
                usuario = input("Ingrese el nombre de usuario: ").strip().upper()
                email = input("Ingrese el email: ").strip().lower()
                password = input("Ingrese la contraseña: ").strip()
                rol = input("Ingrese el rol (admin/user): ").strip().lower()
                
                if nombre == "" or usuario == "" or email == "" or password == "" or rol == "":
                    print(Fore.RED + "Error: Todos los campos son obligatorios."+Fore.RESET)
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    ver_menu()
                else:
                    crear_usuario(nombre, usuario, email, password, rol)
                    time.sleep(2)
            
            elif opcion_usuario == '3':
                print(Fore.YELLOW+"Modificar usuario:\n"+Fore.RESET)
                id_usuario = int(input("Ingrese el ID del usuario a modificar: ")).strip()
                nuevo_nombre = input("Ingrese el nuevo nombre completo: ").strip().upper()
                nuevo_usuario = input("Ingrese el nuevo nombre de usuario: ").strip().upper()
                nuevo_email = input("Ingrese el nuevo email: ").strip().lower()
                nuevo_password = input("Ingrese la nueva contraseña: ").strip()
                nuevo_rol = input("Ingrese el nuevo rol (admin/user): ").strip().lower()
                
                if nuevo_nombre == "" or nuevo_usuario == "" or nuevo_email == "" or nuevo_password == "" or nuevo_rol == "":
                    print(Fore.RED + "Error: Todos los campos son obligatorios."+Fore.RESET)
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    ver_menu()
                else:
                    modificar_usuario(id_usuario, nuevo_nombre, nuevo_usuario, nuevo_email, nuevo_password, nuevo_rol)
                    time.sleep(2)
            
            elif opcion_usuario == '4':
                print(Fore.YELLOW+"Eliminar usuario:\n"+Fore.RESET)
                id_usuario = int(input("Ingrese el ID del usuario a eliminar: ")).strip()
                if not id_usuario or id_usuario <= 0 or id_usuario == "" or id_usuario is None:
                    print(Fore.RED + "Error: El ID del usuario es obligatorio." + Fore.RESET)
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    ver_menu()
                else:
                    eliminar_usuario(id_usuario)
                    time.sleep(2)
            else:
                print(Fore.RED+"\nOpción no válida. Volviendo al menú principal..."+Fore.RESET)
                time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            ver_menu()
            
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
            ver_menu()
    except Exception as e:
        print(Fore.RED + f"Error al procesar la selección del menú: {e}"+Fore.RESET)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        ver_menu()  
      