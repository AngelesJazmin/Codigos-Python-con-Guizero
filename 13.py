#Haz un código que dado el año de nacimiento y el año actual, indique cuantos años va a cumplir una persona el siguiente año


from guizero import App, Box, Text, PushButton, TextBox

def calcular_edad():
    try:
        año_nacimiento = int(entrada_nacimiento.value)
        año_actual = int(entrada_actual.value)

        if año_nacimiento <= 0:
            resultado.value = "El año de nacimiento debe ser mayor que 0."
        elif año_nacimiento > año_actual:
            resultado.value = "El año de nacimiento no puede ser mayor que el año actual."
        else:
            edad = año_actual - año_nacimiento + 1
            resultado.value = f"La edad que cumplirás el sigueinte año es: {edad} años"
    except ValueError:
        resultado.value = "Ingrese un año de nacimiento válido."

app = App("Calculadora de edad siguiente año")

caja = Box(app, layout="grid")

Text(caja, text="Año de Nacimiento:", grid=[0, 0])
entrada_nacimiento = TextBox(caja, grid=[1, 0])
Text(caja, text="Año Actual:", grid=[0, 1])
entrada_actual = TextBox(caja, grid=[1, 1])

boton_calcular = PushButton(caja, text="Calcular Edad", command=calcular_edad, grid=[0, 2, 2, 1])

resultado = Text(caja, text="", grid=[0, 3, 2, 1])

app.display()
