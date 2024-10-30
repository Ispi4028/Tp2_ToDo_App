from PySide6 import QtWidgets
from ui.ventana_principal import VentanaPrincipal
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())