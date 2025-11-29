from src.Controllers.controladores import *
from src.Logic.logica import *
from src.Persistencia.persistencia import * 

# Para ver la documentacion de la funcion correspondiente cambia el nombre del parametro por el nombre de la funcion


os.system('cls' if os.name == 'nt' else 'clear')

funcion = ingreso_usuario  # Cambia 'aplicacion' por el nombre de la función que deseas documentar

def documentacion(funcion):
    print(funcion.__doc__)

documentacion(funcion)

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
