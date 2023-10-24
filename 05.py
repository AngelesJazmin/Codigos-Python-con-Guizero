#Obtener el promedio de n numeros positivos leidos del teclado

from guizero import App, TextBox, PushButton, Text

def calcular_promedio():
    numeros = entrada_numeros.value.split()
    numeros = [float(numero) for numero in numeros if float(numero) > 0]
    
    if numeros:
        promedio = sum(numeros) / len(numeros)
        resultado.value = f"Promedio: {promedio:.2f}"
    else:
        resultado.value = "No se ingresaron números positivos válidos."

app = App("Calculadora de Promedio", width=300, height=200)

Text(app, text="Ingrese números positivos separados por espacios:")
entrada_numeros = TextBox(app)
boton_calcular = PushButton(app, text="Calcular Promedio", command=calcular_promedio)
resultado = Text(app, text="Resultado:")

app.display()





