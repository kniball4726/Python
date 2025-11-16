import os, time
from colorama import init, Fore, Back 
from Logic.controladores import *
from Logic.persistencia import *


def ingreso():
  try:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + "Bienvenido al sistema de gestión de productos\n")
    usuario = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    
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
      
  