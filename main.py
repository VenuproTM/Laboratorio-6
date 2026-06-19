from utilidades import mostrar_bienvenida, calcular_promedio, validar_correo

# Función sin parámetros
mostrar_bienvenida()

# Función con parámetros
try:
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    promedio = calcular_promedio(numero1, numero2)
    print(f"El promedio es: {promedio}")

except ValueError:
    print("Error: Debe ingresar únicamente números.")

# Función para validar correo
correo = input("Ingrese un correo electrónico: ")

if validar_correo(correo):
    print("Correo electrónico válido.")
else:
    print("Correo electrónico inválido.")