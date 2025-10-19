import os
import time
import sys

menu = ['1.- Agregar Productos','2.- Ver Productos','3.- Buscar Productos','4.- Eliminar Productos','5.- Salir']
productos = []

while True:
  ingreso = input("Bienvenid@ a SISCAPROD 'Sistema de carga de productos'\n\nIndique usuario\n\n")
  if len(ingreso)>0:
    break
  else:
    os.system("clear")
    print("Debe ingresar un usuario valido\n")
    time.sleep(2)
    os.system("clear")

os.system("clear")
print(f'Bienvenid@ {ingreso}\n\n')
time.sleep(1)
os.system("clear")

def preguntar():
  print(f"Usuario: {ingreso}\n\nSeleccione una opción del menú\n")
  for i in menu:
    print(f"{i}\n")
    time.sleep(0.3)

  seleccion = int(input())

  while seleccion > 0 or seleccion < 6:
    if seleccion == 1:
      os.system("clear")
      print("Agregar Producto\n\n")
      producto = input("Ingrese el nombre del producto\n\n")
      productos.append(producto)
      print(f"El producto {producto} ha sido agregado\n")
      time.sleep(1)
      os.system("clear")
      preguntar()
      break
    elif seleccion == 2:
      os.system("clear")
      print("Ver Productos\n\n")
      if len(productos) == 0:
        print("No hay productos cargados\n")
        time.sleep(1)
        os.system("clear")
        preguntar()
        break
      else:
        print("Productos cargados\n")
        for i in productos:
          print(f"{i}\n")
        time.sleep(4)
        preguntar()
        break
    elif seleccion == 3:
      os.system("clear")
      print("Buscar Producto\n\n")
      producto = input("Ingrese el nombre del producto a buscar\n\n")
      if producto in productos:
        print(f"El producto {producto} se encuentra cargado\n")
        time.sleep(1)
        os.system("clear")
        preguntar()
        break
      else:
        print(f"El producto {producto} no se encuentra cargado\n")
        time.sleep(1)
        os.system("clear")
        preguntar()
        break
    elif seleccion == 4:
      os.system("clear")
      print("Eliminar Producto\n")
      producto = input("Ingrese el nombre del producto a eliminar\n")
      if producto in productos:
        productos.remove(producto)
        print(f"El producto {producto} ha sido eliminado\n")
        time.sleep(1)
        os.system("clear")
        preguntar()
        break
      else:
        print(f"El producto {producto} no se encuentra cargado\n")
        time.sleep(1)
        os.system("clear")
        preguntar()
        break
    elif seleccion == 5:
      os.system("clear")
      print("Gracias por usar el sistema\nAutor: Gregory Rodriguez\nDNI 95777596")
      time.sleep(3)
      sys.exit()
    else:
      print("Opción no válida\n")
      time.sleep(1)
      os.system("clear")
      preguntar()
      break


preguntar()