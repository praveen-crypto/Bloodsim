from PyQt5 import QtCore, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FC
import numpy as np; import MAIN


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(999, 686)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.setMinimumSize(QtCore.QSize(987, 661))
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setWindowState(QtCore.Qt.WindowMaximized)
        MainWindow.mouseDoubleClickEvent()



        #-----------------------------------------------Central_Widget--------------------------------------------------
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")

        #-------------------------------------------------Canvas------------------------------------------------------
        self.figure = plt.figure()
        self.canvas_1 = FC(self.figure)
        self.canvas_1.resize(351, 231)

        #-----------------------------------------------LineEdit_1------------------------------------------------------
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(85, 136, 41, 19))
        self.lineEdit_1.setObjectName("lineEdit_1")

        #-----------------------------------------------LineEdit_2------------------------------------------------------
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 171, 41, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")

        # -------------------------------------------------LineEdit_3---------------------------------------------------
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 310, 71, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        # --------------------------------------------------LineEdit_5--------------------------------------------------
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(330, 22, 133, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")

        #-----------------------------------------------Label_1---------------------------------------------------------
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(11, 130, 52, 19))
        self.label_1.setObjectName("label_1")

        #-------------------------------------------------Label_2-------------------------------------------------------
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(11, 171, 48, 16))
        self.label_2.setObjectName("label_2")

        # ---------------------------------------------------Label_3----------------------------------------------------
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(12, 290, 126, 16))
        self.label_3.setObjectName("label_3")

        #-------------------------------------------GridLayout----------------------------------------------------
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 70, 351, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_1.setObjectName("gridLayout_1")
        self.gridLayout_1.addChildWidget(self.canvas_1)

        # ----------------------------------------------------ComboBox_1------------------------------------------------
        self.comboBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_1.setGeometry(QtCore.QRect(12, 310, 81, 20))
        self.comboBox_1.setFrame(False)
        self.comboBox_1.setObjectName("comboBox_1")
        for x in range(20):
            self.comboBox_1.addItem("")

        #-------------------------------------Combobox_3----------------------------------------------------
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(212, 22, 101, 20))
        self.comboBox_3.setFrame(False)
        self.comboBox_3.setObjectName("comboBox_3")
        for x in range(20):
            self.comboBox_3.addItem("")

        #-----------------------------pushbutton_1 & pushbutton_2-------------------------------------------------------
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(11, 620, 181, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_1 = QtWidgets.QPushButton(self.widget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout_3.addWidget(self.pushButton_1)        #adding widget pushbutton_1
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)         #adding widget pushbutton_2
        self.pushButton_1.clicked.connect(self.plot)
        self.pushButton_2.clicked.connect(self.reset)

        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(920, 167, 67, 61))
        self.widget1.setObjectName("widget1")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.radioButton_1 = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_1.setObjectName("radioButton_1")
        self.verticalLayout.addWidget(self.radioButton_1)

        self.radioButton_2 = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 999, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ASS"))
        self.label_1.setText(_translate("MainWindow", "Heart Rate"))
        self.label_2.setText(_translate("MainWindow", "Peak Flow"))
        self.label_3.setText(_translate("MainWindow", "% Of Stenosis In Artery-1"))
        self.comboBox_1.setItemText(0, _translate("MainWindow", "PULSE ODE"))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "Ascending aorta"))
        self.comboBox_1.setItemText(2, _translate("MainWindow", "Aortic arch"))
        self.comboBox_1.setItemText(3, _translate("MainWindow", "Subclavian artery left"))
        self.comboBox_1.setItemText(4, _translate("MainWindow", "Subclavian artery right"))
        self.comboBox_1.setItemText(5, _translate("MainWindow", "Common carotid(L)"))
        self.comboBox_1.setItemText(6, _translate("MainWindow", "Common carotid(R)"))
        self.comboBox_1.setItemText(7, _translate("MainWindow", "Thoracic aorta"))
        self.comboBox_1.setItemText(8, _translate("MainWindow", "cerebral artery right"))
        self.comboBox_1.setItemText(9, _translate("MainWindow", "cerebral artery left"))
        self.comboBox_1.setItemText(10, _translate("MainWindow", "abdominal aorta"))
        self.comboBox_1.setItemText(11, _translate("MainWindow", "Brachial artery right"))
        self.comboBox_1.setItemText(12, _translate("MainWindow", "Brachial artery left"))
        self.comboBox_1.setItemText(13, _translate("MainWindow", "Hepatic artery"))
        self.comboBox_1.setItemText(14, _translate("MainWindow", "Renal artery"))
        self.comboBox_1.setItemText(15, _translate("MainWindow", "femoral artery left"))
        self.comboBox_1.setItemText(16, _translate("MainWindow", "femoral artery right"))
        self.comboBox_1.setItemText(17, _translate("MainWindow", "ulnar artery left"))
        self.comboBox_1.setItemText(18, _translate("MainWindow", "ulnar artery right"))
        self.comboBox_1.setItemText(19, _translate("MainWindow", "radial artery left"))
        self.comboBox_1.setItemText(20, _translate("MainWindow", "radial artery right"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "PULSE ODE"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Ascending aorta"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Aortic arch"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Subclavian artery left"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Subclavian artery right"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "Common carotid(L)"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "Common carotid(R)"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "Thoracic aorta"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "cerebral artery right"))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "cerebral artery left"))
        self.comboBox_3.setItemText(10, _translate("MainWindow", "abdominal aorta"))
        self.comboBox_3.setItemText(11, _translate("MainWindow", "Brachial artery right"))
        self.comboBox_3.setItemText(12, _translate("MainWindow", "Brachial artery left"))
        self.comboBox_3.setItemText(13, _translate("MainWindow", "Hepatic artery"))
        self.comboBox_3.setItemText(14, _translate("MainWindow", "Renal artery"))
        self.comboBox_3.setItemText(15, _translate("MainWindow", "femoral artery left"))
        self.comboBox_3.setItemText(16, _translate("MainWindow", "femoral artery right"))
        self.comboBox_3.setItemText(17, _translate("MainWindow", "ulnar artery left"))
        self.comboBox_3.setItemText(18, _translate("MainWindow", "ulnar artery right"))
        self.comboBox_3.setItemText(19, _translate("MainWindow", "radial artery left"))
        self.comboBox_3.setItemText(20, _translate("MainWindow", "radial artery right"))
        self.pushButton_1.setText(_translate("MainWindow", "SIMULATE"))
        self.pushButton_2.setText(_translate("MainWindow", "RESET"))
        self.radioButton_1.setText(_translate("MainWindow", "Pressure"))
        self.radioButton_2.setText(_translate("MainWindow", "Flow"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))

    def plot(self):
        H = self.lineEdit_1.text()
        P = self.lineEdit_2.text()
        clock, pulse = MAIN.cal(H, P)
        print(clock,pulse)
        c = np.all(clock != -1)
        p = np.all(pulse != -10000)
        if c and p:
            print(H, P)
            id = self.comboBox_3.currentIndex()
            txt = self.comboBox_3.currentText()
            self.lineEdit_5.setText(txt)
            self.figure.suptitle(self.comboBox_3.currentText())
            self.figure.add_subplot(111)
            plt.plot(clock, pulse[255][:])
            self.canvas_1.draw()
        else:
            self.alert("Incorrect args...!!!")

    def reset(self):
        self.figure.clear()
        self.canvas_1.draw()

#=====================================# alert box=====================================
    def alert(self, msg):
        alert = QtWidgets.QMessageBox()
        alert.setText(msg)
        alert.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())