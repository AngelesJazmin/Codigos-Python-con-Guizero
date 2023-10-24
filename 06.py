#Obtener la edad promedio de “n” personas preguntándoles su año de nacimiento y asumiendo que el año actual es 2023

from guizero import App, TextBox, PushButton, Text

def calcular_edad_promedio():  #realizará el cálculo del promedio y gestionará las validaciones.
    a_nacimiento = entrada_a_nacimiento.value.split() #Obtiene los años de nacimiento ingresados por el usuario en el campo de entrada
                                                      #y los divide en una lista utilizando el espacio como separador
    a_nacimiento = [int(a_nac) for a_nac in a_nacimiento if int(a_nac) > 0] #Convierte los años de nacimiento a enteros y crea una 
                                                      #nueva lista que contiene solo los años de nacimiento válidos (mayores que 0).

    if a_nacimiento:
        edad_promedio = (2023 - sum(a_nacimiento) / len(a_nacimiento))
        #Calcula el promedio restando el año actual (2023) a cada año de nacimiento, y va agregando cada edad en acumulador suma
        #luego divide esa suma por la cantidad de años en la lista.
        resultado.value = f"Edad promedio: {edad_promedio:.2f}" #El resultado se muestra con dos decimales
    else:
        resultado.value = "No se ingresaron años de nacimiento válidos."
        #Si no hay años de nacimiento válidos en la lista, muestra un mensaje de error en el elemento de texto de resultado

app = App("Calculadora de Edad Promedio", width=500, height=300)

Text(app, text="Ingrese los años de nacimiento separados por espacios:")
entrada_a_nacimiento = TextBox(app)
boton_calcular = PushButton(app, text="Calcular Edad Promedio", command=calcular_edad_promedio)
resultado = Text(app, text="Resultado:")

app.display()