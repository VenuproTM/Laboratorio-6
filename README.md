# Laboratorio 6 - Fundamentos de Programación

Integrante: [Pablo Diaz]

## Tema: Introducción a la Programación Modular y Reutilización

Este repositorio contiene la entrega correspondiente al **Laboratorio 6**, desarrollado bajo los principios del paradigma de programación modular. Esta sección documenta específicamente las implementaciones, mejoras y optimizaciones realizadas para cumplir con la **Parte 3 (Integración)** y **Parte 4 (Buenas Prácticas)** de la guía de laboratorio de la Universidad Privada del Norte (UPN).

---

## Contribuciones y Mejoras Realizadas (Parte 3 y 4)

Se tomó como base la estructura inicial compartida y se refactorizó el sistema para elevar su calidad técnica, robustez, legibilidad y usabilidad. Las actividades principales realizadas se detallan a continuación:

### 1. Robustez e Integración de Funciones (Parte 3)

* **Menú Interactivo de Control:** Se implementó un ciclo de control continuo (`while True`) en el archivo principal `main.py` que despliega un menú interactivo en consola. Esto permite realizar múltiples pruebas secuenciales sin necesidad de reiniciar la ejecución del script de forma manual.
* **Escalabilidad del Sistema:** Se expandió el módulo auxiliar agregando nuevas funciones reutilizables (`calcular_suma` y `calcular_resta`), demostrando la capacidad de la programación modular para incorporar nuevas soluciones de software de forma limpia y transparente sin alterar la estabilidad del flujo principal.

### 2. Aplicación Estricta de Buenas Prácticas (Parte 4)

* **Documentación Técnica Estandarizada (*Docstrings*):** Se reemplazaron los comentarios simples de una sola línea por bloques de documentación completos (`\\"\\"\\" Docstrings \\"\\"\\"`) en todas las funciones del archivo `utilidades.py`. Cada bloque detalla formalmente el propósito de la función, los parámetros de entrada con sus respectivos tipos de datos y el valor de retorno esperado.
* **Manejo de Excepciones Avanzado:** Se blindó el programa principal mediante el uso estratégico de estructuras `try-except`. Se captura de manera específica la excepción `ValueError` para gestionar de forma segura los ingresos de datos inválidos (como cadenas de texto en campos de cálculo numérico), evitando interrupciones abruptas o caídas del sistema.
* **Estándar de Ejecución:** Se reestructuró el archivo de arranque utilizando el bloque condicional estándar `if __name__ == "__main__":`, garantizando que el código principal solo se ejecute cuando el archivo sea invocado directamente y no de manera accidental si llega a ser importado por otros módulos.

---