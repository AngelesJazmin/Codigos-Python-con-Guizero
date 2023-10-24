#Calcule el cuadrado de un número positivo leído desde el teclado

from guizero import App, Text, TextBox, PushButton

def calcular_cuadrado():
    try:
        numero = int(entrada_numero.value)
        if numero >= 0:
            cuadrado = numero ** 2
            resultado.value = f"El cuadrado de {numero} es {cuadrado}"
        else:
            resultado.value = "Ingrese un número positivo."
    except ValueError:
        resultado.value = "Ingrese un número válido."

app = App("Calculadora de Cuadrado", width=300, height=200)

Text(app, text="Ingrese un número positivo:")
entrada_numero = TextBox(app)
boton_calcular = PushButton(app, text="Calcular Cuadrado", command=calcular_cuadrado)
resultado = Text(app, text="Resultado:")

app.display()