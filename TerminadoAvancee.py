import random
import string

# Caracteres a usar para generar una contraseña
MAYUSCULAS = string.ascii_uppercase
MINUSCULAS = string.ascii_lowercase
NUMEROS = string.digits
SIMBOLOS = "@#$%&*+="

# Proceso para que se genere una contraseña automática de 12 caracteres
def generar_contraseña_fija():
    longitud = 12

    # Caracteres obligatorios a usar
    obligatorios = [
        random.choice(MAYUSCULAS),
        random.choice(MINUSCULAS),
        random.choice(NUMEROS),
        random.choice(SIMBOLOS)
    ]

    # Para asegurar que la longitud se cumpla y que todos los elementos estén dentro de la contraseña
    restantes = longitud - len(obligatorios)
    todos = MAYUSCULAS + MINUSCULAS + NUMEROS + SIMBOLOS

    # Para que los caracteres obligatorios se mezclen entre sí
    contraseña_generada = obligatorios[:]
    contraseña_generada += [random.choice(todos) for _ in range(restantes)]
    random.shuffle(contraseña_generada)

    # Para que la lista se convierta en un texto
    return "".join(contraseña_generada)


# Función para validar la contraseña ingresada por el usuario
def validar_contraseña(contraseña):
    # Para verificar el uso de todos los caracteres, sino, mostrar lo que falta
    faltantes = []

    if len(contraseña) < 12:
        faltantes.append("longitud mínima de 12 caracteres")

    if not any(c in MAYUSCULAS for c in contraseña):
        faltantes.append("incluir al menos 1 mayúscula")

    if not any(c in MINUSCULAS for c in contraseña):
        faltantes.append("incluir al menos 1 minúscula")

    if not any(c in NUMEROS for c in contraseña):
        faltantes.append("incluir al menos 1 número")

    if not any(c in SIMBOLOS for c in contraseña):
        faltantes.append(f"incluir al menos 1 símbolo ({SIMBOLOS})")

    # Para ver la lista de los caracteres faltantes
    return faltantes


# Función para preguntar si el usuario desea guardar la contraseña
def preguntar_guardar():
    while True:
        resp = input("¿Desea guardar la contraseña? (Si o No): ").strip().lower()

        if resp in ("si", "sí"):
            print("Contraseña guardada exitosamente")
            return

        if resp == "no":
            return

        # Para evitar otra respuesta que no sea SÍ o NO
        print("Respuesta no válida. Escriba Si o No.")


# Proceso que el usuario escriba su propia contraseña
def crear_contraseña_usuario():
    # Lo que el usuario debe tomar en cuenta para escribir la contraseña
    print("\nTu contraseña debe tener:")
    print("- Longitud de 12 caracteres (mínimo)")
    print("- Mayúsculas")
    print("- Minúsculas")
    print("- Números")
    print(f"- Símbolos ({SIMBOLOS})")

    # Bucle que se repetirá hasta que la contraseña sea válida
    while True:
        # El usuario escribirá su contraseña aquí
        contraseña = input("\nEscribe tu contraseña: ")

        # Para verificar la contraseña
        faltantes = validar_contraseña(contraseña)

        # Si no le falta nada, la contraseña será válida
        if not faltantes:
            print("Contraseña ingresada válida")
            preguntar_guardar()
            return 

        # Si falta algo, se mostrará lo que falta
        print("Su contraseña ingresada no es válida")
        for f in faltantes:
            print("-", f)


# Lo que verá el usuario
def menu():
    while True:
        print("\nGenerador de contraseñas")
        print("1. Generar una contraseña automática aleatoria")
        print("2. Crear mi propia contraseña")

        opcion = input("Elige una opción (1 o 2): ").strip()

        if opcion == "1":
            contraseña = generar_contraseña_fija()
            print("\nSu contraseña generada es:", contraseña)

        elif opcion == "2":
            crear_contraseña_usuario()

        # Para evitar otra respuesta a la que el sistema le da a elegir al usuario
        else:
            print("Opción no válida. Intente nuevamente.")


menu()
