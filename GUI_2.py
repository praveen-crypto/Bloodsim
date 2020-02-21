from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FC
import numpy as np
import MAIN
import stenosis



class Ui_MainWindow(object):
    def __init__(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.figure = plt.figure(dpi= 150, facecolor= (0.12941, 0.22353, 0.33725))
        self.canvas_1 = FC(self.figure)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.splitter_4 = QtWidgets.QSplitter(self.centralwidget)
        self.label_3 = QtWidgets.QLabel(self.splitter_4)
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.comboBox_1 = QtWidgets.QComboBox(self.splitter_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.splitter_3)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)

    def setupUi(self, MainWindow):
        #MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1489, 896)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 700))
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setStyleSheet("color: rgb(255, 210, 119);\n"
                                 "selection-color: rgb(237, 85, 59);\n"
                                 "selection-background-color: rgb(33, 57, 86);\n"
                                 "background-color: rgb(33, 57, 86);\n"
                                 "font: 11pt \"Garamond\";\n"
                                 "\n"
                                 "")
        MainWindow.setIconSize(QtCore.QSize(32, 32))

        #Central_Widget
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout.setObjectName("gridLayout")

        #Button
        self.pushButton_1.setStyleSheet("font: 12.5pt \"Garamond\";\n"
                                        "background-color: rgb(35, 35, 35);\n"
                                        "color: rgb(255, 210, 119);\n"
                                        "selection-color: rgb(237, 85, 59);\n"
                                        "selection-background-color: rgb(33, 57, 86);")
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 4, 7, 1, 1)
        self.pushButton_1.clicked.connect(self.plot)

        # Radiobutton_1
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.radioButton_1.sizePolicy().hasHeightForWidth())
        self.radioButton_1.setSizePolicy(sizePolicy)
        self.radioButton_1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "font: 12.5pt \"Garamond\";")
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_1.clicked.connect(self.pressure_plot)
        self.gridLayout.addWidget(self.radioButton_1, 0, 6, 1, 1)

        #Radiobutton_2
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "font: 12.5pt \"Garamond\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 0, 7, 1, 1)
        self.radioButton_2.clicked.connect(self.flow_plot)

        #Button_2
        self.pushButton_2.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                        "color: rgb(255, 210, 119);\n"
                                        "font: 12.5pt \"Garamond\";\n"
                                        "selection-color: rgb(237, 85, 59);\n"
                                        "selection-background-color: rgb(33, 57, 86);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 5, 7, 1, 1)
        self.pushButton_2.clicked.connect(self.reset)

        #doubleSpinBox_2
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_2.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_2.setSizePolicy(sizePolicy)
        self.doubleSpinBox_2.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                           "selection-color: rgb(237, 85, 59);\n"
                                           "selection-background-color: rgb(33, 57, 86);\n"
                                           "\n"
                                           "font: 11pt \"Calibri\";")
        self.doubleSpinBox_2.setMaximum(122.99)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_2.setMaximum(1000)
        self.gridLayout.addWidget(self.doubleSpinBox_2, 4, 3, 1, 1)

        # Label_1
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setStyleSheet("font: 12.5pt \"Garamond\";\n"
                                   "color: rgb(255,255,255);")
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 4, 2, 1, 1)

        #Label_2
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("font: 12.5pt \"Garamond\";\n"
                                   "color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 2, 1, 1)

        #doubleSpinBox_3
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_3.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_3.setSizePolicy(sizePolicy)
        self.doubleSpinBox_3.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                           "selection-color: rgb(237, 85, 59);\n"
                                           "selection-background-color: rgb(33, 57, 86);\n"
                                           "font: 11pt \"Calibri\";")
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.doubleSpinBox_3.setMaximum(1000)
        self.gridLayout.addWidget(self.doubleSpinBox_3, 5, 3, 1, 1)

        # comboBox_1
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.comboBox_1.sizePolicy().hasHeightForWidth())
        self.comboBox_1.setSizePolicy(sizePolicy)
        self.comboBox_1.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                      "selection-color: rgb(237, 85, 59);\n"
                                      "selection-background-color: rgb(33, 57, 86);\n"
                                      "color: rgb(255, 210, 119);\n"
                                      "border-color: rgb(255, 255, 255);\n"
                                      "gridline-color: rgb(255, 255, 255);\n"
                                      "\n"
                                      "font: 12.5pt \"Garamond\";")
        self.comboBox_1.setFrame(False)
        self.comboBox_1.setObjectName("comboBox_1")
        for i in range(20):
            self.comboBox_1.addItem("")

        #comboBox_2
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setStyleSheet("font: 12.5pt \"Garamond\";\n"
                                      "background-color: rgb(35, 35, 35);\n"
                                      "color: rgb(255, 210, 119);\n"
                                      "selection-color: rgb(237, 85, 59);\n"
                                      "selection-background-color: rgb(33, 57, 86);\n"
                                      "border-color: rgb(85, 170, 255);\n"
                                      "border-top-color: rgb(85, 255, 255);\n"
                                      "border-right-color: rgb(85, 255, 255);\n"
                                      "border-bottom-color: rgb(85, 255, 255);\n"
                                      "border-left-color: rgb(85, 255, 255);\n"
                                      "gridline-color: rgb(255, 255, 255);\n"
                                      "")
        self.comboBox_2.setFrame(False)
        self.comboBox_2.setObjectName("comboBox_2")
        for j in range(20):
            self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 0, 4, 1, 1)
        self.comboBox_2.currentIndexChanged.connect(self.viewing)

        #Matplot_canvas
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        #sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.canvas_1.setSizePolicy(sizePolicy)
        self.canvas_1.setSizeIncrement(QtCore.QSize(5, 5))
        self.gridLayout.addWidget(self.canvas_1, 2, 1, 1, 7)

        #splitter_4
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")

        #label_3
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12.5pt \"Garamond\";\n"
                                   "")
        self.label_3.setObjectName("label_3")

        #splitter_3
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")

        #doubleSpinBox
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy)
        self.doubleSpinBox.setMinimumSize(QtCore.QSize(0, 26))
        self.doubleSpinBox.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                         "selection-color: rgb(237, 85, 59);\n"
                                         "selection-background-color: rgb(33, 57, 86);\n"
                                         "font: 12.5pt \"Garamond\";")
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.splitter_4, 4, 5, 2, 1)

        #spacerItem
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        #menubar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1489, 27))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)

        #statusBar
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setEnabled(True)
        self.statusBar.setAutoFillBackground(False)
        self.statusBar.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                     "color: rgb(255, 255, 255);")
        self.statusBar.setSizeGripEnabled(True)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionName_1 = QtWidgets.QAction(MainWindow)
        self.actionName_2 = QtWidgets.QAction(MainWindow)
        self.actionName_3 = QtWidgets.QAction(MainWindow)
        self.actionName_4 = QtWidgets.QAction(MainWindow)
        self.actionName_5 = QtWidgets.QAction(MainWindow)

        #sub_menu
        self.actionSave.setObjectName("actionSave")
        self.actionExit.setObjectName("actionExit")
        self.actionName_1.setObjectName("actionName_1")
        self.actionName_2.setObjectName("actionName_2")
        self.actionName_3.setObjectName("actionName_3")
        self.actionName_4.setObjectName("actionName_4")
        self.actionName_5.setObjectName("actionName_5")

        self.menuMenu.addAction(self.actionSave)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit)
        self.menuOptions.addAction(self.actionName_1)
        self.menuOptions.addAction(self.actionName_2)
        self.menuOptions.addAction(self.actionName_3)
        self.menuHelp.addAction(self.actionName_4)
        self.menuHelp.addAction(self.actionName_5)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.actionExit.triggered.connect(self.exit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PSS"))
        self.pushButton_1.setText(_translate("MainWindow", "SIMULATE"))
        self.pushButton_2.setText(_translate("MainWindow", "RESET"))
        self.radioButton_2.setText(_translate("MainWindow", "Flow"))
        self.radioButton_1.setText(_translate("MainWindow", "Pressure"))
        self.label_2.setText(_translate("MainWindow", "Peak Flow"))
        self.label_1.setText(_translate("MainWindow", "Heart Rate"))
        self.label_3.setText(_translate("MainWindow", "% Of Stenosis In Artery "))

        self.comboBox_1.setItemText(0, _translate("MainWindow", "Ascending aorta"))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "Aortic arch"))
        self.comboBox_1.setItemText(2, _translate("MainWindow", "Subclavian artery left"))
        self.comboBox_1.setItemText(3, _translate("MainWindow", "Subclavian artery right"))
        self.comboBox_1.setItemText(4, _translate("MainWindow", "Common carotid(L)"))
        self.comboBox_1.setItemText(5, _translate("MainWindow", "Common carotid(R)"))
        self.comboBox_1.setItemText(6, _translate("MainWindow", "Thoracic aorta"))
        self.comboBox_1.setItemText(7, _translate("MainWindow", "Cerebral artery right"))
        self.comboBox_1.setItemText(8, _translate("MainWindow", "Cerebral artery left"))
        self.comboBox_1.setItemText(9, _translate("MainWindow", "Abdominal aorta"))
        self.comboBox_1.setItemText(10, _translate("MainWindow", "Brachial artery right"))
        self.comboBox_1.setItemText(11, _translate("MainWindow", "Brachial artery left"))
        self.comboBox_1.setItemText(12, _translate("MainWindow", "Hepatic artery"))
        self.comboBox_1.setItemText(13, _translate("MainWindow", "Renal artery"))
        self.comboBox_1.setItemText(14, _translate("MainWindow", "Femoral artery left"))
        self.comboBox_1.setItemText(15, _translate("MainWindow", "Femoral artery right"))
        self.comboBox_1.setItemText(16, _translate("MainWindow", "Ulnar artery left"))
        self.comboBox_1.setItemText(17, _translate("MainWindow", "Ulnar artery right"))
        self.comboBox_1.setItemText(18, _translate("MainWindow", "Radial artery left"))
        self.comboBox_1.setItemText(19, _translate("MainWindow", "Radial artery right"))

        self.comboBox_2.setItemText(0, _translate("MainWindow", "Ascending aorta"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Aortic arch"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Subclavian artery left"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Subclavian artery right"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Common carotid(L)"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Common carotid(R)"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Thoracic aorta"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Cerebral artery right"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "Cerebral artery left"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "Abdominal aorta"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "Brachial artery right"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "Brachial artery left"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "Hepatic artery"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "Renal artery"))
        self.comboBox_2.setItemText(14, _translate("MainWindow", "Femoral artery left"))
        self.comboBox_2.setItemText(15, _translate("MainWindow", "Femoral artery right"))
        self.comboBox_2.setItemText(16, _translate("MainWindow", "Ulnar artery left"))
        self.comboBox_2.setItemText(17, _translate("MainWindow", "Ulnar artery right"))
        self.comboBox_2.setItemText(18, _translate("MainWindow", "Radial artery left"))
        self.comboBox_2.setItemText(19, _translate("MainWindow", "Radial artery right"))

        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Quit"))
        self.actionName_1.setText(_translate("MainWindow", "Name-1"))
        self.actionName_2.setText(_translate("MainWindow", "Name-2"))
        self.actionName_3.setText(_translate("MainWindow", "Name-2"))
        self.actionName_4.setText(_translate("MainWindow", "Name-1"))
        self.actionName_5.setText(_translate("MainWindow", "Name-2"))

    def plot(self):
        H = self.doubleSpinBox_2.value()              #read HR value
        P = self.doubleSpinBox_3.value()              #read P value
        S = self.doubleSpinBox.value()
        Index = self.comboBox_1.currentIndex()

        if Index==0:
            Pos = 0
            self.plot_p = 1
            self.plot_f = 0

        elif Index==1:
            Pos = 1
            self.plot_p = 3
            self.plot_f = 2

        elif Index==2:
            Pos = 7
            self.plot_p = 7
            self.plot_f = 6

        elif Index==3:
            Pos = 13
            self.plot_p = 31
            self.plot_f = 30

        elif Index==4:
            Pos = 3
            self.plot_p = 53
            self.plot_f = 52

        elif Index==5:
            Pos = 11
            self.plot_p = 83
            self.plot_f = 82

        elif Index==6:
            Pos = 10
            self.plot_p = 113
            self.plot_f = 112

        elif Index==7:
            Pos = 51
            self.plot_p = 103
            self.plot_f = 102

        elif Index==8:
            Pos = 46
            self.plot_p = 75
            self.plot_f = 74

        elif Index==9:
            Pos = 74
            self.plot_p = 123
            self.plot_f = 122

        elif Index==10:
            Pos = 56
            self.plot_p = 207
            self.plot_f = 206

        elif Index==11:
            Pos = 70
            self.plot_p = 211
            self.plot_f = 210

        elif Index==12:
            Pos = 62
            self.plot_p = 131
            self.plot_f = 130

        elif Index==13:
            Pos = 63
            self.plot_p = 133
            self.plot_f = 132

        elif Index==14:
            Pos = 108
            self.plot_p = 149
            self.plot_f = 148

        elif Index==15:
            Pos = 109
            self.plot_p = 181
            self.plot_f = 180

        elif Index==16:
            Pos = 102
            self.plot_p = 249
            self.plot_f = 248

        elif Index==17:
            Pos = 107
            self.plot_p = 253
            self.plot_f = 252

        elif Index == 18:
            Pos = 96
            self.plot_p = 251
            self.plot_f = 250

        elif Index == 19:
            Pos = 92
            self.plot_p = 245
            self.plot_f = 244

        print(Pos, S)
        stenosis.steno(Pos, S)

        self.clock, self.pulse = MAIN.cal(H, P)
        print(self.clock, self.pulse)
        self.c = np.all(self.clock != -1)
        self.p = np.all(self.pulse != -10000)
        if self.c and self.p:
            self.canvas_1.draw()
            self.figure.clear()
            self.radioButton_1.setChecked(True)
            mplstyle.use(['ggplot', 'fast'])

            plt.plot(self.clock, self.pulse[self.plot_p][:],'g', linewidth=1.0,)
            self.canvas_1.draw()
            self.statusBar.showMessage('PLOTTED', msecs=4000)
        else:
            self.alert("Invalid values...!!")

    def pressure_plot(self):
        self.canvas_1.draw()
        self.figure.clear()
        mplstyle.use(['ggplot', 'fast'])

        if self.c and self.p:
            plt.plot(self.clock, self.pulse[self.plot_p][:],'g', linewidth=1.0,)
            self.canvas_1.draw()
            self.statusBar.showMessage('PLOTTED', msecs=3000)
        else:
            self.alert("Invalid values...!!")

    def flow_plot(self):
        self.canvas_1.draw()
        self.figure.clear()
        mplstyle.use(['ggplot', 'fast'])

        if self.c and self.p:
            plt.plot(self.clock, self.pulse[self.plot_f][:], 'b', linewidth=1.0,)
            self.canvas_1.draw()
            self.statusBar.showMessage('PLOTTED', msecs=3000)
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
        MainWindow.close()

    def viewing(self):

        print('viewing called')
        Index = self.comboBox_2.currentIndex()
        if Index==0:
            Pos = 0
            self.plot_p = 1
            self.plot_f = 0

            if self.radioButton_1.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_p][:], 'r', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)
            elif self.radioButton_2.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_f][:], 'b', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)

        elif Index==1:
            Pos = 1
            self.plot_p = 3
            self.plot_f = 2
            if self.radioButton_1.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_p][:], 'r', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)
            elif self.radioButton_2.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_f][:], 'b', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)

        elif Index==2:
            Pos = 7
            self.plot_p = 7
            self.plot_f = 6
            if self.radioButton_1.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_p][:], 'r', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)
            elif self.radioButton_2.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_f][:], 'b', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)

        elif Index==3:
            Pos = 13
            self.plot_p = 31
            self.plot_f = 30
            if self.radioButton_1.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_p][:], 'r', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)
            elif self.radioButton_2.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_f][:], 'b', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)

        elif Index==4:
            Pos = 3
            self.plot_p = 53
            self.plot_f = 52
            if self.radioButton_1.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_p][:], 'r', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)
            elif self.radioButton_2.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_f][:], 'b', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)

        elif Index==5:
            Pos = 11
            self.plot_p = 83
            self.plot_f = 82
            if self.radioButton_1.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_p][:], 'r', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)
            elif self.radioButton_2.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_f][:], 'b', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)

        elif Index==6:
            Pos = 10
            self.plot_p = 113
            self.plot_f = 112
            if self.radioButton_1.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_p][:], 'r', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)
            elif self.radioButton_2.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_f][:], 'b', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)

        elif Index==7:
            Pos = 51
            self.plot_p = 103
            self.plot_f = 102
            if self.radioButton_1.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_p][:], 'r', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)
            elif self.radioButton_2.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_f][:], 'b', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)

        elif Index==8:
            Pos = 46
            self.plot_p = 75
            self.plot_f = 74
            if self.radioButton_1.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_p][:], 'r', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)
            elif self.radioButton_2.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_f][:], 'b', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)

        elif Index==9:
            Pos = 74
            self.plot_p = 123
            self.plot_f = 122
            if self.radioButton_1.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_p][:], 'r', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)
            elif self.radioButton_2.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_f][:], 'b', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)

        elif Index==10:
            Pos = 56
            self.plot_p = 207
            self.plot_f = 206
            if self.radioButton_1.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_p][:], 'r', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)
            elif self.radioButton_2.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_f][:], 'b', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)

        elif Index==11:
            Pos = 70
            self.plot_p = 211
            self.plot_f = 210
            if self.radioButton_1.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_p][:], 'r', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)
            elif self.radioButton_2.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_f][:], 'b', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)

        elif Index==12:
            Pos = 62
            self.plot_p = 131
            self.plot_f = 130
            if self.radioButton_1.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_p][:], 'r', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)
            elif self.radioButton_2.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_f][:], 'b', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)

        elif Index==13:
            Pos = 63
            self.plot_p = 133
            self.plot_f = 132
            if self.radioButton_1.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_p][:], 'r', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)
            elif self.radioButton_2.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_f][:], 'b', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)

        elif Index==14:
            Pos = 108
            self.plot_p = 149
            self.plot_f = 148
            if self.radioButton_1.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_p][:], 'r', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)
            elif self.radioButton_2.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_f][:], 'b', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)

        elif Index==15:
            Pos = 109
            self.plot_p = 181
            self.plot_f = 180
            if self.radioButton_1.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_p][:], 'r', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)
            elif self.radioButton_2.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_f][:], 'b', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)

        elif Index==16:
            Pos = 102
            self.plot_p = 249
            self.plot_f = 248
            if self.radioButton_1.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_p][:], 'r', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)
            elif self.radioButton_2.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_f][:], 'b', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)

        elif Index==17:
            Pos = 107
            self.plot_p = 253
            self.plot_f = 252
            if self.radioButton_1.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_p][:], 'r', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)
            elif self.radioButton_2.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_f][:], 'b', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)

        elif Index == 18:
            Pos = 96
            self.plot_p = 251
            self.plot_f = 250
            if self.radioButton_1.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_p][:], 'r', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)
            elif self.radioButton_2.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_f][:], 'b', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)

        elif Index == 19:
            Pos = 92
            self.plot_p = 245
            self.plot_f = 244
            if self.radioButton_1.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_p][:], 'r', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)
            elif self.radioButton_2.isChecked():
                self.canvas_1.draw()
                self.figure.clear()
                mplstyle.use(['ggplot', 'fast'])
                plt.plot(self.clock, self.pulse[self.plot_f][:], 'b', linewidth=1.0, )
                self.canvas_1.draw()
                self.statusBar.showMessage('PLOTTED', msecs=3000)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())