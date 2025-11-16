import os, time
from colorama import init, Fore, Back 
from Logic.controladores import *
from Logic.persistencia import *


def ingreso():
  try:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + "Bienvenido al sistema de gestión de productos\n")
    usuario = input("Ingrese su usuario: ").strip().upper()
    password = input("Ingrese su contraseña: ").strip()
    
    if ingreso_usuario(usuario, password):
      print(Fore.GREEN + "Ingreso exitoso\n")
      print("Cargando el sistema...")
      time.sleep(1)
      os.system('cls' if os.name == 'nt' else 'clear')
      ver_menu()
    else:
      print(Fore.RED + "Usuario o contraseña incorrectos\n")
      time.sleep(2)
      os.system('cls' if os.name == 'nt' else 'clear')
      ingreso()
  except Exception as e:
    print(Fore.RED + f"Error durante el ingreso: {e}")
  finally:
    init(autoreset=True)
      
  
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
        nombre = input("Ingrese el nombre del producto: ").strip().upper()
        precio = float(input("Ingrese el precio del producto: ")).strip()
        categoria = input("Ingrese la categoría del producto: ").strip().upper()
        descripcion = input("Ingrese la descripción del producto: ").strip()
        agregar_producto(nombre, precio, categoria, descripcion)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        ver_menu()
    elif seleccion == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Ver productos:\n")
        ver_productos()
        input("\nPresione Enter para volver al menú principal...")
        os.system('cls' if os.name == 'nt' else 'clear')
        ver_menu()
    elif seleccion == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Buscar producto:\n")
        termino_busqueda = input("Ingrese el nombre del producto a buscar: ")
        buscar_producto(termino_busqueda)
        input("\nPresione Enter para volver al menú principal...")
        os.system('cls' if os.name == 'nt' else 'clear')
        ver_menu()
    elif seleccion == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Modificar producto:\n")
        id_producto = int(input("Ingrese el ID del producto a modificar: ")).strip()
        nuevo_nombre = input("Ingrese el nuevo nombre del producto: ").strip().upper()
        nuevo_precio = float(input("Ingrese el nuevo precio del producto: ")).strip()
        nueva_categoria = input("Ingrese la nueva categoría del producto: ").strip().upper()
        nueva_descripcion = input("Ingrese la nueva descripción del producto: ").strip()
        modificar_producto(id_producto, nuevo_nombre, nuevo_precio, nueva_categoria, nueva_descripcion)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        ver_menu()
    elif seleccion == '5':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Eliminar producto:\n")
        id_producto = int(input("Ingrese el ID del producto a eliminar: ")).strip()
        eliminar_producto(id_producto)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        ver_menu()
    elif seleccion == '6':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Gestión de usuarios:\n")
        menu_usuarios = ["1.- Ver usuarios", "2.- Agregar usuario", "3.- Modificar usuario", "4.- Eliminar usuario"]
        for item in menu_usuarios:
            print(item)
            time.sleep(0.4)
        opcion_usuario = input("\nSeleccione una opción del menú de usuarios: ")
        
        os.system('cls' if os.name == 'nt' else 'clear')
        if opcion_usuario == '1':
            ver_usuarios()
            input("\nPresione Enter para volver al menú principal...")
        elif opcion_usuario == '2':
            print("Agregar nuevo usuario:\n")
            nombre = input("Ingrese el nombre completo: ").strip().upper()
            usuario = input("Ingrese el nombre de usuario: ").strip().upper()
            email = input("Ingrese el email: ").strip().lower()
            password = input("Ingrese la contraseña: ").strip()
            rol = input("Ingrese el rol (admin/user): ").strip().lower()
            crear_usuario(nombre, usuario, email, password, rol)
            time.sleep(2)
        elif opcion_usuario == '3':
            print("Modificar usuario:\n")
            id_usuario = int(input("Ingrese el ID del usuario a modificar: ")).strip()
            nuevo_nombre = input("Ingrese el nuevo nombre completo: ").strip().upper()
            nuevo_usuario = input("Ingrese el nuevo nombre de usuario: ").strip().upper()
            nuevo_email = input("Ingrese el nuevo email: ").strip().lower()
            nuevo_password = input("Ingrese la nueva contraseña: ").strip()
            nuevo_rol = input("Ingrese el nuevo rol (admin/user): ").strip().lower()
            modificar_usuario(id_usuario, nuevo_nombre, nuevo_usuario, nuevo_email, nuevo_password, nuevo_rol)
            time.sleep(2)
        elif opcion_usuario == '4':
            print("Eliminar usuario:\n")
            id_usuario = int(input("Ingrese el ID del usuario a eliminar: ")).strip()
            eliminar_usuario(id_usuario)
            time.sleep(2)
        else:
            print(Fore.RED + "Opción no válida. Volviendo al menú principal...")
            time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        ver_menu()
        
    elif seleccion == '0':
        print(Fore.GREEN + "Saliendo del sistema...")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.GREEN + "Gregory Rodriguez © 2025\nDNI 95777596\nGracias por usar la aplicación.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print(Fore.RED + "Opción no válida. Intente de nuevo.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        ver_menu()
        
      