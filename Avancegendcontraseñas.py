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

    # Para asegurar que la longitud se cumpla
    restantes = longitud - len(obligatorios)

    # Para asegurar que todos los elementos esten dentro de la contraseña
    todos = MAYUSCULAS + MINUSCULAS + NUMEROS + SIMBOLOS

    # Todo lo que va a tener la contraseña
    contraseña_generada = obligatorios[:]  
    contraseña_generada += [
        random.choice(todos) for _ in range(restantes)
    ]

    # Para que sea aleatorio
    random.shuffle(contraseña_generada)

    # Para que la lista sea un texto
    contrasena = "".join(contraseña_generada)
    return contraseña

# Lo que verá el usuario
def menu():
    while True:
        print("\nGenerador de contraseñas")
        print("1. Generar una contraseña automática aleatoria")
        print("2. Escribir mi propia contraseña")

        opcion = input("Elige una opción (1 o 2): ")

        if opcion == "1":
            contrasena = generar_contraseña_fija()
            print("\nSu contraseña generada es:", contraseña)

menu()