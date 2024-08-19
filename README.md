KEY LOGGER 
======

Descripción
------------
Este proyecto implementa un keylogger básico en Python que captura la entrada del teclado y la guarda en un archivo de registro en intervalos seleccionados por el usuario.

Librerías Utilizadas
--------------------
### pynput
- **Descripción**: La librería `pynput` permite controlar y monitorizar entradas del teclado y el ratón en Python.
- **Uso en el Proyecto**:
  - `pynput.keyboard.Listener` se utiliza para escuchar eventos de teclado, permitiendo capturar cada tecla presionada por el usuario.

### threading
- **Descripción**: El módulo `threading` proporciona herramientas para trabajar con múltiples hilos (threads) en Python.
- **Uso en el Proyecto**:
  - `threading.Timer` se utiliza para configurar un temporizador que ejecuta periódicamente la función de reporte del keylogger, permitiendo guardar el log en el archivo en intervalos regulares.

Archivo `keyloggerV3.py`
------------------------
Este archivo contiene la implementación de la clase `Keylogger`.

### Clase `Keylogger`

- **Constructor `__init__(self, intervalo, archivo_log)`**:
  - `intervalo`: Intervalo en segundos para reportar el log (e.g., 60 segundos).
  - `archivo_log`: Ruta del archivo donde se guardará el log de teclas (e.g., `"C:\\keylogger_files\\log_teclas.txt"`).

- **Métodos**:
  - `append_to_log(self, string)`: Agrega texto al log.
  - `process_key_press(self, key)`: Maneja las teclas presionadas y agrega su representación al log.
  - `report(self)`: Guarda el contenido del log en el archivo y reinicia el log. Se llama a intervalos regulares.
  - `start(self)`: Inicia el escuchador de teclado y comienza el proceso de reporte.

Archivo `zlogger.py`
--------------------
Este archivo es el script principal que utiliza la clase `Keylogger` para capturar y registrar la entrada del teclado.

### Uso de `Keylogger`

```python
import keyloggerV3  
# Crea una instancia del Keylogger con el intervalo y el archivo de log
my_keylogger = keyloggerV3.Keylogger(intervalo=5, archivo_log=r"C:\keylogger_files\log_teclas.txt")
# Iniciar el keylogger
my_keylogger.start()
