#Calcular la edad de una persona dados el año de nacimiento y el año actual

from guizero import App, Box, Text, PushButton, TextBox #Elementos que se necesitan para correr el programa de forma dinámica

def calcular_edad():
    try:
        año_nacimiento = int(entrada_nacimiento.value) #Para que ingresen el año de nacimiento 
        año_actual = int(entrada_actual.value) #Para que ingrese el año actual
        edad = año_actual - año_nacimiento     #Resta para obtener edad
        resultado.value = f"Tienes: {edad} años" #Cómo mostrará el resultado (edad)
    except ValueError:
        resultado.value = "Ingrese años válidos." #Sólo deja ingresar números

app = App(title="Calculadora de Edad") #Nombre de la app

caja = Box(app, layout="grid") #crea una caja que servirá como un contenedor organizado en forma de cuadrícula

Text(caja, text="Año de Nacimiento:", grid=[0, 0]) #Como aparecerá la etiqueta que dirá "año de nacimiento" al lado de la caja (identifica que dato poner en la caja)
entrada_nacimiento = TextBox(caja, grid=[1, 0])    #La caja para la entrada de datos del año de nacimiento
Text(caja, text="Año Actual:", grid=[0, 1]) #Cómo aparecera la etiqueta que dirá "Año actual"
entrada_actual = TextBox(caja, grid=[1, 1]) #La caja para la entrada de datos del año actual

boton_calcular = PushButton(caja, text="Calcular Edad", command=calcular_edad, grid=[0, 2, 2, 1])
#boton_calcular es la variable que representa el boton
#pusbutton es la clase de la biblioteca guizero utlizada para crear botones
#caja es el contenedor (caja) donde se colocará este botón
#text="Calcular edad" es el texto que aparecerá en el botón
#command=calcular_edad: especifica la función calcular_edad que se ejecutará cuando se haga clic en el botón.
resultado = Text(caja, text="", grid=[0, 3, 2, 1])

app.display()