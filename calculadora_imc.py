# calculadora_imc.py

'''
Este programa solicita los datos básicos de una persona
(nombre, apellidos, edad, peso y estatura) y calcula
su Índice de Masa Corporal (IMC).
'''

# Solicita el nombre de la persona (tipo string)
nombre = input("Ingrese su nombre: ")

# Solicita el apellido paterno (tipo string)
apellido_paterno = input("Ingrese su apellido paterno: ")

# Solicita el apellido materno (tipo string)
apellido_materno = input("Ingrese su apellido materno: ")

# Solicita la edad y la convierte a entero (tipo int)
edad = int(input("Ingrese su edad: "))

# Solicita el peso y lo convierte a decimal (tipo float)
peso = float(input("Ingrese su peso en kilogramos: "))

# Solicita la estatura y la convierte a decimal (tipo float)
estatura = float(input("Ingrese su estatura en metros: "))

# Calcula el Índice de Masa Corporal
imc = peso / (estatura ** 2)

# Muestra los datos y el resultado del cálculo
print("\n--- Datos de la persona ---")
print("Nombre:", nombre)
print("Apellido paterno:", apellido_paterno)
print("Apellido materno:", apellido_materno)
print("Edad:", edad)
print("Peso:", peso, "kg")
print("Estatura:", estatura, "m")

print("\n--- Resultado ---")
print("IMC:", imc)