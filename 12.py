#Capture n números enteros positivos que obtenga la suma del cuadrado de los pares y el cubo de los impares.

from guizero import App, Text, TextBox, PushButton

def calcular_suma_cuadrado_cubo():
    try:
        numeros = entrada_numeros.value.split()
        numeros = [int(numero) for numero in numeros if numero.isdigit()] #Convierte los números ingresados a numeros enteros 
                                                                          #y filtra aquellos que no son enteros válidos.
        
        suma_pares_cuadrado = sum(x**2 for x in numeros if x % 2 == 0)
        suma_impares_cubo = sum(x**3 for x in numeros if x % 2 != 0)
        
        resultado.value = f"Suma de cuadrados de pares: {suma_pares_cuadrado}\nSuma de cubos de impares: {suma_impares_cubo}"
    except ValueError:
        resultado.value = "Ingrese números enteros positivos válidos."

app = App("Calculadora de Suma de Cuadrados pares y Cubos impares", width=600, height=500)

Text(app, text="Ingrese números enteros positivos separados por espacios:")
entrada_numeros = TextBox(app)
boton_calcular = PushButton(app, text="Calcular Suma", command=calcular_suma_cuadrado_cubo)
resultado = Text(app, text="Resultado:")

app.display()