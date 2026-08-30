# calculadora_imc.py

'''
Este programa solicita los datos básicos de una persona
(nombre, apellidos, edad, peso y estatura) y calcula
su Índice de Masa Corporal (IMC).
'''


# Solicita un texto y verifica que no esté vacío
def solicitar_texto(mensaje):
    while True:
        dato = input(mensaje).strip()

        if dato:
            return dato.capitalize()

        print("Error: este campo no puede quedar vacío.")


# Solicita un número entero y verifica que sea válido
def solicitar_entero(mensaje):
    while True:
        dato = input(mensaje).strip()

        if not dato:
            print("Error: este campo no puede quedar vacío.")
            continue

        try:
            return int(dato)
        except ValueError:
            print("Error: ingrese una edad válida usando números.")


# Solicita un número decimal y verifica que sea válido
def solicitar_decimal(mensaje):
    while True:
        dato = input(mensaje).strip()

        if not dato:
            print("Error: este campo no puede quedar vacío.")
            continue

        try:
            return float(dato)
        except ValueError:
            print("Error: ingrese un valor numérico válido.")


# Solicita los datos de la persona
nombre = solicitar_texto("Ingrese su nombre: ")
apellido_paterno = solicitar_texto("Ingrese su apellido paterno: ")
apellido_materno = solicitar_texto("Ingrese su apellido materno: ")
edad = solicitar_entero("Ingrese su edad: ")
peso = solicitar_decimal("Ingrese su peso en kilogramos: ")
estatura = solicitar_decimal("Ingrese su estatura en metros: ")

# Calcula el Índice de Masa Corporal
imc = peso / (estatura ** 2)

# Muestra los datos y el resultado utilizando una f-string
print(f"""
--- Datos de la persona ---
Nombre: {nombre}
Apellido paterno: {apellido_paterno}
Apellido materno: {apellido_materno}
Edad: {edad} años
Peso: {peso} kg
Estatura: {estatura} m

--- Resultado ---
IMC: {imc:.2f}
""")