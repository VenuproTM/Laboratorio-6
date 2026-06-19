

# Laboratorio 6 - Fundamentos de Programación
**Universidad Privada del Norte (UPN)** **Curso:** Fundamentos de Programación  
**Tema:** Introducción a la Programación Modular, Buenas Prácticas y Reutilización de Código

---

## Integrantes y Roles

Para el desarrollo de este laboratorio, nuestro equipo se organizó dividiendo las responsabilidades según los principios de la programación modular y las buenas prácticas aprendidas en las sesiones de clase:

| Integrante | Rol / Responsabilidad Principal | Aporte Específico |
| :--- | :--- | :--- |
| **Edith Huingo** | Responsable de Pruebas y QA | Ejecución del programa principal, diseño de casos de prueba (válidos e inválidos), verificación del manejo de errores (`try-except`) y documentación de resultados. |
| **Elizabeth** | Desarrolladora del Módulo Base | Creación y estructuración del archivo `utilidades.py`, definición de las funciones esenciales de cálculo (`suma`, `resta`, `promedio`) y lógica de validación con expresiones regulares (`re`). |
| **Miembro 6 (Tú)** | Desarrollador de Extensiones | Implementación de la **Parte Número 6**: integración de la nueva funcionalidad aritmética (`calcular_multiplicacion`), actualización del menú interactivo en `main.py` y propagación automática de cambios. |

---

## Descripción del Proyecto

Este proyecto consiste en una aplicación de consola interactiva desarrollada en **Python 3** que demuestra los beneficios de la **Programación Modular** y el cumplimiento de las **Buenas Prácticas de Codificación** (legibilidad, comentado selectivo y convenciones de estilo como *snake_case*).

El sistema separa completamente la interfaz de usuario y control de flujo (`main.py`) de la lógica de negocio y operaciones matemáticas (`utilidades.py`), permitiendo que cualquier mejora en las funciones se propague de manera automática y transparente a todo el sistema.

---

## Estructura del Repositorio

El código fuente está organizado de forma limpia y eficiente en los siguientes archivos:

* **`utilidades.py`**: Módulo contenedor que agrupa todas las funciones lógicas, reutilizables y especializadas (cálculos matemáticos y validación de texto).
* **`main.py`**: Script principal que actúa como punto de entrada del programa. Gestiona el bucle interactivo (`while True`), captura las entradas del usuario, invoca los módulos y maneja las excepciones para evitar caídas del sistema.
* **`README.md`**: Documentación técnica completa del proyecto (este archivo).

---