#Obtenga el promedio de 3 números cualquiera

from guizero import App, TextBox, PushButton, Text

def calcular_promedio():
    try:
        numero1 = float(entrada_numero1.value)
        numero2 = float(entrada_numero2.value)
        numero3 = float(entrada_numero3.value)
        promedio = (numero1 + numero2 + numero3) / 3
        resultado.value = f"Promedio: {promedio:.2f}"
    except ValueError:
        resultado.value = "Ingrese números válidos."

app = App("Calculadora de Promedio", width=300, height=200)

Text(app, text="Ingrese el primer número:")
entrada_numero1 = TextBox(app)
Text(app, text="Ingrese el segundo número:")
entrada_numero2 = TextBox(app)
Text(app, text="Ingrese el tercer número:")
entrada_numero3 = TextBox(app)

boton_calcular = PushButton(app, text="Calcular Promedio", command=calcular_promedio)
resultado = Text(app, text="Resultado:")

app.display()
