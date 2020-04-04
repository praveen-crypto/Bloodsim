from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import MAIN2
import numpy as np
import STENOSIS

class Ui_MainWindow(object):
    def __init__(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.gridLayout_9 = QtWidgets.QGridLayout(self.centralwidget)
        self.widget_1 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)

        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.comboBox_G2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_G1 = QtWidgets.QComboBox(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.dockWidget_1 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetContents_1 = QtWidgets.QWidget()
        #self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents_1)
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents_1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.dockWidgetContents_1)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.groupBox_2)

        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_2)

        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)

        self.groupBox_1 = QtWidgets.QGroupBox(self.dockWidgetContents_1)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_1)
        self.checkBox_1 = QtWidgets.QCheckBox(self.groupBox_1)
        self.doubleSpinBox_1 = QtWidgets.QDoubleSpinBox(self.groupBox_1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox_1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_1)
        self.comboBox_1 = QtWidgets.QComboBox(self.groupBox_1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_1)
        self.label_1 = QtWidgets.QLabel(self.groupBox_1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.groupBox_1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_1)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_1)

        self.dockWidget_2 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetContents_5 = QtWidgets.QWidget()
        self.gridLayout_4 = QtWidgets.QGridLayout(self.dockWidgetContents_5)
        self.groupBox_3 = QtWidgets.QGroupBox(self.dockWidgetContents_5)
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_3)
        self.textEdit_1 = QtWidgets.QTextEdit(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.dockWidgetContents_5)
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_4)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1143, 685)
        MainWindow.setMinimumSize(QtCore.QSize(259, 0))
        MainWindow.setStyleSheet("color: rgb(255, 210, 119);\n"
                                 "gridline-color: rgb(33, 57, 86);\n"
                                 "background-color: rgb(46, 80, 120);\n"
                                 "selection-color: rgb(237, 85, 59);\n"
                                 "\n"
                                 "selection-background-color: rgb(33, 57, 86);")
        MainWindow.setDockOptions(
            QtWidgets.QMainWindow.AllowNestedDocks | QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks | QtWidgets.QMainWindow.ForceTabbedDocks | QtWidgets.QMainWindow.VerticalTabs)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_9.setObjectName("gridLayout_9")

####GRAPH_WIDGET - 1 ======================================================================================================
        #GRAPH
        self.graphWidget_1 = pg.PlotWidget()
        self.graphWidget_1.setBackground('#213956')
        self.graphWidget_1.setAntialiasing(True)
        labelStyle = {'color': '#ED553B', 'font-size': '9pt'}
        self.graphWidget_1.setLabel('left', text='x axis' , **labelStyle )
        self.graphWidget_1.setLabel('bottom', text='y axis',**labelStyle )

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_1.sizePolicy().hasHeightForWidth())
        self.graphWidget_1.setSizePolicy(sizePolicy)
        self.graphWidget_1.setMinimumSize(QtCore.QSize(0, 0))
        self.graphWidget_1.setObjectName("widget_1")
        self.gridLayout_9.addWidget(self.graphWidget_1, 1, 0, 1, 3)


#####GRAPH_WIDGET - 2 ======================================================================================================
        #GRAPH-2
        self.graphWidget_2 = pg.PlotWidget()
        self.graphWidget_2.setBackground('#213956')
        self.graphWidget_2.setAntialiasing(True)
        labelStyle = {'color': '#ED553B', 'font-size': '9pt'}
        self.graphWidget_2.setLabel('left', text='x axis', **labelStyle)
        self.graphWidget_2.setLabel('bottom', text='y axis', **labelStyle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.graphWidget_2.setSizePolicy(sizePolicy)
        self.graphWidget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.graphWidget_2.setSizeIncrement(QtCore.QSize(5, 5))
        self.graphWidget_2.setObjectName("widget_2")
        self.gridLayout_9.addWidget(self.graphWidget_2, 3, 0, 1, 3)



####SECOND GRAPH=====================================================================================================
        #ComboBox_G2
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.comboBox_G2.sizePolicy().hasHeightForWidth())
        self.comboBox_G2.setSizePolicy(sizePolicy)
        self.comboBox_G2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
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
        self.comboBox_G2.setFrame(False)
        self.comboBox_G2.setObjectName("comboBox_G2")
        for i in range(20):
            self.comboBox_G2.addItem("")
        self.gridLayout_9.addWidget(self.comboBox_G2, 2, 0, 1, 1)
        self.comboBox_G2.currentIndexChanged.connect(self.mainViewer_2)

        # Radiobutton_3
        # self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.radioButton_3.sizePolicy().hasHeightForWidth())
        self.radioButton_3.setSizePolicy(sizePolicy)
        self.radioButton_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup_2.addButton(self.radioButton_3)
        self.gridLayout_9.addWidget(self.radioButton_3, 2, 1, 1, 1)
        self.radioButton_3.clicked.connect(self.pressure_plot_2)

        #RadioButton_4
        #self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_4.setObjectName("radioButton_4")
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_4)
        self.gridLayout_9.addWidget(self.radioButton_4, 2, 2, 1, 1)
        self.radioButton_4.clicked.connect(self.flow_plot_2)

#####GRAPH -1 =================================================================================
        #comboBox_G1
        #self.comboBox_G1 = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.comboBox_G1.sizePolicy().hasHeightForWidth())
        self.comboBox_G1.setSizePolicy(sizePolicy)
        self.comboBox_G1.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                       "background-color: rgb(35, 35, 35);\n"
                                       "color: rgb(255, 210, 119);\n"
                                       "selection-color: rgb(237, 85, 59);\n"
                                       "\n"
                                       "selection-background-color: rgb(33, 57, 86);\n"
                                       "gridline-color: rgb(255, 255, 255);\n"
                                       "")
        self.comboBox_G1.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_G1.setFrame(False)
        self.comboBox_G1.setObjectName("comboBox_G1")
        for i in range(20):
            self.comboBox_G1.addItem("")
        self.gridLayout_9.addWidget(self.comboBox_G1, 0, 0, 1, 1)
        self.comboBox_G1.currentIndexChanged.connect(self.mainViewer_1)

        # radioButton_1
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.radioButton_1.sizePolicy().hasHeightForWidth())
        self.radioButton_1.setSizePolicy(sizePolicy)
        self.radioButton_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_1.setChecked(True)
        self.radioButton_1.setObjectName("radioButton_1")
        self.buttonGroup.addButton(self.radioButton_1)
        self.gridLayout_9.addWidget(self.radioButton_1, 0, 1, 1, 1)
        self.radioButton_1.clicked.connect(self.pressure_plot_1)

        # radioButton_2
        # self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setStyleSheet(  "color: rgb(255, 255, 255);")
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_2)
        self.gridLayout_9.addWidget(self.radioButton_2, 0, 2, 1, 1)
        self.radioButton_2.clicked.connect(self.flow_plot_1)

#####LEFT SIDE DOCK WIDGET====================================================================================
        #DockWidget_1

        self.dockWidget_1.setMinimumSize(QtCore.QSize(366, 534))
        self.dockWidget_1.setMouseTracking(True)
        self.dockWidget_1.setFloating(False)
        self.dockWidget_1.setFeatures(
            QtWidgets.QDockWidget.DockWidgetFloatable | QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget_1.setObjectName("dockWidget_1")

        self.dockWidgetContents_1.setObjectName("dockWidgetContents_1")
        self.gridLayout.setObjectName("gridLayout")

       # LEFTSIDE SECOND GroupBox========================================================================================

       #GroupBox_2
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(331, 251))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")

        #gridLayout_2
        self.gridLayout_2.setObjectName("gridLayout_2")

        #label_9
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_9.setStyleSheet("background-color: rgb(32, 99, 155);\n"
                                   "font: 9pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 3, 1, 1)

        #doublePsinBox_5
        self.doubleSpinBox_5.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_5.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_5.setSizePolicy(sizePolicy)
        self.doubleSpinBox_5.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                           "selection-color: rgb(237, 85, 59);\n"
                                           "selection-background-color: rgb(33, 57, 86);\n"
                                           "\n"
                                           "font: 11pt \"Calibri\";")
        self.doubleSpinBox_5.setProperty("showGroupSeparator", False)
        self.doubleSpinBox_5.setDecimals(3)
        self.doubleSpinBox_5.setMinimum(1.05)
        self.doubleSpinBox_5.setMaximum(3.00)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout_2.addWidget(self.doubleSpinBox_5, 2, 3, 1, 1)

        #doubleSpinBox_6
        self.doubleSpinBox_6.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_6.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_6.setSizePolicy(sizePolicy)
        self.doubleSpinBox_6.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                           "selection-color: rgb(237, 85, 59);\n"
                                           "selection-background-color: rgb(33, 57, 86);\n"
                                           "\n"
                                           "font: 11pt \"Calibri\";")
        self.doubleSpinBox_6.setProperty("showGroupSeparator", False)
        self.doubleSpinBox_6.setDecimals(3)
        self.doubleSpinBox_6.setMinimum(0.6)
        self.doubleSpinBox_6.setMaximum(3.0)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.gridLayout_2.addWidget(self.doubleSpinBox_6, 3, 3, 1, 1)



        #doubleSpinBox_4
        self.doubleSpinBox_4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_4.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_4.setSizePolicy(sizePolicy)
        self.doubleSpinBox_4.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                           "selection-color: rgb(237, 85, 59);\n"
                                           "selection-background-color: rgb(33, 57, 86);\n"
                                           "\n"
                                           "font: 11pt \"Calibri\";")
        self.doubleSpinBox_4.setProperty("showGroupSeparator", False)
        self.doubleSpinBox_4.setDecimals(3)
        self.doubleSpinBox_4.setMinimum(0.04)
        self.doubleSpinBox_4.setMaximum(3.00)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout_2.addWidget(self.doubleSpinBox_4, 1, 3, 1, 1)

        #checkBox_3
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)
        self.checkBox_3.setText("")
        self.checkBox_3.setChecked(False)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_2.addWidget(self.checkBox_3, 1, 2, 1, 1)
        self.checkBox_3.clicked.connect(self.enable)

        #checkBox_4
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy)
        self.checkBox_4.setText("")
        self.checkBox_4.setChecked(False)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_2.addWidget(self.checkBox_4, 2, 2, 1, 1)
        self.checkBox_4.clicked.connect(self.enable)

        #checkBox_5
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy)
        self.checkBox_5.setText("")
        self.checkBox_5.setChecked(False)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_2.addWidget(self.checkBox_5, 3, 2, 1, 1)
        self.checkBox_5.clicked.connect(self.enable)

        #label_10
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(255,255,255);")
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 2)

        #label_11
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(255,255,255);")
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 2)

        #label_8
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_8.setStyleSheet("background-color: rgb(32, 99, 155);\n"
                                   "font: 9pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 2)

        #label_12
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(255,255,255);")
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 3, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)

###LEFTSIDE FIRST BOX========================================================================================
        #groupBox_1
        self.groupBox_1.setTitle("")
        self.groupBox_1.setFlat(True)
        self.groupBox_1.setObjectName("groupBox_1")

        #gridLayout_3
        self.gridLayout_3.setObjectName("gridLayout_3")

        #checkBox_1
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_1.sizePolicy().hasHeightForWidth())
        self.checkBox_1.setSizePolicy(sizePolicy)
        self.checkBox_1.setText("")
        self.checkBox_1.setChecked(False)
        self.checkBox_1.setObjectName("checkBox_1")
        self.gridLayout_3.addWidget(self.checkBox_1, 1, 2, 1, 1)
        self.checkBox_1.clicked.connect(self.enable)

        #doubleSpinBox_1
        self.doubleSpinBox_1.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_1.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_1.setSizePolicy(sizePolicy)
        self.doubleSpinBox_1.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                           "selection-color: rgb(237, 85, 59);\n"
                                           "selection-background-color: rgb(33, 57, 86);\n"
                                           "\n"
                                           "font: 11pt \"Calibri\";")
        self.doubleSpinBox_1.setProperty("showGroupSeparator", False)
        self.doubleSpinBox_1.setDecimals(0)
        self.doubleSpinBox_1.setMinimum(72.0)
        self.doubleSpinBox_1.setMaximum(150.0)
        self.doubleSpinBox_1.setObjectName("doubleSpinBox_1")
        self.gridLayout_3.addWidget(self.doubleSpinBox_1, 1, 3, 1, 1)

        #doubleSpinBox_2
        self.doubleSpinBox_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_2.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_2.setSizePolicy(sizePolicy)
        self.doubleSpinBox_2.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                           "selection-color: rgb(237, 85, 59);\n"
                                           "selection-background-color: rgb(33, 57, 86);\n"
                                           "\n"
                                           "font: 11pt \"Calibri\";")
        self.doubleSpinBox_2.setProperty("showGroupSeparator", False)
        self.doubleSpinBox_2.setDecimals(0)
        self.doubleSpinBox_2.setMinimum(450.0)
        self.doubleSpinBox_2.setMaximum(600.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout_3.addWidget(self.doubleSpinBox_2, 2, 3, 1, 1)

        #label_6
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(255,255,255);")
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 4, 0, 1, 2)

        #comboBox_1
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.comboBox_1.sizePolicy().hasHeightForWidth())
        self.comboBox_1.setSizePolicy(sizePolicy)
        self.comboBox_1.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                      "\n"
                                      "selection-color: rgb(237, 85, 59);\n"
                                      "selection-background-color: rgb(33, 57, 86);\n"
                                      "color: rgb(255, 210, 119);\n"
                                      "border-color: rgb(255, 255, 255);\n"
                                      "gridline-color: rgb(255, 255, 255);\n"
                                      "font: 10pt \"MS Shell Dlg 2\";")
        self.comboBox_1.setFrame(False)
        self.comboBox_1.setObjectName("comboBox_1")
        for i in range(20):
            self.comboBox_1.addItem("")
        self.comboBox_1.currentIndexChanged.connect(self.val)




        self.gridLayout_3.addWidget(self.comboBox_1, 4, 3, 1, 1)

        #label_7
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(255,255,255);")
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 5, 0, 1, 1)

        #label_1
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_1.setStyleSheet("background-color: rgb(32, 99, 155);\n"
                                   "font: 9pt \"MS Shell Dlg 2\";")
        self.label_1.setObjectName("label_1")
        self.gridLayout_3.addWidget(self.label_1, 0, 0, 1, 2)

        #doubleSpinBox_3
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_3.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_3.setSizePolicy(sizePolicy)
        self.doubleSpinBox_3.setMinimumSize(QtCore.QSize(0, 26))
        self.doubleSpinBox_3.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                           "selection-color: rgb(237, 85, 59);\n"
                                           "selection-background-color: rgb(33, 57, 86);\n"
                                           "font: 12.5pt \"Garamond\";")
        self.doubleSpinBox_3.setDecimals(0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout_3.addWidget(self.doubleSpinBox_3, 6, 3, 1, 1)

        #label_2
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_2.setStyleSheet("background-color: rgb(32, 99, 155);\n"
                                   "font: 9pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 3, 1, 1)

        #label_4
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(255,255,255);")
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)

        #comboBox_2
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                      "\n"
                                      "selection-color: rgb(237, 85, 59);\n"
                                      "selection-background-color: rgb(33, 57, 86);\n"
                                      "color: rgb(255, 210, 119);\n"
                                      "border-color: rgb(255, 255, 255);\n"
                                      "gridline-color: rgb(255, 255, 255);\n"
                                      "font: 10pt \"MS Shell Dlg 2\";")
        self.comboBox_2.setFrame(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("1")
        '''for i in range(20):
            self.comboBox_2.addItem("")
        '''

        self.gridLayout_3.addWidget(self.comboBox_2, 5, 3, 1, 1)

        #label_3
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(255,255,255);")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        #comboBox_3
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                      "\n"
                                      "selection-color: rgb(237, 85, 59);\n"
                                      "selection-background-color: rgb(33, 57, 86);\n"
                                      "color: rgb(255, 210, 119);\n"
                                      "border-color: rgb(255, 255, 255);\n"
                                      "gridline-color: rgb(255, 255, 255);\n"
                                      "font: 10pt \"MS Shell Dlg 2\";")
        self.comboBox_3.setFrame(False)
        self.comboBox_3.setObjectName("comboBox_3")
        for i in range(20):
            self.comboBox_3.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_3, 6, 0, 1, 1)

        #label_5
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet("background-color: rgb(32, 99, 155);\n"
                                   "font: 9pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)

        #checkBox_2
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)
        self.checkBox_2.setText("")
        self.checkBox_2.setChecked(False)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_3.addWidget(self.checkBox_2, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox_1, 0, 0, 1, 1)
        self.dockWidget_1.setWidget(self.dockWidgetContents_1)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_1)
        self.checkBox_2.clicked.connect(self.enable)

        #dockWidget_2
        self.dockWidget_2.setMinimumSize(QtCore.QSize(250, 487))
        self.dockWidget_2.setObjectName("dockWidget_2")

        #dockWidgetContents_5
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")

        #gridLayout_4
        self.gridLayout_4.setObjectName("gridLayout_4")

        #groupBox_3
        self.groupBox_3.setMinimumSize(QtCore.QSize(221, 191))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName("groupBox_3")

        #gridLayout_8
        self.gridLayout_8.setObjectName("gridLayout_8")

        #textEdit_1
        self.textEdit_1.setStyleSheet("background-color: rgb(33, 57, 86);")
        self.textEdit_1.setObjectName("textEdit")
        self.gridLayout_8.addWidget(self.textEdit_1, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 0, 0, 1, 1)

        #groupBox_4
        self.groupBox_4.setMinimumSize(QtCore.QSize(221, 241))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")

        #textEdit_2
        self.textEdit_2.setStyleSheet("background-color: rgb(33, 57, 86);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_5.addWidget(self.textEdit_2, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.dockWidget_2.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_2)

        # Menubar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1143, 26))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuMenu")

        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuOptions")

        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuHelp")

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp_2")
        MainWindow.setMenuBar(self.menubar)

        # Statusbar
        self.statusbar.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                     "color: rgb(255, 210, 119);")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #Action_Declaration
        self.actionRun = QtWidgets.QAction(MainWindow)
        self.actionRun.setObjectName("actionRUN")

        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setObjectName("actionSTOP")

        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionQuit")

        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit_2")

        self.actionIp = QtWidgets.QAction(MainWindow)
        self.actionIp.setObjectName("actionView")

        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")

        self.actionReset_2 = QtWidgets.QAction(MainWindow)
        self.actionReset_2.setObjectName("actionReset_2")

        self.actionWaveform = QtWidgets.QAction(MainWindow)
        self.actionWaveform.setObjectName("actionWaveform")

        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.actionBloodsim = QtWidgets.QAction(MainWindow)
        self.actionBloodsim.setObjectName("actionBloodsim")

        self.actionAbout_Bloodsim = QtWidgets.QAction(MainWindow)
        self.actionAbout_Bloodsim.setObjectName("actionAbout_Bloodsim")

        self.actionHeart_Parameter = QtWidgets.QAction(MainWindow)
        self.actionHeart_Parameter.setObjectName("actionHeart_Parameter")

        #Action_Adding
        self.menuFile.addAction(self.actionClear)
        self.menuFile.addAction(self.actionReset_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)

        self.menuView.addAction(self.actionIp)
        self.menuView.addAction(self.actionWaveform)
        self.menuView.addAction(self.actionHeart_Parameter)
        self.actionIp.setCheckable(True)
        self.actionWaveform.setCheckable(True)
        self.actionIp.setChecked(True)
        self.actionWaveform.setChecked(True)
        self.actionHeart_Parameter.setCheckable(True)
        self.actionHeart_Parameter.setChecked(True)

        self.menuRun.addAction(self.actionRun)
        self.menuRun.addSeparator()
        self.menuRun.addAction(self.actionStop)
        self.menuRun.addSeparator()
        self.menuRun.addAction(self.actionReset)

        self.menuHelp.addAction(self.actionBloodsim)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Bloodsim)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        #MenuTrigger
         #FileMenu_trigger
        self.actionClear.triggered.connect(self.reset)
        self.actionReset_2.triggered.connect(self.reset)
        self.actionQuit.triggered.connect(self.exit)

        #ViewMenu_trigger
        self.actionIp.triggered.connect(self.showDock_1)
        self.actionWaveform.triggered.connect(self.showDock_2)

        #RunMenu_trigger
        self.actionRun.triggered.connect(self.plot)
        self.actionReset.triggered.connect(self.reset)
        #HelpMenu_trigger
        self.actionBloodsim.triggered.connect(self.about)
        #self.actionAbout_Bloodsim.triggered.connect(self.about)

        #setBuddy
        self.label_10.setBuddy(self.checkBox_3)
        self.label_11.setBuddy(self.checkBox_4)
        self.label_12.setBuddy(self.checkBox_5)
        self.label_6.setBuddy(self.comboBox_1)
        self.label_7.setBuddy(self.comboBox_2)
        self.label_4.setBuddy(self.checkBox_2)
        self.label_3.setBuddy(self.checkBox_1)

        #TabOrder
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.comboBox_G1, self.radioButton_1)
        MainWindow.setTabOrder(self.radioButton_1, self.radioButton_2)
        MainWindow.setTabOrder(self.radioButton_2, self.radioButton_3)
        MainWindow.setTabOrder(self.radioButton_3, self.radioButton_4)
        MainWindow.setTabOrder(self.radioButton_4, self.checkBox_1)
        MainWindow.setTabOrder(self.checkBox_1, self.doubleSpinBox_1)
        MainWindow.setTabOrder(self.doubleSpinBox_1, self.checkBox_2)
        MainWindow.setTabOrder(self.checkBox_2, self.doubleSpinBox_2)
        MainWindow.setTabOrder(self.doubleSpinBox_2, self.comboBox_1)
        MainWindow.setTabOrder(self.comboBox_1, self.comboBox_2)
        MainWindow.setTabOrder(self.comboBox_2, self.doubleSpinBox_3)
        MainWindow.setTabOrder(self.doubleSpinBox_3, self.comboBox_G2)
        MainWindow.setTabOrder(self.comboBox_G2, self.comboBox_3)
        MainWindow.setTabOrder(self.comboBox_3, self.checkBox_3)
        MainWindow.setTabOrder(self.checkBox_3, self.doubleSpinBox_4)
        MainWindow.setTabOrder(self.doubleSpinBox_4, self.checkBox_4)
        MainWindow.setTabOrder(self.checkBox_4, self.doubleSpinBox_5)
        MainWindow.setTabOrder(self.doubleSpinBox_5, self.checkBox_5)
        MainWindow.setTabOrder(self.checkBox_5, self.doubleSpinBox_6)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bloodsim"))
        self.radioButton_2.setText(_translate("MainWindow", "Flow"))

        self.radioButton_4.setText(_translate("MainWindow", "Flow"))
        self.radioButton_3.setText(_translate("MainWindow", "Pressure"))
        self.radioButton_1.setText(_translate("MainWindow", "Pressure"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.dockWidget_1.setWindowTitle(_translate("MainWindow", "Input Parameters"))
        self.label_9.setText(_translate("MainWindow", "Value"))
        self.label_10.setText(_translate("MainWindow", "Blood viscosity"))
        self.label_11.setText(_translate("MainWindow", "Blood density"))
        self.label_8.setText(_translate("MainWindow", "Property"))
        self.label_12.setText(_translate("MainWindow", "Reflection Coefficient"))
        self.label_6.setText(_translate("MainWindow", "Number of Arteries"))
        self.label_7.setText(_translate("MainWindow", "Select Artery"))
        self.label_1.setText(_translate("MainWindow", "Property"))
        self.label_2.setText(_translate("MainWindow", "Value"))
        self.label_4.setText(_translate("MainWindow", "Peak Flow"))
        self.label_3.setText(_translate("MainWindow", "Heart Rate"))
        self.label_5.setText(_translate("MainWindow", "Stenosis"))

        self.comboBox_G1.setItemText(0, _translate("MainWindow", "Ascending aorta"))
        self.comboBox_G1.setItemText(1, _translate("MainWindow", "Aortic arch"))
        self.comboBox_G1.setItemText(2, _translate("MainWindow", "Subclavian artery left"))
        self.comboBox_G1.setItemText(3, _translate("MainWindow", "Subclavian artery right"))
        self.comboBox_G1.setItemText(4, _translate("MainWindow", "Common carotid(L)"))
        self.comboBox_G1.setItemText(5, _translate("MainWindow", "Common carotid(R)"))
        self.comboBox_G1.setItemText(6, _translate("MainWindow", "Thoracic aorta"))
        self.comboBox_G1.setItemText(7, _translate("MainWindow", "Cerebral artery right"))
        self.comboBox_G1.setItemText(8, _translate("MainWindow", "Cerebral artey left"))
        self.comboBox_G1.setItemText(9, _translate("MainWindow", "Abdominal aorta"))
        self.comboBox_G1.setItemText(10, _translate("MainWindow", "Brachial Artery Right"))
        self.comboBox_G1.setItemText(11, _translate("MainWindow", "Brachial Artery Left"))
        self.comboBox_G1.setItemText(12, _translate("MainWindow", "Hepatic artery"))
        self.comboBox_G1.setItemText(13, _translate("MainWindow", "Renal Artery"))
        self.comboBox_G1.setItemText(14, _translate("MainWindow", "Femoral Artery Left"))
        self.comboBox_G1.setItemText(15, _translate("MainWindow", "Femoral Artery Right"))
        self.comboBox_G1.setItemText(16, _translate("MainWindow", "Ulnar artery left"))
        self.comboBox_G1.setItemText(17, _translate("MainWindow", "Ulnar artery right"))
        self.comboBox_G1.setItemText(18, _translate("MainWindow", "Radial Artery Left"))
        self.comboBox_G1.setItemText(19, _translate("MainWindow", "Radial Artery Right"))

        self.comboBox_G2.setItemText(0, _translate("MainWindow", "Ascending aorta"))
        self.comboBox_G2.setItemText(1, _translate("MainWindow", "Aortic arch"))
        self.comboBox_G2.setItemText(2, _translate("MainWindow", "Subclavian artery left"))
        self.comboBox_G2.setItemText(3, _translate("MainWindow", "Subclavian artery right"))
        self.comboBox_G2.setItemText(4, _translate("MainWindow", "Common carotid(L)"))
        self.comboBox_G2.setItemText(5, _translate("MainWindow", "Common carotid(R)"))
        self.comboBox_G2.setItemText(6, _translate("MainWindow", "Thoracic aorta"))
        self.comboBox_G2.setItemText(7, _translate("MainWindow", "Cerebral artery right"))
        self.comboBox_G2.setItemText(8, _translate("MainWindow", "Cerebral artey left"))
        self.comboBox_G2.setItemText(9, _translate("MainWindow", "Abdominal aorta"))
        self.comboBox_G2.setItemText(10, _translate("MainWindow", "Brachial Artery Right"))
        self.comboBox_G2.setItemText(11, _translate("MainWindow", "Brachial Artery Left"))
        self.comboBox_G2.setItemText(12, _translate("MainWindow", "Hepatic artery"))
        self.comboBox_G2.setItemText(13, _translate("MainWindow", "Renal Artery"))
        self.comboBox_G2.setItemText(14, _translate("MainWindow", "Femoral Artery Left"))
        self.comboBox_G2.setItemText(15, _translate("MainWindow", "Femoral Artery Right"))
        self.comboBox_G2.setItemText(16, _translate("MainWindow", "Ulnar artery left"))
        self.comboBox_G2.setItemText(17, _translate("MainWindow", "Ulnar artery right"))
        self.comboBox_G2.setItemText(18, _translate("MainWindow", "Radial Artery Left"))
        self.comboBox_G2.setItemText(19, _translate("MainWindow", "Radial Artery Right"))

        self.comboBox_1.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_1.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_1.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_1.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_1.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox_1.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox_1.setItemText(7, _translate("MainWindow", "8"))
        self.comboBox_1.setItemText(8, _translate("MainWindow", "9"))
        self.comboBox_1.setItemText(9, _translate("MainWindow", "10"))
        self.comboBox_1.setItemText(10, _translate("MainWindow", "11"))
        self.comboBox_1.setItemText(11, _translate("MainWindow", "12"))
        self.comboBox_1.setItemText(12, _translate("MainWindow", "13"))
        self.comboBox_1.setItemText(13, _translate("MainWindow", "14"))
        self.comboBox_1.setItemText(14, _translate("MainWindow", "15"))
        self.comboBox_1.setItemText(15, _translate("MainWindow", "16"))
        self.comboBox_1.setItemText(16, _translate("MainWindow", "17"))
        self.comboBox_1.setItemText(17, _translate("MainWindow", "18"))
        self.comboBox_1.setItemText(18, _translate("MainWindow", "19"))
        self.comboBox_1.setItemText(19, _translate("MainWindow", "20"))

        self.comboBox_3.setItemText(0, _translate("MainWindow", "Ascending aorta"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Aortic arch"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Subclavian artery left"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Subclavian artery right"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Common carotid(L)"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "Common carotid(R)"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "Thoracic aorta"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "Cerebral artery right"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "Cerebral artery left"))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "Abdominal aorta"))
        self.comboBox_3.setItemText(10, _translate("MainWindow", "Brachial artery right"))
        self.comboBox_3.setItemText(11, _translate("MainWindow", "Brachial artery left"))
        self.comboBox_3.setItemText(12, _translate("MainWindow", "Hepatic artery"))
        self.comboBox_3.setItemText(13, _translate("MainWindow", "Renal artery"))
        self.comboBox_3.setItemText(14, _translate("MainWindow", "Femoral artery left"))
        self.comboBox_3.setItemText(15, _translate("MainWindow", "Femoral artery right"))
        self.comboBox_3.setItemText(16, _translate("MainWindow", "Ulnar artery left"))
        self.comboBox_3.setItemText(17, _translate("MainWindow", "Ulnar artery right"))
        self.comboBox_3.setItemText(18, _translate("MainWindow", "Radial artery left"))
        self.comboBox_3.setItemText(19, _translate("MainWindow", "Radial artery right"))

        self.dockWidget_2.setWindowTitle(_translate("MainWindow", "Information"))

        self.actionRun.setText(_translate("MainWindow", "Run.."))
        self.actionStop.setText(_translate("MainWindow", "Stop"))

        self.actionClear.setText(_translate("MainWindow", "Clear"))

        self.actionIp.setText(_translate("MainWindow", "Input Parmeters"))
        self.actionWaveform.setText(_translate("MainWindow", "Information"))
        self.actionHeart_Parameter.setText(_translate("MainWindow", "Heart Parameter"))

        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionReset_2.setText(_translate("MainWindow", "Reset"))

        self.actionQuit.setText(_translate("MainWindow", "Quit"))

        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionBloodsim.setText(_translate("MainWindow", "Bloodsim Help"))
        self.actionAbout_Bloodsim.setText(_translate("MainWindow", "About Bloodsim"))

    def val(self):
        data = self.comboBox_1.currentIndex()
        data = int(data)
        self.comboBox_2.clear()
        for i in range(data+1):
            j = i + 1
            j = str(j)
            self.comboBox_2.addItem(j)

    def enable(self):
        if self.checkBox_1.isChecked() == True:
            self.doubleSpinBox_1.setEnabled(True)
        else:
            self.doubleSpinBox_1.setEnabled(False)

        if self.checkBox_2.isChecked() == True:
            self.doubleSpinBox_2.setEnabled(True)
        else:
            self.doubleSpinBox_2.setEnabled(False)

        if self.checkBox_3.isChecked() == True:
            self.doubleSpinBox_4.setEnabled(True)
        else:
            self.doubleSpinBox_4.setEnabled(False)

        if self.checkBox_4.isChecked() == True:
            self.doubleSpinBox_5.setEnabled(True)
        else:
            self.doubleSpinBox_5.setEnabled(False)
        if self.checkBox_5.isChecked() == True:
            self.doubleSpinBox_6.setEnabled(True)
        else:
            self.doubleSpinBox_6.setEnabled(False)

    def exit(self):
        MainWindow.close()

    def showDock_1(self):
        if self.actionIp.isChecked() == True:
            self.dockWidget_1.show()

        if self.actionIp.isChecked() == False:
            self.dockWidget_1.hide()

    def showDock_2(self):
        if self.actionWaveform.isChecked() == True:
            self.dockWidget_2.show()

        if self.actionWaveform.isChecked() == False:
            self.dockWidget_2.hide()

    def plot(self):
        #t = np.arange(0.0,2.0,0.02)
        #x = np.sin(2*3.14*t)
        H = self.doubleSpinBox_1.value()  # read HR value
        P = self.doubleSpinBox_2.value()  # read P value
        S = self.doubleSpinBox_3.value()  # Stenosis Value
        Index = self.comboBox_3.currentIndex()

        if Index==0:
            Pos = 0
            self.plot_p = 1
            self.plot_f = 0

        elif Index==1:                              #Index value in combo_box
            Pos = 1                                 #Initalize position
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

        print('positon value:', Pos, 'stenosis value:', S)
        STENOSIS.steno(Pos, S)  # s : value of stenosis in %, pos: in which area to induce
        self.clock, self.pulse = MAIN2.calc(H, P)

        self.c = np.all(self.clock != -1)
        self.p = np.all(self.pulse != -10000)

        if self.c and self.p:
            self.p_Peak = self.pulse[self.plot_p][:].max()
            self.p_Peak = str(self.p_Peak)
            labelStyle = {'color': '#ED553B', 'font-size': '9pt'}
            #self.graphWidget_1.addLegend()
            self.graphWidget_1.showGrid(x=True, y=True)
            self.graphWidget_1.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen('#3CAEA3', width=2))
            self.graphWidget_1.setLabel('left', 'Pressure (mmHg)', **labelStyle)
            self.graphWidget_1.plotItem.setLabel('bottom', 'Time (s)', **labelStyle)

            self.textEdit_1.clear()
            self.textEdit_1.insertPlainText(self.p_Peak)
            self.statusbar.showMessage('PLOTTED', msecs=9000)

            #self.graphWidget_2.addLegend()
            self.graphWidget_2.showGrid(x=True, y=True)
            self.graphWidget_2.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen('#3CAEA3', width=2))
            self.graphWidget_2.setLabel('left', 'Pressure (mmHg)', **labelStyle)
            self.graphWidget_2.setLabel('bottom', 'Time (s)', **labelStyle)

            self.textEdit_2.clear()
            self.textEdit_2.insertPlainText(self.p_Peak)
            self.statusbar.showMessage('PLOTTED', msecs=9000)
        else:
            self.alert("Invalid values...!!")

    def pressure_plot_1(self):
        self.graphWidget_1.plotItem.clear()
        plt = self.graphWidget_1
        Txt = self.comboBox_G1.currentText()
        print('graphWidget-1_pressure')
        plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen(2, width=2), name=Txt)
        self.statusbar.showMessage('PLOTTED', msecs=5000)

    def pressure_plot_2(self):
        self.graphWidget_2.plotItem.clear()
        plt = self.graphWidget_2
        Txt = self.comboBox_G2.currentText()
        print('graphWidget-2_pressure')
        plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen(2, width=2), name = Txt)
        self.statusbar.showMessage('PLOTTED', msecs=5000)

    def flow_plot_1(self):
        self.graphWidget_1.plotItem.clear()
        plt = self.graphWidget_1
        Txt = self.comboBox_G1.currentText()
        print('graphWidget-1_flow')
        plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen(2, width=2), name=Txt)
        self.statusbar.showMessage('PLOTTED', msecs=5000)

    def flow_plot_2(self):
        self.graphWidget_2.plotItem.clear()
        plt = self.graphWidget_2
        Txt = self.comboBox_G2.currentText()
        print('graphWidget-2_flow')
        plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen(2, width=2), name=Txt)
        self.statusbar.showMessage('PLOTTED', msecs=5000)

    def alert(self, msg):
        alert = QtWidgets.QMessageBox()
        alert.setText(msg)
        alert.exec_()

    def Help(self):
        help = QtWidgets.QMessageBox()
        help.setWindowTitle("Help")
        help.setText("Kindly ")
        help.exec_()


    def about(self):
        about = QtWidgets.QMessageBox()
        about.setWindowTitle("About")
        about.setText('This is an open source software developed for the simulation of blood pressure and blood flow'
                      '\nKindly support us by contributing your part to this software.')
        about.exec_()

    def reset(self):
        self.statusbar.showMessage('cleared', msecs =  6000)
        self.graphWidget_1.plotItem.clearPlots()
        self.graphWidget_2.plotItem.clearPlots()
        self.textEdit_1.clear()
        self.textEdit_2.clear()
        self.comboBox_G1.setCurrentIndex(0)
        self.comboBox_G2.setCurrentIndex(0)

    def mainViewer_1(self):
        Id = self.comboBox_G1.currentIndex()
        self.graphWidget_1.plotItem.clear()
        gW1 = self.graphWidget_1
        Text = self.comboBox_G1.currentText()
        self.viewing(Id, Text, gW1)

    def mainViewer_2(self):
        Id = self.comboBox_G2.currentIndex()
        self.graphWidget_2.plotItem.clear()
        gW2 = self.graphWidget_2
        Text = self.comboBox_G2.currentText()
        self.viewing(Id, Text, gW2)

    def viewing(self, Index, Txt, plt):
        print('viewing called')
        if Index==0:
            Pos = 0
            self.plot_p = 1
            self.plot_f = 0
            if self.radioButton_1.isChecked()  or self.radioButton_3.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen('#3CAEA3', width=2), name = Txt)
            elif self.radioButton_2.isChecked() or self.radioButton_4.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen('#3CAEA3', width=2), name = Txt)

        elif Index==1:
            Pos = 1
            self.plot_p = 3
            self.plot_f = 2
            if self.radioButton_1.isChecked() or self.radioButton_3.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen(2, width=2), name = Txt)

            elif self.radioButton_2.isChecked() or self.radioButton_4.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen(2, width=2), name = Txt)

        elif Index==2:
            Pos = 7
            self.plot_p = 7
            self.plot_f = 6
            if self.radioButton_1.isChecked() or self.radioButton_3.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen(2, width=2), name = Txt)

            elif self.radioButton_2.isChecked() or self.radioButton_4.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen(2, width=2), name = Txt)

        elif Index==3:
            Pos = 13
            self.plot_p = 31
            self.plot_f = 30
            if self.radioButton_1.isChecked() or self.radioButton_3.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen(2, width=2), name = Txt)

            elif self.radioButton_2.isChecked() or self.radioButton_4.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen(2, width=2), name = Txt)

        elif Index==4:
            Pos = 3
            self.plot_p = 53
            self.plot_f = 52
            if self.radioButton_1.isChecked() or self.radioButton_3.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen(2, width=2), name = Txt)

            elif self.radioButton_2.isChecked() or self.radioButton_4.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen(2, width=2), name = Txt)

        elif Index==5:
            Pos = 11
            self.plot_p = 83
            self.plot_f = 82
            if self.radioButton_1.isChecked() or self.radioButton_3.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen(2, width=2), name = Txt)

            elif self.radioButton_2.isChecked() or self.radioButton_4.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen(2, width=2), name = Txt)

        elif Index==6:
            Pos = 10
            self.plot_p = 113
            self.plot_f = 112
            if self.radioButton_1.isChecked() or self.radioButton_3.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen(2, width=2), name = Txt)

            elif self.radioButton_2.isChecked() or self.radioButton_4.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen(2, width=2), name = Txt)

        elif Index==7:
            Pos = 51
            self.plot_p = 103
            self.plot_f = 102
            if self.radioButton_1.isChecked() or self.radioButton_3.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen(2, width=2), name = Txt)

            elif self.radioButton_2.isChecked() or self.radioButton_4.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen(2, width=2), name = Txt)

        elif Index==8:
            Pos = 46
            self.plot_p = 75
            self.plot_f = 74
            if self.radioButton_1.isChecked() or self.radioButton_3.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen(2, width=2), name = Txt)

            elif self.radioButton_2.isChecked() or self.radioButton_4.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen(2, width=2), name = Txt)

        elif Index==9:
            Pos = 74
            self.plot_p = 123
            self.plot_f = 122
            if self.radioButton_1.isChecked() or self.radioButton_3.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen(2, width=2), name = Txt)

            elif self.radioButton_2.isChecked() or self.radioButton_4.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen(2, width=2), name = Txt)

        elif Index==10:
            Pos = 56
            self.plot_p = 207
            self.plot_f = 206
            if self.radioButton_1.isChecked() or self.radioButton_3.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen(2, width=2), name = Txt)

            elif self.radioButton_2.isChecked() or self.radioButton_4.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen(2, width=2), name = Txt)

        elif Index==11:
            Pos = 70
            self.plot_p = 211
            self.plot_f = 210
            if self.radioButton_1.isChecked() or self.radioButton_3.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen(2, width=2), name = Txt)

            elif self.radioButton_2.isChecked() or self.radioButton_4.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen(2, width=2), name=Txt)

        elif Index==12:
            Pos = 62
            self.plot_p = 131
            self.plot_f = 130
            if self.radioButton_1.isChecked() or self.radioButton_3.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen(2, width=2), name = Txt)

            elif self.radioButton_2.isChecked() or self.radioButton_4.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen(2, width=2), name = Txt)

        elif Index==13:
            Pos = 63
            self.plot_p = 133
            self.plot_f = 132
            if self.radioButton_1.isChecked() or self.radioButton_3.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen(2, width=2), name = Txt)

            elif self.radioButton_2.isChecked()or self.radioButton_4.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen(2, width=2), name=Txt)

        elif Index==14:
            Pos = 108
            self.plot_p = 149
            self.plot_f = 148
            if self.radioButton_1.isChecked()or self.radioButton_3.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen(2, width=2), name = Txt)

            elif self.radioButton_2.isChecked()or self.radioButton_4.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen(2, width=2), name= Txt)

        elif Index==15:
            Pos = 109
            self.plot_p = 181
            self.plot_f = 180
            if self.radioButton_1.isChecked()or self.radioButton_3.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen(2, width=2), name = Txt)

            elif self.radioButton_2.isChecked()or self.radioButton_4.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen(2, width=2), name= Txt)

        elif Index==16:
            Pos = 102
            self.plot_p = 249
            self.plot_f = 248
            if self.radioButton_1.isChecked()or self.radioButton_3.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen(2, width=2), name = Txt)

            elif self.radioButton_2.isChecked()or self.radioButton_4.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen(2, width=2),  name= Txt)

        elif Index==17:
            Pos = 107
            self.plot_p = 253
            self.plot_f = 252
            if self.radioButton_1.isChecked()or self.radioButton_3.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen(2, width=2), name = Txt)

            elif self.radioButton_2.isChecked()or self.radioButton_4.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen(2, width=2),  name = Txt)

        elif Index == 18:
            Pos = 96
            self.plot_p = 251
            self.plot_f = 250
            if self.radioButton_1.isChecked()or self.radioButton_3.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen(2, width=2), name = Txt)

            elif self.radioButton_2.isChecked()or self.radioButton_4.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen(2, width=2), name= Txt)

        elif Index == 19:
            Pos = 92
            self.plot_p = 245
            self.plot_f = 244
            if self.radioButton_1.isChecked() or self.radioButton_3.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen('#3CAEA3', width=2), name = Txt)

            elif self.radioButton_2.isChecked() or self.radioButton_4.isChecked():
                plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen('#3CAEA3', width=2), name = Txt)
        labelStyle = {'color': '#ED553B', 'font-size': '9pt'}
        if self.radioButton_1.isChecked():
            self.graphWidget_1.setLabel('left', text='Pressure (mmHg)', **labelStyle)
            self.graphWidget_1.setLabel('bottom', text='Time', **labelStyle)
            self.peak = self.pulse[self.plot_p][:].max()
        if self.radioButton_3.isChecked():
            self.graphWidget_2.setLabel('left', text='Pressure (mmHg)', **labelStyle)
            self.graphWidget_2.setLabel('bottom', text='Time', **labelStyle)
            self.peak = self.pulse[self.plot_p][:].max()
        if self.radioButton_2.isChecked():
            self.graphWidget_1.setLabel('left', text='Pressure (mmHg)', **labelStyle)
            self.graphWidget_1.setLabel('bottom', text='Time', **labelStyle)
            self.peak = self.pulse[self.plot_f][:].max()
        if self.radioButton_4.isChecked():
            self.graphWidget_2.setLabel('left', text='Pressure (mmHg)', **labelStyle)
            self.graphWidget_2.setLabel('bottom', text='Time', **labelStyle)
            self.peak = self.pulse[self.plot_f][:].max()
        self.Peak = str(self.peak)
        self.textEdit_1.clear()
        self.textEdit_1.setText(self.Peak)
        self.statusbar.showMessage('PLOTTED', msecs=10000)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
