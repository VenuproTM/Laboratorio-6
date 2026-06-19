import re

# muestra un mensaje de bienvenida al usuario
def mostrar_bienvenida():
    """Muestra un mensaje de bienvenida."""
    print("¡Bienvenido al sistema de funciones!")

# recibe dos números y devuelve su promedio
def calcular_promedio(num1, num2):
    """Recibe dos números y devuelve su promedio."""
    return (num1 + num2) / 2

# valida si una cadena tiene formato de correo electrónico
def validar_correo(correo):
    """Valida si una cadena tiene formato de correo electrónico."""
    # patrón básico para validar correos electrónicos
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    # retorna True si coincide con el patrón y False en caso contrario
    return bool(re.match(patron, correo))

# recibe dos números y devuelve su suma
def calcular_suma(num1, num2):
    """Recibe dos números y devuelve su suma."""
    return num1 + num2

# recibe dos números y devuelve la resta
def calcular_resta(num1, num2):
    """Recibe dos números y devuelve la resta (num1 - num2)."""
    return num1 - num2

# recibe dos números y devuelve su multiplicación
def calcular_multiplicacion(num1, num2):
    """Recibe dos números y devuelve su multiplicación."""
    return num1 * num2