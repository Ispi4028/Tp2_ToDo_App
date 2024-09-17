from PySide6 import QtCore
from controlador.tarea import Tarea

class ControladorDeTareas(QtCore.QObject):
    tarea_agregada = QtCore.Signal(str)
    tarea_eliminada = QtCore.Signal(int)

    def __init__(self):
        super().__init__()
        self.tareas = []

    def agregar_tarea(self, descripcion):
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)
        self.tarea_agregada.emit(nueva_tarea.descripcion)

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
            #Emitir señal para actualizar la UI
            self.tarea_eliminada.emit(indice)
