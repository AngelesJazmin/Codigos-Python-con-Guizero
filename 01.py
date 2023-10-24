from guizero import App, Text, PushButton

def calcular_edad():
    año_nacimiento = 1997
    año_actual = 2023
    edad = año_actual - año_nacimiento
    resultado.value = f"Edad: {edad} años"

app = App("Calculadora de Edad", width=500, height=400)

Text(app, text="Año de Nacimiento: 1997")
boton_calcular = PushButton(app, text="Calcular Edad", command=calcular_edad)
resultado = Text(app, text="Resultado:")

app.display()