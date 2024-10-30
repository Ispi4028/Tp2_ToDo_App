from PySide6 import QtCore
from modelo.tarea import Tarea

class ControladorDeTareas(QtCore.QObject):
    tarea_agregada = QtCore.Signal(str)
    tarea_eliminada = QtCore.Signal(int)

    def __init__(self):
        super().__init__()
        self.__tareas = []

    def agregar_tarea(self, descripcion):
        nueva_tarea = Tarea(descripcion)
        self.__tareas.append(nueva_tarea)
        self.__emitir_tarea_agregada(nueva_tarea)

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.__tareas):
            del self.__tareas[indice]
            self.__emitir_tarea_eliminada(indice)

    def __emitir_tarea_agregada(self, tarea):
        self.tarea_agregada.emit(tarea.obtener_descripcion())

    def __emitir_tarea_eliminada(self, indice):
        self.tarea_eliminada.emit(indice)