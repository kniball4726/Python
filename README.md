**Curso de Python inicial**

**Proyecto integrador**

Consigna:




**Notas del desarrollador**

Autor: Gregory Rodriguez
DNI: 95777596

Proyecto: Sistema de gestión de productos

**Pasos iniciales**

    Se recomienda iniciar un entorno virtual, se puede hacer de la siguiente manera:

        en la terminal desplegada se corre la siguiente linea de codigo `pip install virtualenv`

        al instalar usamos `virtualenv .env`

        se crea el ambiente virtual, para activarlo se utiliza `cd .env\Scrips\activate`

        en la linea de comando inicialmente deberia salir (.env)

        para instalar las dependencias utilizadasa en el proyecto se usa el siguiente comando:
        `pip install -r requirements.txt`
        en la raiz del proyecto se debera crear una carpeta llamada .env esta ultima contendra las variables de entorno utilizadas en el proyecto
    
    la carpeta .gitignore contiene los archivos que no se suben al repositorio ya que no son necesarios o contienen  informacion sensible.

    generalmente se ignoran archivos como .venv que es el entorno virtual .env repositorio de variables de entorno y src/DB bases de datos, tablas y datos iniciales, los cuales se crean de manera automatica al iniciar la aaplicacion.
    
**Iniciar aplicación**

        El usuario debe ubicar el archivo **app.py** el cual representa la funcion principal, index o main dentro de la aplicación, dentro de este archivo solo se encontraran
    una función la cual contiene todas las funciones, la persistencia y la logica de la aplicación.


**Estructura**

   Inicialmente la aplicación se compone por una carpetta llamada "Logic", donde esta contenido los siguientes archivos.
    A.- controladores.py: este archivo contiene funciones que son llamadas para realizar tareas en especifico generalmente el CRUD
    B.- logica.py: contiene toda la lógica de negocio y realiza el llamado de las funciones contenidas en controladores.py
    C.- persistencia.py: contiene todo lo referente a bases de datos, conexiones, creación de base de datos, de tablas e ingreso de datos iniciales,
    a traves de este archivo al iniciar la aplicación por primera vez se crea una carpeta llama DB, en la cual estara contenido el archivo productosapp.db
    el cual es la base de datos relacional SQL creada por defecto con tres tablas que se utilizaran para el funcionamiento correcto de la aplicación.

**Base de datos**

    La base de datos se crea por defecto al inicar la plicación por primera vez, su nombre por defecto es productosapp.db, en la misma se crean tres tablas iniciales 
    las cuales son:

    - tabla 'usuarios': esta tabla esta precargada con un usuario por defecto para el ingreso inicial, este usuario es de tipo admin, teniendo todos los privilegios dentro de 
    la aplicación, esta compuesta por los campos:
        
        . id
        . nombre
        . usuario
        . email
        . password
        . rol
        . estado


    Para el ingreso inicial la aplicación le solicitara usuario y contraseña para lo cual sera:
    usuario: ADMIN
    contraseña: admin123

    - tabla 'menu': contiene los datos del menú principal ya precargado, esta compuesta por los campos:

        . id
        . nombre
        . descripcion
        . estado

    - tabla 'productos': tabla vacia donde se guardaran todos los datos de los productos compuesta por los campos
        
        . id
        . nombre
        . precio
        . categoria
        . descripcion
        . fecha_agregado
        . estado

**Menú**

    Luego de ingresar con los datos iniciales precargados y reconocidos como datos validos, la aplicación muestra un menú prinicipal, el cual esta compuesto por:

    1.- Ingresar producto: al seleccionar esta opción se despliega un formulario para agregar productos donde se debe introducir el nombre del producto, el precio del producto,
