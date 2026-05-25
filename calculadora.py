def suma(num1, num2):
    return num1 + num2
    
def resta(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        print("Error: División por cero no permitida.")
        return None    
    return num1 / num2  

def promedio():
    notas = []
    while True:
        nota = float(input("Ingresa una nota // Ingresa (-1) para finalizar: "))

        if nota == -1:
            break
        notas.append(nota)

    if not notas:
        print("No se han ingresado notas.")
            
    else:   
        prom = sum(notas) / len(notas)
        print(f"Promedio: {prom:.2f}")

def menu():
    print("--------------------------------------")
    print("         Calculadora AG ")
    print("--------------------------------------")
    print("1. SUMA")
    print("2. RESTA")
    print("3. MULTIPLICACIÓN")
    print("4. DIVISIÓN")
    print("5. PROMEDIO")
    print("6. SALIR")

def main():
    while True:
        menu()

        opcion = int(input("Selecciona la operación que deseas realizar: "))

        if 1<= opcion <= 4:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if opcion == 1:
                print("\n ----SUMA----")
                resultado = suma(num1, num2)
                print(f"Resultado: {resultado}")
    
            elif opcion == 2:
                print("\n ----RESTA----")
                resultado = resta(num1, num2)
                print(f"Resultado: {resultado}")

            elif opcion == 3:
                print("\n ----MULTIPLICACIÓN----")
                resultado = multiplicar(num1, num2)
                print(f"Resultado: {resultado}")

            elif opcion == 4:
                print("\n ----DIVISIÓN----")
                resultado = dividir(num1, num2)

                if resultado is not None:
                    print(f"Resultado: {resultado:.2f}") 

        elif opcion == 5:
            print("----------\n PROMEDIO\n----------")
            promedio()

        elif opcion == 6:
            print("Cerrando la calculadora...")
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")

if __name__ == "__main__":
    main()