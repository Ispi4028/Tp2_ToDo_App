# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'listado_tareas.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(397, 411)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.objeto_lista = QListWidget(self.centralwidget)
        self.objeto_lista.setObjectName(u"objeto_lista")

        self.gridLayout.addWidget(self.objeto_lista, 0, 0, 1, 2)

        self.agregar_button = QPushButton(self.centralwidget)
        self.agregar_button.setObjectName(u"agregar_button")

        self.gridLayout.addWidget(self.agregar_button, 1, 0, 1, 1)

        self.eliminiar_button = QPushButton(self.centralwidget)
        self.eliminiar_button.setObjectName(u"eliminiar_button")

        self.gridLayout.addWidget(self.eliminiar_button, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 397, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.agregar_button.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.eliminiar_button.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
    # retranslateUi

