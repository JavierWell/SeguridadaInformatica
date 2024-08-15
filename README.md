# Keylogger Python

Este proyecto contiene un keylogger básico implementado en Python. Utiliza la biblioteca `pynput` para capturar eventos del teclado y registrar las teclas presionadas.

## Archivos del Proyecto

### 1. `keyloggerV2.py`

Contiene la definición de la clase `Keylogger`. Implementa la lógica para capturar teclas, registrar las teclas presionadas en una variable y reportarlas periódicamente.

### 2. `run_keylogger.py`

Ejecuta el keylogger instanciando la clase `Keylogger` desde `keyloggerV2.py` y comienza a capturar y reportar teclas presionadas.

## Requisitos

- Python 3.x
- Biblioteca `pynput`

Puedes instalar la biblioteca `pynput` usando pip:

```bash
pip install pynput
