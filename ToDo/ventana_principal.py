from PySide6 import QtWidgets, QtCore
from ui.listado_tareas import Ui_MainWindow
from controlador.controlador_tareas import ControladorDeTareas


class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.controlador = ControladorDeTareas()

        self.ui.agregar_button.clicked.connect(self.redactar_nueva_tarea)
        self.ui.eliminiar_button.clicked.connect(self.eliminar_tarea)

        self.controlador.tarea_agregada.connect(self.agregar_tarea_ui)
        self.controlador.tarea_eliminada.connect(self.eliminar_tarea_ui)

    @QtCore.Slot()
    def redactar_nueva_tarea(self):
        texto, ok = QtWidgets.QInputDialog.getText(self, "Nueva Tarea", "Descripción:")
        if ok and texto:
            # Delegar la creación de la tarea al controlador
            self.controlador.agregar_tarea(texto)

    @QtCore.Slot(str)
    def agregar_tarea_ui(self, descripcion):
        item = QtWidgets.QListWidgetItem(descripcion)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.ui.objeto_lista.addItem(item)

    @QtCore.Slot()
    def eliminar_tarea(self):
        items_seleccionados = self.ui.objeto_lista.selectedItems()
        for item in items_seleccionados:
            indice = self.ui.objeto_lista.row(item)
            self.controlador.eliminar_tarea(indice)

    @QtCore.Slot(int)
    def eliminar_tarea_ui(self, indice):
        self.ui.objeto_lista.takeItem(indice)