readme_content = """# Laboratorio 6 - Fundamentos de Programación

**Integrante:** Pablo Diaz

## Tema: Introducción a la Programación Modular y Reutilización

Este repositorio contiene mi parte del **Laboratorio 6**. Me encargué de realizar la **Parte 3 (Integración)** y la **Parte 4 (Buenas Prácticas)** de la guía, mejorando el código base que hicimos en grupo.

---

## 🛠️ ¿Qué mejoras le hice al código?

### Parte 3: Integración y nuevas funciones
* **Menú Interactivo:** Le agregué un ciclo `while True` en el `main.py` para crear un menú de opciones. Así podemos probar todas las operaciones sin que el programa se cierre a cada rato.
* **Nuevas operaciones:** Agregué las funciones `calcular_suma` y `calcular_resta` en el archivo auxiliar para demostrar lo fácil que es agregar cosas a un proyecto modular.

### Parte 4: Buenas Prácticas
* **Comentarios profesionales (Docstrings):** Cambié los comentarios básicos por *Docstrings* (`\"\"\"`) en todas las funciones de `utilidades.py`. Ahora cada función explica claramente qué hace, qué parámetros necesita y qué devuelve.
* **Manejo de errores (try-except):** Agregué validaciones para que si el usuario escribe letras en lugar de números, el programa muestre un mensaje de error amigable (`ValueError`) en lugar de cerrarse de golpe.
* **Buenas prácticas de ejecución:** Metí el código principal dentro de una función `def main():` y usé `if __name__ == "__main__":` para seguir los estándares de Python.

---

##  Archivos del proyecto

* `main.py`: Es el archivo principal que ejecutamos. Tiene el menú y valida los errores.
* `utilidades.py`: Es el archivo "módulo" donde guardamos todas las operaciones matemáticas y de validación.

---

##  Tabla de Funciones

Estas son las funciones que tenemos listas en nuestro archivo `utilidades.py`:

| Función | Parámetros | Retorno | ¿Qué hace? |
| :--- | :--- | :--- | :--- |
| `mostrar_bienvenida()` | Ninguno | `None` | Muestra el saludo inicial. |
| `calcular_suma(num1, num2)` | 2 números (`float`) | `float` | Suma los dos números ingresados. |
| `calcular_resta(num1, num2)` | 2 números (`float`) | `float` | Resta los dos números ingresados. |
| `calcular_promedio(num1, num2)`| 2 números (`float`) | `float` | Calcula el promedio de los dos números. |
| `validar_correo(correo)` | 1 texto (`str`) | `bool` | Revisa si el texto ingresado tiene un formato válido de correo usando regex. |
"""

with open("README-v2.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("File generated successfully as README-v2.md")