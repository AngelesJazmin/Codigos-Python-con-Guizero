#Obtenga la suma de todos los cuadrados de n números capturados del teclado

from guizero import App, Text, TextBox, PushButton

def calcular_suma_cuadrados():
    try:
        numeros = entrada_numeros.value.split()
        numeros = [float(numero) for numero in numeros]
        
        suma_cuadrados = sum(x**2 for x in numeros)
        resultado.value = f"La suma de los cuadrados es {suma_cuadrados:.2f}"
    except ValueError:
        resultado.value = "Ingrese números válidos."

app = App("Calculadora de Suma de Cuadrados", width=500, height=400)

Text(app, text="Ingrese números separados por espacios:")
entrada_numeros = TextBox(app)
boton_calcular = PushButton(app, text="Calcular Suma de Cuadrados", command=calcular_suma_cuadrados)
resultado = Text(app, text="Resultado:")

app.display()



