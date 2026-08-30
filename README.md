# Proyecto Python - Calculadora de IMC

## Descripción del programa

Este proyecto consiste en una calculadora del Índice de Masa Corporal (IMC) desarrollada en Python.

El programa solicita al usuario los siguientes datos:

* Nombre
* Apellido paterno
* Apellido materno
* Edad
* Peso en kilogramos
* Estatura en metros

Con estos datos, el programa calcula el IMC mediante la fórmula:

**IMC = peso / (estatura ** 2)**

El programa también cuenta con validaciones para evitar que los campos queden vacíos y para comprobar que la edad, el peso y la estatura sean valores numéricos válidos.

Además, los nombres y apellidos se muestran con la primera letra en mayúscula y el resultado del IMC se presenta redondeado a dos decimales.

## Instrucciones de ejecución

Para ejecutar el programa se deben seguir estos pasos:

1. Tener Python instalado en el computador.
2. Descargar o clonar el repositorio de GitHub.
3. Abrir la carpeta del proyecto en Visual Studio Code.
4. Abrir una terminal dentro de la carpeta del proyecto.
5. Ejecutar el siguiente comando:

```bash
python calculadora_imc.py
```

6. Ingresar los datos solicitados por el programa.
7. Revisar el resumen de los datos y el resultado final del IMC.

Si se deja algún campo vacío o se ingresan letras en los campos numéricos, el programa mostrará un mensaje de error y solicitará nuevamente el dato.

## Validaciones implementadas

El programa cuenta con las siguientes validaciones:

* No permite dejar los campos de texto vacíos.
* No permite dejar los campos numéricos vacíos.
* Verifica que la edad sea un número entero.
* Verifica que el peso sea un número decimal.
* Verifica que la estatura sea un número decimal.
* Evita que el programa se cierre cuando se ingresan letras en los campos numéricos.

## Tecnologías utilizadas

* Python
* Visual Studio Code
* Git
* GitHub

## Archivo principal

* `calculadora_imc.py`: contiene el programa que solicita los datos, realiza las validaciones y calcula el IMC.

## Reflexión personal

Durante el bootcamp aprendí diferentes conceptos básicos de Python y pude aplicarlos en la creación de una calculadora de IMC.

Al comenzar el proyecto aprendí a trabajar con variables y diferentes tipos de datos. Después aprendí a utilizar `input()` para permitir que el usuario ingresara información desde la consola y a realizar conversiones de tipos para poder trabajar correctamente con números enteros y decimales.

También aprendí a utilizar operaciones matemáticas, métodos de cadenas como `capitalize()` y f-strings para mostrar los resultados de una manera más organizada.

Otro aprendizaje importante fue conocer Git y GitHub. Aprendí a crear un repositorio, realizar commits y utilizar comandos como `git add`, `git commit` y `git push` para guardar y subir los cambios del proyecto.

Finalmente, aprendí la importancia de validar los datos ingresados por el usuario. Esto permite que el programa sea más seguro y evita que se cierre cuando se introducen datos incorrectos.

Este proyecto me ayudó a reforzar mis conocimientos de Python y a comprender mejor cómo diferentes conceptos de programación pueden combinarse para crear un programa funcional.
