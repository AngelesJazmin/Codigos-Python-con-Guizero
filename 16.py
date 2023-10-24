#Genere la siguiente secuencia o serie: 1,0,1,0,1,0…. Que sea finito

from guizero import App, Text, PushButton

def generar_secuencia():
    global secuencia, indice
    secuencia_text = str(secuencia[indice])
    resultado.value = secuencia_text
    indice = (indice + 1) % len(secuencia)

def finalizar_aplicacion():
    app.destroy()

secuencia = [1, 0]
indice = 0

app = App("Generador de Secuencia", width=600, height=500)

Text(app, text="Serie: 1, 0, 1, 0, 1, 0...")
boton_generar = PushButton(app, text="Generar Siguiente", command=generar_secuencia)
boton_finalizar = PushButton(app, text="Finalizar", command=finalizar_aplicacion)
resultado = Text(app, text="Resultado:")

app.display()
