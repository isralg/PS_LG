# PS_LG

### Como ejecutar el código del Ejercicio 1
Para probar la ejecución del Ejercicio 1 describo a continuación el proceso que he utilizado, una vez implementado el código (usando como IDE PyCharm)

1. Subir código al servidor o máquina virtual. 
    * En mi caso, tengo una máquina virtual con VirtualBox y Vagrant, y el interprete de python configurado, así como el mapeo de las carpetas correspondientes entre mi proyecto en local y mi Vagrant en VirtualBox.
2. Una vez alojado el código, arrancar el proyecto. 
    * En mi caso "Run" desde PyCharm.
3. La salida del script será mostrada por pantalla. 
    * En mi caso, en la parte inferior del IDE, en la pestana "Run"
     
    
### Notas
Ahora mismo, el fichero "main.py" tiene una lista de números hardcodeada, de modo que simplemente ejecutando el proyecto se verá el resultado.
No obstante, el proyecto está preparado para poder ejecutarse de las siguientes formas:
1. Introduciendo una lista de números desde la consola de python y Enter. (OPTION 2 comentada en el código de main.py)
    * En mi caso, en la parte inferior del IDE, en la pestana "Run"
2. Introduciendo dos números, para indicar el inicio y el fin de un rango y Enter, desde la consola de python y Enter. (OPTION 3 comentada en el código de main.py)
    * En mi caso, en la parte inferior del IDE, en la pestana "Run"

El proyecto está probado con las tres opciones y funciona correctamente.


### Como ejecutar el código del Ejercicio 2
Para probar la ejecución del Ejercicio 2 describo a continuación algunas consideraciones

1. Descargar el código en la máquina donde vaya a ejecutarse 
2. Una vez alojado el código en la máquina basta con poner la ruta del fichero "index.html" de la carpeta "Ejercicio2". 
    * En mi caso _"C:/Users/israel/Pycharmprojects/PS_LG/Ejercicio2/index.html"_
3. Hacer click en el botón "Cargar datos" y las gráficas generadas serán mostradas por pantalla. 
     
    
### Notas
    * Si se ejecuta en el navegador "Mozila Firefox" la página se visualiza correctamente sin necesidad de ninguna.
    * Si se ejecuta en el navegador "Google Chrome" directamente, no se mostrarán las gráficas debido al error 
    _**"Cross origin requests are only supported for protocol schemes: http, data, chrome, chrome-extension, https."**_
    propio del navegador.
    Esto es debido a que Chrome no permite la carga de archivos desde local, para evitar esto basta con 
    instalar la extensión de Chrome "Web Server" y configurar como carpeta de arranque "index.html" de la carpeta
    "Ejercicio2" en dicha extensión.
    En mi caso la ruta para visualizar la página web con las gráficas es http://127.0.0.1:8887/
