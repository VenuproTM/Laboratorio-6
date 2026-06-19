from utilidades import mostrar_bienvenida, calcular_promedio, validar_correo, calcular_suma, calcular_resta

def main():
    mostrar_bienvenida()
    
    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Calcular Suma")
        print("2. Calcular Promedio")
        print("3. Calcular Resta")
        print("4. Validar Correo")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "5":
            print("¡Hasta luego!")
            break
        
        if opcion in ["1", "2", "3"]:
            try:
                n1 = float(input("Ingrese el primer número: "))
                n2 = float(input("Ingrese el segundo número: "))
                if opcion == "1":
                    print(f"El resultado de la suma es: {calcular_suma(n1, n2)}")
                elif opcion == "2":
                    print(f"El resultado del promedio es: {calcular_promedio(n1, n2)}")
                elif opcion == "3":
                    print(f"El resultado de la resta es: {calcular_resta(n1, n2)}")
            except ValueError:
                print("Error: Debe ingresar únicamente números.")
        
        elif opcion == "4":
            correo = input("Ingrese un correo electrónico: ")
            if validar_correo(correo):
                print("Correo electrónico VÁLIDO.")
            else:
                print("Correo electrónico INVÁLIDO.")
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()