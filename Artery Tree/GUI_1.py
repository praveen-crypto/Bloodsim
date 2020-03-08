from PyQt5 import QtCore, QtWidgets
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMenuBar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FC
import numpy as np
import MAIN


class Ui_MainWindow(object):
    menubar: QMenuBar

    def __init__(self):
        super().__init__()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.figure = plt.figure()
        self.canvas_1 = FC(self.figure)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.comboBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayout_1 = QtWidgets.QGridLayout(self.widget)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionExit = QtWidgets.QAction(MainWindow)


    def setupUi(self, MainWindow):
        #Mainwidow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        MainWindow.resize(1946, 1000)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setStyleSheet("\n" "background-color: rgb(243, 243, 243);")
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        #MainWindow.showFullScreen()

        #central_widget
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        #Canvas
        self.canvas_1.resize(300, 300)

        #Label_3
        self.label_3.setGeometry(QtCore.QRect(1480, 870, 171, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")

        #ComboBox_1
        self.comboBox_1.setGeometry(QtCore.QRect(1470, 910, 151, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.comboBox_1.sizePolicy().hasHeightForWidth())
        self.comboBox_1.setSizePolicy(sizePolicy)
        self.comboBox_1.setStyleSheet("background-color: rgb(43,43,43);\n"
                                      "color: rgb(255, 255, 255);\n" "")
        self.comboBox_1.setFrame(False)
        self.comboBox_1.setObjectName("comboBox_1")
        for i in range(20):
            self.comboBox_1.addItem("")

        # ComboBox_2
        self.comboBox_2.setGeometry(QtCore.QRect(1370, 10, 151, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setStyleSheet("background-color: rgb(35,35,35);\n"
                                      "color: rgb(255, 255, 255);")
        self.comboBox_2.setFrame(False)
        self.comboBox_2.setObjectName("comboBox_2")
        for j in range(20):
            self.comboBox_2.addItem("")

        #Matplot_widget
        self.widget.setGeometry(QtCore.QRect(20, 50, 1871, 801))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setSizeIncrement(QtCore.QSize(5, 5))
        self.widget.setStyleSheet("background-color: rgb(255,255,255);\n"
                                   "border-color: rgb(0,0,0);\n"
                                   "gridline-color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        self.gridLayout_1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_1.setObjectName("gridLayout_1")
        self.gridLayout_1.addChildWidget(self.canvas_1)

        #LineEdit
        self.lineEdit_1.setGeometry(QtCore.QRect(1550, 10, 111, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy)
        self.lineEdit_1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(243,243,243);\n"
                                      "border-color: rgb(60, 0, 91);")
        self.lineEdit_1.setObjectName("lineEdit_1")

        #Radiobutton_1
        self.radioButton_1.setGeometry(QtCore.QRect(1740, 10, 87, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.radioButton_1.sizePolicy().hasHeightForWidth())
        self.radioButton_1.setSizePolicy(sizePolicy)
        self.radioButton_1.setStyleSheet("")
        self.radioButton_1.setChecked(True)
        self.radioButton_1.setObjectName("radioButton_1")

        # radiobutton_2
        self.radioButton_2.setGeometry(QtCore.QRect(1850, 10, 87, 22))
        self.radioButton_2.setStyleSheet("")
        self.radioButton_2.setObjectName("radioButton_2")

        #Button_1
        self.pushButton_1.setGeometry(QtCore.QRect(1790, 870, 101, 28))
        self.pushButton_1.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                        "color: rgb(255, 255, 255);\n" "selection-background-color: rgb(0, 170, 255);\n" 
                                        "selection-color: rgb(0, 170, 255);")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(self.plot)

        #Button_2
        self.pushButton_2.setGeometry(QtCore.QRect(1790, 910, 101, 28))
        self.pushButton_2.setStyleSheet("background-color: rgb(35, 35, 35);\n" 
                                        "color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.reset)

        #label_1
        self.label_1.setGeometry(QtCore.QRect(1130, 870, 80, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setStyleSheet("")
        self.label_1.setObjectName("label_1")

        #label_2
        self.label_2.setGeometry(QtCore.QRect(1130, 910, 81, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")

        # double_spinbox
        self.doubleSpinBox.setGeometry(QtCore.QRect(1640, 910, 62, 22))
        self.doubleSpinBox.setStyleSheet("background-color: rgb(243,243,243);")
        self.doubleSpinBox.setObjectName("doubleSpinBox")

        #Double_spinbox_2
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(1230, 870, 62, 22))
        self.doubleSpinBox_2.setStyleSheet("background-color: rgb(243,243,243);")
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_2.setDecimals(1)
        self.doubleSpinBox_2.setMaximum(100)

        #double_spinbox_3
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(1230, 910, 62, 21))
        self.doubleSpinBox_3.setStyleSheet("background-color: rgb(243, 243, 243);")
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.doubleSpinBox_3.setMaximum(1000)
        self.doubleSpinBox_3.setDecimals(1)

        #Menubar
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1946, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu.setObjectName("menuMenu")
        self.menuOptions.setObjectName("menuOptions")
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionSave.setObjectName("actionSave")
        self.actionExit.setObjectName("actionExit")
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuMenu.addAction(self.actionSave)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit)
        self.actionExit.triggered.connect(self.exit)

        #StatusBar
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.statusBar.setEnabled(True)
        self.statusBar.setAutoFillBackground(False)
        self.statusBar.setStyleSheet("background-color: rgb(110, 120, 115);" "font-size: 8pt;")
        self.statusBar.setSizeGripEnabled(True)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ASS"))
        self.label_3.setText(_translate("MainWindow", "% Of Stenosis In Artery "))
        self.comboBox_1.setItemText(0,  _translate("MainWindow", "Abdominal Aorta"))
        self.comboBox_1.setItemText(1,  _translate("MainWindow", "Aortic Arch"))
        self.comboBox_1.setItemText(2,  _translate("MainWindow", "Ascending Aorta"))
        self.comboBox_1.setItemText(3,  _translate("MainWindow", "Brachial Artery Left"))
        self.comboBox_1.setItemText(4,  _translate("MainWindow", "Brachial Artery Right"))
        self.comboBox_1.setItemText(5,  _translate("MainWindow", "Cerebral Artery Left"))
        self.comboBox_1.setItemText(6,  _translate("MainWindow", "Cerebral Artery Right"))
        self.comboBox_1.setItemText(7,  _translate("MainWindow", "Common Carotid Right"))
        self.comboBox_1.setItemText(8,  _translate("MainWindow", "Common Carotid Left"))
        self.comboBox_1.setItemText(9,  _translate("MainWindow", "Femoral Artery Left"))
        self.comboBox_1.setItemText(10, _translate("MainWindow", "Femoral Artery Right"))
        self.comboBox_1.setItemText(11, _translate("MainWindow", "Hepatic Artery"))
        self.comboBox_1.setItemText(12, _translate("MainWindow", "Radial Artery Left"))
        self.comboBox_1.setItemText(13, _translate("MainWindow", "Radial Artery Right"))
        self.comboBox_1.setItemText(14, _translate("MainWindow", "Renal Artery"))
        self.comboBox_1.setItemText(15, _translate("MainWindow", "Subclavian Artery Left"))
        self.comboBox_1.setItemText(16, _translate("MainWindow", "Subclavian Artery Right"))
        self.comboBox_1.setItemText(17, _translate("MainWindow", "Thoracic Aorta"))
        self.comboBox_1.setItemText(18, _translate("MainWindow", "Ulnar Artery Left"))
        self.comboBox_1.setItemText(19, _translate("MainWindow", "Ulnar Artery Right"))

        self.comboBox_2.setItemText(0, _translate("MainWindow", "Abdominal Aorta"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Aortic Arch"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Ascending Aorta"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Brachial Artery Left"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Brachial Artery Right"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Cerebral Artery Left"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Cerebral Artery Right"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Common Carotid Right"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "Common Carotid Left"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "Femoral Artery Left"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "Femoral Artery Right"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "Hepatic Artery"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "Radial Artery Left"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "Radial Artery Right"))
        self.comboBox_2.setItemText(14, _translate("MainWindow", "Renal Artery"))
        self.comboBox_2.setItemText(15, _translate("MainWindow", "Subclavian Artery Left"))
        self.comboBox_2.setItemText(16, _translate("MainWindow", "Subclavian Artery Right"))
        self.comboBox_2.setItemText(17, _translate("MainWindow", "Thoracic Aorta"))
        self.comboBox_2.setItemText(18, _translate("MainWindow", "Ulnar Artery Left"))
        self.comboBox_2.setItemText(19, _translate("MainWindow", "Ulnar Artery Right"))

        self.radioButton_2.setText(_translate("MainWindow", "Flow"))
        self.radioButton_1.setText(_translate("MainWindow", "Pressure"))
        self.pushButton_1.setText(_translate("MainWindow", "SIMULATE"))
        self.pushButton_2.setText(_translate("MainWindow", "RESET"))
        self.label_1.setText(_translate("MainWindow", "Heart Rate"))
        self.label_2.setText(_translate("MainWindow", "Peak Flow"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Quit"))


    def plot(self):
        H = self.doubleSpinBox_2.value()              #read HR value
        P = self.doubleSpinBox_3.value()              #read P value
        print(P)
        clock, pulse = MAIN.cal(H, P)
        print(clock, pulse)
        c = np.all(clock != -1)
        p = np.all(pulse != -10000)
        if c and p:
            txt = self.comboBox_2.currentText()
            self.lineEdit_1.setText(txt)
            self.figure.suptitle(self.comboBox_2.currentText())
            self.figure.add_subplot(111)
            plt.plot(clock, pulse[255][:])
            self.canvas_1.draw()

        else:
            self.alert("Invalid values...!!")

    def reset(self):
        self.statusBar.showMessage('cleared', msecs =  2000)
        self.figure.clear()
        self.canvas_1.draw()

    def alert(self, msg):
        alert = QtWidgets.QMessageBox()
        alert.setText(msg)
        alert.exec_()

    def exit(self):
        exit_sure = QtWidgets.QMessageBox
        #exit_sure = QtWidgets.QMessageBox.question(self,'Exit', 'Do you want to exit the app?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        es = exit_sure.question('Exit', 'Do you want to exit the app?', exit_sure.Yes | exit_sure.No)
        if es == exit_sure.yes :
            MainWindow.close()
        else :
            exit_sure.exit()
            pass





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
