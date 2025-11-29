from src.Controllers.controladores import *
from src.Logic.logica import *
from src.Persistencia.persistencia import * 
from colorama import Fore, Style, Back, init

# Para ver la documentacion de la funcion correspondiente cambia el nombre del parametro por el nombre de la funcion
init()

os.system('cls' if os.name == 'nt' else 'clear')


def documentacion():
    
    funciones = [aplicacion, conexion, datos, ingreso, agregar_producto, buscar_producto, crear_usuario, eliminar_producto, eliminar_usuario, ingreso_usuario, modificar_producto, modificar_usuario, ver_productos, ver_usuarios, ver_menu, submenu, submenu_usuarios]
    for funcion in funciones:
        print(Style.BRIGHT + "\nFuncion: " + Style.RESET_ALL + Fore.YELLOW + funcion.__name__ + Style.RESET_ALL+ Fore.RESET)
        print(funcion.__doc__)
        print(Style.BRIGHT + Back.BLUE + "------------------------" + Style.RESET_ALL)
        
        
        
documentacion()


"""
Imprime la documentacion de las funciones creadas por el desarrollador para el la aplicación

para ver la documentación de una función específica, copia el nombre de la funcion de la lista de funciones y pegala en la variable funcion = 
    
Lista de funciones:

['aplicacion',
'conexion',
'datos',
'ingreso',
'agregar_producto', 
'buscar_producto', 
'crear_usuario', 
'eliminar_producto', 
'eliminar_usuario', 
'ingreso_usuario', 
'modificar_producto', 
'modificar_usuario', 
'ver_productos', 
'ver_usuarios',
'ver_menu',
'sumenu',
'submenu_usuarios']

"""
