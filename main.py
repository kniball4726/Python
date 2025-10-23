import os
import time
import sys

menu = ['Agregar Productos','Ver Productos','Buscar Productos','Eliminar Productos','Salir']
productos = []

while True:
  os.system('cls' if os.name == 'nt' else 'clear')
  ingreso = input("Bienvenid@ a SISCAPROD 'Sistema de carga de productos'\n\nIndique usuario\n\n")
  if len(ingreso)>0:
    break
  else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Debe ingresar un usuario valido\n")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

os.system('cls' if os.name == 'nt' else 'clear')
print(f'Bienvenid@ {ingreso}\n\n')
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

def preguntar():
  print(f"Usuario: {ingreso}\n\nSeleccione una opción del menú\n")
  for idx, i in enumerate(menu, start=1):
    print(f"{idx}.- {i}\n")
    time.sleep(0.3)

  seleccion = input()
  
  while seleccion > '0' or seleccion < '6':
    if seleccion == '1':
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Agregar Producto\n\n")
      producto = input("Ingrese el nombre del producto\n\n")
      productos.append(producto)
      print(f"El producto {producto} ha sido agregado\n")
      time.sleep(1)
      os.system('cls' if os.name == 'nt' else 'clear')
      preguntar()
      break
    elif seleccion == '2':
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Ver Productos\n\n")
      if len(productos) == 0:
        print("No hay productos cargados\n")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        preguntar()
        break
      else:
        print("Productos cargados\n")
        for idx, i in enumerate(productos, start=1):
          print(f"{idx}. {i}\n")
        time.sleep(4)
        preguntar()
        break
    elif seleccion == '3':
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Buscar Producto\n\n")
      producto = input("Ingrese el nombre del producto a buscar\n\n")
      if producto in productos:
        print(f"El producto {producto} se encuentra cargado\n")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        preguntar()
        break
      else:
        print(f"El producto {producto} no se encuentra cargado\n")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        preguntar()
        break
    elif seleccion == '4':
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Eliminar Producto\n")
      producto = input("Ingrese el nombre del producto a eliminar\n")
      if producto in productos:
        productos.remove(producto)
        print(f"El producto {producto} ha sido eliminado\n")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        preguntar()
        break
      else:
        print(f"El producto {producto} no se encuentra cargado\n")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        preguntar()
        break
    elif seleccion == '5':
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Gracias por usar el sistema\nAutor: Gregory Rodriguez\nDNI 95777596")
      time.sleep(3)
      sys.exit()
    else:
      print("Opción no válida\n")
      time.sleep(1)
      os.system('cls' if os.name == 'nt' else 'clear')
      preguntar()
      break


preguntar()