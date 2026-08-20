# calculadora_imc.py

'''
Este programa solicita los datos básicos de una persona
(nombre, apellidos, edad, peso y estatura) y calcula
su Índice de Masa Corporal (IMC).
'''

# Solicita el nombre y lo muestra con la primera letra en mayúscula
nombre = input("Ingrese su nombre: ").capitalize()

# Solicita el apellido paterno y lo muestra con la primera letra en mayúscula
apellido_paterno = input("Ingrese su apellido paterno: ").capitalize()

# Solicita el apellido materno y lo muestra con la primera letra en mayúscula
apellido_materno = input("Ingrese su apellido materno: ").capitalize()

# Solicita la edad y la convierte a entero
edad = int(input("Ingrese su edad: "))

# Solicita el peso y lo convierte a decimal
peso = float(input("Ingrese su peso en kilogramos: "))

# Solicita la estatura y la convierte a decimal
estatura = float(input("Ingrese su estatura en metros: "))

# Calcula el Índice de Masa Corporal
imc = peso / (estatura ** 2)

# Muestra todos los datos y el resultado utilizando una f-string
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