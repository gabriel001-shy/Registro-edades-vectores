# ============================================
# PROYECTO: REGISTRO DE EDADES CON VECTORES
# ASIGNATURA: INTRODUCCION A LA PROGRAMACION
# TEMA: ARREGLOS Y VECTORES
# ============================================

# Vector inicial con las edades registradas
edades = [18, 25, 32, 21, 40]


# Funcion para mostrar todas las edades
def mostrar_edades():
    if len(edades) == 0:
        print(f"\nNo hay edades registradas.")
        return

    print("\n--- REGISTRO DE EDADES ---")

    for indice, edad in enumerate(edades):
        print(f"Persona {indice + 1}: {edad} años")

    print(f"Total de personas: {len(edades)}")


# Funcion para agregar una edad
def agregar_edad():
    try:
        edad = int(input("\nIntroduce la nueva edad: "))

        if edad > 0:
            edades.append(edad)
            print("La edad se registro correctamente.")
        else:
            print("Error: la edad debe ser un numero entero positivo.")

    except ValueError:
        print("Error: debes introducir un numero entero.")


# Funcion para consultar una edad por su posicion
def consultar_edad():
    if len(edades) == 0:
        print("\nNo hay edades registradas.")
        return

    try:
        posicion = int(input("Introduce el numero de la persona: "))

        if 1 <= posicion <= len(edades):
            indice = posicion - 1
            print(
                f"La edad de la persona {posicion} "
                f"es {edades[indice]} años."
            )
        else:
            print("Error: la posicion seleccionada no existe.")

    except ValueError:
        print("Error: debes introducir un numero entero.")


# Funcion para modificar una edad
def modificar_edad():
    if len(edades) == 0:
        print(f"\nNo hay edades para modificar.")
        return

    try:
        posicion = int(input(f"Introduce el numero de la persona: "))

        if 1 <= posicion <= len(edades):
            nueva_edad = int(input(f"Introduce la nueva edad: "))

            if nueva_edad > 0:
                indice = posicion - 1
                edades[indice] = nueva_edad

                print(f"La edad se modifico correctamente.")
            else:
                print(f"Error: la edad debe ser positiva.")
        else:
            print(f"Error: la posicion seleccionada no existe.")

    except ValueError:
        print(f"Error: debes introducir numeros enteros.")


# Funcion para calcular el promedio
def calcular_promedio():
    if len(edades) == 0:
        print(f"\nNo hay edades para calcular el promedio.")
        return

    suma = 0

    for edad in edades:
        suma += edad

    promedio = suma / len(edades)

    print(f"\nEl promedio de las edades es: {promedio:.2f} años.")


# Funcion para mostrar la edad mayor y la menor
def mostrar_extremos():
    if len(edades) == 0:
        print(f"\nNo hay edades registradas.")
        return

    edad_mayor = max(edades)
    edad_menor = min(edades)

    print(f"\nLa edad mayor registrada es: {edad_mayor} años.")
    print(f"La edad menor registrada es: {edad_menor} años.")


# Funcion para contar las personas registradas
def contar_personas():
    cantidad = len(edades)

    print(f"\nHay {cantidad} persona(s) registrada(s).")


# Funcion principal que muestra el menu
def menu():
    while True:
        print("\n===================================")
        print("       REGISTRO DE EDADES")
        print("===================================")
        print("1. Mostrar todas las edades")
        print("2. Agregar una nueva edad")
        print("3. Consultar una edad")
        print("4. Modificar una edad")
        print("5. Calcular el promedio")
        print("6. Mostrar edad mayor y menor")
        print("7. Contar personas registradas")
        print("8. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            mostrar_edades()

        elif opcion == "2":
            agregar_edad()

        elif opcion == "3":
            consultar_edad()

        elif opcion == "4":
            modificar_edad()

        elif opcion == "5":
            calcular_promedio()

        elif opcion == "6":
            mostrar_extremos()

        elif opcion == "7":
            contar_personas()

        elif opcion == "8":
            print("\nGracias por utilizar el Registro de Edades.")
            break

        else:
            print("\nOpcion no valida. Intenta nuevamente.")


# Inicio del programa
if __name__ == "__main__":
    menu()
