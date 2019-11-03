from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib as mat; import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FC
import numpy as np; import MAIN


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(999, 686)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(987, 661))
        #MainWindow.setMaximumSize(QtCore.QSize(990, 700))
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)

        #-----------------------------------------------Central_Widget--------------------------------------------------
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")

        #---------------------------------------------------Canvas------------------------------------------------------
        self.figure = plt.figure()
        self.canvas_1 = FC(self.figure)
        self.canvas_1.resize(351, 231)
        self.canvas_2 = FC(self.figure)
        self.canvas_2.resize(351, 231)
        self.canvas_3 = FC(self.figure)
        self.canvas_3.resize(351, 231)
        self.canvas_4 = FC(self.figure)
        self.canvas_4.resize(351, 231)


        #-----------------------------------------------LineEdit_1------------------------------------------------------
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(80, 131, 41, 19))
        self.lineEdit_1.setObjectName("lineEdit_1")

        #--------------------------------------LineEdit_2---------------------------------------------------------------
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 171, 41, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")

        #-----------------------------------------------Label_1---------------------------------------------------------
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(11, 130, 52, 19))
        self.label_1.setObjectName("label_1")

        #-------------------------------------------------Label_2-------------------------------------------------------
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(11, 171, 48, 16))
        self.label_2.setObjectName("label_2")

        #------------------------------------------------canvas_1-------------------------------------------------------
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 70, 351, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_1.setObjectName("gridLayout_1")
        self.gridLayout_1.addChildWidget(self.canvas_1)

        #-------------------------------------------------canvas_2------------------------------------------------------
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(570, 70, 341, 231))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.addChildWidget(self.canvas_2)

        #-----------------------------------------canvas_3--------------------------------------------------------------
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(200, 380, 351, 231))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.addChildWidget(self.canvas_3)

        #-----------------------------------------canvas_4--------------------------------------------------------------
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(570, 380, 341, 231))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_4.addChildWidget(self.canvas_4)

        #-------------------------------------------------Label_5---------------------------------------------------
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 50, 61, 16))
        self.label_5.setObjectName("label_5")

        #--------------------------------------------------Label_6-----------------------------------------------
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(720, 50, 47, 13))
        self.label_6.setObjectName("label_6")

        #--------------------------------------Label_7----------------------------------------------------------------
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(350, 360, 51, 21))
        self.label_7.setObjectName("label_7")

        #---------------------------------------Label_8-------------------------------------------------------------
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(720, 360, 51, 20))
        self.label_8.setObjectName("label_8")

        #-------------------------------------Combobox_3----------------------------------------------------
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(212, 22, 101, 20))
        self.comboBox_3.setFrame(False)
        self.comboBox_3.setObjectName("comboBox_3")
        for x in range(20):
            self.comboBox_3.addItem("")

        #------------------------------------------------LineEdit_5----------------------------------------------------
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(330, 22, 133, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")

        #-------------------------------------------------Combobox_4---------------------------------------------------
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(212, 331, 101, 20))
        self.comboBox_4.setFrame(False)
        self.comboBox_4.setObjectName("comboBox_4")
        x = 0
        for x in range(20):
            self.comboBox_4.addItem("")

        #-------------------------------------------------LineEdit_6---------------------------------------------------
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(330, 331, 133, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")

        #----------------------------------------------------Label_4---------------------------------------------------
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(12, 350, 126, 16))
        self.label_4.setObjectName("label_4")

        #---------------------------------------------------Combobox_2-----------------------------------------------
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(12, 371, 81, 20))
        self.comboBox_2.setFrame(False)
        self.comboBox_2.setObjectName("comboBox_2")
        for x in range(20):
            self.comboBox_2.addItem("")

        #-----------------------------------------------------LineEdit_4-----------------------------------------------
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 371, 71, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")

        #---------------------------------------------------Label_3----------------------------------------------------
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(12, 290, 126, 16))
        self.label_3.setObjectName("label_3")

        #---------------------------------------------------LineEdit_3-------------------------------------------------
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 310, 71, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        #----------------------------------------------------ComboBox_1------------------------------------------------
        self.comboBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_1.setGeometry(QtCore.QRect(12, 310, 81, 20))
        self.comboBox_1.setFrame(False)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")

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


        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(920, 460, 67, 61))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget2)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_2.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget2)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_2.addWidget(self.radioButton_4)

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
        MainWindow.setTabOrder(self.lineEdit_5, self.radioButton_1)
        MainWindow.setTabOrder(self.radioButton_1, self.radioButton_2)
        MainWindow.setTabOrder(self.radioButton_2, self.comboBox_4)
        MainWindow.setTabOrder(self.comboBox_4, self.lineEdit_6)
        MainWindow.setTabOrder(self.lineEdit_6, self.radioButton_3)
        MainWindow.setTabOrder(self.radioButton_3, self.radioButton_4)
        MainWindow.setTabOrder(self.radioButton_4, self.pushButton_1)
        MainWindow.setTabOrder(self.pushButton_1, self.pushButton_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ASS"))
        self.label_1.setText(_translate("MainWindow", "Heart Rate"))
        self.label_2.setText(_translate("MainWindow", "Peak Flow"))
        self.label_5.setText(_translate("MainWindow", "STENOSIS"))
        self.label_6.setText(_translate("MainWindow", "NORMAL"))
        self.label_7.setText(_translate("MainWindow", "STENOSIS"))
        self.label_8.setText(_translate("MainWindow", "NORMAL"))
        self.label_4.setText(_translate("MainWindow", "% Of Stenosis In Artery-2"))
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
        self.comboBox_2.setItemText(0, _translate("MainWindow", "PULSE ODE"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Ascending aorta"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Aortic arch"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Subclavian artery left"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Subclavian artery right"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Common carotid(L)"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Common carotid(R)"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Thoracic aorta"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "cerebral artery right"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "cerebral artery left"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "abdominal aorta"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "Brachial artery right"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "Brachial artery left"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "Hepatic artery"))
        self.comboBox_2.setItemText(14, _translate("MainWindow", "Renal artery"))
        self.comboBox_2.setItemText(15, _translate("MainWindow", "femoral artery left"))
        self.comboBox_2.setItemText(16, _translate("MainWindow", "femoral artery right"))
        self.comboBox_2.setItemText(17, _translate("MainWindow", "ulnar artery left"))
        self.comboBox_2.setItemText(18, _translate("MainWindow", "ulnar artery right"))
        self.comboBox_2.setItemText(19, _translate("MainWindow", "radial artery left"))
        self.comboBox_2.setItemText(20, _translate("MainWindow", "radial artery right"))
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
        self.comboBox_4.setItemText(0, _translate("MainWindow", "PULSE ODE"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Ascending aorta"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Aortic arch"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Subclavian artery left"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "Subclavian artery right"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "Common carotid(L)"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "Common carotid(R)"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "Thoracic aorta"))
        self.comboBox_4.setItemText(8, _translate("MainWindow", "cerebral artery right"))
        self.comboBox_4.setItemText(9, _translate("MainWindow", "cerebral artery left"))
        self.comboBox_4.setItemText(10, _translate("MainWindow", "abdominal aorta"))
        self.comboBox_4.setItemText(11, _translate("MainWindow", "Brachial artery right"))
        self.comboBox_4.setItemText(12, _translate("MainWindow", "Brachial artery left"))
        self.comboBox_4.setItemText(13, _translate("MainWindow", "Hepatic artery"))
        self.comboBox_4.setItemText(14, _translate("MainWindow", "Renal artery"))
        self.comboBox_4.setItemText(15, _translate("MainWindow", "femoral artery left"))
        self.comboBox_4.setItemText(16, _translate("MainWindow", "femoral artery right"))
        self.comboBox_4.setItemText(17, _translate("MainWindow", "ulnar artery left"))
        self.comboBox_4.setItemText(18, _translate("MainWindow", "ulnar artery right"))
        self.comboBox_4.setItemText(19, _translate("MainWindow", "radial artery left"))
        self.comboBox_4.setItemText(20, _translate("MainWindow", "radial artery right"))

        self.pushButton_1.setText(_translate("MainWindow", "SIMULATE"))
        self.pushButton_2.setText(_translate("MainWindow", "RESET"))
        self.radioButton_1.setText(_translate("MainWindow", "Pressure"))
        self.radioButton_2.setText(_translate("MainWindow", "Flow"))
        self.radioButton_3.setText(_translate("MainWindow", "Pressure"))
        self.radioButton_4.setText(_translate("MainWindow", "Flow"))
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
            plt.plot(clock, pulse)
            self.canvas_1.draw()
            self.canvas_2.draw()
            self.canvas_3.draw()
            self.canvas_4.draw()
        else:
            self.alert("Incorrect args...!!!")


    def reset(self):
        self.figure.clear()
        self.canvas_2.draw()
        self.canvas_1.draw()
        self.canvas_3.draw()
        self.canvas_4.draw()

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
