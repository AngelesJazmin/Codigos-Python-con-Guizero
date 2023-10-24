#Obtenga la suma de todos los cuadrados de los números pares entre 0 y 20

from guizero import App, Text, PushButton

def calcular_suma_cuadrados():
    suma = sum(x**2 for x in range(0, 21, 2))
    resultado.value = f"La suma de los cuadrados de los números pares entre 0 y 20 es {suma}"

app = App("Calculadora de Suma de Cuadrados", width=500, height=400)

Text(app, text="Haga clic en el botón para calcular la suma de cuadrados:")

boton_calcular = PushButton(app, text="Calcular Suma", command=calcular_suma_cuadrados)
resultado = Text(app, text="Resultado:")

app.display()