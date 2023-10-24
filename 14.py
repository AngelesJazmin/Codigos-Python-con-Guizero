#Obtener la suma de 5 números capturados por el usuario, asegurándose de que estén dentro del rango de 5 a 10, inclusive:

from guizero import App, Text, TextBox, PushButton

def calcular_suma():
    try:
        numeros = entrada_numeros.value.split()
        numeros = [int(numero) for numero in numeros if 5 <= int(numero) <= 10]
        
        if len(numeros) == 5: #Verifica que se hayan ingresado 5 números dentro del rango
            suma = sum(numeros) #Calcula la suma de los números en la lista "numeros"
            resultado.value = f"La suma de los 5 números es {suma}"
        else:
            resultado.value = "Ingrese exactamente 5 números en el rango [5, 10]." #Si no se ingresan 5 números válidos
    except ValueError:
        resultado.value = "Ingrese números válidos en el rango [5, 10]." #Si no están dentro del rango

app = App("Calculadora de Suma de Números (Rango 5-10)", width=600, height=500)

Text(app, text="Ingrese 5 números en el rango [5, 10], separados por espacios:")
entrada_numeros = TextBox(app, width=50)
boton_calcular = PushButton(app, text="Calcular Suma", command=calcular_suma)
resultado = Text(app, text="Resultado:")

app.display()
