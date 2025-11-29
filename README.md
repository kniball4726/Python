
# Sistema de gestión de productos

Entrega final de proyecto integrador del curso basico de python desde la plataforma de talento tech.



## Comenzando 🚀

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

Prerrequisitos 📋

1.- Instalar python desde la pagina oficial:

- [Descarga de python](https://www.python.org/downloads/)

2.- Verificar instalacion de python

```bash
  python --version
```

3.- Verificar la instalación del gestor de paquetes PIP

```bash
  pip --version
```

4.- Instalación de editor de codigo Visual Studio Code 

- [Descarga de VSC](https://code.visualstudio.com/)


## Instalación local

Abrir visual estudio code y abrir una terminal con Ctrl+Shift+ñ

hacer un clon del repositorio

```bash
  git clone https://github.com/kniball4726/Python.git
```

Desde el terminal entrar en la carpeta Python

```bash
  cd python
```


Estando dentro del proyecto desde terminal se debe crear un entorno virtual

```bash
  python -m venv .venv
```

Para activar el entorno virtual se debe entrar en la carpeta .venv/Scrips y correr Activate de la siguiente manera 

```bash
  cd .\.venv\Scripts\
```
```bash
  .\activate
```
Volvemos a la carpeta raiz de nuestro proyecto 

```bash
  cd ../..
```
Se deben instalar las dependencias utilizadas en el proyecto para que funciona de manera optima

```bash
  pip install -r requirements.txt
```

## Variables de entorno

Para poder correr este proyecto deberas agregar las siguientes variables de entorno dentro de la carpeta .env 

`DATABASE_NAME`

Se debe crear nuestra carpeta de variables de entorno, donde se guardaran la informacion de la base de datos

en la raiz creamos un archivo llamado .env y dentro de este se debe pegar lo que esta dentro del archivo .env.dev cambiando el nombre de la base de datos, en este caso la consigna del proyecto final pide una base de datos llamada inventario.db 

quedaria de la siguiente manera:

`DATABASE_NAME = "src/db/inventario.db"`



En la carpeta raiz Python se encuentra el archivo app.py es el archivo inicial de ingreso a nuestro sistema, se debe correr desde la consola o descargando una extencion desde el Visual estudio code  


## Despliegue 📦

Correr el sistema desde terminal, estando en la carpeta raiz python

```bash
  python app.py
```

Al correr este comando automaticamente dentro de la carpeta `src` se va a crear la carpeta `db` y dentro de ella un archivo con nombre de la base de datos que se le dio en las variables de entorno, en nuestro caso `inventario.db`, esta base de datos estara comprendida por cuatro tablas que se crean automaticamente:

`usuarios`
`menu`
`submenu`
`productos`

La tabla `usuarios` se carga con un usuario inicial llamado `ADMIN` y password `admin123`
La tabla `menu` y `submenu` estan precargadas con los menus del sistema

para hacer un despliegue con ejecutable desde windows se debe usar:

```bash
    pyinstaller --onefile app.py
```

al correr este comando se crearan dos carpetas denominadas `build` y `dist`

dentro de la carpeta `dist` encontraremos un archivo llamado `app.exe`

este ejecutable de windows puede utilizarse directamente desde el escritorio de su pc otorgandole un acceso directo, se puede modificar el nombre y el icono
## Autor

Gregory Rodriguez - Trabajo inicial, Desarrollo y documentación
- [@kniball4726](https://github.com/kniball4726)


## License

[MIT](https://choosealicense.com/licenses/mit/)

## Documentación

En la carpeta raiz se encuentra un archivo llamado `documentacion.py` al ejecutar este archivo por terminal se observa la documentación completa de todas las funciones utilizadas en la aplicación