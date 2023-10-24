#Obtener la cantidad de alumnos que pasaron una materia, si son 25 alumnos y la calificación aprobatoria es de 7
#que genere las califcaciones al azar.

from guizero import App, PushButton, Text
import random

def contar_alumnos_aprobados():
    calificaciones = [random.randint(1, 10) for _ in range(25)]
    aprobados = [calificacion for calificacion in calificaciones if calificacion >= 7]
    cantidad_aprobados = len(aprobados)
    resultado.value = f"Alumnos aprobados: {cantidad_aprobados}"

app = App("Contador de Alumnos Aprobados", width=500, height=400)

Text(app, text="Haga clic en el botón para contar alumnos aprobados:")

boton_contar = PushButton(app, text="Contar Alumnos Aprobados", command=contar_alumnos_aprobados)
resultado = Text(app, text="Resultado:")

app.display()
