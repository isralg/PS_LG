# PS_LG

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
