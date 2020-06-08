from PyQt5 import QtGui, QtCore, QtWidgets
import os


class Ui_HomeWindow(object):
    def __init__(self, HomeWin):
        super().__init__()
        HomeWin.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.HomeWin = HomeWin
        self.setupUi()

    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget(self.HomeWin)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.pushButton_2.setFlat(True)
        self.pushButton_3.setFlat(True)
        self.pushButton_1.setDefault(False)
        self.pushButton_1.setFlat(True)

        self.HomeWin.setObjectName("MainWindow")
        self.HomeWin.resize(800, 400)
        self.HomeWin.setMinimumSize(QtCore.QSize(800, 400))
        self.HomeWin.setMaximumSize(QtCore.QSize(1000, 500))
        self.HomeWin.setStyleSheet("background-color: rgb(37, 118, 184);\n")
        self.HomeWin.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.HomeWin.setDocumentMode(False)
        self.HomeWin.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.HomeWin.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.HomeWin.setWindowTitle("BloodSim")

        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_2.setGeometry(QtCore.QRect(570, 260, 191, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(23, 63, 95);\n"
                                        "color: rgb(246, 213, 92);\n")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setIcon(QtGui.QIcon(os.path.join('images', 'Homebutton2.png')))
        self.pushButton_2.setIconSize(QtCore.QSize(190, 41))

        self.pushButton_3.setGeometry(QtCore.QRect(570, 320, 191, 41))
        self.pushButton_3.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_3.setStyleSheet("background-color: rgb(23, 63, 95);\n"
                                        "color: rgb(246, 213, 92);\n")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setIcon(QtGui.QIcon(os.path.join('images', 'Homebutton3.png')))
        self.pushButton_3.setIconSize(QtCore.QSize(190, 41))

        self.pushButton_1.setGeometry(QtCore.QRect(570, 200, 191, 41))
        self.pushButton_1.setStyleSheet("border-color: rgb(0, 0, 0);\n"
                                        "color: rgb(246, 213, 92);\n"
                                        "background-color: rgb(23, 63, 95);\n")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.setIcon(QtGui.QIcon(os.path.join('images', 'Homebutton1.png')))
        self.pushButton_1.setIconSize(QtCore.QSize(190, 41))

        self.label.setGeometry(QtCore.QRect(80, 0, 491, 296))
        self.label.setObjectName("label")
        self.label.setPixmap(QtGui.QPixmap(os.path.join('images', 'icon.jpeg')))

        self.label_2.setGeometry(QtCore.QRect(72, 290, 491, 81))
        self.label_2.setObjectName("label_2")
        self.label_2.setPixmap(QtGui.QPixmap(os.path.join('images', 'title.jpeg')))

        self.HomeWin.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(self.HomeWin)