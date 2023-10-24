##Obtener la cantidad de alumnos que pasaron una materia, si son 25 alumnos y la calificación aprobatoria es de 7
from guizero import App, Box, Text, TextBox, PushButton

# Función para contar alumnos aprobados
def contar_aprobados():
    calificaciones = entrada_calificaciones.value.split()
    calificaciones = [int(calificacion) for calificacion in calificaciones if calificacion.isdigit()]
    
    if len(calificaciones) == 25:
        aprobados = [calificacion for calificacion in calificaciones if calificacion >= 7]
        cantidad_aprobados = len(aprobados)
        resultado.value = f"Alumnos aprobados: {cantidad_aprobados}"
    else:
        resultado.value = "Ingrese 25 calificaciones válidas."

app = App("Contador de Alumnos Aprobados", width=600, height=400)

caja = Box(app, layout="grid")

Text(caja, text="Ingrese 25 calificaciones (separadas por espacios):", grid=[0, 0])
entrada_calificaciones = TextBox(caja, grid=[1, 0], width=20)
boton_contar = PushButton(caja, text="Contar Aprobados", command=contar_aprobados, grid=[0, 5, 2, 1])
resultado = Text(caja, text="", grid=[0, 2, 2, 1])

app.display()
