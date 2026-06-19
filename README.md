# Laboratorio 6 - Fundamentos de Programación

**Integrante:** Edith Huingo

## Tema: Introducción a la Programación Modular y Reutilización

Yo me encargué de **ejecutar el programa principal y verificar el correcto funcionamiento de cada función**, asegurándome de que todo lo implementado funcione sin errores.

### ¿Qué hice?

* **Probé todas las opciones del menú** una por una: Suma, Promedio, Resta, Validar Correo y Salida.
* **Probé casos válidos:** Números correctos y correos electrónicos reales.
* **Probé casos inválidos:** Letras en lugar de números y cadenas sin formato de correo.
* **Verifiqué el manejo de errores:** Comprobé que el `try-except` atrapa correctamente entradas incorrectas sin que el programa se cierre.
* **Documenté los resultados** en una tabla comparativa con entradas, salidas esperadas y salidas obtenidas.

### Resultados de las pruebas

| Función | Entrada | Salida esperada | Salida obtenida | Estado |
| :--- | :--- | :--- | :--- | :--- |
| `calcular_suma(5, 3)` | 5, 3 | 8.0 | 8.0 | Correcto |
| `calcular_promedio(8, 4)` | 8, 4 | 6.0 | 6.0 | Correcto |
| `calcular_resta(10, 3)` | 10, 3 | 7.0 | 7.0 | Correcto |
| `validar_correo("user@example.com")` | user@example.com | VÁLIDO | VÁLIDO | Correcto |
| `validar_correo("hola")` | hola | INVÁLIDO | INVÁLIDO | Correcto |
| Manejo de error (letras en número) | abc | Mensaje de error | "Debe ingresar únicamente números." | Correcto |

Todas las funciones se ejecutaron correctamente, lo que confirma que la implementación modular es sólida y que cada función hace exactamente lo que debe hacer, incluso cuando el usuario ingresa datos inesperados. 
