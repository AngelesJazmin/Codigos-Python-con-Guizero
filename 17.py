#Preguntar un número del 1 al 7 y determinar qué día de la semana es

from guizero import App, Text, TextBox, PushButton

def determinar_dia_semana():
    try:
        numero = int(entrada_numero.value)
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

        if 1 <= numero <= 7:
            dia_semana = dias_semana[numero - 1] #Como lunes en la lista tiene un indice de cero (porque así son las listas, 
            #comienzan en cero) es necesario restar 1 al número ingresado por el usuario para mapear correctamente el número 
            #al día de la semana correspondiente en la lista. por ejemplo si pongo 1 (va a restar 1-1 = 0 y cero corresponde a lunes)
            #así me estaría dando el día que le corresponde a 1
            resultado.value = f"Día de la semana: {dia_semana}"
        else:
            resultado.value = "Ingrese un número entre 1 y 7."
    except ValueError:
        resultado.value = "Ingrese un número válido."

app = App("Determinador de Día de la Semana", width=600, height=500)

Text(app, text="Ingrese un número del 1 al 7:")
entrada_numero = TextBox(app)
boton_determinar = PushButton(app, text="Determinar Día", command=determinar_dia_semana)
resultado = Text(app, text="Resultado:")

app.display()

