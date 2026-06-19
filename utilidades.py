import re

def mostrar_bienvenida():
    """Muestra un mensaje de bienvenida."""
    print("¡Bienvenido al sistema de funciones!")

def calcular_promedio(num1, num2):
    """Recibe dos números y devuelve su promedio."""
    return (num1 + num2) / 2

def validar_correo(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(patron, correo))

def calcular_suma(num1, num2):
    """Recibe dos números y devuelve su suma."""
    return num1 + num2

def calcular_resta(num1, num2):
    """Recibe dos números y devuelve la resta (num1 - num2)."""
    return num1 - num2

def calcular_multiplicacion(num1, num2):
    """Recibe dos números y devuelve su multiplicación."""
    return num1 * num2