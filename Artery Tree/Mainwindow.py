from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import Artery_model
import numpy as np
import STENOSIS
import os
import CARDIAC
from SQLFILE import create_connection, execute_query, execute_read_query, execute_many_query


stn_dat = {'0': None, '1': None, '7': None, '13': None, '3': None, '11': None, '10': None, '51': None,
           '46': None, '74': None, '56': None, '70': None, '62': None, '63': None, '108': None,
           '109': None, '102': None, '107': None, '96': None, '92': None}

class Ui_MainWindow(object):
    try:
        def __init__(self, MainWindow):
            super().__init__()
            self.MainWindow = MainWindow
            self._translate = QtCore.QCoreApplication.translate
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.gridLayout_1 = QtWidgets.QGridLayout(self.centralwidget)
            self.widget_1 = QtWidgets.QWidget(self.centralwidget)
            self.widget_2 = QtWidgets.QWidget(self.centralwidget)
            self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
            self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
            self.buttonGroup_3 = QtWidgets.QButtonGroup(MainWindow)
            self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
            self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
            self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
            self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
            self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
            self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
            self.radioButton_1.setDisabled(True)
            self.radioButton_2.setDisabled(True)
            self.radioButton_3.setDisabled(True)
            self.radioButton_4.setDisabled(True)
            self.radioButton_5.hide()
            self.radioButton_6.hide()
            self.comboBox_G1 = QtWidgets.QComboBox(self.centralwidget)
            self.comboBox_G2 = QtWidgets.QComboBox(self.centralwidget)
            self.comboBox_G3 = QtWidgets.QComboBox(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.dockWidget_1 = QtWidgets.QDockWidget(MainWindow)
            self.dockWidgetContents_1 = QtWidgets.QWidget()
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
            self.label_1 = QtWidgets.QLabel(self.groupBox_1)
            self.label_2 = QtWidgets.QLabel(self.groupBox_1)
            self.label_3 = QtWidgets.QLabel(self.groupBox_1)
            self.label_4 = QtWidgets.QLabel(self.groupBox_1)
            self.label_5 = QtWidgets.QLabel(self.groupBox_1)
            self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_1)
            self.dockWidget_2 = QtWidgets.QDockWidget(MainWindow)
            self.dockWidgetContents_2 = QtWidgets.QWidget()
            self.gridLayout_4 = QtWidgets.QGridLayout(self.dockWidgetContents_2)
            self.groupBox_3 = QtWidgets.QGroupBox(self.dockWidgetContents_2)
            self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_3)
            self.labelEdit_1 = QtWidgets.QLabel(self.groupBox_3)
            self.groupBox_4 = QtWidgets.QGroupBox(self.dockWidgetContents_2)
            self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_4)
            self.stn_dat = {'0': None, '1': None, '7': None, '13': None, '3': None, '11': None, '10': None, '51': None,
                            '46': None, '74': None, '56': None, '70': None, '62': None, '63': None, '108': None,
                            '109': None, '102': None, '107': None, '96': None, '92': None}
            self.c = 0
            self.cv = 0
            self.labelStyle = {'color': '#ED553B', 'font-size': '9pt'}
            self.dockWidget_3 = QtWidgets.QDockWidget(MainWindow)
            self.dockWidgetContents_3 = QtWidgets.QWidget()
            self.gridLayout_11 = QtWidgets.QGridLayout(self.dockWidgetContents_3)
            self.groupBox_5 = QtWidgets.QGroupBox(self.dockWidgetContents_3)
            self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_5)
            self.label_heart = QtWidgets.QLabel(self.groupBox_5)
            self.groupBox_6 = QtWidgets.QGroupBox(self.dockWidgetContents_3)
            self.text_heartinfo = QtWidgets.QTextBrowser(self.groupBox_6)
            self.labelEdit_1.setPixmap(QtGui.QPixmap(os.path.join("images/artery tree images", "art_tree_img.png")))
            self.textBrowser_2.setText(
                "The primary function of the heart is to serve as a muscular pump propelling blood"
                "into and through vessels to and from all parts of the body. The arteries, "
                "which "
                "receive this blood at high pressure and velocity and conduct it throughout the "
                "body, have thick walls that are composed of elastic fibrous tissue and muscle "
                "cells. The arterial tree—the branching system of arteries—terminates in short, "
                "narrow, muscular vessels called arterioles, from which blood enters simple "
                "endothelial tubes (i.e., tubes formed of endothelial, or lining, cells) known "
                "as capillaries. These thin, microscopic capillaries are permeable to vital cellular"
                " nutrients and waste products that they receive and distribute. From the"
                " capillaries, the blood, now depleted of oxygen and burdened with waste products,"
                " moving more slowly and under low pressure, enters small vessels called venules"
                " that converge to form veins, ultimately guiding the blood on its way back to the"
                " heart.")
            self.setupUi()

        def setupUi(self):
            MainWindow = self.MainWindow
            MainWindow.setWindowTitle(self._translate("MainWindow", "Bloodsim"))
            MainWindow.setObjectName("MainWindow")
            MainWindow.setWindowIcon(QtGui.QIcon('images/logo.png'))
            MainWindow.resize(1400, 800)
            MainWindow.setMinimumSize(QtCore.QSize(1400, 800))
            MainWindow.setStyleSheet("color: rgb(255, 210, 119);\n"
                                     "gridline-color: rgb(33, 57, 86);\n"
                                     "background-color: rgb(46, 80, 120);\n"
                                     "selection-color: rgb(237, 85, 59);\n"
                                     "selection-background-color: rgb(33, 57, 86);")
            MainWindow.setDockOptions(
                QtWidgets.QMainWindow.AllowNestedDocks | QtWidgets.QMainWindow.AllowTabbedDocks |
                QtWidgets.QMainWindow.AnimatedDocks | QtWidgets.QMainWindow.ForceTabbedDocks | QtWidgets.QMainWindow.VerticalTabs)
            self.centralwidget.setObjectName("centralwidget")
            self.gridLayout_1.setObjectName("gridLayout_1")
            # GRAPH_WIDGET - 1 ===============================================================================
            # GRAPH
            self.graphWidget_1 = pg.PlotWidget()
            self.graphWidget_1.setBackground('#213956')
            self.graphWidget_1.setAntialiasing(True)
            self.graphWidget_1.setLabel('left', text='x axis', **self.labelStyle)
            self.graphWidget_1.setLabel('bottom', text='y axis', **self.labelStyle)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(1)
            sizePolicy.setVerticalStretch(1)
            sizePolicy.setHeightForWidth(self.widget_1.sizePolicy().hasHeightForWidth())
            self.graphWidget_1.setSizePolicy(sizePolicy)
            self.graphWidget_1.setMinimumSize(QtCore.QSize(0, 0))
            self.graphWidget_1.setObjectName("widget_1")
            self.gridLayout_1.addWidget(self.graphWidget_1, 1, 0, 1, 3)
            # GRAPH_WIDGET - 2 ============================================================================
            # GRAPH-2
            self.graphWidget_2 = pg.PlotWidget()
            self.graphWidget_2.setBackground('#213956')
            self.graphWidget_2.setAntialiasing(True)
            self.graphWidget_2.setLabel('left', text='x axis', **self.labelStyle)
            self.graphWidget_2.setLabel('bottom', text='y axis', **self.labelStyle)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(1)
            sizePolicy.setVerticalStretch(1)
            sizePolicy.setHeightForWidth(self.graphWidget_2.sizePolicy().hasHeightForWidth())
            self.graphWidget_2.setSizePolicy(sizePolicy)
            self.graphWidget_2.setMinimumSize(QtCore.QSize(0, 0))
            self.graphWidget_2.setSizeIncrement(QtCore.QSize(5, 5))
            self.graphWidget_2.setObjectName("widget_2")
            self.gridLayout_1.addWidget(self.graphWidget_2, 3, 0, 1, 3)
            # FIRST GRAPH =================================================================================
            # comboBox_G1
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(1)
            sizePolicy.setVerticalStretch(1)
            sizePolicy.setHeightForWidth(self.comboBox_G1.sizePolicy().hasHeightForWidth())
            self.comboBox_G1.setSizePolicy(sizePolicy)
            self.comboBox_G1.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                           "background-color: rgb(35, 35, 35);\n"
                                           "color: rgb(255, 210, 119);\n"
                                           "selection-color: rgb(237, 85, 59);\n"
                                           "selection-background-color: rgb(33, 57, 86);\n"
                                           "gridline-color: rgb(255, 255, 255);\n"
                                           "")
            self.comboBox_G1.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
            self.comboBox_G1.setFrame(False)
            self.comboBox_G1.setObjectName("comboBox_G1")
            for i in range(21):
                self.comboBox_G1.addItem("")
            self.gridLayout_1.addWidget(self.comboBox_G1, 0, 0, 1, 1)
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
            self.gridLayout_1.addWidget(self.radioButton_1, 0, 1, 1, 1)
            self.radioButton_1.clicked.connect(self.pressure_plot_1)
            # radioButton_2
            self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);")
            self.radioButton_2.setChecked(False)
            self.radioButton_2.setObjectName("radioButton_2")
            self.buttonGroup.setObjectName("buttonGroup")
            self.buttonGroup.addButton(self.radioButton_2)
            self.gridLayout_1.addWidget(self.radioButton_2, 0, 2, 1, 1)
            self.radioButton_2.clicked.connect(self.flow_plot_1)
            # SECOND GRAPH =====================================================================================================
            # ComboBox_G2
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
            for i in range(21):
                self.comboBox_G2.addItem("")
            self.gridLayout_1.addWidget(self.comboBox_G2, 2, 0, 1, 1)
            self.comboBox_G2.currentIndexChanged.connect(self.mainViewer_2)
            # Radiobutton_3
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(1)
            sizePolicy.setVerticalStretch(1)
            sizePolicy.setHeightForWidth(self.radioButton_3.sizePolicy().hasHeightForWidth())
            self.radioButton_3.setSizePolicy(sizePolicy)
            self.radioButton_3.setStyleSheet("color: rgb(255, 255, 255);")
            self.radioButton_3.setChecked(True)
            self.radioButton_3.setObjectName("radioButton_3")
            self.buttonGroup_2.addButton(self.radioButton_3)
            self.gridLayout_1.addWidget(self.radioButton_3, 2, 1, 1, 1)
            self.radioButton_3.clicked.connect(self.pressure_plot_2)
            # RadioButton_4
            self.radioButton_4.setStyleSheet("color: rgb(255, 255, 255);")
            self.radioButton_4.setObjectName("radioButton_4")
            self.buttonGroup_2.setObjectName("buttonGroup_2")
            self.buttonGroup_2.addButton(self.radioButton_4)
            self.gridLayout_1.addWidget(self.radioButton_4, 2, 2, 1, 1)
            self.radioButton_4.clicked.connect(self.flow_plot_2)
            # THIRD GRAPH =====================================================================================================
            # ComboBox_G3
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(1)
            sizePolicy.setVerticalStretch(1)
            sizePolicy.setHeightForWidth(self.comboBox_G3.sizePolicy().hasHeightForWidth())
            self.comboBox_G3.setSizePolicy(sizePolicy)
            self.comboBox_G3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
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
            self.comboBox_G3.setFrame(False)
            self.comboBox_G3.setObjectName("comboBox_G3")
            for i in range(2):
                self.comboBox_G3.addItem("")
            self.gridLayout_1.addWidget(self.comboBox_G3, 2, 0, 1, 1)
            self.comboBox_G3.hide()
            # Radiobutton_5
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(1)
            sizePolicy.setVerticalStretch(1)
            sizePolicy.setHeightForWidth(self.radioButton_5.sizePolicy().hasHeightForWidth())
            self.radioButton_5.setSizePolicy(sizePolicy)
            self.radioButton_5.setStyleSheet("color: rgb(255, 255, 255);")
            self.radioButton_5.setChecked(True)
            self.radioButton_5.setObjectName("radioButton_5")
            self.buttonGroup_3.addButton(self.radioButton_5)
            self.gridLayout_1.addWidget(self.radioButton_5, 2, 1, 1, 1)
            self.radioButton_5.clicked.connect(self.radio_plot)
            # RadioButton_6
            self.radioButton_6.setStyleSheet("color: rgb(255, 255, 255);")
            self.radioButton_6.setObjectName("radioButton_6")
            self.buttonGroup_3.setObjectName("buttonGroup_3")
            self.buttonGroup_3.addButton(self.radioButton_6)
            self.gridLayout_1.addWidget(self.radioButton_6, 2, 2, 1, 1)
            self.radioButton_6.clicked.connect(self.radio_plot)
            # LEFT SIDE DOCK WIDGET====================================================================================
            # DockWidget_1
            self.dockWidget_1.setMinimumSize(QtCore.QSize(366, 534))
            self.dockWidget_1.setMouseTracking(True)
            self.dockWidget_1.setFloating(False)
            self.dockWidget_1.setFeatures(
                QtWidgets.QDockWidget.DockWidgetFloatable | QtWidgets.QDockWidget.DockWidgetMovable)
            self.dockWidget_1.setObjectName("dockWidget_1")
            self.dockWidgetContents_1.setObjectName("dockWidgetContents_1")
            self.gridLayout.setObjectName("gridLayout")
            # LEFTSIDE SECOND GroupBox========================================================================================
            # GroupBox_2
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
            self.groupBox_2.setSizePolicy(sizePolicy)
            self.groupBox_2.setMinimumSize(QtCore.QSize(331, 251))
            self.groupBox_2.setTitle("")
            self.groupBox_2.setFlat(True)
            self.groupBox_2.setObjectName("groupBox_2")
            # gridLayout_2
            self.gridLayout_2.setObjectName("gridLayout_2")
            # label_9
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
            # doubleSpinBox_4
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
            # doublePsinBox_5
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
            # doubleSpinBox_6
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
            # checkBox_3
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
            # checkBox_4
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
            # checkBox_5
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
            # label_10
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
            self.label_10.setSizePolicy(sizePolicy)
            self.label_10.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255,255,255);")
            self.label_10.setObjectName("label_10")
            self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 2)
            # label_11
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
            self.label_11.setSizePolicy(sizePolicy)
            self.label_11.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255,255,255);")
            self.label_11.setObjectName("label_11")
            self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 2)

            # label_8
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

            # label_12
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
            # groupBox_1========================================================================================
            # groupBox_1
            self.groupBox_1.setTitle("")
            self.groupBox_1.setFlat(True)
            self.groupBox_1.setObjectName("groupBox_1")
            # gridLayout_3
            self.gridLayout_3.setObjectName("gridLayout_3")
            # checkBox_1
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.checkBox_1.sizePolicy().hasHeightForWidth())
            self.checkBox_1.setSizePolicy(sizePolicy)
            self.checkBox_1.setText("")
            self.checkBox_1.setChecked(False)
            self.checkBox_1.setObjectName("checkBox_1")
            self.gridLayout_3.addWidget(self.checkBox_1, 1, 1, 1, 1)
            self.checkBox_1.clicked.connect(self.enable)
            # doubleSpinBox_1
            self.doubleSpinBox_1.setEnabled(False)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
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
            self.doubleSpinBox_1.setDecimals(2)
            self.doubleSpinBox_1.setMinimum(60.0)
            self.doubleSpinBox_1.setMaximum(150.0)
            self.doubleSpinBox_1.setValue(72.0)
            self.doubleSpinBox_1.setObjectName("doubleSpinBox_1")
            self.gridLayout_3.addWidget(self.doubleSpinBox_1, 1, 2, 1, 1)
            # doubleSpinBox_2
            self.doubleSpinBox_2.setEnabled(False)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
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
            self.doubleSpinBox_2.setDecimals(2)
            self.doubleSpinBox_2.setMinimum(350.0)
            self.doubleSpinBox_2.setMaximum(600.0)
            self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
            self.gridLayout_3.addWidget(self.doubleSpinBox_2, 2, 2, 1, 1)
            self.doubleSpinBox_2.setValue(450.0)
            # label_1
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
            self.label_1.setSizePolicy(sizePolicy)
            self.label_1.setMaximumSize(QtCore.QSize(16777215, 15))
            self.label_1.setStyleSheet("background-color: rgb(32, 99, 155);\n"
                                       "font: 9pt \"MS Shell Dlg 2\";")
            self.label_1.setObjectName("label_1")
            self.gridLayout_3.addWidget(self.label_1, 0, 0, 1, 1)
            # label_2
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
            self.label_2.setSizePolicy(sizePolicy)
            self.label_2.setMaximumSize(QtCore.QSize(16777215, 15))
            self.label_2.setStyleSheet("background-color: rgb(32, 99, 155);\n"
                                       "font: 9pt \"MS Shell Dlg 2\";")
            self.label_2.setObjectName("label_2")
            self.gridLayout_3.addWidget(self.label_2, 0, 2, 1, 1)

            # label_3
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
            self.label_3.setSizePolicy(sizePolicy)
            self.label_3.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                       "color: rgb(255,255,255);")
            self.label_3.setObjectName("label_3")
            self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

            # label_4
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
            self.label_4.setSizePolicy(sizePolicy)
            self.label_4.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                       "color: rgb(255,255,255);")
            self.label_4.setObjectName("label_4")
            self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)

            # label_5
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
            self.label_5.setSizePolicy(sizePolicy)
            self.label_5.setStyleSheet("background-color: rgb(32, 99, 155);\n"
                                       "font: 9pt \"MS Shell Dlg 2\";")
            self.label_5.setObjectName("label_5")
            self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)

            # PushButton-STENO
            self.pushButton_STENO = QtWidgets.QPushButton(self.groupBox_1)
            self.pushButton_STENO.setStyleSheet("background-color: rgb(35, 35, 35);")
            self.pushButton_STENO.setObjectName("pushButton_STENO")
            self.gridLayout_3.addWidget(self.pushButton_STENO, 5, 0, 1, 3)

            # PushButton-HP
            self.pushButton_HP = QtWidgets.QPushButton(self.groupBox_1)
            self.pushButton_HP.setStyleSheet("background-color: rgb(35, 35, 35);")
            self.pushButton_HP.setObjectName("pushButton_HP")
            self.gridLayout_3.addWidget(self.pushButton_HP, 6, 0, 1, 3)
            # self.pushButton_HP.clicked.connect(self.Heart_para)

            # PushButton-1
            #self.pushButton_1 = QtWidgets.QPushButton(self.groupBox_1)
            #self.pushButton_1.setStyleSheet("background-color: rgb(35, 35, 35);")
            #self.pushButton_1.setObjectName("pushButton_1")
            #self.gridLayout_3.addWidget(self.pushButton_1, 7, 0, 1, 3)

            # checkBox_2
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
            self.checkBox_2.setSizePolicy(sizePolicy)
            self.checkBox_2.setText("")
            self.checkBox_2.setChecked(False)
            self.checkBox_2.setObjectName("checkBox_2")
            self.gridLayout_3.addWidget(self.checkBox_2, 2, 1, 1, 1)
            self.gridLayout.addWidget(self.groupBox_1, 0, 0, 1, 1)
            self.dockWidget_1.setWidget(self.dockWidgetContents_1)
            MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_1)
            self.checkBox_2.clicked.connect(self.enable)

            # ========dockWidget_2================================================
            self.dockWidget_2.setMinimumSize(QtCore.QSize(250, 487))
            self.dockWidget_2.setMaximumWidth(450)
            self.dockWidget_2.setObjectName("dockWidget_2")

            # dockWidgetContents_5
            self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")

            # gridLayout_4
            self.gridLayout_4.setObjectName("gridLayout_4")
            ################### groupBox_3
            self.groupBox_3.setMinimumSize(QtCore.QSize(221, 300))
            self.groupBox_3.setTitle("")
            self.groupBox_3.setFlat(True)
            self.groupBox_3.setObjectName("groupBox_3")

            # gridLayout_8
            self.gridLayout_8.setObjectName("gridLayout_8")

            # labelEdit_1
            self.labelEdit_1.setStyleSheet("background-color: rgb(33, 57, 86);")
            self.labelEdit_1.setObjectName("labelsEdit")
            self.gridLayout_8.addWidget(self.labelEdit_1, 0, 0, 1, 1)
            self.gridLayout_4.addWidget(self.groupBox_3, 0, 0, 1, 1)

            # groupBox_4
            self.groupBox_4.setMinimumSize(QtCore.QSize(221, 241))
            self.groupBox_4.setTitle("")
            self.groupBox_4.setFlat(True)
            self.groupBox_4.setObjectName("groupBox_4")
            self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
            self.gridLayout_5.setObjectName("gridLayout_5")

            # textBrowser_2
            self.textBrowser_2.setStyleSheet("background-color: rgb(33, 57, 86);")
            self.textBrowser_2.setObjectName("textEdit_2")
            self.gridLayout_5.addWidget(self.textBrowser_2, 1, 0, 1, 3)

            # pushButton_5
            self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_4)
            self.pushButton_5.setStyleSheet("background-color: rgb(35, 35, 35);")
            self.pushButton_5.setObjectName("pushButton_2")
            self.gridLayout_5.addWidget(self.pushButton_5, 0, 0, 1, 1)
            self.pushButton_5.clicked.connect(self.button_graph_1)

            # pushButton_6
            self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_4)
            self.pushButton_6.setStyleSheet("background-color: rgb(35, 35, 35);")
            self.pushButton_6.setObjectName("pushButton_3")
            self.gridLayout_5.addWidget(self.pushButton_6, 0, 1, 1, 1)
            self.pushButton_6.clicked.connect(self.button_graph_2)

            # pushButton_7
            self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_4)
            self.pushButton_7.setStyleSheet("background-color: rgb(35, 35, 35);")
            self.pushButton_7.setObjectName("pushButton_4")
            self.pushButton_7.clicked.connect(self.button_analyse)
            self.gridLayout_5.addWidget(self.pushButton_7, 0, 2, 1, 1)
            self.gridLayout_4.addWidget(self.groupBox_4, 1, 0, 1, 1)
            self.dockWidget_2.setWidget(self.dockWidgetContents_2)
            MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_2)

            # ========================================================================================
            # dockWidget_3
            self.dockWidget_3.setMinimumSize(QtCore.QSize(250, 487))
            self.dockWidget_3.setMaximumWidth(450)
            self.dockWidget_3.setObjectName("dockWidget_2")

            # dockWidgetContents_3
            self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")

            # gridLayout_11
            self.gridLayout_11.setObjectName("gridLayout_11")

            # groupBox_5
            self.groupBox_5.setMinimumSize(QtCore.QSize(221, 191))
            self.groupBox_5.setTitle("")
            self.groupBox_5.setFlat(True)
            self.groupBox_5.setObjectName("groupBox_5")

            # gridLayout_12
            self.gridLayout_12.setObjectName("gridLayout_12")

            # label_heart
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_heart.sizePolicy().hasHeightForWidth())
            self.label_heart.setStyleSheet("background-color: rgb(33, 57, 86);")
            self.label_heart.setObjectName("label_heart")
            self.gridLayout_12.addWidget(self.label_heart, 0, 0, 1, 1)
            self.gridLayout_11.addWidget(self.groupBox_5, 0, 0, 1, 1)

            # groupBox_6
            self.groupBox_6.setMinimumSize(QtCore.QSize(221, 241))
            self.groupBox_6.setTitle("")
            self.groupBox_6.setFlat(True)
            self.groupBox_6.setObjectName("groupBox_6")
            self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox_6)
            self.gridLayout_13.setObjectName("gridLayout_13")

            # label_text_4
            self.text_heartinfo.setObjectName("text_heartinfo")
            self.text_heartinfo.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                              "background - color: rgb(33, 57, 86);")
            self.gridLayout_13.addWidget(self.text_heartinfo, 1, 0, 1, 3)

            # pushButton_2
            self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_6)
            self.pushButton_2.setStyleSheet("background-color: rgb(35, 35, 35);")
            self.pushButton_2.setObjectName("pushButton_2")
            self.gridLayout_13.addWidget(self.pushButton_2, 0, 0, 1, 1)
            self.pushButton_2.clicked.connect(self.button_chambers)

            # pushButton_3
            self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_6)
            self.pushButton_3.setStyleSheet("background-color: rgb(35, 35, 35);")
            self.pushButton_3.setObjectName("pushButton_3")
            self.gridLayout_13.addWidget(self.pushButton_3, 0, 1, 1, 1)
            self.pushButton_3.clicked.connect(self.button_valves)

            # pushButton_4
            self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_6)
            self.pushButton_4.setStyleSheet("background-color: rgb(35, 35, 35);")
            self.pushButton_4.setObjectName("pushButton_4")
            self.pushButton_4.clicked.connect(self.button_iandolet)
            self.gridLayout_13.addWidget(self.pushButton_4, 0, 2, 1, 1)
            self.gridLayout_11.addWidget(self.groupBox_6, 1, 0, 1, 1)
            self.dockWidget_3.setWidget(self.dockWidgetContents_3)
            MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_3)
            self.dockWidget_3.hide()
            # END OF DOCKWIDGET_3

            # Menubar
            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 1143, 26))
            self.menubar.setObjectName("menubar")
            # File Menu
            self.menuFile = QtWidgets.QMenu(self.menubar)
            self.menuFile.setObjectName("menuMenu")
            # View
            self.menuView = QtWidgets.QMenu(self.menubar)
            self.menuView.setObjectName("menuOptions")
            # Run
            self.menuRun = QtWidgets.QMenu(self.menubar)
            self.menuRun.setObjectName("menuHelp")
            # Help
            self.menuHelp = QtWidgets.QMenu(self.menubar)
            self.menuHelp.setObjectName("menuHelp_2")
            MainWindow.setMenuBar(self.menubar)
            # Statusbar
            self.statusbar.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                         "color: rgb(255, 210, 119);")
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)

            # Action_Declaration
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

            # Action_Adding
            self.menuFile.addAction(self.actionClear)
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

            # MenuTrigger
            # FileMenu_trigger
            self.actionClear.triggered.connect(self.clear)
            # self.actionQuit.triggered.connect()
            # ViewMenu_trigger
            self.actionIp.triggered.connect(self.showDock_1)
            self.actionWaveform.triggered.connect(self.showDock_2)
            self.actionHeart_Parameter.triggered.connect(self.showDock_3)
            # RunMenu_trigger
            self.actionRun.triggered.connect(self.artery_model)
            self.actionReset.triggered.connect(self.reset)
            self.actionStop.triggered.connect(self.cardiac_model)
            # HelpMenu_trigger
            self.actionBloodsim.triggered.connect(self.help)
            self.actionAbout_Bloodsim.triggered.connect(self.about)
            # TabOrder
            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)
            '''
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
            '''

        def retranslateUi(self, MainWindow):
            #self.pushButton_1.setText(self._translate("MainWindow", "OK"))
            self.pushButton_2.setText(self._translate("MainWindow", "CHAMBERS"))
            self.pushButton_3.setText(self._translate("MainWindow", "VALVES"))
            self.pushButton_4.setText(self._translate("MainWindow", "INLET/OUTLET"))
            self.pushButton_5.setText(self._translate("MainWindow", "GRAPH-1"))
            self.pushButton_6.setText(self._translate("MainWindow", "GRAPH-2"))
            self.pushButton_7.setText(self._translate("MainWindow", "ANALYSE"))
            self.pushButton_HP.setText(self._translate("MainWindow", "HEART PARAMETERS"))
            self.pushButton_STENO.setText(self._translate("MainWindow", "STENOSIS PARAMETERS"))
            self.radioButton_1.setText(self._translate("MainWindow", "Pressure"))
            self.radioButton_2.setText(self._translate("MainWindow", "Flow"))
            self.radioButton_3.setText(self._translate("MainWindow", "Pressure"))
            self.radioButton_4.setText(self._translate("MainWindow", "Flow"))
            self.menuFile.setTitle(self._translate("MainWindow", "File"))
            self.menuView.setTitle(self._translate("MainWindow", "View"))
            self.menuRun.setTitle(self._translate("MainWindow", "Run"))
            self.menuHelp.setTitle(self._translate("MainWindow", "Help"))
            self.dockWidget_1.setWindowTitle(self._translate("MainWindow", "Input Parameters"))
            self.label_9.setText(self._translate("MainWindow", "Value"))
            self.label_10.setText(self._translate("MainWindow", "Blood viscosity"))
            self.label_11.setText(self._translate("MainWindow", "Blood density"))
            self.label_8.setText(self._translate("MainWindow", "Property"))
            self.label_12.setText(self._translate("MainWindow", "Reflection Coefficient"))
            self.label_1.setText(self._translate("MainWindow", "Property"))
            self.label_2.setText(self._translate("MainWindow", "Value"))
            self.label_4.setText(self._translate("MainWindow", "Peak Flow (ml/sec)"))
            self.label_3.setText(self._translate("MainWindow", "Heart Rate (bpm)"))
            self.label_5.setText(self._translate("MainWindow", "Stenosis"))

            self.comboBox_G1.setItemText(0, self._translate("MainWindow", "Choose Section"))
            self.comboBox_G1.setItemText(1, self._translate("MainWindow", "Ascending aorta"))
            self.comboBox_G1.setItemText(2, self._translate("MainWindow", "Aortic arch"))
            self.comboBox_G1.setItemText(3, self._translate("MainWindow", "Subclavian artery left"))
            self.comboBox_G1.setItemText(4, self._translate("MainWindow", "Subclavian artery right"))
            self.comboBox_G1.setItemText(5, self._translate("MainWindow", "Common carotid(L)"))
            self.comboBox_G1.setItemText(6, self._translate("MainWindow", "Common carotid(R)"))
            self.comboBox_G1.setItemText(7, self._translate("MainWindow", "Thoracic aorta"))
            self.comboBox_G1.setItemText(8, self._translate("MainWindow", "Cerebral artery right"))
            self.comboBox_G1.setItemText(9, self._translate("MainWindow", "Cerebral artey left"))
            self.comboBox_G1.setItemText(10, self._translate("MainWindow", "Abdominal aorta"))
            self.comboBox_G1.setItemText(11, self._translate("MainWindow", "Brachial Artery Right"))
            self.comboBox_G1.setItemText(12, self._translate("MainWindow", "Brachial Artery Left"))
            self.comboBox_G1.setItemText(13, self._translate("MainWindow", "Hepatic artery"))
            self.comboBox_G1.setItemText(14, self._translate("MainWindow", "Renal Artery"))
            self.comboBox_G1.setItemText(15, self._translate("MainWindow", "Femoral Artery Left"))
            self.comboBox_G1.setItemText(16, self._translate("MainWindow", "Femoral Artery Right"))
            self.comboBox_G1.setItemText(17, self._translate("MainWindow", "Ulnar artery left"))
            self.comboBox_G1.setItemText(18, self._translate("MainWindow", "Ulnar artery right"))
            self.comboBox_G1.setItemText(19, self._translate("MainWindow", "Radial Artery Left"))
            self.comboBox_G1.setItemText(20, self._translate("MainWindow", "Radial Artery Right"))

            self.comboBox_G2.setItemText(0, self._translate("MainWindow", "Choose Section"))
            self.comboBox_G2.setItemText(1, self._translate("MainWindow", "Ascending aorta"))
            self.comboBox_G2.setItemText(2, self._translate("MainWindow", "Aortic arch"))
            self.comboBox_G2.setItemText(3, self._translate("MainWindow", "Subclavian artery left"))
            self.comboBox_G2.setItemText(4, self._translate("MainWindow", "Subclavian artery right"))
            self.comboBox_G2.setItemText(5, self._translate("MainWindow", "Common carotid(L)"))
            self.comboBox_G2.setItemText(6, self._translate("MainWindow", "Common carotid(R)"))
            self.comboBox_G2.setItemText(7, self._translate("MainWindow", "Thoracic aorta"))
            self.comboBox_G2.setItemText(8, self._translate("MainWindow", "Cerebral artery right"))
            self.comboBox_G2.setItemText(9, self._translate("MainWindow", "Cerebral artey left"))
            self.comboBox_G2.setItemText(10, self._translate("MainWindow", "Abdominal aorta"))
            self.comboBox_G2.setItemText(11, self._translate("MainWindow", "Brachial Artery Right"))
            self.comboBox_G2.setItemText(12, self._translate("MainWindow", "Brachial Artery Left"))
            self.comboBox_G2.setItemText(13, self._translate("MainWindow", "Hepatic artery"))
            self.comboBox_G2.setItemText(14, self._translate("MainWindow", "Renal Artery"))
            self.comboBox_G2.setItemText(15, self._translate("MainWindow", "Femoral Artery Left"))
            self.comboBox_G2.setItemText(16, self._translate("MainWindow", "Femoral Artery Right"))
            self.comboBox_G2.setItemText(17, self._translate("MainWindow", "Ulnar artery left"))
            self.comboBox_G2.setItemText(18, self._translate("MainWindow", "Ulnar artery right"))
            self.comboBox_G2.setItemText(19, self._translate("MainWindow", "Radial Artery Left"))
            self.comboBox_G2.setItemText(20, self._translate("MainWindow", "Radial Artery Right"))
            self.dockWidget_2.setWindowTitle(self._translate("MainWindow", "ARTERY DOCK"))
            self.dockWidget_3.setWindowTitle(self._translate("MainWindow", "HEART DOCK"))

            self.actionRun.setText(self._translate("MainWindow", "Artery Model"))
            self.actionStop.setText(self._translate("MainWindow", "Heart Model"))
            self.actionClear.setText(self._translate("MainWindow", "Clear"))
            self.actionIp.setText(self._translate("MainWindow", "Input Parmeters"))
            self.actionWaveform.setText(self._translate("MainWindow", "Artery Dock"))
            self.actionHeart_Parameter.setText(self._translate("MainWindow", "Heart Dock"))
            self.actionReset.setText(self._translate("MainWindow", "Reset"))
            self.actionQuit.setText(self._translate("MainWindow", "Quit"))
            self.actionQuit.setText(self._translate("MainWindow", "Quit"))
            self.actionBloodsim.setText(self._translate("MainWindow", "Bloodsim Help"))
            self.actionAbout_Bloodsim.setText(self._translate("MainWindow", "About Bloodsim"))

        def enable(self):
            if self.checkBox_1.isChecked():
                self.doubleSpinBox_1.setEnabled(True)
            else:
                self.doubleSpinBox_1.setEnabled(False)
            if self.checkBox_2.isChecked():
                self.doubleSpinBox_2.setEnabled(True)
            else:
                self.doubleSpinBox_2.setEnabled(False)
            if self.checkBox_3.isChecked():
                self.doubleSpinBox_4.setEnabled(True)
            else:
                self.doubleSpinBox_4.setEnabled(False)
            if self.checkBox_4.isChecked():
                self.doubleSpinBox_5.setEnabled(True)
            else:
                self.doubleSpinBox_5.setEnabled(False)
            if self.checkBox_5.isChecked():
                self.doubleSpinBox_6.setEnabled(True)
            else:
                self.doubleSpinBox_6.setEnabled(False)

        def showDock_1(self):
            if not self.actionIp.isChecked():
                self.dockWidget_1.hide()
            if self.actionIp.isChecked():
                self.dockWidget_1.show()

        def showDock_2(self, MainWindow):
            if self.actionWaveform.isChecked():
                Ui_MainWindow.retranslateUi(self, MainWindow)
                self.radioButton_3.setText(self._translate("MainWindow", "Pressure"))
                self.radioButton_3.show()
                self.radioButton_4.show()
                self.radioButton_5.hide()
                self.radioButton_6.hide()
                self.comboBox_G3.hide()
                self.comboBox_G3.setDisabled(True)
                self.comboBox_G2.show()
                self.comboBox_G2.setDisabled(False)
                self.dockWidget_2.show()
                self.dockWidget_3.hide()
                self.actionHeart_Parameter.setChecked(False)
            if not self.actionWaveform.isChecked():
                self.dockWidget_2.hide()

        def showDock_3(self):
            if self.actionHeart_Parameter.isChecked():
                self.comboBox_G2.hide()
                self.comboBox_G2.setDisabled(True)
                self.comboBox_G3.show()
                self.comboBox_G3.setDisabled(False)
                self.graphWidget_2.plotItem.clear()
                self.radioButton_3.hide()
                self.radioButton_4.hide()
                self.radioButton_5.show()
                self.radioButton_6.show()
                self.radioButton_5.setText(self._translate("MainWindow", "Flow"))
                self.radioButton_6.setText(self._translate("MainWindow", "Volume"))
                self.dockWidget_2.hide()
                self.dockWidget_3.show()
                self.actionWaveform.setChecked(False)
                self.text_heartinfo.setText(
                    "The heart is comprised of two atria and two ventricles. Blood enters the heart through the two atria and exits through the two ventricles."
                    "Deoxygenated blood enters the right atrium through the inferior and superior vena cava. The right side of the heart then pumps this deoxygenated"
                    "blood into the pulmonary arteries around the lungs. There, fresh oxygen enters the blood stream, and the blood moves to the left side of the heart."
                    "From the lungs, blood is brought to the left atrium through the pulmonary vein, and then to the left ventricle through the mitral valve, from where it"
                    "is pumped to the rest of the body.")
                self.label_heart.setPixmap(QtGui.QPixmap(
                    os.path.join('images', 'heart.png')))
            if not self.actionHeart_Parameter.isChecked():
                self.dockWidget_3.hide()
                self.dockWidget_2.show()
                self.actionWaveform.setChecked(True)

        def artery_model(self, MainWindow):
            try:
                self.showDock_2(MainWindow)
                self.comboBox_G1.setEnabled(True)
                self.comboBox_G2.setEnabled(True)
                self.radioButton_1.setEnabled(True)
                self.radioButton_2.setEnabled(True)
                self.radioButton_3.setEnabled(True)
                self.radioButton_4.setEnabled(True)
                H = self.doubleSpinBox_1.value()  # read HR value
                P = self.doubleSpinBox_2.value()  # read P value
                datas = stn_dat
                m = self.doubleSpinBox_4.value()
                r = self.doubleSpinBox_5.value()
                g = self.doubleSpinBox_6.value()
                STENOSIS.steno(m, r, g, **datas)
                self.clock, self.pulse = Artery_model.calc(H, P)
                self.c = np.all(self.clock != -1)
                self.p = np.all(self.pulse != -10000)
                self.alert('ARTERY MODEL EXECUTED')
                if self.c and self.p and (not Index == 0):
                    self.graphWidget_1.showGrid(x=True, y=True)
                    self.graphWidget_1.plot(self.clock, self.pulse[self.plot_p, :], pen=pg.mkPen('#3CAEA3', width=2))
                    self.graphWidget_1.setLabel('left', 'Pressure (mmHg)', **self.labelStyle)
                    self.graphWidget_1.plotItem.setLabel('bottom', 'Time (s)', **self.labelStyle)
                    self.statusbar.showMessage('PLOTTED', msecs=9000)
                    self.graphWidget_2.showGrid(x=True, y=True)
                    self.graphWidget_2.plot(self.clock, self.pulse[self.plot_p, :], pen=pg.mkPen('#3CAEA3', width=2))
                    self.graphWidget_2.setLabel('left', 'Pressure (mmHg)', **self.labelStyle)
                    self.graphWidget_2.setLabel('bottom', 'Time (s)', **self.labelStyle)
                    self.statusbar.showMessage('PLOTTED', msecs=9000)
            except Exception as e:
                self.alert(str(e))

        def cardiac_model(self):
            self.cv = 1
            H = self.doubleSpinBox_1.value()
            self.cardiac, self.ctime = CARDIAC.lumped(H, 5, 0.00015)
            self.actionHeart_Parameter.setChecked(True)
            self.showDock_3()
            self.alert('Heat Model Executed')

        def pressure_plot_1(self):
            self.graphWidget_1.plotItem.clear()
            plt = self.graphWidget_1
            Txt = self.comboBox_G1.currentText()
            plt.plot(self.clock, self.pulse[self.plot_p, :], pen=pg.mkPen(2, width=2), name=Txt)
            self.statusbar.showMessage('PLOTTED', msecs=5000)

        def pressure_plot_2(self):
            self.graphWidget_2.plotItem.clear()
            plt = self.graphWidget_2
            Txt = self.comboBox_G2.currentText()
            plt.plot(self.clock, self.pulse[self.plot_p, :], pen=pg.mkPen(2, width=2), name=Txt)
            self.statusbar.showMessage('PLOTTED', msecs=5000)

        def flow_plot_1(self):
            self.graphWidget_1.plotItem.clear()
            plt = self.graphWidget_1
            Txt = self.comboBox_G1.currentText()
            plt.plot(self.clock, self.pulse[self.plot_f, :], pen=pg.mkPen(2, width=2), name=Txt)
            self.statusbar.showMessage('PLOTTED', msecs=5000)

        def flow_plot_2(self):
            self.graphWidget_2.plotItem.clear()
            plt = self.graphWidget_2
            Txt = self.comboBox_G2.currentText()
            plt.plot(self.clock, self.pulse[self.plot_f, :], pen=pg.mkPen(2, width=2), name=Txt)
            self.statusbar.showMessage('PLOTTED', msecs=5000)

        def alert(self, msg):
            alert = QtWidgets.QMessageBox()
            alert.setWindowTitle("Alert!!")
            alert.setText(msg)
            alert.exec_()

        def help(self):
            help = QtWidgets.QMessageBox()
            help.setWindowIcon(QtGui.QIcon('images/logo.png'))
            help.setWindowTitle("Help")
            help.setText(
                "To run Artery model, go to \n\n RUN >> ARTERY MODEL\n\nTo run Heart model, go to \n\nRUN  HEART MODEL")
            help.exec_()

        def about(self):
            self.about = QtWidgets.QWidget()
            self.about.setWindowIcon(QtGui.QIcon('images/logo.png'))
            self.about.setWindowTitle("About")
            # self.about.setWindowFlag(QtCore.Qt.AA_EnableHighDpiScaling )#| QtCore.Qt.FramelessWindowHint)
            self.about.resize(800,400)
            self.about.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                     "color: rgb(255, 210, 119);\n")
            line_edit = QtWidgets.QTextBrowser(self.about)
            line_edit.setDisabled(1)
            layout = QtWidgets.QGridLayout(self.about)
            layout.addWidget(line_edit, 0,1,1,1)
            line_edit.setText(
                'BloodSim is an open-source software to simulate blood pressure, flow and volume waveforms in the cardiovascular system. Effect of stenosis on the pressure and flow of blood in the arterial tree is modelled.\n'
                '\nThe model is based on the following authors works,\n'
                '\nDr.Suganthi L     (Associate professor, Department of Biomedical Engineering, SSN college of Engineering)\n'
                '\nDr,Manivannan M     (Professor, Department of Applied Mechanics, Indian Institute of Technology, Madras)\n'
                '\nDr. Hemalatha K\n'
                '\nThe model is based on the following works,\n'
                '1.  HYBRID CARDIOPULMONARY INTERACTION MODEL TOWARDS NOVEL DIGNOSTIC TECHNIQUES\n'
                '2.  TAKAYASUS ARTERITIS – CLINICAL ANALYSIS, MODELING AND SIMULATION TOWARDS NOVEL DIAGNOSTIC TECHNIQUE\n'
                '\nThe software is developed in Python using Qt designer\n'
                '\nDevelopers\n\n'
                'Praveen Kumar S\n'
                'Arvindh Swaminathan MB\n')
            self.about.show()
            # return self.about

        def mainViewer_1(self):
            try:
                Id = self.comboBox_G1.currentIndex()
                self.graphWidget_1.plotItem.clear()
                gW1 = self.graphWidget_1
                Text = self.comboBox_G1.currentText()
                self.viewing(Id, Text, gW1)
                self.art_text_display(1)
            except:
                self.alert('error ocurred')

        def mainViewer_2(self):
            try:
                Id = self.comboBox_G2.currentIndex()
                self.graphWidget_2.plotItem.clear()
                gW2 = self.graphWidget_2
                Text = self.comboBox_G2.currentText()
                self.viewing(Id, Text, gW2)
                self.art_text_display(2)
            except:
                self.alert('error ocurred')

        def viewing(self, Index, Txt, plt):
            try:

                if Index == 1:
                    Pos = 0
                    self.plot_p = 1
                    self.plot_f = 0
                elif Index == 2:
                    Pos = 1
                    self.plot_p = 3
                    self.plot_f = 2
                elif Index == 3:
                    Pos = 7
                    self.plot_p = 7
                    self.plot_f = 6
                elif Index == 4:
                    Pos = 13
                    self.plot_p = 31
                    self.plot_f = 30
                elif Index == 5:
                    Pos = 3
                    self.plot_p = 53
                    self.plot_f = 52
                elif Index == 6:
                    Pos = 11
                    self.plot_p = 83
                    self.plot_f = 82
                elif Index == 7:
                    Pos = 10
                    self.plot_p = 113
                    self.plot_f = 112
                elif Index == 8:
                    Pos = 51
                    self.plot_p = 103
                    self.plot_f = 102
                elif Index == 9:
                    Pos = 46
                    self.plot_p = 75
                    self.plot_f = 74
                elif Index == 10:
                    Pos = 74
                    self.plot_p = 123
                    self.plot_f = 122
                elif Index == 11:
                    Pos = 56
                    self.plot_p = 207
                    self.plot_f = 206
                elif Index == 12:
                    Pos = 70
                    self.plot_p = 211
                    self.plot_f = 210
                elif Index == 13:
                    Pos = 62
                    self.plot_p = 131
                    self.plot_f = 130
                elif Index == 14:
                    Pos = 63
                    self.plot_p = 133
                    self.plot_f = 132
                elif Index == 15:
                    Pos = 108
                    self.plot_p = 149
                    self.plot_f = 148
                elif Index == 16:
                    Pos = 109
                    self.plot_p = 181
                    self.plot_f = 180
                elif Index == 17:
                    Pos = 102
                    self.plot_p = 249
                    self.plot_f = 248
                elif Index == 18:
                    Pos = 107
                    self.plot_p = 253
                    self.plot_f = 252
                elif Index == 19:
                    Pos = 96
                    self.plot_p = 251
                    self.plot_f = 250
                elif Index == 20:
                    Pos = 92
                    self.plot_p = 245
                    self.plot_f = 244

                if self.radioButton_1.isChecked() or self.radioButton_3.isChecked():
                    plt.plot(self.clock, self.pulse[self.plot_p][:], pen=pg.mkPen('#3CAEA3', width=2), name=Txt)
                elif self.radioButton_2.isChecked() or self.radioButton_4.isChecked():
                    plt.plot(self.clock, self.pulse[self.plot_f][:], pen=pg.mkPen('#3CAEA3', width=2), name=Txt)
                self.statusbar.showMessage('PLOTTED', msecs=10000)
            except:
                self.alert('error ocurred')

        def button_graph_1(self):
            if self.comboBox_G1.currentIndex() == 0 or self.comboBox_G2.currentIndex() == 1:
                self.alert('select an artery')
            else:
                index = self.comboBox_G1.currentIndex()
                if index == 1:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images', 'ascending_aorta.png')))
                    self.textBrowser_2.setText('The ascending aorta  is a portion of the commencing at the upper part '
                                               'of the base of the left ventricle, on a level with the lower border of '
                                               'the third costal cartilage behind the left half of the sternum. '
                                               'The upper limit of standard reference range of the ascending aorta '
                                               'may be up to 4.3 cm among large, elderly individuals. The ascending '
                                               'aorta is contained within the pericardium, and is enclosed in a tube of '
                                               'the serous pericardium, common to it and the pulmonary artery. The only '
                                               'branches of the ascending aorta are the two coronary arteries which '
                                               'supply the heart; they arise near the commencement of the aorta from '
                                               'the aortic sinuses which are opposite the aortic valve.')
                elif index == 2:
                    self.labelEdit_1.setPixmap(
                        QtGui.QPixmap(os.path.join('images/artery tree images', 'aortic_arch.png')))
                    self.textBrowser_2.setText(
                        'The aortic arch s the part of the aorta between the ascending and descending '
                        'aorta. The arch travels backward, so that it ultimately runs to the left of the'
                        'trachea. The aortic arch has three branches,'
                        '1.     brachiocephalic trunk'
                        '2.     left common carotid artery'
                        '3.     left subclavian artery'
                        'The aortic arch is the connection between the ascending and descending aorta,'
                        'and its central part is formed by the left 4th aortic arch during early '
                        'development.')
                elif index == 3:
                    self.labelEdit_1.setPixmap(
                        QtGui.QPixmap(os.path.join('images/artery tree images', 'subclavian_left.png')))
                    self.textBrowser_2.setText(
                        'The subclavian arteries are paired major arteries of the upper thorax, below'
                        ' the clavicle. They receive blood from the aortic arch. The left subclavian '
                        'artery supplies blood to the left arm and the right subclavian artery supplies'
                        ' blood to the right arm, with some branches supplying the head and thorax. '
                        'On the left side of the body, the subclavian comes directly off the aortic '
                        'arch, while on the right side it arises from the relatively short '
                        'brachiocephalic artery when it bifurcates into the subclavian and the '
                        'right common carotid artery. The first part of the left subclavian artery'
                        ' arises from the arch of the aorta, behind the left common carotid, and at the'
                        ' level of the fourth thoracic vertebra; it ascends in the superior mediastinal'
                        ' cavity to the root of the neck and then arches lateralward to the medial'
                        ' border of the Scalenus anterior.')
                elif index == 4:
                    self.labelEdit_1.setPixmap(
                        QtGui.QPixmap(os.path.join('images/artery tree images', 'subclavian_right.png')))
                    self.textBrowser_2.setText(
                        'The subclavian arteries are paired major arteries of the upper thorax, below'
                        ' the clavicle. They receive blood from the aortic arch. The left subclavian'
                        ' artery supplies blood to the left arm and the right subclavian artery'
                        ' supplies blood to the right arm, with some branches supplying the head'
                        ' and thorax. On the left side of the body, the subclavian comes directly'
                        ' off the aortic arch, while on the right side it arises from the relatively'
                        ' short brachiocephalic artery when it bifurcates into the subclavian and the'
                        ' right common carotid artery. The first part of the right subclavian artery'
                        ' arises from the brachiocephalic trunk, behind the upper part of the right'
                        ' sternoclavicular articulation, and passes upward and lateralward to the'
                        ' medial margin of the Scalenus anterior. It ascends a little above the'
                        ' clavicle, the extent to which it does so varying in different cases.')
                elif index == 5:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'common_carotid_left.png')))
                    self.textBrowser_2.setText(
                        'The common carotid arteries are present on the left and right sides of the'
                        ' body. These arteries originate from different arteries but follow'
                        ' symmetrical courses. The right common carotid originates in the neck from'
                        ' the brachiocephalic trunk; the left from the aortic arch in the thorax.'
                        ' These split into the external and internal carotid arteries at the upper'
                        ' border of the thyroid cartilage, at around the level of the fourth cervical'
                        ' vertebra. On the left, the common carotid arises directly from the aortic'
                        ' arch whereas, on the right, the origin is from the brachiocephaic trunk. The'
                        ' left common carotid artery can be thought of as having two distinct parts: '
                        'thoracic and cervical. Since the right common carotid arises cranially, '
                        'it only really has a cervical portion.In the thoracic section, the left '
                        'common carotid travels upwards through the superior mediastinum to the level'
                        ' of the left sternoclavicular joint where it is continuous with the '
                        'cervical portion.')
                elif index == 6:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'common_carotid_right.png')))
                    self.textBrowser_2.setText(
                        'The common carotid arteries are present on the left and right sides of the'
                        ' body. These arteries originate from different arteries but follow'
                        ' symmetrical courses. The right common carotid originates in the neck from'
                        ' the brachiocephalic trunk; the left from the aortic arch in the thorax.'
                        ' These split into the external and internal carotid arteries at the upper'
                        ' border of the thyroid cartilage, at around the level of the fourth cervical'
                        ' vertebra. On the left, the common carotid arises directly from the aortic'
                        ' arch whereas, on the right, the origin is from the brachiocephaic trunk. The'
                        ' left common carotid artery can be thought of as having two distinct parts: '
                        'thoracic and cervical. Since the right common carotid arises cranially, '
                        'it only really has a cervical portion.In the thoracic section, the left '
                        'common carotid travels upwards through the superior mediastinum to the level'
                        ' of the left sternoclavicular joint where it is continuous with the '
                        'cervical portion.')
                elif index == 7:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images', 'thoracic_aorta.png')))
                    self.textBrowser_2.setText('This artery supplies the anterior chest wall and the breasts. '
                                               'It is a paired artery, with one running along each side of the sternum, to'
                                               ' continue after its bifurcation as the superior epigastric and musculophrenic'
                                               ' arteries. The internal thoracic artery is the cardiac surgeons blood vessel'
                                               'of choice for coronary artery bypass grafting. The left ITA has a superior'
                                               'long-term patency to saphenous vein grafts[1][2] and other arterial grafts'
                                               '(e.g. radial artery, gastroepiploic artery) when grafted to the left anterior'
                                               'descending coronary artery, generally the most important vessel, clinically,'
                                               'to revascularize. Plastic surgeons may use either the left or right internal'
                                               ' thoracic arteries for autologous free flap reconstruction of the breast after'
                                               ' mastectomy. Usually, a microvascular anastomosis is performed at the second'
                                               ' intercostal space to the artery on which the free flap is based.')
                elif index == 8:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images', 'cereberal_artery_right.png')))
                    self.textBrowser_2.setText(
                        'The cerebral arteries describe three main pairs of arteries and their branches, '
                        'which perfuse the cerebrum of the brain. The three main arteries are '
                        'the:Anterior cerebral artery (ACA)'
                        'Middle cerebral artery (MCA)'
                        'Posterior cerebral artery (PCA)'
                        'Both the ACA and MCA originate from the cerebral portion of internal carotid '
                        'artery, while PCA branches from the intersection of the posterior '
                        'communicating artery and the anterior portion of the basilar artery. '
                        'The three pairs of arteries are linked via the anterior communicating '
                        'artery and the posterior communicating arteries. All three arteries send '
                        'out arteries that perforate brain in the medial central portions prior to '
                        'branching and bifurcating further. The arteries are usually divided into '
                        'different segments from 1–4 or 5 to denote how far the level of the branch'
                        ' with the lower numbers denoting vessels closer to the source artery. '
                        'Even though the arteries branching off these vessels retain some aspect '
                        'of constancy in terms of size and position, a great amount of variety in '
                        'topography, position, source and prominence nevertheless exists.')
                elif index == 9:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images', 'cereberal_artery_left.png')))
                    self.textBrowser_2.setText(
                        'The cerebral arteries describe three main pairs of arteries and their branches, '
                        'which perfuse the cerebrum of the brain. The three main arteries are '
                        'the:Anterior cerebral artery (ACA)'
                        'Middle cerebral artery (MCA)'
                        'Posterior cerebral artery (PCA)'
                        'Both the ACA and MCA originate from the cerebral portion of internal carotid '
                        'artery, while PCA branches from the intersection of the posterior '
                        'communicating artery and the anterior portion of the basilar artery. '
                        'The three pairs of arteries are linked via the anterior communicating '
                        'artery and the posterior communicating arteries. All three arteries send '
                        'out arteries that perforate brain in the medial central portions prior to '
                        'branching and bifurcating further. The arteries are usually divided into '
                        'different segments from 1–4 or 5 to denote how far the level of the branch'
                        ' with the lower numbers denoting vessels closer to the source artery. '
                        'Even though the arteries branching off these vessels retain some aspect '
                        'of constancy in terms of size and position, a great amount of variety in '
                        'topography, position, source and prominence nevertheless exists.')
                elif index == 10:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'abdominal_aorta.png')))
                    self.textBrowser_2.setText('The abdominal aorta is the largest artery in the abdominal cavity. '
                                               'As part of the aorta, it is a direct continuation of the descending aorta'
                                               ' (of the thorax)The abdominal aorta begins at the level of the diaphragm,'
                                               ' crossing it via the aortic hiatus, technically behind the diaphragm, at '
                                               'the vertebral level of T12. It travels down the posterior wall of the '
                                               'abdomen, anterior to the vertebral column. It thus follows the curvature of '
                                               'the lumbar vertebrae, that is, convex anteriorly. The peak of this convexity'
                                               ' is at the level of the third lumbar vertebra (L3). It runs parallel to the'
                                               ' inferior vena cava, which is located just to the right of the abdominal aorta,'
                                               ' and becomes smaller in diameter as it gives off branches. This is thought to '
                                               'be due to the large size of its principal branches. At the 11th rib, '
                                               'the diameter is 122mm long and 55mm wide and this is because of the constant'
                                               ' pressure. The abdominal aorta is clinically divided into 2 segments: '
                                               '>> The suprarenal abdominal or paravisceral segment, inferior to the diaphragm '
                                               'but superior to the renal arteries.'
                                               '>> The Infrarenal segment, inferior to the renal arteries and superior to '
                                               'the iliac bifurcation.')
                elif index == 11:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'brachial_right.png')))
                    self.textBrowser_2.setText('The brachial artery is the major blood vessel of the (upper) arm. It'
                                               ' is the continuation of the axillary artery beyond the lower margin of'
                                               ' teres major muscle. It continues down the ventral surface of the arm'
                                               ' until it reaches the cubital fossa at the elbow. It then divides into'
                                               ' the radial and ulnar arteries which run down the forearm.[1][2] In some '
                                               'individuals, the bifurcation occurs much earlier and the ulnar and radial'
                                               ' arteries extend through the upper arm. The pulse of the brachial artery is'
                                               ' palpable on the anterior aspect of the elbow, medial to the tendon of the'
                                               ' biceps, and, with the use of a stethoscope and sphygmomanometer'
                                               ' (blood pressure cuff) often used to measure the blood pressure.'
                                               'The brachial artery is closely related to the median nerve; in proximal'
                                               ' regions, the median nerve is immediately lateral to the brachial artery.'
                                               ' Distally, the median nerve crosses the medial side of the brachial artery'
                                               ' and lies anterior to the elbow joint.')
                elif index == 12:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'brachial_left.png')))
                    self.textBrowser_2.setText('The brachial artery is the major blood vessel of the (upper) arm. It'
                                               ' is the continuation of the axillary artery beyond the lower margin of'
                                               ' teres major muscle. It continues down the ventral surface of the arm'
                                               ' until it reaches the cubital fossa at the elbow. It then divides into'
                                               ' the radial and ulnar arteries which run down the forearm.[1][2] In some '
                                               'individuals, the bifurcation occurs much earlier and the ulnar and radial'
                                               ' arteries extend through the upper arm. The pulse of the brachial artery is'
                                               ' palpable on the anterior aspect of the elbow, medial to the tendon of the'
                                               ' biceps, and, with the use of a stethoscope and sphygmomanometer'
                                               ' (blood pressure cuff) often used to measure the blood pressure.'
                                               'The brachial artery is closely related to the median nerve; in proximal'
                                               ' regions, the median nerve is immediately lateral to the brachial artery.'
                                               ' Distally, the median nerve crosses the medial side of the brachial artery'
                                               ' and lies anterior to the elbow joint.')
                elif index == 13:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'hepatic_artery.png')))
                    self.textBrowser_2.setText('The common hepatic artery is a short blood vessel that supplies'
                                               ' oxygenated blood to the liver, pylorus of the stomach, duodenum,'
                                               ' pancreas, and gallbladder. It arises from the celiac artery and has the'
                                               ' following branches: hepatic artery proper - supplies the gallbladder'
                                               ' via the cystic artery and the liver via the left and right hepatic arteries.'
                                               '       gastroduodenal artery - branches into the right gastroepiploic artery'
                                               ' and superior pancreaticoduodenal artery· right gastric artery -  branches'
                                               ' to supply the lesser curvature of the stomach inferiorly')
                elif index == 14:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'renal_artery.png')))
                    self.textBrowser_2.setText(
                        'The renal arteries normally arise off the left interior side of the abdominal'
                        ' aorta, immediately below the superior mesenteric artery, and supply the'
                        ' kidneys with blood. Each is directed across the crus of the diaphragm, so'
                        ' as to form nearly a right angle. The renal arteries carry a large portion of'
                        ' total blood flow to the kidneys. Up to a third of total cardiac output can'
                        ' pass through the renal arteries to be filtered by the kidneys. One or two'
                        ' accessory renal arteries are frequently found, especially on the left side'
                        ' since they usually arise from the aorta, and may come off above (more common)'
                        ' or below the main artery. Instead of entering the kidney at the hilus, they'
                        ' usually pierce the upper or lower part of the organ.')
                elif index == 15:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'femoral_left.png')))
                    self.textBrowser_2.setText(
                        'The femoral artery is a large artery in the thigh and the main arterial '
                        'supply to the thigh and leg. It enters the thigh from behind the inguinal '
                        'ligament as the continuation of the external iliac artery. Here, it lies '
                        'midway between the anterior superior iliac spine and the symphysis pubis. '
                        'The femoral artery gives off the deep femoral artery or profunda femoris '
                        'artery and descends along the anteromedial part of the thigh in the femoral '
                        'triangle. It enters and passes through the adductor canal, and becomes the'
                        ' popliteal artery as it passes through the adductor hiatus in the adductor '
                        'magnus near the junction of the middle and distal thirds of the thigh. As the'
                        ' femoral artery can often be palpated through the skin, it is often used as a'
                        ' catheter access artery. From it, wires and catheters can be directed anywhere'
                        ' in the arterial system for intervention or diagnostics, including the heart,'
                        ' brain, kidneys, arms and legs.')
                elif index == 16:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'femoral_right.png')))
                    self.textBrowser_2.setText(
                        'The femoral artery is a large artery in the thigh and the main arterial '
                        'supply to the thigh and leg. It enters the thigh from behind the inguinal '
                        'ligament as the continuation of the external iliac artery. Here, it lies '
                        'midway between the anterior superior iliac spine and the symphysis pubis. '
                        'The femoral artery gives off the deep femoral artery or profunda femoris '
                        'artery and descends along the anteromedial part of the thigh in the femoral '
                        'triangle. It enters and passes through the adductor canal, and becomes the'
                        ' popliteal artery as it passes through the adductor hiatus in the adductor '
                        'magnus near the junction of the middle and distal thirds of the thigh. As the'
                        ' femoral artery can often be palpated through the skin, it is often used as a'
                        ' catheter access artery. From it, wires and catheters can be directed anywhere'
                        ' in the arterial system for intervention or diagnostics, including the heart,'
                        ' brain, kidneys, arms and legs.')
                elif index == 17:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'ulnar_left.png')))
                    self.textBrowser_2.setText(
                        'The ulnar artery is the main blood vessel, with oxygenated blood, of the'
                        ' medial aspect of the forearm. It arises from the brachial artery and'
                        ' terminates in the superficial palmar arch, which joins with the superficial'
                        ' branch of the radial artery. It is palpable on the anterior and medial aspect'
                        ' of the wrist. Along its course, it is accompanied by a similarly named vein'
                        ' or veins, the ulnar vein or ulnar veins. The ulnar artery, the larger of the'
                        ' two terminal branches of the brachial, begins a little below the bend of the'
                        ' elbow in the cubital fossa, and, passing obliquely downward, reaches the ulnar'
                        ' side of the forearm at a point about midway between the elbow and the wrist.'
                        ' It then runs along the ulnar border to the wrist, crosses the transverse'
                        ' carpal ligament on the radial side of the pisiform bone, and immediately'
                        ' beyond this bone divides into two branches, which enter into the formation'
                        ' of the superficial and deep volar arches.')
                elif index == 18:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'ulnar_right.png')))
                    self.textBrowser_2.setText(
                        'The ulnar artery is the main blood vessel, with oxygenated blood, of the'
                        ' medial aspect of the forearm. It arises from the brachial artery and'
                        ' terminates in the superficial palmar arch, which joins with the superficial'
                        ' branch of the radial artery. It is palpable on the anterior and medial aspect'
                        ' of the wrist. Along its course, it is accompanied by a similarly named vein'
                        ' or veins, the ulnar vein or ulnar veins. The ulnar artery, the larger of the'
                        ' two terminal branches of the brachial, begins a little below the bend of the'
                        ' elbow in the cubital fossa, and, passing obliquely downward, reaches the ulnar'
                        ' side of the forearm at a point about midway between the elbow and the wrist.'
                        ' It then runs along the ulnar border to the wrist, crosses the transverse'
                        ' carpal ligament on the radial side of the pisiform bone, and immediately'
                        ' beyond this bone divides into two branches, which enter into the formation'
                        ' of the superficial and deep volar arches.')
                elif index == 19:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'radial_right.png')))
                    self.textBrowser_2.setText(
                        'The radial artery arises from the bifurcation of the brachial artery in the'
                        ' antecubital fossa. It runs distally on the anterior part of the forearm. '
                        'There, it serves as a landmark for the division between the anterior and'
                        ' posterior compartments of the forearm, with the posterior compartment'
                        ' beginning just lateral to the artery. The artery winds laterally around'
                        ' the wrist, passing through the anatomical snuff box and between the heads'
                        ' of the first dorsal interosseous muscle. It passes anteriorly between the'
                        ' heads of the adductor pollicis, and becomes the deep palmar arch, which '
                        'joins with the deep branch of the ulnar artery. Along its course, it is'
                        ' accompanied by a similarly named vein, the radial vein. The named branches'
                        ' of the radial artery may be divided into three groups, corresponding with'
                        ' the three regions in which the vessel is situated. '
                        '>> In the forearm'
                        '>> At the wrist'
                        '>> In the hand')
                elif index == 20:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'radial_right.png')))
                    self.textBrowser_2.setText(
                        'The radial artery arises from the bifurcation of the brachial artery in the'
                        ' antecubital fossa. It runs distally on the anterior part of the forearm. '
                        'There, it serves as a landmark for the division between the anterior and'
                        ' posterior compartments of the forearm, with the posterior compartment'
                        ' beginning just lateral to the artery. The artery winds laterally around'
                        ' the wrist, passing through the anatomical snuff box and between the heads'
                        ' of the first dorsal interosseous muscle. It passes anteriorly between the'
                        ' heads of the adductor pollicis, and becomes the deep palmar arch, which '
                        'joins with the deep branch of the ulnar artery. Along its course, it is'
                        ' accompanied by a similarly named vein, the radial vein. The named branches'
                        ' of the radial artery may be divided into three groups, corresponding with'
                        ' the three regions in which the vessel is situated. '
                        '>> In the forearm'
                        '>> At the wrist'
                        '>> In the hand')
            self.p_Peak = self.pulse[self.plot_p, :].max()
            self.p_Peak = str(self.p_Peak)
            self.bottom = self.pulse[self.plot_p, :].min()
            self.Bottom = str(self.bottom)

        def button_graph_2(self):
            if self.comboBox_G1.currentIndex() == 0 or self.comboBox_G2.currentIndex() == 0:
                self.alert('select an artery')
            else:
                index = self.comboBox_G2.currentIndex()
                if index == 1:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'ascending_aorta.png')))
                    self.textBrowser_2.setText('The ascending aorta  is a portion of the commencing at the upper part '
                                               'of the base of the left ventricle, on a level with the lower border of '
                                               'the third costal cartilage behind the left half of the sternum. '
                                               'The upper limit of standard reference range of the ascending aorta '
                                               'may be up to 4.3 cm among large, elderly individuals. The ascending '
                                               'aorta is contained within the pericardium, and is enclosed in a tube of '
                                               'the serous pericardium, common to it and the pulmonary artery. The only '
                                               'branches of the ascending aorta are the two coronary arteries which '
                                               'supply the heart; they arise near the commencement of the aorta from '
                                               'the aortic sinuses which are opposite the aortic valve.')
                elif index == 2:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'aortic_arch.png')))
                    self.textBrowser_2.setText(
                        'The aortic arch s the part of the aorta between the ascending and descending '
                        'aorta. The arch travels backward, so that it ultimately runs to the left of the'
                        'trachea. The aortic arch has three branches,'
                        '1.     brachiocephalic trunk'
                        '2.     left common carotid artery'
                        '3.     left subclavian artery'
                        'The aortic arch is the connection between the ascending and descending aorta,'
                        'and its central part is formed by the left 4th aortic arch during early '
                        'development.')
                elif index == 3:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'subclavian_left.png')))
                    self.textBrowser_2.setText(
                        'The subclavian arteries are paired major arteries of the upper thorax, below'
                        ' the clavicle. They receive blood from the aortic arch. The left subclavian '
                        'artery supplies blood to the left arm and the right subclavian artery supplies'
                        ' blood to the right arm, with some branches supplying the head and thorax. '
                        'On the left side of the body, the subclavian comes directly off the aortic '
                        'arch, while on the right side it arises from the relatively short '
                        'brachiocephalic artery when it bifurcates into the subclavian and the '
                        'right common carotid artery. The first part of the left subclavian artery'
                        ' arises from the arch of the aorta, behind the left common carotid, and at the'
                        ' level of the fourth thoracic vertebra; it ascends in the superior mediastinal'
                        ' cavity to the root of the neck and then arches lateralward to the medial'
                        ' border of the Scalenus anterior.')
                elif index == 4:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'subclavian_right.png')))
                    self.textBrowser_2.setText(
                        'The subclavian arteries are paired major arteries of the upper thorax, below'
                        ' the clavicle. They receive blood from the aortic arch. The left subclavian'
                        ' artery supplies blood to the left arm and the right subclavian artery'
                        ' supplies blood to the right arm, with some branches supplying the head'
                        ' and thorax. On the left side of the body, the subclavian comes directly'
                        ' off the aortic arch, while on the right side it arises from the relatively'
                        ' short brachiocephalic artery when it bifurcates into the subclavian and the'
                        ' right common carotid artery. The first part of the right subclavian artery'
                        ' arises from the brachiocephalic trunk, behind the upper part of the right'
                        ' sternoclavicular articulation, and passes upward and lateralward to the'
                        ' medial margin of the Scalenus anterior. It ascends a little above the'
                        ' clavicle, the extent to which it does so varying in different cases.')
                elif index == 5:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'common_carotid_left.png')))
                    self.textBrowser_2.setText(
                        'The common carotid arteries are present on the left and right sides of the'
                        ' body. These arteries originate from different arteries but follow'
                        ' symmetrical courses. The right common carotid originates in the neck from'
                        ' the brachiocephalic trunk; the left from the aortic arch in the thorax.'
                        ' These split into the external and internal carotid arteries at the upper'
                        ' border of the thyroid cartilage, at around the level of the fourth cervical'
                        ' vertebra. On the left, the common carotid arises directly from the aortic'
                        ' arch whereas, on the right, the origin is from the brachiocephaic trunk. The'
                        ' left common carotid artery can be thought of as having two distinct parts: '
                        'thoracic and cervical. Since the right common carotid arises cranially, '
                        'it only really has a cervical portion.In the thoracic section, the left '
                        'common carotid travels upwards through the superior mediastinum to the level'
                        ' of the left sternoclavicular joint where it is continuous with the '
                        'cervical portion.')
                elif index == 6:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'common_carotid_right.png')))
                    self.textBrowser_2.setText(
                        'The common carotid arteries are present on the left and right sides of the'
                        ' body. These arteries originate from different arteries but follow'
                        ' symmetrical courses. The right common carotid originates in the neck from'
                        ' the brachiocephalic trunk; the left from the aortic arch in the thorax.'
                        ' These split into the external and internal carotid arteries at the upper'
                        ' border of the thyroid cartilage, at around the level of the fourth cervical'
                        ' vertebra. On the left, the common carotid arises directly from the aortic'
                        ' arch whereas, on the right, the origin is from the brachiocephaic trunk. The'
                        ' left common carotid artery can be thought of as having two distinct parts: '
                        'thoracic and cervical. Since the right common carotid arises cranially, '
                        'it only really has a cervical portion.In the thoracic section, the left '
                        'common carotid travels upwards through the superior mediastinum to the level'
                        ' of the left sternoclavicular joint where it is continuous with the '
                        'cervical portion.')
                elif index == 7:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'thoracic_aorta.png')))
                    self.textBrowser_2.setText('This artery supplies the anterior chest wall and the breasts. '
                                               'It is a paired artery, with one running along each side of the sternum, to'
                                               ' continue after its bifurcation as the superior epigastric and musculophrenic'
                                               ' arteries. The internal thoracic artery is the cardiac surgeons blood vessel'
                                               'of choice for coronary artery bypass grafting. The left ITA has a superior'
                                               'long-term patency to saphenous vein grafts[1][2] and other arterial grafts'
                                               '(e.g. radial artery, gastroepiploic artery) when grafted to the left anterior'
                                               'descending coronary artery, generally the most important vessel, clinically,'
                                               'to revascularize. Plastic surgeons may use either the left or right internal'
                                               ' thoracic arteries for autologous free flap reconstruction of the breast after'
                                               ' mastectomy. Usually, a microvascular anastomosis is performed at the second'
                                               ' intercostal space to the artery on which the free flap is based.')
                elif index == 8:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'cereberal_artery_right.png')))
                    self.textBrowser_2.setText(
                        'The cerebral arteries describe three main pairs of arteries and their branches, '
                        'which perfuse the cerebrum of the brain. The three main arteries are '
                        'the:Anterior cerebral artery (ACA)'
                        'Middle cerebral artery (MCA)'
                        'Posterior cerebral artery (PCA)'
                        'Both the ACA and MCA originate from the cerebral portion of internal carotid '
                        'artery, while PCA branches from the intersection of the posterior '
                        'communicating artery and the anterior portion of the basilar artery. '
                        'The three pairs of arteries are linked via the anterior communicating '
                        'artery and the posterior communicating arteries. All three arteries send '
                        'out arteries that perforate brain in the medial central portions prior to '
                        'branching and bifurcating further. The arteries are usually divided into '
                        'different segments from 1–4 or 5 to denote how far the level of the branch'
                        ' with the lower numbers denoting vessels closer to the source artery. '
                        'Even though the arteries branching off these vessels retain some aspect '
                        'of constancy in terms of size and position, a great amount of variety in '
                        'topography, position, source and prominence nevertheless exists.')
                elif index == 9:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'cereberal_artery_left.png')))
                    self.textBrowser_2.setText(
                        'The cerebral arteries describe three main pairs of arteries and their branches, '
                        'which perfuse the cerebrum of the brain. The three main arteries are '
                        'the:Anterior cerebral artery (ACA)'
                        'Middle cerebral artery (MCA)'
                        'Posterior cerebral artery (PCA)'
                        'Both the ACA and MCA originate from the cerebral portion of internal carotid '
                        'artery, while PCA branches from the intersection of the posterior '
                        'communicating artery and the anterior portion of the basilar artery. '
                        'The three pairs of arteries are linked via the anterior communicating '
                        'artery and the posterior communicating arteries. All three arteries send '
                        'out arteries that perforate brain in the medial central portions prior to '
                        'branching and bifurcating further. The arteries are usually divided into '
                        'different segments from 1–4 or 5 to denote how far the level of the branch'
                        ' with the lower numbers denoting vessels closer to the source artery. '
                        'Even though the arteries branching off these vessels retain some aspect '
                        'of constancy in terms of size and position, a great amount of variety in '
                        'topography, position, source and prominence nevertheless exists.')
                elif index == 10:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'abdominal_aorta.png')))
                    self.textBrowser_2.setText('The abdominal aorta is the largest artery in the abdominal cavity. '
                                               'As part of the aorta, it is a direct continuation of the descending aorta'
                                               ' (of the thorax)The abdominal aorta begins at the level of the diaphragm,'
                                               ' crossing it via the aortic hiatus, technically behind the diaphragm, at '
                                               'the vertebral level of T12. It travels down the posterior wall of the '
                                               'abdomen, anterior to the vertebral column. It thus follows the curvature of '
                                               'the lumbar vertebrae, that is, convex anteriorly. The peak of this convexity'
                                               ' is at the level of the third lumbar vertebra (L3). It runs parallel to the'
                                               ' inferior vena cava, which is located just to the right of the abdominal aorta,'
                                               ' and becomes smaller in diameter as it gives off branches. This is thought to '
                                               'be due to the large size of its principal branches. At the 11th rib, '
                                               'the diameter is 122mm long and 55mm wide and this is because of the constant'
                                               ' pressure. The abdominal aorta is clinically divided into 2 segments: '
                                               '>> The suprarenal abdominal or paravisceral segment, inferior to the diaphragm '
                                               'but superior to the renal arteries.'
                                               '>> The Infrarenal segment, inferior to the renal arteries and superior to '
                                               'the iliac bifurcation.')
                elif index == 11:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'brachial_right.png')))
                    self.textBrowser_2.setText('The brachial artery is the major blood vessel of the (upper) arm. It'
                                               ' is the continuation of the axillary artery beyond the lower margin of'
                                               ' teres major muscle. It continues down the ventral surface of the arm'
                                               ' until it reaches the cubital fossa at the elbow. It then divides into'
                                               ' the radial and ulnar arteries which run down the forearm.[1][2] In some '
                                               'individuals, the bifurcation occurs much earlier and the ulnar and radial'
                                               ' arteries extend through the upper arm. The pulse of the brachial artery is'
                                               ' palpable on the anterior aspect of the elbow, medial to the tendon of the'
                                               ' biceps, and, with the use of a stethoscope and sphygmomanometer'
                                               ' (blood pressure cuff) often used to measure the blood pressure.'
                                               'The brachial artery is closely related to the median nerve; in proximal'
                                               ' regions, the median nerve is immediately lateral to the brachial artery.'
                                               ' Distally, the median nerve crosses the medial side of the brachial artery'
                                               ' and lies anterior to the elbow joint.')
                elif index == 12:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'brachial_left.png')))
                    self.textBrowser_2.setText('The brachial artery is the major blood vessel of the (upper) arm. It'
                                               ' is the continuation of the axillary artery beyond the lower margin of'
                                               ' teres major muscle. It continues down the ventral surface of the arm'
                                               ' until it reaches the cubital fossa at the elbow. It then divides into'
                                               ' the radial and ulnar arteries which run down the forearm.[1][2] In some '
                                               'individuals, the bifurcation occurs much earlier and the ulnar and radial'
                                               ' arteries extend through the upper arm. The pulse of the brachial artery is'
                                               ' palpable on the anterior aspect of the elbow, medial to the tendon of the'
                                               ' biceps, and, with the use of a stethoscope and sphygmomanometer'
                                               ' (blood pressure cuff) often used to measure the blood pressure.'
                                               'The brachial artery is closely related to the median nerve; in proximal'
                                               ' regions, the median nerve is immediately lateral to the brachial artery.'
                                               ' Distally, the median nerve crosses the medial side of the brachial artery'
                                               ' and lies anterior to the elbow joint.')
                elif index == 13:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'hepatic_artery.png')))
                    self.textBrowser_2.setText('The common hepatic artery is a short blood vessel that supplies'
                                               ' oxygenated blood to the liver, pylorus of the stomach, duodenum,'
                                               ' pancreas, and gallbladder. It arises from the celiac artery and has the'
                                               ' following branches: hepatic artery proper - supplies the gallbladder'
                                               ' via the cystic artery and the liver via the left and right hepatic arteries.'
                                               '       gastroduodenal artery - branches into the right gastroepiploic artery'
                                               ' and superior pancreaticoduodenal artery· right gastric artery -  branches'
                                               ' to supply the lesser curvature of the stomach inferiorly')
                elif index == 14:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'renal_artery.png')))
                    self.textBrowser_2.setText(
                        'The renal arteries normally arise off the left interior side of the abdominal'
                        ' aorta, immediately below the superior mesenteric artery, and supply the'
                        ' kidneys with blood. Each is directed across the crus of the diaphragm, so'
                        ' as to form nearly a right angle. The renal arteries carry a large portion of'
                        ' total blood flow to the kidneys. Up to a third of total cardiac output can'
                        ' pass through the renal arteries to be filtered by the kidneys. One or two'
                        ' accessory renal arteries are frequently found, especially on the left side'
                        ' since they usually arise from the aorta, and may come off above (more common)'
                        ' or below the main artery. Instead of entering the kidney at the hilus, they'
                        ' usually pierce the upper or lower part of the organ.')
                elif index == 15:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'femoral_left.png')))
                    self.textBrowser_2.setText(
                        'The femoral artery is a large artery in the thigh and the main arterial '
                        'supply to the thigh and leg. It enters the thigh from behind the inguinal '
                        'ligament as the continuation of the external iliac artery. Here, it lies '
                        'midway between the anterior superior iliac spine and the symphysis pubis. '
                        'The femoral artery gives off the deep femoral artery or profunda femoris '
                        'artery and descends along the anteromedial part of the thigh in the femoral '
                        'triangle. It enters and passes through the adductor canal, and becomes the'
                        ' popliteal artery as it passes through the adductor hiatus in the adductor '
                        'magnus near the junction of the middle and distal thirds of the thigh. As the'
                        ' femoral artery can often be palpated through the skin, it is often used as a'
                        ' catheter access artery. From it, wires and catheters can be directed anywhere'
                        ' in the arterial system for intervention or diagnostics, including the heart,'
                        ' brain, kidneys, arms and legs.')
                elif index == 16:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'femoral_right.png')))
                    self.textBrowser_2.setText(
                        'The femoral artery is a large artery in the thigh and the main arterial '
                        'supply to the thigh and leg. It enters the thigh from behind the inguinal '
                        'ligament as the continuation of the external iliac artery. Here, it lies '
                        'midway between the anterior superior iliac spine and the symphysis pubis. '
                        'The femoral artery gives off the deep femoral artery or profunda femoris '
                        'artery and descends along the anteromedial part of the thigh in the femoral '
                        'triangle. It enters and passes through the adductor canal, and becomes the'
                        ' popliteal artery as it passes through the adductor hiatus in the adductor '
                        'magnus near the junction of the middle and distal thirds of the thigh. As the'
                        ' femoral artery can often be palpated through the skin, it is often used as a'
                        ' catheter access artery. From it, wires and catheters can be directed anywhere'
                        ' in the arterial system for intervention or diagnostics, including the heart,'
                        ' brain, kidneys, arms and legs.')
                elif index == 17:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'ulnar_left.png')))
                    self.textBrowser_2.setText(
                        'The ulnar artery is the main blood vessel, with oxygenated blood, of the'
                        ' medial aspect of the forearm. It arises from the brachial artery and'
                        ' terminates in the superficial palmar arch, which joins with the superficial'
                        ' branch of the radial artery. It is palpable on the anterior and medial aspect'
                        ' of the wrist. Along its course, it is accompanied by a similarly named vein'
                        ' or veins, the ulnar vein or ulnar veins. The ulnar artery, the larger of the'
                        ' two terminal branches of the brachial, begins a little below the bend of the'
                        ' elbow in the cubital fossa, and, passing obliquely downward, reaches the ulnar'
                        ' side of the forearm at a point about midway between the elbow and the wrist.'
                        ' It then runs along the ulnar border to the wrist, crosses the transverse'
                        ' carpal ligament on the radial side of the pisiform bone, and immediately'
                        ' beyond this bone divides into two branches, which enter into the formation'
                        ' of the superficial and deep volar arches.')
                elif index == 18:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'ulnar_right.png')))
                    self.textBrowser_2.setText(
                        'The ulnar artery is the main blood vessel, with oxygenated blood, of the'
                        ' medial aspect of the forearm. It arises from the brachial artery and'
                        ' terminates in the superficial palmar arch, which joins with the superficial'
                        ' branch of the radial artery. It is palpable on the anterior and medial aspect'
                        ' of the wrist. Along its course, it is accompanied by a similarly named vein'
                        ' or veins, the ulnar vein or ulnar veins. The ulnar artery, the larger of the'
                        ' two terminal branches of the brachial, begins a little below the bend of the'
                        ' elbow in the cubital fossa, and, passing obliquely downward, reaches the ulnar'
                        ' side of the forearm at a point about midway between the elbow and the wrist.'
                        ' It then runs along the ulnar border to the wrist, crosses the transverse'
                        ' carpal ligament on the radial side of the pisiform bone, and immediately'
                        ' beyond this bone divides into two branches, which enter into the formation'
                        ' of the superficial and deep volar arches.')
                elif index == 19:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'radial_right.png')))
                    self.textBrowser_2.setText(
                        'The radial artery arises from the bifurcation of the brachial artery in the'
                        ' antecubital fossa. It runs distally on the anterior part of the forearm. '
                        'There, it serves as a landmark for the division between the anterior and'
                        ' posterior compartments of the forearm, with the posterior compartment'
                        ' beginning just lateral to the artery. The artery winds laterally around'
                        ' the wrist, passing through the anatomical snuff box and between the heads'
                        ' of the first dorsal interosseous muscle. It passes anteriorly between the'
                        ' heads of the adductor pollicis, and becomes the deep palmar arch, which '
                        'joins with the deep branch of the ulnar artery. Along its course, it is'
                        ' accompanied by a similarly named vein, the radial vein. The named branches'
                        ' of the radial artery may be divided into three groups, corresponding with'
                        ' the three regions in which the vessel is situated. '
                        '>> In the forearm'
                        '>> At the wrist'
                        '>> In the hand')
                elif index == 20:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'radial_right.png')))
                    self.textBrowser_2.setText(
                        'The radial artery arises from the bifurcation of the brachial artery in the'
                        ' antecubital fossa. It runs distally on the anterior part of the forearm. '
                        'There, it serves as a landmark for the division between the anterior and'
                        ' posterior compartments of the forearm, with the posterior compartment'
                        ' beginning just lateral to the artery. The artery winds laterally around'
                        ' the wrist, passing through the anatomical snuff box and between the heads'
                        ' of the first dorsal interosseous muscle. It passes anteriorly between the'
                        ' heads of the adductor pollicis, and becomes the deep palmar arch, which '
                        'joins with the deep branch of the ulnar artery. Along its course, it is'
                        ' accompanied by a similarly named vein, the radial vein. The named branches'
                        ' of the radial artery may be divided into three groups, corresponding with'
                        ' the three regions in which the vessel is situated. '
                        '>> In the forearm'
                        '>> At the wrist'
                        '>> In the hand')

        def button_analyse(self):
            Index = self.comboBox_G1.currentIndex()
            Index1 = self.comboBox_G2.currentIndex()
            if Index == 0 or Index1 == 0:
                self.alert("Select a section")
            else:
                if Index == 1:
                    self.plot_p = 1
                    self.plot_f = 0
                elif Index == 2:
                    self.plot_p = 3
                    self.plot_f = 2
                elif Index == 3:
                    self.plot_p = 7
                    self.plot_f = 6
                elif Index == 4:
                    self.plot_p = 31
                    self.plot_f = 30
                elif Index == 5:
                    self.plot_p = 53
                    self.plot_f = 52
                elif Index == 6:
                    self.plot_p = 83
                    self.plot_f = 82
                elif Index == 7:
                    self.plot_p = 113
                    self.plot_f = 112
                elif Index == 8:
                    self.plot_p = 103
                    self.plot_f = 102
                elif Index == 9:
                    self.plot_p = 75
                    self.plot_f = 74
                elif Index == 10:
                    self.plot_p = 123
                    self.plot_f = 122
                elif Index == 11:
                    self.plot_p = 207
                    self.plot_f = 206
                elif Index == 12:
                    self.plot_p = 211
                    self.plot_f = 210
                elif Index == 13:
                    self.plot_p = 131
                    self.plot_f = 130
                elif Index == 14:
                    self.plot_p = 133
                    self.plot_f = 132
                elif Index == 15:
                    self.plot_p = 149
                    self.plot_f = 148
                elif Index == 16:
                    self.plot_p = 181
                    self.plot_f = 180
                elif Index == 17:
                    self.plot_p = 249
                    self.plot_f = 248
                elif Index == 18:
                    self.plot_p = 253
                    self.plot_f = 252
                elif Index == 19:
                    self.plot_p = 251
                    self.plot_f = 250
                elif Index == 20:
                    self.plot_p = 245
                    self.plot_f = 244

                self.pressure_max = str(self.pulse[self.plot_p, :].max())
                self.pressure_min = str(self.pulse[self.plot_p, :].min())
                self.flowmax = str(self.pulse[self.plot_f, :].max())
                self.flowmin = str(self.pulse[self.plot_f, :].min())

                if Index1 == 0:
                    self.alert("Select a section")
                elif Index1 == 1:
                    self.plot_p_2 = 1
                    self.plot_f_2 = 0
                elif Index1 == 2:
                    self.plot_p_2 = 3
                    self.plot_f_2 = 2
                elif Index1 == 3:
                    self.plot_p_2 = 7
                    self.plot_f_2 = 6
                elif Index1 == 4:
                    self.plot_p_2 = 31
                    self.plot_f_2 = 30
                elif Index1 == 5:
                    self.plot_p_2 = 53
                    self.plot_f_2 = 52
                elif Index1 == 6:
                    self.plot_p_2 = 83
                    self.plot_f_2 = 82
                elif Index1 == 7:
                    self.plot_p_2 = 113
                    self.plot_f_2 = 112
                elif Index1 == 8:
                    self.plot_p_2 = 103
                    self.plot_f_2 = 102
                elif Index1 == 9:
                    self.plot_p_2 = 75
                    self.plot_f_2 = 74
                elif Index1 == 10:
                    self.plot_p_2 = 123
                    self.plot_f_2 = 122
                elif Index1 == 11:
                    self.plot_p_2 = 207
                    self.plot_f_2 = 206
                elif Index1 == 12:
                    self.plot_p_2 = 211
                    self.plot_f_2 = 210
                elif Index1 == 13:
                    self.plot_p_2 = 131
                    self.plot_f_2 = 130
                elif Index1 == 14:
                    self.plot_p_2 = 133
                    self.plot_f_2 = 132
                elif Index1 == 15:
                    self.plot_p_2 = 149
                    self.plot_f_2 = 148
                elif Index1 == 16:
                    self.plot_p_2 = 181
                    self.plot_f_2 = 180
                elif Index1 == 17:
                    self.plot_p_2 = 249
                    self.plot_f_2 = 248
                elif Index1 == 18:
                    self.plot_p_2 = 253
                    self.plot_f_2 = 252
                elif Index1 == 19:
                    self.plot_p_2 = 251
                    self.plot_f_2 = 250
                elif Index1 == 20:
                    self.plot_p_2 = 245
                    self.plot_f_2 = 244
                self.pressure_max_2 = str(self.pulse[self.plot_p_2][:].max())
                self.pressure_min_2 = str(self.pulse[self.plot_p_2][:].min())
                self.flowmax_2 = str(self.pulse[self.plot_f_2, :].max())
                self.flowmin_2 = str(self.pulse[self.plot_f_2, :].min())

                self.textBrowser_2.setText(
                    'This section displays the features extracted from the blood pressure and flow waveforms simulated.'
                    '\n\n GRAPH-1\n\n'
                    'Selected waveform  -  %s\n'
                    '\nSBP   =  %s mm HG\n'
                    '\nDBP  =   %s mm Hg\n'
                    '\nPeak flow  =   %s mL/sec\n'
                    '\nMinimum flow  =  %s mL/sec\n'

                    '\n\nGRAPH-2 \n\n'
                    'Selected Waveform = %s\n'
                    '\nSBP  =  %s\n'
                    '\nDBP  =  %s\n'
                    '\nPeak flow  =  %s\n'
                    '\nMin Flow  =  %s\n'
                    % (self.comboBox_G1.currentText(), self.pressure_max, self.pressure_min, self.flowmax, self.flowmin,
                       self.comboBox_G2.currentText(), self.pressure_max_2, self.pressure_min_2, self.flowmax_2,
                       self.flowmin_2))

        def art_text_display(self, a):
            if a == 1:
                Id = self.comboBox_G1.currentIndex()
            elif a == 2:
                Id = self.comboBox_G2.currentIndex()
            if Id == 0:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images', 'art_tree_img.png')))
                self.textBrowser_2.setText(
                    'The primary function of the heart is to serve as a muscular pump propelling blood into and through vessels to and from all parts of the body. The arteries, which receive this blood at high pressure and velocity and conduct it throughout the body, have thick walls that are composed of elastic fibrous tissue and muscle cells. The arterial tree—the branching system of arteries—terminates in short, narrow, muscular vessels called arterioles, from which blood enters simple endothelial tubes (i.e., tubes formed of endothelial, or lining, cells) known as capillaries. These thin, microscopic capillaries are permeable to vital cellular nutrients and waste products that they receive and distribute. From the capillaries, the blood, now depleted of oxygen and burdened with waste products, moving more slowly and under low pressure, enters small vessels called venules that converge to form veins, ultimately guiding the blood on its way back to the heart.')

            elif Id == 1:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'ascending_aorta.png')))
                self.textBrowser_2.setText(
                    'The ascending aorta  is a portion of the commencing at the upper part of the base of the left ventricle, on a level with the lower border of the third costal cartilage behind the left half of the sternum. The upper limit of standard reference range of the ascending aorta may be up to 4.3 cm among large, elderly individuals. The ascending aorta is contained within the pericardium, and is enclosed in a tube of the serous pericardium, common to it and the pulmonary artery. The only branches of the ascending aorta are the two coronary arteries which supply the heart; they arise near the commencement of the aorta from the aortic sinuses which are opposite the aortic valve.')

            elif Id == 2:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'aortic_arch.png')))
                self.textBrowser_2.setText(
                    'The aortic arch s the part of the aorta between the ascending and descending aorta. The arch travels backward, so that it ultimately runs to the left of the trachea. \n'
                    '\nThe aortic arch has three branches,\n\n1.    brachiocephalic trunk\n2.  left common carotid artery\n3. left subclavian artery\n\nThe aortic arch is the connection between the ascending and descending aorta, and its central part is formed by the left 4th aortic arch during early development.')

            elif Id == 3:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'subclavian_left.png')))
                self.textBrowser_2.setText(
                    'The subclavian arteries are paired major arteries of the upper thorax, below'
                    ' the clavicle. They receive blood from the aortic arch. The left subclavian '
                    'artery supplies blood to the left arm and the right subclavian artery supplies'
                    ' blood to the right arm, with some branches supplying the head and thorax. '
                    'On the left side of the body, the subclavian comes directly off the aortic '
                    'arch, while on the right side it arises from the relatively short '
                    'brachiocephalic artery when it bifurcates into the subclavian and the '
                    'right common carotid artery. The first part of the left subclavian artery'
                    ' arises from the arch of the aorta, behind the left common carotid, and at the'
                    ' level of the fourth thoracic vertebra; it ascends in the superior mediastinal'
                    ' cavity to the root of the neck and then arches lateralward to the medial'
                    ' border of the Scalenus anterior.')
            elif Id == 4:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'subclavian_right.png')))
                self.textBrowser_2.setText(
                    'The subclavian arteries are paired major arteries of the upper thorax, below'
                    ' the clavicle. They receive blood from the aortic arch. The left subclavian'
                    ' artery supplies blood to the left arm and the right subclavian artery'
                    ' supplies blood to the right arm, with some branches supplying the head'
                    ' and thorax. On the left side of the body, the subclavian comes directly'
                    ' off the aortic arch, while on the right side it arises from the relatively'
                    ' short brachiocephalic artery when it bifurcates into the subclavian and the'
                    ' right common carotid artery. The first part of the right subclavian artery'
                    ' arises from the brachiocephalic trunk, behind the upper part of the right'
                    ' sternoclavicular articulation, and passes upward and lateralward to the'
                    ' medial margin of the Scalenus anterior. It ascends a little above the'
                    ' clavicle, the extent to which it does so varying in different cases.')
            elif Id == 5:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'common_carotid_left.png')))
                self.textBrowser_2.setText('The common carotid arteries are present on the left and right sides of the'
                                           ' body. These arteries originate from different arteries but follow'
                                           ' symmetrical courses. The right common carotid originates in the neck from'
                                           ' the brachiocephalic trunk; the left from the aortic arch in the thorax.'
                                           ' These split into the external and internal carotid arteries at the upper'
                                           ' border of the thyroid cartilage, at around the level of the fourth cervical'
                                           ' vertebra. On the left, the common carotid arises directly from the aortic'
                                           ' arch whereas, on the right, the origin is from the brachiocephaic trunk. The'
                                           ' left common carotid artery can be thought of as having two distinct parts: '
                                           'thoracic and cervical. Since the right common carotid arises cranially, '
                                           'it only really has a cervical portion.In the thoracic section, the left '
                                           'common carotid travels upwards through the superior mediastinum to the level'
                                           ' of the left sternoclavicular joint where it is continuous with the '
                                           'cervical portion.')
            elif Id == 6:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images', 'common_carotid_right.png')))
                self.textBrowser_2.setText('The common carotid arteries are present on the left and right sides of the'
                                           ' body. These arteries originate from different arteries but follow'
                                           ' symmetrical courses. The right common carotid originates in the neck from'
                                           ' the brachiocephalic trunk; the left from the aortic arch in the thorax.'
                                           ' These split into the external and internal carotid arteries at the upper'
                                           ' border of the thyroid cartilage, at around the level of the fourth cervical'
                                           ' vertebra. On the left, the common carotid arises directly from the aortic'
                                           ' arch whereas, on the right, the origin is from the brachiocephaic trunk. The'
                                           ' left common carotid artery can be thought of as having two distinct parts: '
                                           'thoracic and cervical. Since the right common carotid arises cranially, '
                                           'it only really has a cervical portion.In the thoracic section, the left '
                                           'common carotid travels upwards through the superior mediastinum to the level'
                                           ' of the left sternoclavicular joint where it is continuous with the '
                                           'cervical portion.')
            elif Id == 7:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'thoracic_aorta.png')))
                self.textBrowser_2.setText('This artery supplies the anterior chest wall and the breasts. '
                                           'It is a paired artery, with one running along each side of the sternum, to'
                                           ' continue after its bifurcation as the superior epigastric and musculophrenic'
                                           ' arteries. The internal thoracic artery is the cardiac surgeons blood vessel'
                                           'of choice for coronary artery bypass grafting. The left ITA has a superior'
                                           'long-term patency to saphenous vein grafts[1][2] and other arterial grafts'
                                           '(e.g. radial artery, gastroepiploic artery) when grafted to the left anterior'
                                           'descending coronary artery, generally the most important vessel, clinically,'
                                           'to revascularize. Plastic surgeons may use either the left or right internal'
                                           ' thoracic arteries for autologous free flap reconstruction of the breast after'
                                           ' mastectomy. Usually, a microvascular anastomosis is performed at the second'
                                           ' intercostal space to the artery on which the free flap is based.')
            elif Id == 8:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'cereberal_artery_right.png')))
                self.textBrowser_2.setText(
                    'The cerebral arteries describe three main pairs of arteries and their branches, '
                    'which perfuse the cerebrum of the brain. The three main arteries are '
                    'the:Anterior cerebral artery (ACA)'
                    'Middle cerebral artery (MCA)'
                    'Posterior cerebral artery (PCA)'
                    'Both the ACA and MCA originate from the cerebral portion of internal carotid '
                    'artery, while PCA branches from the intersection of the posterior '
                    'communicating artery and the anterior portion of the basilar artery. '
                    'The three pairs of arteries are linked via the anterior communicating '
                    'artery and the posterior communicating arteries. All three arteries send '
                    'out arteries that perforate brain in the medial central portions prior to '
                    'branching and bifurcating further. The arteries are usually divided into '
                    'different segments from 1–4 or 5 to denote how far the level of the branch'
                    ' with the lower numbers denoting vessels closer to the source artery. '
                    'Even though the arteries branching off these vessels retain some aspect '
                    'of constancy in terms of size and position, a great amount of variety in '
                    'topography, position, source and prominence nevertheless exists.')
            elif Id == 9:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'cereberal_artery_left.png')))
                self.textBrowser_2.setText(
                    'The cerebral arteries describe three main pairs of arteries and their branches, '
                    'which perfuse the cerebrum of the brain. The three main arteries are '
                    'the:Anterior cerebral artery (ACA)'
                    'Middle cerebral artery (MCA)'
                    'Posterior cerebral artery (PCA)'
                    'Both the ACA and MCA originate from the cerebral portion of internal carotid '
                    'artery, while PCA branches from the intersection of the posterior '
                    'communicating artery and the anterior portion of the basilar artery. '
                    'The three pairs of arteries are linked via the anterior communicating '
                    'artery and the posterior communicating arteries. All three arteries send '
                    'out arteries that perforate brain in the medial central portions prior to '
                    'branching and bifurcating further. The arteries are usually divided into '
                    'different segments from 1–4 or 5 to denote how far the level of the branch'
                    ' with the lower numbers denoting vessels closer to the source artery. '
                    'Even though the arteries branching off these vessels retain some aspect '
                    'of constancy in terms of size and position, a great amount of variety in '
                    'topography, position, source and prominence nevertheless exists.')
            elif Id == 10:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'abdominal_aorta.png')))
                self.textBrowser_2.setText('The abdominal aorta is the largest artery in the abdominal cavity. '
                                           'As part of the aorta, it is a direct continuation of the descending aorta'
                                           ' (of the thorax)The abdominal aorta begins at the level of the diaphragm,'
                                           ' crossing it via the aortic hiatus, technically behind the diaphragm, at '
                                           'the vertebral level of T12. It travels down the posterior wall of the '
                                           'abdomen, anterior to the vertebral column. It thus follows the curvature of '
                                           'the lumbar vertebrae, that is, convex anteriorly. The peak of this convexity'
                                           ' is at the level of the third lumbar vertebra (L3). It runs parallel to the'
                                           ' inferior vena cava, which is located just to the right of the abdominal aorta,'
                                           ' and becomes smaller in diameter as it gives off branches. This is thought to '
                                           'be due to the large size of its principal branches. At the 11th rib, '
                                           'the diameter is 122mm long and 55mm wide and this is because of the constant'
                                           ' pressure. The abdominal aorta is clinically divided into 2 segments: '
                                           '>> The suprarenal abdominal or paravisceral segment, inferior to the diaphragm '
                                           'but superior to the renal arteries.'
                                           '>> The Infrarenal segment, inferior to the renal arteries and superior to '
                                           'the iliac bifurcation.')
            elif Id == 11:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'brachial_right.png')))
                self.textBrowser_2.setText('The brachial artery is the major blood vessel of the (upper) arm. It'
                                           ' is the continuation of the axillary artery beyond the lower margin of'
                                           ' teres major muscle. It continues down the ventral surface of the arm'
                                           ' until it reaches the cubital fossa at the elbow. It then divides into'
                                           ' the radial and ulnar arteries which run down the forearm.[1][2] In some '
                                           'individuals, the bifurcation occurs much earlier and the ulnar and radial'
                                           ' arteries extend through the upper arm. The pulse of the brachial artery is'
                                           ' palpable on the anterior aspect of the elbow, medial to the tendon of the'
                                           ' biceps, and, with the use of a stethoscope and sphygmomanometer'
                                           ' (blood pressure cuff) often used to measure the blood pressure.'
                                           'The brachial artery is closely related to the median nerve; in proximal'
                                           ' regions, the median nerve is immediately lateral to the brachial artery.'
                                           ' Distally, the median nerve crosses the medial side of the brachial artery'
                                           ' and lies anterior to the elbow joint.')
            elif Id == 12:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'brachial_left.png')))
                self.textBrowser_2.setText('The brachial artery is the major blood vessel of the (upper) arm. It'
                                           ' is the continuation of the axillary artery beyond the lower margin of'
                                           ' teres major muscle. It continues down the ventral surface of the arm'
                                           ' until it reaches the cubital fossa at the elbow. It then divides into'
                                           ' the radial and ulnar arteries which run down the forearm.[1][2] In some '
                                           'individuals, the bifurcation occurs much earlier and the ulnar and radial'
                                           ' arteries extend through the upper arm. The pulse of the brachial artery is'
                                           ' palpable on the anterior aspect of the elbow, medial to the tendon of the'
                                           ' biceps, and, with the use of a stethoscope and sphygmomanometer'
                                           ' (blood pressure cuff) often used to measure the blood pressure.'
                                           'The brachial artery is closely related to the median nerve; in proximal'
                                           ' regions, the median nerve is immediately lateral to the brachial artery.'
                                           ' Distally, the median nerve crosses the medial side of the brachial artery'
                                           ' and lies anterior to the elbow joint.')
            elif Id == 13:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'hepatic_artery.png')))
                self.textBrowser_2.setText('The common hepatic artery is a short blood vessel that supplies'
                                           ' oxygenated blood to the liver, pylorus of the stomach, duodenum,'
                                           ' pancreas, and gallbladder. It arises from the celiac artery and has the'
                                           ' following branches: hepatic artery proper - supplies the gallbladder'
                                           ' via the cystic artery and the liver via the left and right hepatic arteries.'
                                           '       gastroduodenal artery - branches into the right gastroepiploic artery'
                                           ' and superior pancreaticoduodenal artery· right gastric artery -  branches'
                                           ' to supply the lesser curvature of the stomach inferiorly')
            elif Id == 14:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'renal_artery.png')))
                self.textBrowser_2.setText(
                    'The renal arteries normally arise off the left interior side of the abdominal'
                    ' aorta, immediately below the superior mesenteric artery, and supply the'
                    ' kidneys with blood. Each is directed across the crus of the diaphragm, so'
                    ' as to form nearly a right angle. The renal arteries carry a large portion of'
                    ' total blood flow to the kidneys. Up to a third of total cardiac output can'
                    ' pass through the renal arteries to be filtered by the kidneys. One or two'
                    ' accessory renal arteries are frequently found, especially on the left side'
                    ' since they usually arise from the aorta, and may come off above (more common)'
                    ' or below the main artery. Instead of entering the kidney at the hilus, they'
                    ' usually pierce the upper or lower part of the organ.')
            elif Id == 15:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'femoral_left.png')))
                self.textBrowser_2.setText('The femoral artery is a large artery in the thigh and the main arterial '
                                           'supply to the thigh and leg. It enters the thigh from behind the inguinal '
                                           'ligament as the continuation of the external iliac artery. Here, it lies '
                                           'midway between the anterior superior iliac spine and the symphysis pubis. '
                                           'The femoral artery gives off the deep femoral artery or profunda femoris '
                                           'artery and descends along the anteromedial part of the thigh in the femoral '
                                           'triangle. It enters and passes through the adductor canal, and becomes the'
                                           ' popliteal artery as it passes through the adductor hiatus in the adductor '
                                           'magnus near the junction of the middle and distal thirds of the thigh. As the'
                                           ' femoral artery can often be palpated through the skin, it is often used as a'
                                           ' catheter access artery. From it, wires and catheters can be directed anywhere'
                                           ' in the arterial system for intervention or diagnostics, including the heart,'
                                           ' brain, kidneys, arms and legs.')
            elif Id == 16:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'femoral_right.png')))
                self.textBrowser_2.setText('The femoral artery is a large artery in the thigh and the main arterial '
                                           'supply to the thigh and leg. It enters the thigh from behind the inguinal '
                                           'ligament as the continuation of the external iliac artery. Here, it lies '
                                           'midway between the anterior superior iliac spine and the symphysis pubis. '
                                           'The femoral artery gives off the deep femoral artery or profunda femoris '
                                           'artery and descends along the anteromedial part of the thigh in the femoral '
                                           'triangle. It enters and passes through the adductor canal, and becomes the'
                                           ' popliteal artery as it passes through the adductor hiatus in the adductor '
                                           'magnus near the junction of the middle and distal thirds of the thigh. As the'
                                           ' femoral artery can often be palpated through the skin, it is often used as a'
                                           ' catheter access artery. From it, wires and catheters can be directed anywhere'
                                           ' in the arterial system for intervention or diagnostics, including the heart,'
                                           ' brain, kidneys, arms and legs.')
            elif Id == 17:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'ulnar_left.png')))
                self.textBrowser_2.setText('The ulnar artery is the main blood vessel, with oxygenated blood, of the'
                                           ' medial aspect of the forearm. It arises from the brachial artery and'
                                           ' terminates in the superficial palmar arch, which joins with the superficial'
                                           ' branch of the radial artery. It is palpable on the anterior and medial aspect'
                                           ' of the wrist. Along its course, it is accompanied by a similarly named vein'
                                           ' or veins, the ulnar vein or ulnar veins. The ulnar artery, the larger of the'
                                           ' two terminal branches of the brachial, begins a little below the bend of the'
                                           ' elbow in the cubital fossa, and, passing obliquely downward, reaches the ulnar'
                                           ' side of the forearm at a point about midway between the elbow and the wrist.'
                                           ' It then runs along the ulnar border to the wrist, crosses the transverse'
                                           ' carpal ligament on the radial side of the pisiform bone, and immediately'
                                           ' beyond this bone divides into two branches, which enter into the formation'
                                           ' of the superficial and deep volar arches.')
            elif Id == 18:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'ulnar_right.png')))
                self.textBrowser_2.setText('The ulnar artery is the main blood vessel, with oxygenated blood, of the'
                                           ' medial aspect of the forearm. It arises from the brachial artery and'
                                           ' terminates in the superficial palmar arch, which joins with the superficial'
                                           ' branch of the radial artery. It is palpable on the anterior and medial aspect'
                                           ' of the wrist. Along its course, it is accompanied by a similarly named vein'
                                           ' or veins, the ulnar vein or ulnar veins. The ulnar artery, the larger of the'
                                           ' two terminal branches of the brachial, begins a little below the bend of the'
                                           ' elbow in the cubital fossa, and, passing obliquely downward, reaches the ulnar'
                                           ' side of the forearm at a point about midway between the elbow and the wrist.'
                                           ' It then runs along the ulnar border to the wrist, crosses the transverse'
                                           ' carpal ligament on the radial side of the pisiform bone, and immediately'
                                           ' beyond this bone divides into two branches, which enter into the formation'
                                           ' of the superficial and deep volar arches.')
            elif Id == 19:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'radial_right.png')))
                self.textBrowser_2.setText('The radial artery arises from the bifurcation of the brachial artery in the'
                                           ' antecubital fossa. It runs distally on the anterior part of the forearm. '
                                           'There, it serves as a landmark for the division between the anterior and'
                                           ' posterior compartments of the forearm, with the posterior compartment'
                                           ' beginning just lateral to the artery. The artery winds laterally around'
                                           ' the wrist, passing through the anatomical snuff box and between the heads'
                                           ' of the first dorsal interosseous muscle. It passes anteriorly between the'
                                           ' heads of the adductor pollicis, and becomes the deep palmar arch, which '
                                           'joins with the deep branch of the ulnar artery. Along its course, it is'
                                           ' accompanied by a similarly named vein, the radial vein. The named branches'
                                           ' of the radial artery may be divided into three groups, corresponding with'
                                           ' the three regions in which the vessel is situated. '
                                           '>> In the forearm'
                                           '>> At the wrist'
                                           '>> In the hand')
            elif Id == 20:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'radial_right.png')))
                self.textBrowser_2.setText('The radial artery arises from the bifurcation of the brachial artery in the'
                                           ' antecubital fossa. It runs distally on the anterior part of the forearm. '
                                           'There, it serves as a landmark for the division between the anterior and'
                                           ' posterior compartments of the forearm, with the posterior compartment'
                                           ' beginning just lateral to the artery. The artery winds laterally around'
                                           ' the wrist, passing through the anatomical snuff box and between the heads'
                                           ' of the first dorsal interosseous muscle. It passes anteriorly between the'
                                           ' heads of the adductor pollicis, and becomes the deep palmar arch, which '
                                           'joins with the deep branch of the ulnar artery. Along its course, it is'
                                           ' accompanied by a similarly named vein, the radial vein. The named branches'
                                           ' of the radial artery may be divided into three groups, corresponding with'
                                           ' the three regions in which the vessel is situated. '
                                           '>> In the forearm'
                                           '>> At the wrist'
                                           '>> In the hand')

        def button_chambers(self):
            self.radioButton_6.setDisabled(False)
            self.bc = 1
            if self.cv == 1:
                self.comboBox_G3.clear()
                for i in range(5):
                    self.comboBox_G3.addItem("")
                self.comboBox_G3.setItemText(0, self._translate("MainWindow", "Select section"))
                self.comboBox_G3.setItemText(1, self._translate("MainWindow", "Left atrium"))
                self.comboBox_G3.setItemText(2, self._translate("MainWindow", "Left ventricle"))
                self.comboBox_G3.setItemText(3, self._translate("MainWindow", "Right atrium"))
                self.comboBox_G3.setItemText(4, self._translate("MainWindow", "Right ventricle"))
                self.label_heart.clear()
                self.label_heart.setPixmap(QtGui.QPixmap(
                    os.path.join('images', 'chambers.png')))
                self.text_heartinfo.setText(
                    "The heart is comprised of two atria and two ventricles. Blood enters the heart through the two atria "
                    "and exits through the two ventricles. Deoxygenated blood enters the right atrium through the inferior "
                    "and superior vena cava. The right side of the heart then pumps this deoxygenated blood into the "
                    "pulmonary arteries around the lungs. There, fresh oxygen enters the blood stream, and the blood moves "
                    "to the left side of the heart. From the lungs, blood is brought to the left atrium through the "
                    "pulmonary vein, and then to the left ventricle through the mitral valve, from where it is pumped to "
                    "the rest of the body.")
                self.comboBox_G3.currentIndexChanged.connect(self.chamber_plot)
            else:
                self.alert("Run Heart Model!!")

        def button_valves(self):
            self.bc = 2
            self.radioButton_6.setDisabled(True)
            if self.cv == 1:
                self.comboBox_G3.clear()
                for i in range(5):
                    self.comboBox_G3.addItem("")
                self.comboBox_G3.setItemText(0, self._translate("MainWindow", "Select section"))
                self.comboBox_G3.setItemText(1, self._translate("MainWindow", "Mitral valve"))
                self.comboBox_G3.setItemText(2, self._translate("MainWindow", "Tricuspid valve"))
                self.comboBox_G3.setItemText(3, self._translate("MainWindow", "Aortic valve"))
                self.comboBox_G3.setItemText(4, self._translate("MainWindow", "Pulmonary valve"))
                self.label_heart.clear()
                self.text_heartinfo.clear()
                self.label_heart.setPixmap(QtGui.QPixmap(
                    os.path.join('images', 'valves.png')))
                self.text_heartinfo.setText(
                    "The heart has four valves - one for each chamber of the heart. The valves keep blood moving through "
                    "the heart in the right direction. The mitral valve and tricuspid valve are located between the atria "
                    "and the ventricles. The aortic valve and pulmonic valve are located between the ventricles and the "
                    "major blood vessels leaving the heart. The four valves are to open and close to let blood flow "
                    "through the heart. The valves prevent the backward flow of blood. Valves are actually flaps (leaflets)"
                    "that act as one-way inlets for blood coming into a ventricle and one-way outlets for blood leaving a "
                    "ventricle. Normal valves have 3 flaps (leaflets), except the mitral valve. It only has 2 flaps.")

                self.comboBox_G3.currentIndexChanged.connect(self.valve_plot)
            else:
                self.alert("Run Heart Model!!")

        def button_iandolet(self):
            self.bc = 3
            self.radioButton_6.setDisabled(False)
            if self.cv == 1:
                self.comboBox_G3.clear()
                for i in range(5):
                    self.comboBox_G3.addItem("")
                self.comboBox_G3.setItemText(0, self._translate("MainWindow", "select section"))
                self.comboBox_G3.setItemText(1, self._translate("MainWindow", "Aorta"))
                self.comboBox_G3.setItemText(2, self._translate("MainWindow", "Pulmonary artery"))
                self.comboBox_G3.setItemText(3, self._translate("MainWindow", "Vena cava"))
                self.comboBox_G3.setItemText(4, self._translate("MainWindow", "Pulmonary vein"))
                self.label_heart.clear()
                self.text_heartinfo.clear()
                self.label_heart.setPixmap(QtGui.QPixmap(
                    os.path.join('images', 'iandolets.png')))

                self.text_heartinfo.setText(
                    "This section is about the volume and flow representation of some of the major blood vessels that "
                    "deliver blood to and from the heart. This section also involves the modelling of the arterioles "
                    "and venules that deliver blood within the heart, to the heart muscles.")
                self.comboBox_G3.currentIndexChanged.connect(self.iandolet_plot)
            else:
                self.alert("Run Heart Model!!")

        def chamber_plot(self):
            self.graphWidget_2.plotItem.clear()
            total = len(self.ctime)
            self.graphWidget_2.setLabel('left', 'Volume', **self.labelStyle)
            self.graphWidget_2.setLabel('bottom', 'Time (s)', **self.labelStyle)
            if self.comboBox_G3.currentIndex() == 1:
                self.label_heart.setPixmap(QtGui.QPixmap(os.path.join('images', 'left_atrium.png')))
                self.text_heartinfo.setText(
                    "The left atrium is located on the left posterior of the heart. It acts as a holding chamber for blood returning from the lungs and to act as a pump to transport blood to other areas of the heart. The walls of the left atrium are slightly thicker than the walls of the right atrium. Oxygen-rich blood from the lungs enters the left atrium through the pulmonary vein. The blood is then pumped into the left ventricle chamber of the heart through the mitral valve.")
                if self.radioButton_5.isChecked():
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 20], pen=pg.mkPen('#3CAEA3', width=2))
                elif self.radioButton_6.isChecked():
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 19], pen=pg.mkPen('#3CAEA3', width=2))

            elif self.comboBox_G3.currentIndex() == 2:
                self.label_heart.setPixmap(QtGui.QPixmap(os.path.join('images', 'left_ventricle.png')))
                self.text_heartinfo.setText(
                    "The left Ventricle is located on the left side of the heart, below the left atrium. It is separated from the atrium by the mitral valve. Of all the chambers, the left ventricle has the thickest wall. The blood coming from the left atrium is pumped by this chamber to the rest of the body through the aorta. The valve between the left ventricle and the aorta is the aortic valve. The left ventricle is separated from the right by the intra ventricular septum. The contraction of the left ventricle corresponds to the QRS complex in the electrocardiogram.")
                if self.radioButton_5.isChecked():
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 22], pen=pg.mkPen('#3CAEA3', width=2))
                elif self.radioButton_6.isChecked():
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 21], pen=pg.mkPen('#3CAEA3', width=2))

            elif self.comboBox_G3.currentIndex() == 3:
                self.label_heart.setPixmap(QtGui.QPixmap(os.path.join('images', 'right_atrium.png')))
                self.text_heartinfo.setText(
                    "The right atrium is located superior to the right ventricle and anteromedial to the left atrium. The right atrium receives the vena cava and coronary sinus, has an appendage, and directs blood into the right ventricle through the tricuspid valve. The right atrium is the first chamber of the heart to receive deoxygenated and carbon dioxide-rich systemic blood from the body through the superior and inferior vena cava. The right atrium also houses the first part of the conduction system, the sinoatrial node (SAN), which is located in the upper section near the superior vena cava. The SAN is made up of pacemaker cells which polarize to generate an action potential.")
                if self.radioButton_5.isChecked():
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 5], pen=pg.mkPen('#3CAEA3', width=2))
                elif self.radioButton_6.isChecked():
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 4], pen=pg.mkPen('#3CAEA3', width=2))

            elif self.comboBox_G3.currentIndex() == 4:
                self.label_heart.setPixmap(QtGui.QPixmap(os.path.join('images', 'right_ventricle.png')))
                self.text_heartinfo.setText(
                    "The right ventricle lies anterior to the other heart chambers. Posteriorly and to the left, it is related to the left ventricle from which it is separated by the interventricular septum. The right ventricle is a unique, asymmetric, crescent-shape structure that is designed to accommodate the entire venous return while maintaining a low atrial pressure. The right ventricle is separated from the right atrium by the tricuspid valve. And the right atrium pumps blood to the lungs through the pulmonary artery gated by the pulmonary valve.")
                if self.radioButton_5.isChecked():
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 7], pen=pg.mkPen('#3CAEA3', width=2))
                elif self.radioButton_6.isChecked():
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 6], pen=pg.mkPen('#3CAEA3', width=2))

        def valve_plot(self):

            self.graphWidget_2.plotItem.clear()
            total = len(self.ctime)
            if self.comboBox_G3.currentIndex() == 1:
                self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 20], pen=pg.mkPen('#3CAEA3', width=2))
                self.graphWidget_2.setLabel('left', 'Volume', **self.labelStyle)
                self.graphWidget_2.setLabel('bottom', 'Time (s)', **self.labelStyle)
                self.label_heart.setPixmap(QtGui.QPixmap(os.path.join('images', 'mitral_valve.png')))
                self.text_heartinfo.setText(
                    "Bicuspid valve, also called the mitral valve, is present between the left atrium and the left ventricle. The mitral valve has only two leaflets. The leaflets are attached to and supported by a ring of tough, fibrous tissue called the annulus. The annulus helps to maintain the proper shape of the valve. The leaflets of the mitral valve are also supported by:\n"
                    "\n\n •  Chordae tendineae: tough, fibrous strings. These are similar to the strings supporting a parachute\n"
                    "\n•	Papillary muscles: part of the inside walls of the ventricles."
                    "\n\nThe chordae tendineae and papillary muscles keep the leaflets stable to prevent blood from flowing backward.\n"
                    "\n\nBlood flows from the left atrium into the left ventricle through the open mitral valve. When the left ventricle is full, the mitral valve closes and keeps blood from flowing backward into the left atrium when the ventricle contracts.")
            elif self.comboBox_G3.currentIndex() == 2:
                self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 5], pen=pg.mkPen('#3CAEA3', width=2))
                self.graphWidget_2.setLabel('left', 'Volume', **self.labelStyle)
                self.graphWidget_2.setLabel('bottom', 'Time (s)', **self.labelStyle)
                self.label_heart.setPixmap(QtGui.QPixmap(os.path.join('images', 'tricuspid_valve.png')))
                self.text_heartinfo.setText(
                    "The tricuspid valve is present between the right atrium and the right ventricle. Unlike the mitral valve, the tricuspid valve has three leaflets. The leaflets of the tricuspid valve are also supported by:"
                    "\n\n•	Chordae tendineae: tough, fibrous strings. These are similar to the strings supporting a parachute."
                    "\n•	Papillary muscles: part of the inside walls of the ventricles.\n"
                    "\n\nThe chordae tendineae and papillary muscles keep the leaflets stable to prevent blood from flowing backward."
                    "\n\nBlood flows from the right atrium into the right ventricle through the open tricuspid valve. When the right ventricle is full, the tricuspid valve closes and keeps blood from flowing backward into the right atrium when the ventricle contracts.")
            elif self.comboBox_G3.currentIndex() == 3:
                self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 22], pen=pg.mkPen('#3CAEA3', width=2))
                self.graphWidget_2.setLabel('left', 'Volume', **self.labelStyle)
                self.graphWidget_2.setLabel('bottom', 'Time (s)', **self.labelStyle)
                self.label_heart.setPixmap(QtGui.QPixmap(os.path.join('images', 'aortic_valve.png')))
                self.text_heartinfo.setText(
                    "The aortic valve is present between the left ventricle and the aorta. Like the tricuspid valve, the aortic valve also has three leaflets. As the left ventricle begins to contract, the aortic valve is forced open. Blood is pumped out of the left ventricle through the aortic valve into the aorta. The aorta branches into many arteries and provides blood to the body. When the left ventricle finishes contracting and begins to relax, the aortic valve snaps shut. This keeps blood from flowing back into the left ventricle.")
            elif self.comboBox_G3.currentIndex() == 4:
                self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 7], pen=pg.mkPen('#3CAEA3', width=2))
                self.graphWidget_2.setLabel('left', 'Volume', **self.labelStyle)
                self.graphWidget_2.setLabel('bottom', 'Time (s)', **self.labelStyle)
                self.label_heart.setPixmap(QtGui.QPixmap(os.path.join('images', 'pulmonary_valve.png')))
                self.text_heartinfo.setText(
                    "The pulmonary valve is present between the right ventricle and the pulmonary artery. This pulmonary valve is also a three-leaflet valve. As the right ventricle begins to contract, the pulmonic valve is forced open. Blood is pumped out of the right ventricle through the pulmonic valve into the pulmonary artery to the lungs. When the right ventricle finishes contracting and starts to relax, the pulmonic valve snaps shut. This keeps blood from flowing back into the right ventricle. This pattern is repeated, causing blood to flow continuously to the heart, lungs, and body. The four normally working heart valves make sure blood always flows freely in one direction and that there is no backward leakage.")

        def iandolet_plot(self):
            self.graphWidget_2.plotItem.clear()
            total = len(self.ctime)
            if self.comboBox_G3.currentIndex() == 1:
                if self.radioButton_5.isChecked():
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 24], pen=pg.mkPen('#3CAEA3', width=2))
                else:
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 25], pen=pg.mkPen('#3CAEA3', width=2))
                self.graphWidget_2.setLabel('left', 'Volume', **self.labelStyle)
                self.graphWidget_2.setLabel('bottom', 'Time (s)', **self.labelStyle)
                self.label_heart.setPixmap(QtGui.QPixmap(os.path.join('images', 'aorta.png')))
                self.text_heartinfo.setText(
                    "The aorta is the main and largest artery in the human body, originating from the left ventricle of the heart and extending down to the abdomen, where it splits into two smaller arteries. After the blood leaves the heart through the aortic valve, it travels through the aorta, making a cane-shaped curve that connects with other major arteries to deliver oxygen-rich blood to the brain, muscles, and other cells.\n"
                    "\nThe aorta is more than an inch wide in some places and has three layers:\n"
                    "•	intima\n"
                    "•	media\n"
                    "•	adventitia\n"
                    "The aorta supplies all of the systemic circulation, which means that the entire body, except for the respiratory zone of the lung, receives its blood from the aorta.\n"
                    "\n In anatomical sources, the aorta is usually divided into sections. They correspond to "
                    "\n•	Ascending aorta"
                    "\n•	Aortic arch"
                    "\n•	Thoracic aorta"
                    "\n•	Abdominal aorta")
            elif self.comboBox_G3.currentIndex() == 2:
                if self.radioButton_5.isChecked():
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 9], pen=pg.mkPen('#3CAEA3', width=2))
                else:
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 8], pen=pg.mkPen('#3CAEA3', width=2))
                self.graphWidget_2.setLabel('left', 'Volume', **self.labelStyle)
                self.graphWidget_2.setLabel('bottom', 'Time (s)', **self.labelStyle)
                self.label_heart.setPixmap(QtGui.QPixmap(
                    os.path.join('images',
                                 'pulmonary_artery.png')))
                self.text_heartinfo.setText(
                    "A pulmonary artery is an artery in the pulmonary circulation that carries deoxygenated blood from the right side of the heart to the lungs. The largest pulmonary artery is the main pulmonary artery or pulmonary trunk from the heart, and the smallest ones are the arterioles, which lead to the capillaries that surround the pulmonary alveoli. The pulmonary artery carries deoxygenated blood from the right ventricle to the lungs. The blood here passes through capillaries adjacent to alveoli and becomes oxygenated as part of the process of respiration. In contrast to the pulmonary arteries, the bronchial arteries supply nutrition to the lungs themselves. ")
            elif self.comboBox_G3.currentIndex() == 3:
                if self.radioButton_5.isChecked():
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 3], pen=pg.mkPen('#3CAEA3', width=2))
                else:
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 2], pen=pg.mkPen('#3CAEA3', width=2))
                self.graphWidget_2.setLabel('left', 'Volume', **self.labelStyle)
                self.graphWidget_2.setLabel('bottom', 'Time (s)', **self.labelStyle)
                self.label_heart.setPixmap(QtGui.QPixmap(
                    os.path.join('images', 'vena_cava.png')))
                self.text_heartinfo.setText(
                    "The venae cavae, singular 'vena cava' are two large veins that return deoxygenated blood from the body into the heart. In humans there are the superior vena cava and the inferior vena cava, and both empty into the right atrium. The inferior vena cava (or caudal vena cava in some animals) travels up alongside the abdominal aorta with blood from the lower part of the body. It is the largest vein in the human body. The superior vena cava (or cranial vena cava in animals) is above the heart, and forms from a convergence of the left and right brachiocephalic veins, which contain blood from the head and the arms. ")
            elif self.comboBox_G3.currentIndex() == 4:
                if self.radioButton_5.isChecked():
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 13], pen=pg.mkPen('#3CAEA3', width=2))
                else:
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 12], pen=pg.mkPen('#3CAEA3', width=2))
                self.graphWidget_2.setLabel('left', 'Volume', **self.labelStyle)
                self.graphWidget_2.setLabel('bottom', 'Time (s)', **self.labelStyle)
                self.label_heart.setPixmap(QtGui.QPixmap(
                    os.path.join('images', 'pulmonary_vein.png')))
                self.text_heartinfo.setText(
                    "Veins are vessels that bring blood to the heart. Pulmonary veins carry oxygenated blood from the lungs to the left atrium. There are four pulmonary veins which extend from the left atrium to the lungs. They are the right superior, right inferior, left superior, and left inferior pulmonary veins. Two main pulmonary veins emerge from each lung hilum, receiving blood from three or four bronchial veins apiece and draining into the left atrium. At the root of the lung, the right superior pulmonary vein lies in front of and a little below the pulmonary artery; the inferior is situated at the lowest part of the lung hilum. Behind the pulmonary artery is the bronchus.[2] The right main pulmonary veins (contains oxygenated blood) pass behind the right atrium and superior vena cava; the left in front of the descending thoracic aorta.")

        def radio_plot(self):
            if self.bc == 1:
                self.radioButton_6.setDisabled(False)
                self.chamber_plot()
            elif self.bc == 2:
                self.radioButton_6.setDisabled(True)
                self.valve_plot()
            else:
                self.radioButton_6.setDisabled(False)
                self.iandolet_plot()

        def clear(self):
            self.graphWidget_2.clear()
            self.graphWidget_1.clear()

        def reset(self):
            self.graphWidget_1.plotItem.clearPlots()
            self.graphWidget_2.plotItem.clearPlots()
            self.comboBox_G1.setCurrentIndex(0)
            self.comboBox_G2.setCurrentIndex(0)
            self.doubleSpinBox_1.setValue(72.0)
            self.doubleSpinBox_2.setValue(450.0)
            self.doubleSpinBox_4.setValue(0.04)
            self.doubleSpinBox_5.setValue(1.05)
            self.doubleSpinBox_6.setValue(0.6)
            self.comboBox_2.clear()
            self.textBrowser_2.setText(
                "The primary function of the heart is to serve as a muscular pump propelling blood"
                " into and through vessels to and from all parts of the body. The arteries, which "
                "receive this blood at high pressure and velocity and conduct it throughout the "
                "body, have thick walls that are composed of elastic fibrous tissue and muscle "
                "cells. The arterial tree—the branching system of arteries—terminates in short, "
                "narrow, muscular vessels called arterioles, from which blood enters simple "
                "endothelial tubes (i.e., tubes formed of endothelial, or lining, cells) known "
                "as capillaries. These thin, microscopic capillaries are permeable to vital cellular"
                " nutrients and waste products that they receive and distribute. From the"
                " capillaries, the blood, now depleted of oxygen and burdened with waste products,"
                " moving more slowly and under low pressure, enters small vessels called venules"
                " that converge to form veins, ultimately guiding the blood on its way back to the"
                " heart.")
            self.stn_dat = {'0': None, '1': None, '7': None, '13': None, '3': None, '11': None, '10': None, '51': None,
                            '46': None, '74': None, '56': None, '70': None, '62': None, '63': None, '108': None,
                            '109': None, '102': None, '107': None, '96': None, '92': None}

            self.c = 0
            self.cv = 0
            self.statusbar.showMessage('RESET', msecs=8000)
    except Exception as e:
        error = QtWidgets.QMessageBox()
        error.setWindowTitle('ERROR!!')
        error.setText(str(e))
        error.exec_()

class Steno_para(object):
    def __init__(self, Form):
        self.doubleSpinBox_RAL = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_AAO = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_UAR = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_CAL = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_RA = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_BAL = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_AA = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_HA = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_SAR = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_AO = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_CCR = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_FAR = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_FAL = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_TA = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_UAL = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_CAR = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_CCL = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_BAR = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_RAR = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_SAL = QtWidgets.QDoubleSpinBox(Form)
        self.Form = Form
        self.state()

    def setupUi(self):
        self.Form.setObjectName("Form")
        self.Form.resize(517, 355)
        self.Form.setMaximumSize(QtCore.QSize(517, 355))
        self.Form.setStyleSheet("background-color: rgb(46, 80, 120);")
        self.gridLayout = QtWidgets.QGridLayout(self.Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_SAL = QtWidgets.QLabel(self.Form)
        self.label_SAL.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(255,255,255);")
        self.label_SAL.setObjectName("label_SAL")
        self.gridLayout.addWidget(self.label_SAL, 3, 0, 1, 1)
        self.checkBox_SAL = QtWidgets.QCheckBox(self.Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_SAL.sizePolicy().hasHeightForWidth())
        self.checkBox_SAL.setSizePolicy(sizePolicy)
        self.checkBox_SAL.setText("")
        self.checkBox_SAL.setChecked(False)
        self.checkBox_SAL.setObjectName("checkBox_SAL")
        self.gridLayout.addWidget(self.checkBox_SAL, 3, 1, 1, 1)

        self.doubleSpinBox_SAL.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                             "color: rgb(255, 210, 119);\n"
                                             "selection-color: rgb(237, 85, 59);\n"
                                             "selection-background-color: rgb(33, 57, 86);\n"
                                             "\n"
                                             "font: 11pt \"Calibri\";")
        self.doubleSpinBox_SAL.setObjectName("doubleSpinBox_SAL")
        self.gridLayout.addWidget(self.doubleSpinBox_SAL, 3, 2, 1, 1)
        self.label_HA = QtWidgets.QLabel(self.Form)
        self.label_HA.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(255,255,255);")
        self.label_HA.setObjectName("label_HA")
        self.gridLayout.addWidget(self.label_HA, 3, 4, 1, 1)
        self.checkBox_HA = QtWidgets.QCheckBox(self.Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_HA.sizePolicy().hasHeightForWidth())
        self.checkBox_HA.setSizePolicy(sizePolicy)
        self.checkBox_HA.setText("")
        self.checkBox_HA.setChecked(False)
        self.checkBox_HA.setObjectName("checkBox_HA")
        self.gridLayout.addWidget(self.checkBox_HA, 3, 5, 1, 1)
        self.label_AO = QtWidgets.QLabel(self.Form)
        self.label_AO.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(255,255,255);")
        self.label_AO.setObjectName("label_AO")
        self.gridLayout.addWidget(self.label_AO, 1, 0, 1, 1)
        self.label_RAL = QtWidgets.QLabel(self.Form)
        self.label_RAL.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(255,255,255);")
        self.label_RAL.setObjectName("label_RAL")
        self.gridLayout.addWidget(self.label_RAL, 9, 4, 1, 1)

        self.doubleSpinBox_RAL.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                             "color: rgb(255, 210, 119);\n"
                                             "selection-color: rgb(237, 85, 59);\n"
                                             "selection-background-color: rgb(33, 57, 86);\n"
                                             "\n"
                                             "font: 11pt \"Calibri\";")
        self.doubleSpinBox_RAL.setObjectName("doubleSpinBox_RAL")
        self.gridLayout.addWidget(self.doubleSpinBox_RAL, 9, 6, 1, 1)
        self.checkBox_RAL = QtWidgets.QCheckBox(self.Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_RAL.sizePolicy().hasHeightForWidth())
        self.checkBox_RAL.setSizePolicy(sizePolicy)
        self.checkBox_RAL.setText("")
        self.checkBox_RAL.setChecked(False)
        self.checkBox_RAL.setObjectName("checkBox_RAL")
        self.gridLayout.addWidget(self.checkBox_RAL, 9, 5, 1, 1)
        self.checkBox_AbAO = QtWidgets.QCheckBox(self.Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_AbAO.sizePolicy().hasHeightForWidth())
        self.checkBox_AbAO.setSizePolicy(sizePolicy)
        self.checkBox_AbAO.setText("")
        self.checkBox_AbAO.setChecked(False)
        self.checkBox_AbAO.setObjectName("checkBox_AbAO")
        self.gridLayout.addWidget(self.checkBox_AbAO, 10, 1, 1, 1)

        self.doubleSpinBox_AAO.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                              "color: rgb(255, 210, 119);\n"
                                              "selection-color: rgb(237, 85, 59);\n"
                                              "selection-background-color: rgb(33, 57, 86);\n"
                                              "\n"
                                              "font: 11pt \"Calibri\";")
        self.doubleSpinBox_AAO.setObjectName("doubleSpinBox_AbAO")
        self.gridLayout.addWidget(self.doubleSpinBox_AAO, 10, 2, 1, 1)
        self.label_AbAO = QtWidgets.QLabel(self.Form)
        self.label_AbAO.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                      "color: rgb(255,255,255);")
        self.label_AbAO.setObjectName("label_AbAO")
        self.gridLayout.addWidget(self.label_AbAO, 10, 0, 1, 1)

        self.doubleSpinBox_UAR.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                             "color: rgb(255, 210, 119);\n"
                                             "selection-color: rgb(237, 85, 59);\n"
                                             "selection-background-color: rgb(33, 57, 86);\n"
                                             "\n"
                                             "font: 11pt \"Calibri\";")
        self.doubleSpinBox_UAR.setObjectName("doubleSpinBox_UAR")
        self.gridLayout.addWidget(self.doubleSpinBox_UAR, 8, 6, 1, 1)
        self.checkBox_CAL = QtWidgets.QCheckBox(self.Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_CAL.sizePolicy().hasHeightForWidth())
        self.checkBox_CAL.setSizePolicy(sizePolicy)
        self.checkBox_CAL.setText("")
        self.checkBox_CAL.setChecked(False)
        self.checkBox_CAL.setObjectName("checkBox_CAL")
        self.gridLayout.addWidget(self.checkBox_CAL, 9, 1, 1, 1)
        self.label_CAL = QtWidgets.QLabel(self.Form)
        self.label_CAL.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(255,255,255);")
        self.label_CAL.setObjectName("label_CAL")
        self.gridLayout.addWidget(self.label_CAL, 9, 0, 1, 1)


        self.doubleSpinBox_CAL.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                             "color: rgb(255, 210, 119);\n"
                                             "selection-color: rgb(237, 85, 59);\n"
                                             "selection-background-color: rgb(33, 57, 86);\n"
                                             "\n"
                                             "font: 11pt \"Calibri\";")
        self.doubleSpinBox_CAL.setObjectName("doubleSpinBox_CAL")

        self.gridLayout.addWidget(self.doubleSpinBox_CAL, 9, 2, 1, 1)
        self.label_RA = QtWidgets.QLabel(self.Form)
        self.label_RA.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(255,255,255);")
        self.label_RA.setObjectName("label_RA")
        self.gridLayout.addWidget(self.label_RA, 4, 4, 1, 1)
        self.checkBox_RA = QtWidgets.QCheckBox(self.Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_RA.sizePolicy().hasHeightForWidth())
        self.checkBox_RA.setSizePolicy(sizePolicy)
        self.checkBox_RA.setText("")
        self.checkBox_RA.setChecked(False)
        self.checkBox_RA.setObjectName("checkBox_RA")
        self.gridLayout.addWidget(self.checkBox_RA, 4, 5, 1, 1)

        self.doubleSpinBox_RA.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                            "color: rgb(255, 210, 119);\n"
                                            "selection-color: rgb(237, 85, 59);\n"
                                            "selection-background-color: rgb(33, 57, 86);\n"
                                            "\n"
                                            "font: 11pt \"Calibri\";")
        self.doubleSpinBox_RA.setObjectName("doubleSpinBox_RA")
        self.gridLayout.addWidget(self.doubleSpinBox_RA, 4, 6, 1, 1)
        self.checkBox_BAL = QtWidgets.QCheckBox(self.Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_BAL.sizePolicy().hasHeightForWidth())
        self.checkBox_BAL.setSizePolicy(sizePolicy)
        self.checkBox_BAL.setText("")
        self.checkBox_BAL.setChecked(False)
        self.checkBox_BAL.setObjectName("checkBox_BAL")
        self.gridLayout.addWidget(self.checkBox_BAL, 2, 5, 1, 1)
        self.label_BAL = QtWidgets.QLabel(self.Form)
        self.label_BAL.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(255,255,255);")
        self.label_BAL.setObjectName("label_BAL")
        self.gridLayout.addWidget(self.label_BAL, 2, 4, 1, 1)

        self.doubleSpinBox_BAL.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                             "color: rgb(255, 210, 119);\n"
                                             "selection-color: rgb(237, 85, 59);\n"
                                             "selection-background-color: rgb(33, 57, 86);\n"
                                             "\n"
                                             "font: 11pt \"Calibri\";")
        self.doubleSpinBox_BAL.setObjectName("doubleSpinBox_BAL")
        self.gridLayout.addWidget(self.doubleSpinBox_BAL, 2, 6, 1, 1)

        self.doubleSpinBox_AA.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                            "color: rgb(255, 210, 119);\n"
                                            "selection-color: rgb(237, 85, 59);\n"
                                            "selection-background-color: rgb(33, 57, 86);\n"
                                            "\n"
                                            "font: 11pt \"Calibri\";")
        self.doubleSpinBox_AA.setObjectName("doubleSpinBox_AA")
        self.gridLayout.addWidget(self.doubleSpinBox_AA, 2, 2, 1, 1)
        self.checkBox_AA = QtWidgets.QCheckBox(self.Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_AA.sizePolicy().hasHeightForWidth())
        self.checkBox_AA.setSizePolicy(sizePolicy)
        self.checkBox_AA.setText("")
        self.checkBox_AA.setChecked(False)
        self.checkBox_AA.setObjectName("checkBox_AA")
        self.gridLayout.addWidget(self.checkBox_AA, 2, 1, 1, 1)

        self.doubleSpinBox_HA.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                            "color: rgb(255, 210, 119);\n"
                                            "selection-color: rgb(237, 85, 59);\n"
                                            "selection-background-color: rgb(33, 57, 86);\n"
                                            "\n"
                                            "font: 11pt \"Calibri\";")
        self.doubleSpinBox_HA.setObjectName("doubleSpinBox_HA")
        self.gridLayout.addWidget(self.doubleSpinBox_HA, 3, 6, 1, 1)
        self.label_SAR = QtWidgets.QLabel(self.Form)
        self.label_SAR.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(255,255,255);")
        self.label_SAR.setObjectName("label_SAR")
        self.gridLayout.addWidget(self.label_SAR, 4, 0, 1, 1)
        self.checkBox_SAR = QtWidgets.QCheckBox(self.Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_SAR.sizePolicy().hasHeightForWidth())
        self.checkBox_SAR.setSizePolicy(sizePolicy)
        self.checkBox_SAR.setText("")
        self.checkBox_SAR.setChecked(False)
        self.checkBox_SAR.setObjectName("checkBox_SAR")
        self.gridLayout.addWidget(self.checkBox_SAR, 4, 1, 1, 1)

        self.doubleSpinBox_SAR.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                             "color: rgb(255, 210, 119);\n"
                                             "selection-color: rgb(237, 85, 59);\n"
                                             "selection-background-color: rgb(33, 57, 86);\n"
                                             "\n"
                                             "font: 11pt \"Calibri\";")
        self.doubleSpinBox_SAR.setObjectName("doubleSpinBox_SAR")
        self.gridLayout.addWidget(self.doubleSpinBox_SAR, 4, 2, 1, 1)
        self.label_BAR = QtWidgets.QLabel(self.Form)
        self.label_BAR.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(255,255,255);")
        self.label_BAR.setObjectName("label_BAR")
        self.gridLayout.addWidget(self.label_BAR, 1, 4, 1, 1)
        self.checkBox_BAR = QtWidgets.QCheckBox(self.Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_BAR.sizePolicy().hasHeightForWidth())
        self.checkBox_BAR.setSizePolicy(sizePolicy)
        self.checkBox_BAR.setText("")
        self.checkBox_BAR.setChecked(False)
        self.checkBox_BAR.setObjectName("checkBox_BAR")
        self.gridLayout.addWidget(self.checkBox_BAR, 1, 5, 1, 1)
        self.checkBox_AO = QtWidgets.QCheckBox(self.Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_AO.sizePolicy().hasHeightForWidth())
        self.checkBox_AO.setSizePolicy(sizePolicy)
        self.checkBox_AO.setText("")
        self.checkBox_AO.setChecked(False)
        self.checkBox_AO.setObjectName("checkBox_AO")
        self.gridLayout.addWidget(self.checkBox_AO, 1, 1, 1, 1)

        self.doubleSpinBox_AO.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                            "color: rgb(255, 210, 119);\n"
                                            "selection-color: rgb(237, 85, 59);\n"
                                            "selection-background-color: rgb(33, 57, 86);\n"
                                            "\n"
                                            "font: 11pt \"Calibri\";")
        self.doubleSpinBox_AO.setObjectName("doubleSpinBox_AO")
        self.gridLayout.addWidget(self.doubleSpinBox_AO, 1, 2, 1, 1)
        self.label_FAR = QtWidgets.QLabel(self.Form)
        self.label_FAR.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(255,255,255);")
        self.label_FAR.setObjectName("label_FAR")
        self.gridLayout.addWidget(self.label_FAR, 6, 4, 1, 1)
        self.checkBox_FAR = QtWidgets.QCheckBox(self.Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_FAR.sizePolicy().hasHeightForWidth())
        self.checkBox_FAR.setSizePolicy(sizePolicy)
        self.checkBox_FAR.setText("")
        self.checkBox_FAR.setChecked(False)
        self.checkBox_FAR.setObjectName("checkBox_FAR")
        self.gridLayout.addWidget(self.checkBox_FAR, 6, 5, 1, 1)

        self.doubleSpinBox_CCR.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                             "color: rgb(255, 210, 119);\n"
                                             "selection-color: rgb(237, 85, 59);\n"
                                             "selection-background-color: rgb(33, 57, 86);\n"
                                             "\n"
                                             "font: 11pt \"Calibri\";")
        self.doubleSpinBox_CCR.setObjectName("doubleSpinBox_CCR")
        self.gridLayout.addWidget(self.doubleSpinBox_CCR, 6, 2, 1, 1)

        self.doubleSpinBox_FAR.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                             "color: rgb(255, 210, 119);\n"
                                             "selection-color: rgb(237, 85, 59);\n"
                                             "selection-background-color: rgb(33, 57, 86);\n"
                                             "\n"
                                             "font: 11pt \"Calibri\";")
        self.doubleSpinBox_FAR.setObjectName("doubleSpinBox_FAR")
        self.gridLayout.addWidget(self.doubleSpinBox_FAR, 6, 6, 1, 1)
        self.label_TA = QtWidgets.QLabel(self.Form)
        self.label_TA.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(255,255,255);")
        self.label_TA.setObjectName("label_TA")
        self.gridLayout.addWidget(self.label_TA, 7, 0, 1, 1)
        self.checkBox_TA = QtWidgets.QCheckBox(self.Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_TA.sizePolicy().hasHeightForWidth())
        self.checkBox_TA.setSizePolicy(sizePolicy)
        self.checkBox_TA.setText("")
        self.checkBox_TA.setChecked(False)
        self.checkBox_TA.setObjectName("checkBox_TA")
        self.gridLayout.addWidget(self.checkBox_TA, 7, 1, 1, 1)
        self.checkBox_CCR = QtWidgets.QCheckBox(self.Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_CCR.sizePolicy().hasHeightForWidth())
        self.checkBox_CCR.setSizePolicy(sizePolicy)
        self.checkBox_CCR.setText("")
        self.checkBox_CCR.setChecked(False)
        self.checkBox_CCR.setObjectName("checkBox_CCR")
        self.gridLayout.addWidget(self.checkBox_CCR, 6, 1, 1, 1)

        self.doubleSpinBox_FAL.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                             "color: rgb(255, 210, 119);\n"
                                             "selection-color: rgb(237, 85, 59);\n"
                                             "selection-background-color: rgb(33, 57, 86);\n"
                                             "\n"
                                             "font: 11pt \"Calibri\";")
        self.doubleSpinBox_FAL.setObjectName("doubleSpinBox_FAL")
        self.gridLayout.addWidget(self.doubleSpinBox_FAL, 5, 6, 1, 1)
        self.label_CCR = QtWidgets.QLabel(self.Form)
        self.label_CCR.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(255,255,255);")
        self.label_CCR.setObjectName("label_CCR")
        self.gridLayout.addWidget(self.label_CCR, 6, 0, 1, 1)
        self.checkBox_UAL = QtWidgets.QCheckBox(self.Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_UAL.sizePolicy().hasHeightForWidth())
        self.checkBox_UAL.setSizePolicy(sizePolicy)
        self.checkBox_UAL.setText("")
        self.checkBox_UAL.setChecked(False)
        self.checkBox_UAL.setObjectName("checkBox_UAL")
        self.gridLayout.addWidget(self.checkBox_UAL, 7, 5, 1, 1)

        self.doubleSpinBox_TA.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                            "color: rgb(255, 210, 119);\n"
                                            "selection-color: rgb(237, 85, 59);\n"
                                            "selection-background-color: rgb(33, 57, 86);\n"
                                            "\n"
                                            "font: 11pt \"Calibri\";")
        self.doubleSpinBox_TA.setObjectName("doubleSpinBox_TA")
        self.gridLayout.addWidget(self.doubleSpinBox_TA, 7, 2, 1, 1)
        self.label_UAL = QtWidgets.QLabel(self.Form)
        self.label_UAL.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(255,255,255);")
        self.label_UAL.setObjectName("label_UAL")
        self.gridLayout.addWidget(self.label_UAL, 7, 4, 1, 1)
        self.checkBox_CAR = QtWidgets.QCheckBox(self.Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_CAR.sizePolicy().hasHeightForWidth())
        self.checkBox_CAR.setSizePolicy(sizePolicy)
        self.checkBox_CAR.setText("")
        self.checkBox_CAR.setChecked(False)
        self.checkBox_CAR.setObjectName("checkBox_CAR")
        self.gridLayout.addWidget(self.checkBox_CAR, 8, 1, 1, 1)

        self.doubleSpinBox_UAL.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                             "color: rgb(255, 210, 119);\n"
                                             "selection-color: rgb(237, 85, 59);\n"
                                             "selection-background-color: rgb(33, 57, 86);\n"
                                             "\n"
                                             "font: 11pt \"Calibri\";")
        self.doubleSpinBox_UAL.setObjectName("doubleSpinBox_UAL")
        self.gridLayout.addWidget(self.doubleSpinBox_UAL, 7, 6, 1, 1)
        self.label_CAR = QtWidgets.QLabel(self.Form)
        self.label_CAR.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(255,255,255);")
        self.label_CAR.setObjectName("label_CAR")
        self.gridLayout.addWidget(self.label_CAR, 8, 0, 1, 1)

        self.doubleSpinBox_CAR.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                             "color: rgb(255, 210, 119);\n"
                                             "selection-color: rgb(237, 85, 59);\n"
                                             "selection-background-color: rgb(33, 57, 86);\n"
                                             "\n"
                                             "font: 11pt \"Calibri\";")
        self.doubleSpinBox_CAR.setObjectName("doubleSpinBox_CAR")
        self.gridLayout.addWidget(self.doubleSpinBox_CAR, 8, 2, 1, 1)
        self.label_UAR = QtWidgets.QLabel(self.Form)
        self.label_UAR.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(255,255,255);")
        self.label_UAR.setObjectName("label_UAR")
        self.gridLayout.addWidget(self.label_UAR, 8, 4, 1, 1)
        self.checkBox_UAR = QtWidgets.QCheckBox(self.Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_UAR.sizePolicy().hasHeightForWidth())
        self.checkBox_UAR.setSizePolicy(sizePolicy)
        self.checkBox_UAR.setText("")
        self.checkBox_UAR.setChecked(False)
        self.checkBox_UAR.setObjectName("checkBox_UAR")
        self.gridLayout.addWidget(self.checkBox_UAR, 8, 5, 1, 1)

        self.doubleSpinBox_CCL.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                             "color: rgb(255, 210, 119);\n"
                                             "selection-color: rgb(237, 85, 59);\n"
                                             "selection-background-color: rgb(33, 57, 86);\n"
                                             "\n"
                                             "font: 11pt \"Calibri\";")
        self.doubleSpinBox_CCL.setObjectName("doubleSpinBox_CCL")
        self.gridLayout.addWidget(self.doubleSpinBox_CCL, 5, 2, 1, 1)
        self.label_CCL = QtWidgets.QLabel(self.Form)
        self.label_CCL.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(255,255,255);")
        self.label_CCL.setObjectName("label_CCL")
        self.gridLayout.addWidget(self.label_CCL, 5, 0, 1, 1)
        self.checkBox_CCL = QtWidgets.QCheckBox(self.Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_CCL.sizePolicy().hasHeightForWidth())
        self.checkBox_CCL.setSizePolicy(sizePolicy)
        self.checkBox_CCL.setText("")
        self.checkBox_CCL.setChecked(False)
        self.checkBox_CCL.setObjectName("checkBox_CCL")
        self.gridLayout.addWidget(self.checkBox_CCL, 5, 1, 1, 1)
        self.label_FAL = QtWidgets.QLabel(self.Form)
        self.label_FAL.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(255,255,255);")
        self.label_FAL.setObjectName("label_FAL")
        self.gridLayout.addWidget(self.label_FAL, 5, 4, 1, 1)
        self.checkBox_FAL = QtWidgets.QCheckBox(self.Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_FAL.sizePolicy().hasHeightForWidth())
        self.checkBox_FAL.setSizePolicy(sizePolicy)
        self.checkBox_FAL.setText("")
        self.checkBox_FAL.setChecked(False)
        self.checkBox_FAL.setObjectName("checkBox_FAL")
        self.gridLayout.addWidget(self.checkBox_FAL, 5, 5, 1, 1)

        self.doubleSpinBox_BAR.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                             "color: rgb(255, 210, 119);\n"
                                             "selection-color: rgb(237, 85, 59);\n"
                                             "selection-background-color: rgb(33, 57, 86);\n"
                                             "\n"
                                             "font: 11pt \"Calibri\";")
        self.doubleSpinBox_BAR.setObjectName("doubleSpinBox_BAR")
        self.gridLayout.addWidget(self.doubleSpinBox_BAR, 1, 6, 1, 1)
        self.label_AA = QtWidgets.QLabel(self.Form)
        self.label_AA.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(255,255,255);")
        self.label_AA.setObjectName("label_AA")
        self.gridLayout.addWidget(self.label_AA, 2, 0, 1, 1)
        self.checkBox_RAR = QtWidgets.QCheckBox(self.Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_RAR.sizePolicy().hasHeightForWidth())
        self.checkBox_RAR.setSizePolicy(sizePolicy)
        self.checkBox_RAR.setText("")
        self.checkBox_RAR.setChecked(False)
        self.checkBox_RAR.setObjectName("checkBox_RAR")
        self.gridLayout.addWidget(self.checkBox_RAR, 10, 5, 1, 1)

        self.doubleSpinBox_RAR.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                             "color: rgb(255, 210, 119);\n"
                                             "selection-color: rgb(237, 85, 59);\n"
                                             "selection-background-color: rgb(33, 57, 86);\n"
                                             "\n"
                                             "font: 11pt \"Calibri\";")
        self.doubleSpinBox_RAR.setObjectName("doubleSpinBox_RAR")
        self.gridLayout.addWidget(self.doubleSpinBox_RAR, 10, 6, 1, 1)
        self.label_RAR = QtWidgets.QLabel(self.Form)
        self.label_RAR.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(255,255,255);")
        self.label_RAR.setObjectName("label_RAR")
        self.gridLayout.addWidget(self.label_RAR, 10, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 3, 1, 1)
        self.line = QtWidgets.QFrame(self.Form)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(6)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 0, 1, 3)
        self.line_2 = QtWidgets.QFrame(self.Form)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(6)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 4, 1, 3)
        # STENO BUTTON OK
        self.button_ok = QtWidgets.QPushButton(self.Form)
        self.button_ok.setText("OK")
        self.button_ok.setStyleSheet("color: rgb(255, 210, 119);\n"
                                     "background-color: rgb(35, 35, 35);\n"
                                     "selection-color: rgb(237, 85, 59);\n"
                                     "selection-background-color: rgb(33, 57, 86);")
        self.gridLayout.addWidget(self.button_ok, 12, 0, 1, 7)
        self.button_ok.clicked.connect(self.clicked)

        self.checkBox_AA.clicked.connect(self.enable_box)
        self.checkBox_AO.clicked.connect(self.enable_box)
        self.checkBox_AbAO.clicked.connect(self.enable_box)
        self.checkBox_BAL.clicked.connect(self.enable_box)
        self.checkBox_BAR.clicked.connect(self.enable_box)
        self.checkBox_CAL.clicked.connect(self.enable_box)
        self.checkBox_CAR.clicked.connect(self.enable_box)
        self.checkBox_CCL.clicked.connect(self.enable_box)
        self.checkBox_CCR.clicked.connect(self.enable_box)
        self.checkBox_FAL.clicked.connect(self.enable_box)
        self.checkBox_FAR.clicked.connect(self.enable_box)
        self.checkBox_HA.clicked.connect(self.enable_box)
        self.checkBox_RA.clicked.connect(self.enable_box)
        self.checkBox_RAL.clicked.connect(self.enable_box)
        self.checkBox_RAR.clicked.connect(self.enable_box)
        self.checkBox_SAL.clicked.connect(self.enable_box)
        self.checkBox_SAR.clicked.connect(self.enable_box)
        self.checkBox_TA.clicked.connect(self.enable_box)
        self.checkBox_UAL.clicked.connect(self.enable_box)
        self.checkBox_UAR.clicked.connect(self.enable_box)


        self.retranslateUi(self.Form)
        QtCore.QMetaObject.connectSlotsByName(self.Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Stenosis Parameters"))
        self.label_SAL.setText(_translate("Form", "Subclavian Artery (L)"))
        self.label_HA.setText(_translate("Form", "Hepatic Artery"))
        self.label_AO.setText(_translate("Form", "Ascending Aorta"))
        self.label_RAL.setText(_translate("Form", "Radial Artery (L)"))
        self.label_AbAO.setText(_translate("Form", "Abdominal Aorta"))
        self.label_CAL.setText(_translate("Form", "Cereberal Artery (L)"))
        self.label_RA.setText(_translate("Form", "Renal Artery"))
        self.label_BAL.setText(_translate("Form", "Brachial Artery (L)"))
        self.label_SAR.setText(_translate("Form", "Subclavian Artery (R)"))
        self.label_BAR.setText(_translate("Form", "Brachial Artery (R)"))
        self.label_FAR.setText(_translate("Form", "Femoral Artery (R)"))
        self.label_TA.setText(_translate("Form", "Thoracic Aorta"))
        self.label_CCR.setText(_translate("Form", "Common Carotid (R)"))
        self.label_UAL.setText(_translate("Form", "Ulnar Artery (L)"))
        self.label_CAR.setText(_translate("Form", "Cereberal Artery (R)"))
        self.label_UAR.setText(_translate("Form", "Ulnar Artery (R)"))
        self.label_CCL.setText(_translate("Form", "Common Carotid (L)"))
        self.label_FAL.setText(_translate("Form", "Femoral Artery (L)"))
        self.label_AA.setText(_translate("Form", "Aortic Arch"))
        self.label_RAR.setText(_translate("Form", "Radial Artery (R)"))

    def enable_box(self):
        if self.checkBox_AA.isChecked():
            self.doubleSpinBox_AA.setDisabled(False)
        else:
            self.doubleSpinBox_AA.setDisabled(True)

        if self.checkBox_AO.isChecked():
            self.doubleSpinBox_AO.setDisabled(False)
        else:
            self.doubleSpinBox_AO.setDisabled(True)

        if self.checkBox_AbAO.isChecked():
            self.doubleSpinBox_AAO.setDisabled(False)
        else:
            self.doubleSpinBox_AAO.setDisabled(True)

        if self.checkBox_BAL.isChecked():
            self.doubleSpinBox_BAL.setDisabled(False)
        else:
            self.doubleSpinBox_BAL.setDisabled(True)

        if self.checkBox_BAR.isChecked():
            self.doubleSpinBox_BAR.setDisabled(False)
        else:
            self.doubleSpinBox_BAR.setDisabled(True)

        if self.checkBox_CAL.isChecked():
            self.doubleSpinBox_CAL.setDisabled(True)
        else:
            self.doubleSpinBox_CAL.setDisabled(True)

        if self.checkBox_CAR.isChecked():
            self.doubleSpinBox_CAR.setDisabled(False)
        else:
            self.doubleSpinBox_CAR.setDisabled(True)

        if self.checkBox_CCL.isChecked():
            self.doubleSpinBox_CCL.setDisabled(False)
        else:
            self.doubleSpinBox_CCL.setDisabled(True)

        if self.checkBox_CCR.isChecked():
            self.doubleSpinBox_CCR.setDisabled(False)
        else:
            self.doubleSpinBox_CCR.setDisabled(True)

        if self.checkBox_FAL.isChecked():
            self.doubleSpinBox_FAL.setDisabled(False)
        else:
            self.doubleSpinBox_FAL.setDisabled(True)

        if self.checkBox_FAR.isChecked():
            self.doubleSpinBox_FAR.setDisabled(False)
        else:
            self.doubleSpinBox_FAR.setDisabled(True)

        if self.checkBox_HA.isChecked():
            self.doubleSpinBox_HA.setDisabled(False)
        else:
            self.doubleSpinBox_HA.setDisabled(True)

        if self.checkBox_RA.isChecked():
            self.doubleSpinBox_RA.setDisabled(False)
        else:
            self.doubleSpinBox_RA.setDisabled(True)

        if self.checkBox_RAL.isChecked():
            self.doubleSpinBox_RAL.setDisabled(False)
        else:
            self.doubleSpinBox_RAL.setDisabled(True)

        if self.checkBox_RAR.isChecked():
            self.doubleSpinBox_RAR.setDisabled(False)
        else:
            self.doubleSpinBox_RAR.setDisabled(True)

        if self.checkBox_SAL.isChecked():
            self.doubleSpinBox_SAL.setDisabled(False)
        else:
            self.doubleSpinBox_SAL.setDisabled(True)

        if self.checkBox_SAR.isChecked():
            self.doubleSpinBox_SAR.setDisabled(False)
        else:
            self.doubleSpinBox_SAR.setDisabled(True)

        if self.checkBox_TA.isChecked():
            self.doubleSpinBox_TA.setDisabled(False)
        else:
            self.doubleSpinBox_TA.setDisabled(True)

        if self.checkBox_UAL.isChecked():
            self.doubleSpinBox_UAL.setDisabled(False)
        else:
            self.doubleSpinBox_UAL.setDisabled(True)

        if self.checkBox_UAR.isChecked():
            self.doubleSpinBox_UAR.setDisabled(False)
        else:
            self.doubleSpinBox_UAR.setDisabled(True)

    def clicked(self):
        global stn_dat
        path = os.path.join("DBS", "bloodsim.sqlite")
        connection = create_connection(path)
        # ==========UPDATE VAL
        AO = self.doubleSpinBox_AO.value()
        AA = self.doubleSpinBox_AA.value()
        SAL = self.doubleSpinBox_SAL.value()
        SAR = self.doubleSpinBox_SAR.value()
        CCL = self.doubleSpinBox_CCL.value()
        CCR = self.doubleSpinBox_CCR.value()
        TA = self.doubleSpinBox_TA.value()
        CAR = self.doubleSpinBox_CAR.value()
        CAL = self.doubleSpinBox_CAL.value()
        AAO = self.doubleSpinBox_AAO.value()
        BAR = self.doubleSpinBox_BAR.value()
        BAL = self.doubleSpinBox_BAL.value()
        HA = self.doubleSpinBox_HA.value()
        RA = self.doubleSpinBox_RA.value()
        FAL = self.doubleSpinBox_FAL.value()
        FAR = self.doubleSpinBox_FAR.value()
        UAL = self.doubleSpinBox_UAL.value()
        UAR = self.doubleSpinBox_UAR.value()
        RAL = self.doubleSpinBox_RAL.value()
        RAR = self.doubleSpinBox_RAR.value()
        query = "Update STENO set val = ? where id = ?"
        query_list = [(AO, 0), (AA, 1), (SAL, 2), (SAR, 3), (CCL, 4), (CCR, 5),
                      (TA, 6), (CAR, 7), (CAL, 8), (AAO, 9), (BAR, 10), (BAL, 11),
                      (HA, 12), (RA, 13), (FAL, 14), (FAR, 15), (UAL, 16),
                      (UAR, 17), (RAL, 18), (RAR, 19)]
        execute_many_query(connection, query, query_list)

        # ====== UPDATE STATE
        css = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        css[0] = AO_STATE = self.doubleSpinBox_AO.isEnabled()
        css[1] = AA_STATE = self.doubleSpinBox_AA.isEnabled()
        css[2] = SAL_STATE = self.doubleSpinBox_SAL.isEnabled()
        css[3] = SAR_STATE = self.doubleSpinBox_SAR.isEnabled()
        css[4] = CCL_STATE = self.doubleSpinBox_CCL.isEnabled()
        css[5] = CCR_STATE = self.doubleSpinBox_CCR.isEnabled()
        css[6] = TA_STATE= self.doubleSpinBox_TA.isEnabled()
        css[7] = CAR_STATE = self.doubleSpinBox_CAR.isEnabled()
        css[8] = CAL_STATE = self.doubleSpinBox_CAL.isEnabled()
        css[9] = AbAo_STATE = self.doubleSpinBox_AAO.isEnabled()
        css[10] = BAR_STATE = self.doubleSpinBox_BAR.isEnabled()
        css[11] = BAL_STATE = self.doubleSpinBox_BAL.isEnabled()
        css[12] = HA_STATE = self.doubleSpinBox_HA.isEnabled()
        css[13] = RA_STATE = self.doubleSpinBox_RA.isEnabled()
        css[14] = FAL_STATE = self.doubleSpinBox_FAL.isEnabled()
        css[15] = FAR_STATE = self.doubleSpinBox_FAR.isEnabled()
        css[16] = UAL_STATE = self.doubleSpinBox_UAL.isEnabled()
        css[17] = UAR_STATE = self.doubleSpinBox_UAR.isEnabled()
        css[18] = RAL_STATE = self.doubleSpinBox_RAL.isEnabled()
        css[19] = RAR_STATE = self.doubleSpinBox_RAR.isEnabled()
        for i in range(20):
            if css[i] == True:
                css[i] = 1
            else:
                css[i] = 0
        query = "Update STENO set state = ? where id = ?"
        query_list = [(css[0], 0), (css[1], 1), (css[2], 2), (css[3], 3), (css[4], 4), (css[5], 5), (css[6], 6),\
                      (css[7], 7), (css[8], 8), (css[9], 9), (css[10], 10), (css[11], 11), (css[12], 12), (css[13], 13),\
                      (css[14], 14), (css[15], 15), (css[16], 16), (css[17], 17), (css[18], 18), (css[19], 19)]
        execute_many_query(connection, query, query_list)
        stn_dat = {'0': AA, '1': AO, '7': AAO, '13': BAL, '3': BAR, '11': CAL, '10': CAR, '51': CCL,
                   '46': CCR, '74': FAL, '56': FAR, '70': HA, '62': RA, '63': RAL, '108': RAR,
                   '109': SAL, '102': SAR, '107': TA, '96': UAL, '92': UAR}

        self.Form.close()

    def state(self):
        path = os.path.join("DBS", "bloodsim.sqlite")
        connection = create_connection(path)
        # ======RETRIVING BOX VALUE
        c1 = []
        query = "SELECT val FROM STENO"
        value = execute_read_query(connection, query)
        c1 = sum(value, ())
        self.doubleSpinBox_AA.setValue(c1[0])
        self.doubleSpinBox_AO.setValue(c1[1])
        self.doubleSpinBox_AAO.setValue(c1[2])
        self.doubleSpinBox_BAL.setValue(c1[3])
        self.doubleSpinBox_BAR.setValue(c1[4])
        self.doubleSpinBox_CAL.setValue(c1[5])
        self.doubleSpinBox_CAR.setValue(c1[6])
        self.doubleSpinBox_CCL.setValue(c1[7])
        self.doubleSpinBox_CCR.setValue(c1[8])
        self.doubleSpinBox_FAL.setValue(c1[9])
        self.doubleSpinBox_FAR.setValue(c1[10])
        self.doubleSpinBox_HA.setValue(c1[11])
        self.doubleSpinBox_RA.setValue(c1[12])
        self.doubleSpinBox_RAL.setValue(c1[13])
        self.doubleSpinBox_RAR.setValue(c1[14])
        self.doubleSpinBox_SAL.setValue(c1[15])
        self.doubleSpinBox_SAR.setValue(c1[16])
        self.doubleSpinBox_TA.setValue(c1[17])
        self.doubleSpinBox_UAL.setValue(c1[18])
        self.doubleSpinBox_UAR.setValue(c1[19])

        # ==========RETRIVING CHECKBOX STATE
        c = []
        query = "SELECT state FROM STENO"
        state = execute_read_query(connection, query)
        c = sum(state, ())
        self.doubleSpinBox_AO.setEnabled(c[0])
        self.doubleSpinBox_AA.setEnabled(c[1])
        self.doubleSpinBox_SAL.setEnabled(c[2])
        self.doubleSpinBox_SAR.setEnabled(c[3])
        self.doubleSpinBox_CCL.setEnabled(c[4])
        self.doubleSpinBox_CCR.setEnabled(c[5])
        self.doubleSpinBox_TA.setEnabled(c[6])
        self.doubleSpinBox_CAR.setEnabled(c[7])
        self.doubleSpinBox_CAL.setEnabled(c[8])
        self.doubleSpinBox_AAO.setEnabled(c[9])
        self.doubleSpinBox_BAL.setEnabled(c[10])
        self.doubleSpinBox_BAR.setEnabled(c[11])
        self.doubleSpinBox_HA.setEnabled(c[12])
        self.doubleSpinBox_RA.setEnabled(c[13])
        self.doubleSpinBox_FAL.setEnabled(c[14])
        self.doubleSpinBox_FAR.setEnabled(c[15])
        self.doubleSpinBox_UAL.setEnabled(c[16])
        self.doubleSpinBox_UAR.setEnabled(c[17])
        self.doubleSpinBox_RAL.setEnabled(c[18])
        self.doubleSpinBox_RAR.setEnabled(c[19])
        self.setupUi()
        self.checkBox_AO.setChecked(c[0])
        self.checkBox_AA.setChecked(c[1])
        self.checkBox_SAL.setChecked(c[2])
        self.checkBox_SAR.setChecked(c[3])
        self.checkBox_CCL.setChecked(c[4])
        self.checkBox_CCR.setChecked(c[5])
        self.checkBox_TA.setChecked(c[6])
        self.checkBox_CAR.setChecked(c[7])
        self.checkBox_CAL.setChecked(c[8])
        self.checkBox_AbAO.setChecked(c[9])
        self.checkBox_BAL.setChecked(c[10])
        self.checkBox_BAR.setChecked(c[11])
        self.checkBox_HA.setChecked(c[12])
        self.checkBox_RA.setChecked(c[13])
        self.checkBox_FAL.setChecked(c[14])
        self.checkBox_FAR.setChecked(c[15])
        self.checkBox_UAL.setChecked(c[16])
        self.checkBox_UAR.setChecked(c[17])
        self.checkBox_RAL.setChecked(c[18])
        self.checkBox_RAR.setChecked(c[19])

class Heart_para(object):
    def __init__(self, widget_1):
        self.widget_1 = widget_1
        self.setupUi()
        self.state()

    def setupUi(self):
        self.widget_1.setObjectName("widget_1")
        self.widget_1.resize(750, 458)
        self.widget_1.setStyleSheet("background-color: rgb(43, 80, 120);\n"
                               "border-color: rgb(0,0,0);\n"
                               "border-right-color: rgb(43, 80, 120);")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        # ____________________HEART PARA BUTTON OK______________________
        self.heart_ok = QtWidgets.QPushButton(self.widget_1)
        self.heart_ok.setText("OK")
        self.heart_ok.setStyleSheet("color: rgb(250, 210, 119);\n"
                                    "background-color: rgb(35, 35, 35);")
        self.heart_ok.clicked.connect(self.clicked)

        # ___________________________TAB WIDGET__________________________
        self.tabWidget = QtWidgets.QTabWidget(self.widget_1)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")

        # _________________________TAB WIDGET (TAB-0)_____________________
        self.tab_0 = QtWidgets.QWidget()
        self.tab_0.setObjectName("tab_0")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_0)
        self.gridLayout_4.setObjectName("gridLayout_4")

        # ==================BERNOULI'S RESISTANCE===========================
        self.label_BR = QtWidgets.QLabel(self.tab_0)
        self.label_BR.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(35, 35, 35);\n"
                                    "color: rgb(255, 210, 119);")
        self.label_BR.setObjectName("label_BR")
        self.gridLayout_4.addWidget(self.label_BR, 0, 0, 1, 4)

        # ------------------------------MITRAL VALVE-----------------
        self.label_BR_MV = QtWidgets.QLabel(self.tab_0)
        self.label_BR_MV.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                       "color: rgb(255,255,255);")
        self.label_BR_MV.setObjectName("label_BR_MV")
        self.gridLayout_4.addWidget(self.label_BR_MV, 1, 0, 1, 1)

        self.checkBox_BR_MV = QtWidgets.QCheckBox(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_BR_MV.sizePolicy().hasHeightForWidth())
        self.checkBox_BR_MV.setSizePolicy(sizePolicy)
        self.checkBox_BR_MV.setText("")
        self.checkBox_BR_MV.setChecked(False)
        self.checkBox_BR_MV.setObjectName("checkBox_BR_MV")
        self.gridLayout_4.addWidget(self.checkBox_BR_MV, 1, 2, 1, 1)
        self.doubleSpinBox_BR_MV = QtWidgets.QDoubleSpinBox(self.tab_0)
        self.doubleSpinBox_BR_MV.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                               "color: rgb(255, 210, 119);\n"
                                               "selection-color: rgb(237, 85, 59);\n"
                                               "selection-background-color: rgb(33, 57, 86);\n"
                                               "\n"
                                               "font: 11pt \"Calibri\";")
        self.doubleSpinBox_BR_MV.setObjectName("doubleSpinBox_BR_MV")
        self.gridLayout_4.addWidget(self.doubleSpinBox_BR_MV, 1, 3, 1, 1)

        # -----------------------AORTIC VALVE--------------------------
        self.label_BR_AV = QtWidgets.QLabel(self.tab_0)
        self.label_BR_AV.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                       "color: rgb(255,255,255);\n"
                                       "")
        self.label_BR_AV.setObjectName("label_BR_AV")
        self.gridLayout_4.addWidget(self.label_BR_AV, 4, 0, 1, 1)

        self.checkBox_BR_AV = QtWidgets.QCheckBox(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_BR_AV.sizePolicy().hasHeightForWidth())
        self.checkBox_BR_AV.setSizePolicy(sizePolicy)
        self.checkBox_BR_AV.setText("")
        self.checkBox_BR_AV.setChecked(False)
        self.checkBox_BR_AV.setObjectName("checkBox_BR_AV")
        self.gridLayout_4.addWidget(self.checkBox_BR_AV, 4, 2, 1, 1)

        self.doubleSpinBox_BR_AV = QtWidgets.QDoubleSpinBox(self.tab_0)
        self.doubleSpinBox_BR_AV.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                               "color: rgb(255, 210, 119);\n"
                                               "selection-color: rgb(237, 85, 59);\n"
                                               "selection-background-color: rgb(33, 57, 86);\n"
                                               "\n"
                                               "font: 11pt \"Calibri\";")
        self.doubleSpinBox_BR_AV.setObjectName("doubleSpinBox_BR_AV")
        self.gridLayout_4.addWidget(self.doubleSpinBox_BR_AV, 4, 3, 1, 1)

        # -----------------------------TRICUSPID VALVE-------------------
        self.label_BR_TV = QtWidgets.QLabel(self.tab_0)
        self.label_BR_TV.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                       "color: rgb(255,255,255);")
        self.label_BR_TV.setObjectName("label_BR_TV")
        self.gridLayout_4.addWidget(self.label_BR_TV, 3, 0, 1, 1)

        self.checkBox_BR_TV = QtWidgets.QCheckBox(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_BR_TV.sizePolicy().hasHeightForWidth())
        self.checkBox_BR_TV.setSizePolicy(sizePolicy)
        self.checkBox_BR_TV.setText("")
        self.checkBox_BR_TV.setChecked(False)
        self.checkBox_BR_TV.setObjectName("checkBox_BR_TV")
        self.gridLayout_4.addWidget(self.checkBox_BR_TV, 3, 2, 1, 1)

        self.doubleSpinBox_BR_TV = QtWidgets.QDoubleSpinBox(self.tab_0)
        self.doubleSpinBox_BR_TV.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                               "color: rgb(255, 210, 119);\n"
                                               "selection-color: rgb(237, 85, 59);\n"
                                               "selection-background-color: rgb(33, 57, 86);\n"
                                               "\n"
                                               "font: 11pt \"Calibri\";")
        self.doubleSpinBox_BR_TV.setObjectName("doubleSpinBox_BR_TV")
        self.gridLayout_4.addWidget(self.doubleSpinBox_BR_TV, 3, 3, 1, 1)

        # ---------------------------PULMONARY VALVE---------------------
        self.label_BR_PV = QtWidgets.QLabel(self.tab_0)
        self.label_BR_PV.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                       "color: rgb(255,255,255);")
        self.label_BR_PV.setObjectName("label_BR_PV")
        self.gridLayout_4.addWidget(self.label_BR_PV, 2, 0, 1, 1)

        self.checkBox_BR_PV = QtWidgets.QCheckBox(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_BR_PV.sizePolicy().hasHeightForWidth())
        self.checkBox_BR_PV.setSizePolicy(sizePolicy)
        self.checkBox_BR_PV.setText("")
        self.checkBox_BR_PV.setChecked(False)
        self.checkBox_BR_PV.setObjectName("checkBox_BR_PV")
        self.gridLayout_4.addWidget(self.checkBox_BR_PV, 2, 2, 1, 1)

        self.doubleSpinBox_BR_PV = QtWidgets.QDoubleSpinBox(self.tab_0)
        self.doubleSpinBox_BR_PV.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                               "color: rgb(255, 210, 119);\n"
                                               "selection-color: rgb(237, 85, 59);\n"
                                               "selection-background-color: rgb(33, 57, 86);\n"
                                               "\n"
                                               "font: 11pt \"Calibri\";")
        self.doubleSpinBox_BR_PV.setObjectName("doubleSpinBox_BR_PV")
        self.gridLayout_4.addWidget(self.doubleSpinBox_BR_PV, 2, 3, 1, 1)

        # ======================COMPLIANCE===============================
        self.label_CMP = QtWidgets.QLabel(self.tab_0)
        self.label_CMP.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                     "background-color: rgb(35, 35, 35);\n"
                                     "color: rgb(255, 210, 119);")
        self.label_CMP.setObjectName("label_CMP")
        self.gridLayout_4.addWidget(self.label_CMP, 5, 0, 1, 4)

        #-------------------------------VENA CAVA---------------------
        self.label_CMP_VC = QtWidgets.QLabel(self.tab_0)
        self.label_CMP_VC.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255,255,255);")
        self.label_CMP_VC.setObjectName("label_CMP_VC")
        self.gridLayout_4.addWidget(self.label_CMP_VC, 6, 0, 1, 1)

        self.checkBox_CMP_VC = QtWidgets.QCheckBox(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_CMP_VC.sizePolicy().hasHeightForWidth())
        self.checkBox_CMP_VC.setSizePolicy(sizePolicy)
        self.checkBox_CMP_VC.setText("")
        self.checkBox_CMP_VC.setChecked(False)
        self.checkBox_CMP_VC.setObjectName("checkBox_CMP_VC")
        self.gridLayout_4.addWidget(self.checkBox_CMP_VC, 6, 2, 1, 1)

        self.doubleSpinBox_CMP_VC = QtWidgets.QDoubleSpinBox(self.tab_0)
        self.doubleSpinBox_CMP_VC.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                "color: rgb(255, 210, 119);\n"
                                                "selection-color: rgb(237, 85, 59);\n"
                                                "selection-background-color: rgb(33, 57, 86);\n"
                                                "\n"
                                                "font: 11pt \"Calibri\";")
        self.doubleSpinBox_CMP_VC.setObjectName("doubleSpinBox_CMP_VC")
        self.gridLayout_4.addWidget(self.doubleSpinBox_CMP_VC, 6, 3, 1, 1)

        #--------------------------AORTA----------------------------
        self.label_CMP_AO = QtWidgets.QLabel(self.tab_0)
        self.label_CMP_AO.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255,255,255);")
        self.label_CMP_AO.setObjectName("label_CMP_AO")
        self.gridLayout_4.addWidget(self.label_CMP_AO, 7, 0, 1, 1)

        self.checkBox_CMP_AO = QtWidgets.QCheckBox(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_CMP_AO.sizePolicy().hasHeightForWidth())
        self.checkBox_CMP_AO.setSizePolicy(sizePolicy)
        self.checkBox_CMP_AO.setText("")
        self.checkBox_CMP_AO.setChecked(False)
        self.checkBox_CMP_AO.setObjectName("checkBox_CMP_AO")
        self.gridLayout_4.addWidget(self.checkBox_CMP_AO, 7, 2, 1, 1)

        self.doubleSpinBox_CMP_AO = QtWidgets.QDoubleSpinBox(self.tab_0)
        self.doubleSpinBox_CMP_AO.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                "color: rgb(255, 210, 119);\n"
                                                "selection-color: rgb(237, 85, 59);\n"
                                                "selection-background-color: rgb(33, 57, 86);\n"
                                                "\n"
                                                "font: 11pt \"Calibri\";")
        self.doubleSpinBox_CMP_AO.setObjectName("doubleSpinBox_CMP_AO")
        self.gridLayout_4.addWidget(self.doubleSpinBox_CMP_AO, 7, 3, 1, 1)

        # ---------------------ARTERY---------------------------
        self.label_CMP_ART = QtWidgets.QLabel(self.tab_0)
        self.label_CMP_ART.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_CMP_ART.setObjectName("label_CMP_ART")
        self.gridLayout_4.addWidget(self.label_CMP_ART, 8, 0, 1, 1)

        self.checkBox_CMP_ART = QtWidgets.QCheckBox(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_CMP_ART.sizePolicy().hasHeightForWidth())
        self.checkBox_CMP_ART.setSizePolicy(sizePolicy)
        self.checkBox_CMP_ART.setText("")
        self.checkBox_CMP_ART.setChecked(False)
        self.checkBox_CMP_ART.setObjectName("checkBox_CMP_ART")
        self.gridLayout_4.addWidget(self.checkBox_CMP_ART, 8, 2, 1, 1)

        self.doubleSpinBox_CMP_ART = QtWidgets.QDoubleSpinBox(self.tab_0)
        self.doubleSpinBox_CMP_ART.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_CMP_ART.setObjectName("doubleSpinBox_CMP_ART")
        self.gridLayout_4.addWidget(self.doubleSpinBox_CMP_ART, 8, 3, 1, 1)

        # --------------------------CAPILLARY--------------------------
        self.label_CMP_CAP = QtWidgets.QLabel(self.tab_0)
        self.label_CMP_CAP.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_CMP_CAP.setObjectName("label_CMP_CAP")
        self.gridLayout_4.addWidget(self.label_CMP_CAP, 9, 0, 1, 1)

        self.checkBox_CMP_CAP = QtWidgets.QCheckBox(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_CMP_CAP.sizePolicy().hasHeightForWidth())
        self.checkBox_CMP_CAP.setSizePolicy(sizePolicy)
        self.checkBox_CMP_CAP.setText("")
        self.checkBox_CMP_CAP.setChecked(False)
        self.checkBox_CMP_CAP.setObjectName("checkBox_CMP_CAP")
        self.gridLayout_4.addWidget(self.checkBox_CMP_CAP, 9, 2, 1, 1)

        self.doubleSpinBox_CMP_CAP = QtWidgets.QDoubleSpinBox(self.tab_0)
        self.doubleSpinBox_CMP_CAP.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_CMP_CAP.setObjectName("doubleSpinBox_CMP_CAP")
        self.gridLayout_4.addWidget(self.doubleSpinBox_CMP_CAP, 9, 3, 1, 1)

        # ---------------------VENOUS COMPLIANCE----------------------
        self.label_CMP_VCO = QtWidgets.QLabel(self.tab_0)
        self.label_CMP_VCO.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_CMP_VCO.setObjectName("label_CMP_VCO")
        self.gridLayout_4.addWidget(self.label_CMP_VCO, 11, 0, 1, 1)

        self.checkBox_CMP_VCO = QtWidgets.QCheckBox(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_CMP_VCO.sizePolicy().hasHeightForWidth())
        self.checkBox_CMP_VCO.setSizePolicy(sizePolicy)
        self.checkBox_CMP_VCO.setText("")
        self.checkBox_CMP_VCO.setChecked(False)
        self.checkBox_CMP_VCO.setObjectName("checkBox_CMP_VCO")
        self.gridLayout_4.addWidget(self.checkBox_CMP_VCO, 11, 2, 1, 1)

        self.doubleSpinBox_CMP_VCO = QtWidgets.QDoubleSpinBox(self.tab_0)
        self.doubleSpinBox_CMP_VCO.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_CMP_VCO.setObjectName("doubleSpinBox_CMP_VCO")
        self.gridLayout_4.addWidget(self.doubleSpinBox_CMP_VCO, 11, 3, 1, 1)


        # ================================ELASTANCE==============================
        self.label_ELAS = QtWidgets.QLabel(self.tab_0)
        self.label_ELAS.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                      "background-color: rgb(35, 35, 35);\n"
                                      "color: rgb(255, 210, 119);")
        self.label_ELAS.setObjectName("label_ELAS")
        self.gridLayout_4.addWidget(self.label_ELAS, 0, 5, 1, 3)

        # ------------------------PULMONARY VEIN------------------------
        self.label_CMP_PUV = QtWidgets.QLabel(self.tab_0)
        self.label_CMP_PUV.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_CMP_PUV.setObjectName("label_CMP_PUV")
        self.gridLayout_4.addWidget(self.label_CMP_PUV, 1, 5, 1, 1)

        self.checkBox_ELA_PUV = QtWidgets.QCheckBox(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_ELA_PUV.sizePolicy().hasHeightForWidth())
        self.checkBox_ELA_PUV.setSizePolicy(sizePolicy)
        self.checkBox_ELA_PUV.setText("")
        self.checkBox_ELA_PUV.setChecked(False)
        self.checkBox_ELA_PUV.setObjectName("checkBox_ELA_PUV")
        self.gridLayout_4.addWidget(self.checkBox_ELA_PUV, 1, 6, 1, 1)

        self.doubleSpinBox_ELA_PUV = QtWidgets.QDoubleSpinBox(self.tab_0)
        self.doubleSpinBox_ELA_PUV.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_ELA_PUV.setObjectName("doubleSpinBox_ELA_PUV")
        self.gridLayout_4.addWidget(self.doubleSpinBox_ELA_PUV, 1, 7, 1, 1)

        #--------------------------PULMONARY ARTERY----------------------------
        self.label_CMP_PUA = QtWidgets.QLabel(self.tab_0)
        self.label_CMP_PUA.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_CMP_PUA.setObjectName("label_CMP_PUA")
        self.gridLayout_4.addWidget(self.label_CMP_PUA, 2, 5, 1, 1)

        self.checkBox_ELA_PUA = QtWidgets.QCheckBox(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_ELA_PUA.sizePolicy().hasHeightForWidth())
        self.checkBox_ELA_PUA.setSizePolicy(sizePolicy)
        self.checkBox_ELA_PUA.setText("")
        self.checkBox_ELA_PUA.setChecked(False)
        self.checkBox_ELA_PUA.setObjectName("checkBox_ELA_PUA")
        self.gridLayout_4.addWidget(self.checkBox_ELA_PUA, 2, 6, 1, 1)

        self.doubleSpinBox_ELA_PUA = QtWidgets.QDoubleSpinBox(self.tab_0)
        self.doubleSpinBox_ELA_PUA.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_ELA_PUA.setObjectName("doubleSpinBox_ELA_PUA")
        self.gridLayout_4.addWidget(self.doubleSpinBox_ELA_PUA, 2, 7, 1, 1)

        #-------------------------- PULMONARY CAPILLARY---------------------
        self.label_ELA_PUC = QtWidgets.QLabel(self.tab_0)
        self.label_ELA_PUC.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_ELA_PUC.setObjectName("label_ELA_PUC")
        self.gridLayout_4.addWidget(self.label_ELA_PUC, 3, 5, 1, 1)

        self.checkBox_ELA_PUC = QtWidgets.QCheckBox(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_ELA_PUC.sizePolicy().hasHeightForWidth())
        self.checkBox_ELA_PUC.setSizePolicy(sizePolicy)
        self.checkBox_ELA_PUC.setText("")
        self.checkBox_ELA_PUC.setChecked(False)
        self.checkBox_ELA_PUC.setObjectName("checkBox_ELA_PUC")
        self.gridLayout_4.addWidget(self.checkBox_ELA_PUC, 3, 6, 1, 1)

        self.doubleSpinBox_ELA_PUC = QtWidgets.QDoubleSpinBox(self.tab_0)
        self.doubleSpinBox_ELA_PUC.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_ELA_PUC.setObjectName("doubleSpinBox_ELA_PUC")
        self.gridLayout_4.addWidget(self.doubleSpinBox_ELA_PUC, 3, 7, 1, 1)




        # -----------------------LEFT ATRIUM (AMPLITUDE)----------------------
        self.label_ELA_LAa = QtWidgets.QLabel(self.tab_0)
        self.label_ELA_LAa.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_ELA_LAa.setObjectName("label_ELA_LAa")
        self.gridLayout_4.addWidget(self.label_ELA_LAa, 4, 5, 1, 1)

        self.checkBox_ELA_LAa = QtWidgets.QCheckBox(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_ELA_LAa.sizePolicy().hasHeightForWidth())
        self.checkBox_ELA_LAa.setSizePolicy(sizePolicy)
        self.checkBox_ELA_LAa.setText("")
        self.checkBox_ELA_LAa.setChecked(False)
        self.checkBox_ELA_LAa.setObjectName("checkBox_ELA_LAa")
        self.gridLayout_4.addWidget(self.checkBox_ELA_LAa, 4, 6, 1, 1)

        self.doubleSpinBox_ELA_LAa = QtWidgets.QDoubleSpinBox(self.tab_0)
        self.doubleSpinBox_ELA_LAa.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_ELA_LAa.setObjectName("doubleSpinBox_ELA_LAa")
        self.gridLayout_4.addWidget(self.doubleSpinBox_ELA_LAa, 4, 7, 1, 1)

        #--------------------------------LEFT ATRIUM(BASE)------------------------
        self.label_ELA_LAb = QtWidgets.QLabel(self.tab_0)
        self.label_ELA_LAb.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_ELA_LAb.setObjectName("label_ELA_LAb")
        self.gridLayout_4.addWidget(self.label_ELA_LAb, 5, 5, 1, 1)

        self.checkBox_ELA_LAb = QtWidgets.QCheckBox(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_ELA_LAb.sizePolicy().hasHeightForWidth())
        self.checkBox_ELA_LAb.setSizePolicy(sizePolicy)
        self.checkBox_ELA_LAb.setText("")
        self.checkBox_ELA_LAb.setChecked(False)
        self.checkBox_ELA_LAb.setObjectName("checkBox_ELA_LAb")
        self.gridLayout_4.addWidget(self.checkBox_ELA_LAb, 5, 6, 1, 1)

        self.doubleSpinBox_ELA_LAb = QtWidgets.QDoubleSpinBox(self.tab_0)
        self.doubleSpinBox_ELA_LAb.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_ELA_LAb.setObjectName("doubleSpinBox_ELA_LAb")
        self.gridLayout_4.addWidget(self.doubleSpinBox_ELA_LAb, 5, 7, 1, 1)



        # ----------------------LEFT VENTRICLE (AMPLITUDE)---------------------------
        self.label_ELA_LVa = QtWidgets.QLabel(self.tab_0)
        self.label_ELA_LVa.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_ELA_LVa.setObjectName("label_ELA_LVa")
        self.gridLayout_4.addWidget(self.label_ELA_LVa, 6, 5, 1, 1)

        self.checkBox_ELA_LVa = QtWidgets.QCheckBox(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_ELA_LVa.sizePolicy().hasHeightForWidth())
        self.checkBox_ELA_LVa.setSizePolicy(sizePolicy)
        self.checkBox_ELA_LVa.setText("")
        self.checkBox_ELA_LVa.setChecked(False)
        self.checkBox_ELA_LVa.setObjectName("checkBox_ELA_LVa")
        self.gridLayout_4.addWidget(self.checkBox_ELA_LVa, 6, 6, 1, 1)

        self.doubleSpinBox_ELA_LVa = QtWidgets.QDoubleSpinBox(self.tab_0)
        self.doubleSpinBox_ELA_LVa.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_ELA_LVa.setObjectName("doubleSpinBox_ELA_LVa")
        self.gridLayout_4.addWidget(self.doubleSpinBox_ELA_LVa, 6, 7, 1, 1)


        # -----------------------LEFT VENTRICLE (BASE)---------------------------
        self.label_ELA_LVb = QtWidgets.QLabel(self.tab_0)
        self.label_ELA_LVb.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_ELA_LVb.setObjectName("label_ELA_LVb")
        self.gridLayout_4.addWidget(self.label_ELA_LVb, 7, 5, 1, 1)

        self.checkBox_ELA_LVb = QtWidgets.QCheckBox(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_ELA_LVb.sizePolicy().hasHeightForWidth())
        self.checkBox_ELA_LVb.setSizePolicy(sizePolicy)
        self.checkBox_ELA_LVb.setText("")
        self.checkBox_ELA_LVb.setChecked(False)
        self.checkBox_ELA_LVb.setObjectName("checkBox_ELA_LVb")
        self.gridLayout_4.addWidget(self.checkBox_ELA_LVb, 7, 6, 1, 1)

        self.doubleSpinBox_ELA_LVb = QtWidgets.QDoubleSpinBox(self.tab_0)
        self.doubleSpinBox_ELA_LVb.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_ELA_LVb.setObjectName("doubleSpinBox_ELA_LVb")
        self.gridLayout_4.addWidget(self.doubleSpinBox_ELA_LVb, 7, 7, 1, 1)

        # -----------------------RIGHT ATRIUM (AMPLITUDE)----------------------
        self.label_ELA_RAa = QtWidgets.QLabel(self.tab_0)
        self.label_ELA_RAa.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_ELA_RAa.setObjectName("label_ELA_RAa")
        self.gridLayout_4.addWidget(self.label_ELA_RAa, 8, 5, 1, 1)

        self.checkBox_ELA_RAa = QtWidgets.QCheckBox(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_ELA_RAa.sizePolicy().hasHeightForWidth())
        self.checkBox_ELA_RAa.setSizePolicy(sizePolicy)
        self.checkBox_ELA_RAa.setText("")
        self.checkBox_ELA_RAa.setChecked(False)
        self.checkBox_ELA_RAa.setObjectName("checkBox_ELA_RAa")
        self.gridLayout_4.addWidget(self.checkBox_ELA_RAa, 8, 6, 1, 1)

        self.doubleSpinBox_ELA_RAa = QtWidgets.QDoubleSpinBox(self.tab_0)
        self.doubleSpinBox_ELA_RAa.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_ELA_RAa.setObjectName("doubleSpinBox_ELA_RAa")
        self.gridLayout_4.addWidget(self.doubleSpinBox_ELA_RAa, 8, 7, 1, 1)

        # -----------------------RIGHT ATRIUM (BASE)----------------------
        self.label_ELA_RAb = QtWidgets.QLabel(self.tab_0)
        self.label_ELA_RAb.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_ELA_RAb.setObjectName("label_ELA_RAb")
        self.gridLayout_4.addWidget(self.label_ELA_RAb, 9, 5, 1, 1)

        self.checkBox_ELA_RAb = QtWidgets.QCheckBox(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_ELA_RAb.sizePolicy().hasHeightForWidth())
        self.checkBox_ELA_RAb.setSizePolicy(sizePolicy)
        self.checkBox_ELA_RAb.setText("")
        self.checkBox_ELA_RAb.setChecked(False)
        self.checkBox_ELA_RAb.setObjectName("checkBox_ELA_RAb")
        self.gridLayout_4.addWidget(self.checkBox_ELA_RAb, 9, 6, 1, 1)

        self.doubleSpinBox_ELA_RAb = QtWidgets.QDoubleSpinBox(self.tab_0)
        self.doubleSpinBox_ELA_RAb.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_ELA_RAb.setObjectName("doubleSpinBox_ELA_RAb")
        self.gridLayout_4.addWidget(self.doubleSpinBox_ELA_RAb, 9, 7, 1, 1)

        # -----------------------RIGHT VENTRICLE (AMPLITUDE)----------------------
        self.label_ELA_RVa = QtWidgets.QLabel(self.tab_0)
        self.label_ELA_RVa.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_ELA_RVa.setObjectName("label_ELA_RVa")
        self.gridLayout_4.addWidget(self.label_ELA_RVa, 11, 5, 1, 1)

        self.checkBox_ELA_RVa = QtWidgets.QCheckBox(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_ELA_RVa.sizePolicy().hasHeightForWidth())
        self.checkBox_ELA_RVa.setSizePolicy(sizePolicy)
        self.checkBox_ELA_RVa.setText("")
        self.checkBox_ELA_RVa.setChecked(False)
        self.checkBox_ELA_RVa.setObjectName("checkBox_ELA_RVa")
        self.gridLayout_4.addWidget(self.checkBox_ELA_RVa, 11, 6, 1, 1)

        self.doubleSpinBox_ELA_RVa = QtWidgets.QDoubleSpinBox(self.tab_0)
        self.doubleSpinBox_ELA_RVa.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_ELA_RVa.setObjectName("doubleSpinBox_ELA_RVa")
        self.gridLayout_4.addWidget(self.doubleSpinBox_ELA_RVa, 11, 7, 1, 1)


        # -----------------------RIGHT VENTRICLE (BASE)----------------------
        self.label_ELA_RVb = QtWidgets.QLabel(self.tab_0)
        self.label_ELA_RVb.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_ELA_RVb.setObjectName("label_ELA_RVb")
        self.gridLayout_4.addWidget(self.label_ELA_RVb, 0, 9, 1, 1)

        self.doubleSpinBox_ELA_RVb = QtWidgets.QDoubleSpinBox(self.tab_0)
        self.doubleSpinBox_ELA_RVb.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_ELA_RVb.setObjectName("doubleSpinBox_ELA_RVb")
        self.gridLayout_4.addWidget(self.doubleSpinBox_ELA_RVb, 0, 11, 1, 1)

        self.checkBox_ELA_RVb = QtWidgets.QCheckBox(self.tab_0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_ELA_RVb.sizePolicy().hasHeightForWidth())
        self.checkBox_ELA_RVb.setSizePolicy(sizePolicy)
        self.checkBox_ELA_RVb.setText("")
        self.checkBox_ELA_RVb.setChecked(False)
        self.checkBox_ELA_RVb.setObjectName("checkBox_ELA_RVb")
        self.gridLayout_4.addWidget(self.checkBox_ELA_RVb, 0, 10, 1, 1)

        #===================================SPACER ITEMS=========================
        #spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        #self.gridLayout_4.addItem(spacerItem, 4, 4, 1, 1)

        #spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        #self.gridLayout_4.addItem(spacerItem1, 2, 8, 1, 1)


        #________________________________TAB WIDGET (TAB 1)_______________________________
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout.setObjectName("gridLayout")
        #_________________________________SPACER ITEMS__________________________
        #spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        #self.gridLayout.addItem(spacerItem2, 5, 3, 1, 1)

        #==========================INDUCTANCE===========================
        self.label_IND = QtWidgets.QLabel(self.tab_1)
        self.label_IND.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                     "background-color: rgb(35, 35, 35);\n"
                                     "color: rgb(255, 210, 119);")
        self.label_IND.setObjectName("label_IND")
        self.gridLayout.addWidget(self.label_IND, 0, 0, 1, 3)

        #------------------------VENOUS INERTANCE------------------------------
        self.label_IND_VI = QtWidgets.QLabel(self.tab_1)
        self.label_IND_VI.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255,255,255);")
        self.label_IND_VI.setObjectName("label_IND_VI")
        self.gridLayout.addWidget(self.label_IND_VI, 1, 0, 1, 1)

        self.checkBox_IND_VI = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_IND_VI.sizePolicy().hasHeightForWidth())
        self.checkBox_IND_VI.setSizePolicy(sizePolicy)
        self.checkBox_IND_VI.setText("")
        self.checkBox_IND_VI.setChecked(False)
        self.checkBox_IND_VI.setObjectName("checkBox_IND_VI")
        self.gridLayout.addWidget(self.checkBox_IND_VI, 1, 1, 1, 1)

        self.doubleSpinBox_IND_VI = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_IND_VI.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                "color: rgb(255, 210, 119);\n"
                                                "selection-color: rgb(237, 85, 59);\n"
                                                "selection-background-color: rgb(33, 57, 86);\n"
                                                "\n"
                                                "font: 11pt \"Calibri\";")
        self.doubleSpinBox_IND_VI.setObjectName("doubleSpinBox_IND_VI")
        self.gridLayout.addWidget(self.doubleSpinBox_IND_VI, 1, 2, 1, 1)

        #----------------------VENA CAVA-----------------------------------
        self.label_IND_VC = QtWidgets.QLabel(self.tab_1)
        self.label_IND_VC.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255,255,255);")
        self.label_IND_VC.setObjectName("label_IND_VC")
        self.gridLayout.addWidget(self.label_IND_VC, 2, 0, 1, 1)

        self.checkBox_IND_VC = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_IND_VC.sizePolicy().hasHeightForWidth())
        self.checkBox_IND_VC.setSizePolicy(sizePolicy)
        self.checkBox_IND_VC.setText("")
        self.checkBox_IND_VC.setChecked(False)
        self.checkBox_IND_VC.setObjectName("checkBox_IND_VC")
        self.gridLayout.addWidget(self.checkBox_IND_VC, 2, 1, 1, 1)

        self.doubleSpinBox_IND_VC = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_IND_VC.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                "color: rgb(255, 210, 119);\n"
                                                "selection-color: rgb(237, 85, 59);\n"
                                                "selection-background-color: rgb(33, 57, 86);\n"
                                                "\n"
                                                "font: 11pt \"Calibri\";")
        self.doubleSpinBox_IND_VC.setObjectName("doubleSpinBox_IND_VC")
        self.gridLayout.addWidget(self.doubleSpinBox_IND_VC, 2, 2, 1, 1)

        # -----------------------TRICUSPID VALVE------------------------------
        self.label_IND_TV = QtWidgets.QLabel(self.tab_1)
        self.label_IND_TV.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255,255,255);")
        self.label_IND_TV.setObjectName("label_IND_TV")
        self.gridLayout.addWidget(self.label_IND_TV, 3, 0, 1, 1)

        self.checkBox_IND_TV = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_IND_TV.sizePolicy().hasHeightForWidth())
        self.checkBox_IND_TV.setSizePolicy(sizePolicy)
        self.checkBox_IND_TV.setText("")
        self.checkBox_IND_TV.setChecked(False)
        self.checkBox_IND_TV.setObjectName("checkBox_IND_TV")
        self.gridLayout.addWidget(self.checkBox_IND_TV, 3, 1, 1, 1)

        self.doubleSpinBox_IND_TV = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_IND_TV.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                "color: rgb(255, 210, 119);\n"
                                                "selection-color: rgb(237, 85, 59);\n"
                                                "selection-background-color: rgb(33, 57, 86);\n"
                                                "\n"
                                                "font: 11pt \"Calibri\";")
        self.doubleSpinBox_IND_TV.setObjectName("doubleSpinBox_IND_TV")
        self.gridLayout.addWidget(self.doubleSpinBox_IND_TV, 3, 2, 1, 1)

        # -----------------------PULMONARY VALVE------------------------------
        self.label_IND_PUVA = QtWidgets.QLabel(self.tab_1)
        self.label_IND_PUVA.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                          "color: rgb(255,255,255);")
        self.label_IND_PUVA.setObjectName("label_IND_PUVA")
        self.gridLayout.addWidget(self.label_IND_PUVA, 4, 0, 1, 1)

        self.doubleSpinBox_IND_PUVA = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_IND_PUVA.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                  "color: rgb(255, 210, 119);\n"
                                                  "selection-color: rgb(237, 85, 59);\n"
                                                  "selection-background-color: rgb(33, 57, 86);\n"
                                                  "\n"
                                                  "font: 11pt \"Calibri\";")
        self.doubleSpinBox_IND_PUVA.setObjectName("doubleSpinBox_IND_PUVA")
        self.gridLayout.addWidget(self.doubleSpinBox_IND_PUVA, 4, 2, 1, 1)

        self.checkBox_IND_PUVA = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_IND_PUVA.sizePolicy().hasHeightForWidth())
        self.checkBox_IND_PUVA.setSizePolicy(sizePolicy)
        self.checkBox_IND_PUVA.setText("")
        self.checkBox_IND_PUVA.setChecked(False)
        self.checkBox_IND_PUVA.setObjectName("checkBox_IND_PUVA")
        self.gridLayout.addWidget(self.checkBox_IND_PUVA, 4, 1, 1, 1)

        # -----------------------PULMONARY ARTERY------------------------------
        self.label_IND_PUA = QtWidgets.QLabel(self.tab_1)
        self.label_IND_PUA.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_IND_PUA.setObjectName("label_IND_PUA")
        self.gridLayout.addWidget(self.label_IND_PUA, 5, 0, 1, 1)

        self.checkBox_IND_PUA = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_IND_PUA.sizePolicy().hasHeightForWidth())
        self.checkBox_IND_PUA.setSizePolicy(sizePolicy)
        self.checkBox_IND_PUA.setText("")
        self.checkBox_IND_PUA.setChecked(False)
        self.checkBox_IND_PUA.setObjectName("checkBox_IND_PUA")
        self.gridLayout.addWidget(self.checkBox_IND_PUA, 5, 1, 1, 1)

        self.doubleSpinBox_IND_PUA = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_IND_PUA.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_IND_PUA.setObjectName("doubleSpinBox_IND_PUA")
        self.gridLayout.addWidget(self.doubleSpinBox_IND_PUA, 5, 2, 1, 1)

        # -----------------------PULMONARY CAPILLARY ------------------------------
        self.label_IND_PUC = QtWidgets.QLabel(self.tab_1)
        self.label_IND_PUC.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_IND_PUC.setObjectName("label_IND_PUC")
        self.gridLayout.addWidget(self.label_IND_PUC, 6, 0, 1, 1)

        self.doubleSpinBox_IND_PUC = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_IND_PUC.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_IND_PUC.setObjectName("doubleSpinBox_IND_PUC")
        self.gridLayout.addWidget(self.doubleSpinBox_IND_PUC, 6, 2, 1, 1)

        self.checkBox_IND_PUC = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_IND_PUC.sizePolicy().hasHeightForWidth())
        self.checkBox_IND_PUC.setSizePolicy(sizePolicy)
        self.checkBox_IND_PUC.setText("")
        self.checkBox_IND_PUC.setChecked(False)
        self.checkBox_IND_PUC.setObjectName("checkBox_IND_PUC")
        self.gridLayout.addWidget(self.checkBox_IND_PUC, 6, 1, 1, 1)

        # -----------------------PULMONARY VEIN------------------------------
        self.label_IND_PUV = QtWidgets.QLabel(self.tab_1)
        self.label_IND_PUV.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_IND_PUV.setObjectName("label_IND_PUV")
        self.gridLayout.addWidget(self.label_IND_PUV, 7, 0, 1, 1)

        self.checkBox_IND_PUV = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_IND_PUV.sizePolicy().hasHeightForWidth())
        self.checkBox_IND_PUV.setSizePolicy(sizePolicy)
        self.checkBox_IND_PUV.setText("")
        self.checkBox_IND_PUV.setChecked(False)
        self.checkBox_IND_PUV.setObjectName("checkBox_IND_PUV")
        self.gridLayout.addWidget(self.checkBox_IND_PUV, 7, 1, 1, 1)

        self.doubleSpinBox_IND_PUV = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_IND_PUV.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_IND_PUV.setObjectName("doubleSpinBox_IND_PUV")
        self.gridLayout.addWidget(self.doubleSpinBox_IND_PUV, 7, 2, 1, 1)

        # -----------------------MITRAL VALVE------------------------------
        self.label_IND_MV = QtWidgets.QLabel(self.tab_1)
        self.label_IND_MV.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255,255,255);")
        self.label_IND_MV.setObjectName("label_IND_MV")
        self.gridLayout.addWidget(self.label_IND_MV, 8, 0, 1, 1)


        self.checkBox_IND_MV = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_IND_MV.sizePolicy().hasHeightForWidth())
        self.checkBox_IND_MV.setSizePolicy(sizePolicy)
        self.checkBox_IND_MV.setText("")
        self.checkBox_IND_MV.setChecked(False)
        self.checkBox_IND_MV.setObjectName("checkBox_IND_MV")
        self.gridLayout.addWidget(self.checkBox_IND_MV, 8, 1, 1, 1)

        self.doubleSpinBox_IND_MV = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_IND_MV.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                "color: rgb(255, 210, 119);\n"
                                                "selection-color: rgb(237, 85, 59);\n"
                                                "selection-background-color: rgb(33, 57, 86);\n"
                                                "\n"
                                                "font: 11pt \"Calibri\";")
        self.doubleSpinBox_IND_MV.setObjectName("doubleSpinBox_IND_MV")
        self.gridLayout.addWidget(self.doubleSpinBox_IND_MV, 8, 2, 1, 1)

        # -----------------------AORTIC VALVE------------------------------
        self.label_IND_AV = QtWidgets.QLabel(self.tab_1)
        self.label_IND_AV.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255,255,255);")
        self.label_IND_AV.setObjectName("label_IND_AV")
        self.gridLayout.addWidget(self.label_IND_AV, 9, 0, 1, 1)

        self.checkBox_IND_AV = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_IND_AV.sizePolicy().hasHeightForWidth())
        self.checkBox_IND_AV.setSizePolicy(sizePolicy)
        self.checkBox_IND_AV.setText("")
        self.checkBox_IND_AV.setChecked(False)
        self.checkBox_IND_AV.setObjectName("checkBox_IND_AV")
        self.gridLayout.addWidget(self.checkBox_IND_AV, 9, 1, 1, 1)

        self.doubleSpinBox_IND_AV = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_IND_AV.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                "color: rgb(255, 210, 119);\n"
                                                "selection-color: rgb(237, 85, 59);\n"
                                                "selection-background-color: rgb(33, 57, 86);\n"
                                                "\n"
                                                "font: 11pt \"Calibri\";")
        self.doubleSpinBox_IND_AV.setObjectName("doubleSpinBox_IND_AV")
        self.gridLayout.addWidget(self.doubleSpinBox_IND_AV, 9, 2, 1, 1)

        # -----------------------AORTA------------------------------
        self.label_IND_AO = QtWidgets.QLabel(self.tab_1)
        self.label_IND_AO.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255,255,255);")
        self.label_IND_AO.setObjectName("label_IND_AO")
        self.gridLayout.addWidget(self.label_IND_AO, 10, 0, 1, 1)

        self.checkBox_IND_AO = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_IND_AO.sizePolicy().hasHeightForWidth())
        self.checkBox_IND_AO.setSizePolicy(sizePolicy)
        self.checkBox_IND_AO.setText("")
        self.checkBox_IND_AO.setChecked(False)
        self.checkBox_IND_AO.setObjectName("checkBox_IND_AO")
        self.gridLayout.addWidget(self.checkBox_IND_AO, 10, 1, 1, 1)

        self.doubleSpinBox_IND_AO = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_IND_AO.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                "color: rgb(255, 210, 119);\n"
                                                "selection-color: rgb(237, 85, 59);\n"
                                                "selection-background-color: rgb(33, 57, 86);\n"
                                                "\n"
                                                "font: 11pt \"Calibri\";")
        self.doubleSpinBox_IND_AO.setObjectName("doubleSpinBox_IND_AO")
        self.gridLayout.addWidget(self.doubleSpinBox_IND_AO, 10, 2, 1, 1)
       # -----------------------CAPILLARY------------------------------
        self.label_IND_CAP = QtWidgets.QLabel(self.tab_1)
        self.label_IND_CAP.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_IND_CAP.setObjectName("label_IND_CAP")
        self.gridLayout.addWidget(self.label_IND_CAP, 11, 0, 1, 1)

        self.checkBox_IND_CAP = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_IND_CAP.sizePolicy().hasHeightForWidth())
        self.checkBox_IND_CAP.setSizePolicy(sizePolicy)
        self.checkBox_IND_CAP.setText("")
        self.checkBox_IND_CAP.setChecked(False)
        self.checkBox_IND_CAP.setObjectName("checkBox_IND_CAP")
        self.gridLayout.addWidget(self.checkBox_IND_CAP, 11, 1, 1, 1)

        self.doubleSpinBox_IND_CAP = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_IND_CAP.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_IND_CAP.setObjectName("doubleSpinBox_IND_CAP")
        self.gridLayout.addWidget(self.doubleSpinBox_IND_CAP, 11, 2, 1, 1)

        #=========================RESISTANCE================================
        self.label_RES = QtWidgets.QLabel(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_RES.sizePolicy().hasHeightForWidth())
        self.label_RES.setSizePolicy(sizePolicy)
        self.label_RES.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                     "background-color: rgb(35, 35, 35);\n"
                                     "color: rgb(255, 210, 119);")
        self.label_RES.setObjectName("label_RES")
        self.gridLayout.addWidget(self.label_RES, 0, 4, 1, 3)

        # -------------------------VENOUS INERTANCE--------------------------
        self.label_RES_VI = QtWidgets.QLabel(self.tab_1)
        self.label_RES_VI.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255,255,255);")

        self.label_RES_VI.setObjectName("label_RES_VI")
        self.gridLayout.addWidget(self.label_RES_VI, 1, 4, 1, 1)

        self.checkBox_RES_VI = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_RES_VI.sizePolicy().hasHeightForWidth())
        self.checkBox_RES_VI.setSizePolicy(sizePolicy)
        self.checkBox_RES_VI.setText("")
        self.checkBox_RES_VI.setChecked(False)
        self.checkBox_RES_VI.setObjectName("checkBox_RES_VI")
        self.gridLayout.addWidget(self.checkBox_RES_VI, 1, 5, 1, 1)


        self.doubleSpinBox_RES_VI = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_RES_VI.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                "color: rgb(255, 210, 119);\n"
                                                "selection-color: rgb(237, 85, 59);\n"
                                                "selection-background-color: rgb(33, 57, 86);\n"
                                                "\n"
                                                "font: 11pt \"Calibri\";")
        self.doubleSpinBox_RES_VI.setObjectName("doubleSpinBox_RES_VI")
        self.gridLayout.addWidget(self.doubleSpinBox_RES_VI, 1, 6, 1, 1)

        # ----------------------VENA CAVA-------------------------------------
        self.label_RES_VC = QtWidgets.QLabel(self.tab_1)
        self.label_RES_VC.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255,255,255);")
        self.label_RES_VC.setObjectName("label_RES_VC")
        self.gridLayout.addWidget(self.label_RES_VC, 2, 4, 1, 1)

        self.checkBox_RES_VC = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_RES_VC.sizePolicy().hasHeightForWidth())
        self.checkBox_RES_VC.setSizePolicy(sizePolicy)
        self.checkBox_RES_VC.setText("")
        self.checkBox_RES_VC.setChecked(False)
        self.checkBox_RES_VC.setObjectName("checkBox_RES_VC")
        self.gridLayout.addWidget(self.checkBox_RES_VC, 2, 5, 1, 1)

        self.doubleSpinBox_RES_VC = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_RES_VC.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                "color: rgb(255, 210, 119);\n"
                                                "selection-color: rgb(237, 85, 59);\n"
                                                "selection-background-color: rgb(33, 57, 86);\n"
                                                "\n"
                                                "font: 11pt \"Calibri\";")
        self.doubleSpinBox_RES_VC.setObjectName("doubleSpinBox_RES_VC")
        self.gridLayout.addWidget(self.doubleSpinBox_RES_VC, 2, 6, 1, 1)

        # --------------------TRICUSUPID VALVE---------------------------------
        self.label_RES_TV = QtWidgets.QLabel(self.tab_1)
        self.label_RES_TV.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255,255,255);")
        self.label_RES_TV.setObjectName("label_RES_TV")
        self.gridLayout.addWidget(self.label_RES_TV, 3, 4, 1, 1)

        self.checkBox_RES_TV = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_RES_TV.sizePolicy().hasHeightForWidth())
        self.checkBox_RES_TV.setSizePolicy(sizePolicy)
        self.checkBox_RES_TV.setText("")
        self.checkBox_RES_TV.setChecked(False)
        self.checkBox_RES_TV.setObjectName("checkBox_RES_TV")
        self.gridLayout.addWidget(self.checkBox_RES_TV, 3, 5, 1, 1)

        self.doubleSpinBox_RES_TV = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_RES_TV.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                "color: rgb(255, 210, 119);\n"
                                                "selection-color: rgb(237, 85, 59);\n"
                                                "selection-background-color: rgb(33, 57, 86);\n"
                                                "\n"
                                                "font: 11pt \"Calibri\";")
        self.doubleSpinBox_RES_TV.setObjectName("doubleSpinBox_RES_TV")
        self.gridLayout.addWidget(self.doubleSpinBox_RES_TV, 3, 6, 1, 1)

       # -----------------PULMONARY VALVE-------------------------------
        self.label_RES_PUVA = QtWidgets.QLabel(self.tab_1)
        self.label_RES_PUVA.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                          "color: rgb(255,255,255);")
        self.label_RES_PUVA.setObjectName("label_RES_PUVA")
        self.gridLayout.addWidget(self.label_RES_PUVA, 4, 4, 1, 1)

        self.checkBox_RES_PUVA = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_RES_PUVA.sizePolicy().hasHeightForWidth())
        self.checkBox_RES_PUVA.setSizePolicy(sizePolicy)
        self.checkBox_RES_PUVA.setText("")
        self.checkBox_RES_PUVA.setChecked(False)
        self.checkBox_RES_PUVA.setObjectName("checkBox_RES_PUVA")
        self.gridLayout.addWidget(self.checkBox_RES_PUVA, 4, 5, 1, 1)

        self.doubleSpinBox_RES_PUVA = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_RES_PUVA.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                  "color: rgb(255, 210, 119);\n"
                                                  "selection-color: rgb(237, 85, 59);\n"
                                                  "selection-background-color: rgb(33, 57, 86);\n"
                                                  "\n"
                                                  "font: 11pt \"Calibri\";")
        self.doubleSpinBox_RES_PUVA.setObjectName("doubleSpinBox_RES_PUVA")
        self.gridLayout.addWidget(self.doubleSpinBox_RES_PUVA, 4, 6, 1, 1)

        # ------------------------PULMONARY ARTERY-------------------
        self.label_RES_PUA = QtWidgets.QLabel(self.tab_1)
        self.label_RES_PUA.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_RES_PUA.setObjectName("label_RES_PUA")
        self.gridLayout.addWidget(self.label_RES_PUA, 5, 4, 1, 1)

        self.checkBox_RES_PUA = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_RES_PUA.sizePolicy().hasHeightForWidth())
        self.checkBox_RES_PUA.setSizePolicy(sizePolicy)
        self.checkBox_RES_PUA.setText("")
        self.checkBox_RES_PUA.setChecked(False)
        self.checkBox_RES_PUA.setObjectName("checkBox_RES_PUA")
        self.gridLayout.addWidget(self.checkBox_RES_PUA, 5, 5, 1, 1)

        self.doubleSpinBox_RES_PUA = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_RES_PUA.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_RES_PUA.setObjectName("doubleSpinBox_RES_PUA")
        self.gridLayout.addWidget(self.doubleSpinBox_RES_PUA, 5, 6, 1, 1)

        # --------------------PULMONARY CAPILLARY------------------------
        self.label_RES_CAP = QtWidgets.QLabel(self.tab_1)
        self.label_RES_CAP.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_RES_CAP.setObjectName("label_RES_CAP")
        self.gridLayout.addWidget(self.label_RES_CAP, 6, 4, 1, 1)

        self.checkBox_RES_PUC = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_RES_PUC.sizePolicy().hasHeightForWidth())
        self.checkBox_RES_PUC.setSizePolicy(sizePolicy)
        self.checkBox_RES_PUC.setText("")
        self.checkBox_RES_PUC.setChecked(False)
        self.checkBox_RES_PUC.setObjectName("checkBox_RES_PUC")
        self.gridLayout.addWidget(self.checkBox_RES_PUC, 6, 5, 1, 1)

        self.doubleSpinBox_RES_PUC = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_RES_PUC.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_RES_PUC.setObjectName("doubleSpinBox_RES_PUC")
        self.gridLayout.addWidget(self.doubleSpinBox_RES_PUC, 6, 6, 1, 1)

        # -----------------PULMONARY VEIN-----------------------------
        self.label_RES_PUV = QtWidgets.QLabel(self.tab_1)
        self.label_RES_PUV.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_RES_PUV.setObjectName("label_RES_PUV")
        self.gridLayout.addWidget(self.label_RES_PUV, 7, 4, 1, 1)

        self.checkBox_RES_PUV = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_RES_PUV.sizePolicy().hasHeightForWidth())
        self.checkBox_RES_PUV.setSizePolicy(sizePolicy)
        self.checkBox_RES_PUV.setText("")
        self.checkBox_RES_PUV.setChecked(False)
        self.checkBox_RES_PUV.setObjectName("checkBox_RES_PUV")
        self.gridLayout.addWidget(self.checkBox_RES_PUV, 7, 5, 1, 1)
        self.doubleSpinBox_RES_PUV = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_RES_PUV.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_RES_PUV.setObjectName("doubleSpinBox_RES_PUV")
        self.gridLayout.addWidget(self.doubleSpinBox_RES_PUV, 7, 6, 1, 1)

        # ---------------------------MITRAL VALVE ------------------------------
        self.label_RES_MV = QtWidgets.QLabel(self.tab_1)
        self.label_RES_MV.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255,255,255);")
        self.label_RES_MV.setObjectName("label_RES_MV")
        self.gridLayout.addWidget(self.label_RES_MV, 8, 4, 1, 1)

        self.checkBox_RES_MV = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_RES_MV.sizePolicy().hasHeightForWidth())
        self.checkBox_RES_MV.setSizePolicy(sizePolicy)
        self.checkBox_RES_MV.setText("")
        self.checkBox_RES_MV.setChecked(False)
        self.checkBox_RES_MV.setObjectName("checkBox_RES_MV")
        self.gridLayout.addWidget(self.checkBox_RES_MV, 8, 5, 1, 1)

        self.doubleSpinBox_RES_MV = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_RES_MV.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                "color: rgb(255, 210, 119);\n"
                                                "selection-color: rgb(237, 85, 59);\n"
                                                "selection-background-color: rgb(33, 57, 86);\n"
                                                "\n"
                                                "font: 11pt \"Calibri\";")
        self.doubleSpinBox_RES_MV.setObjectName("doubleSpinBox_RES_MV")
        self.gridLayout.addWidget(self.doubleSpinBox_RES_MV, 8, 6, 1, 1)

        # --------------------AORTIC VALVE ------------------------------
        self.label_RES_AV = QtWidgets.QLabel(self.tab_1)
        self.label_RES_AV.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255,255,255);")
        self.label_RES_AV.setObjectName("label_RES_AV")
        self.gridLayout.addWidget(self.label_RES_AV, 9, 4, 1, 1)

        self.checkBox_RES_AV = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_RES_AV.sizePolicy().hasHeightForWidth())
        self.checkBox_RES_AV.setSizePolicy(sizePolicy)
        self.checkBox_RES_AV.setText("")
        self.checkBox_RES_AV.setChecked(False)
        self.checkBox_RES_AV.setObjectName("checkBox_RES_AV")
        self.gridLayout.addWidget(self.checkBox_RES_AV, 9, 5, 1, 1)

        self.doubleSpinBox_RES_AV = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_RES_AV.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                "color: rgb(255, 210, 119);\n"
                                                "selection-color: rgb(237, 85, 59);\n"
                                                "selection-background-color: rgb(33, 57, 86);\n"
                                                "\n"
                                                "font: 11pt \"Calibri\";")
        self.doubleSpinBox_RES_AV.setObjectName("doubleSpinBox_RES_AV")
        self.gridLayout.addWidget(self.doubleSpinBox_RES_AV, 9, 6, 1, 1)

        # -----------------------------AORTA---------------------------
        self.label_RES_AO = QtWidgets.QLabel(self.tab_1)
        self.label_RES_AO.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255,255,255);")
        self.label_RES_AO.setObjectName("label_RES_AO")
        self.gridLayout.addWidget(self.label_RES_AO, 10, 4, 1, 1)

        self.doubleSpinBox_RES_AO = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_RES_AO.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                "color: rgb(255, 210, 119);\n"
                                                "selection-color: rgb(237, 85, 59);\n"
                                                "selection-background-color: rgb(33, 57, 86);\n"
                                                "\n"
                                                "font: 11pt \"Calibri\";")
        self.doubleSpinBox_RES_AO.setObjectName("doubleSpinBox_RES_AO")
        self.gridLayout.addWidget(self.doubleSpinBox_RES_AO, 10, 6, 1, 1)

        self.checkBox_RES_AO = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_RES_AO.sizePolicy().hasHeightForWidth())
        self.checkBox_RES_AO.setSizePolicy(sizePolicy)
        self.checkBox_RES_AO.setText("")
        self.checkBox_RES_AO.setChecked(False)
        self.checkBox_RES_AO.setObjectName("checkBox_RES_AO")
        self.gridLayout.addWidget(self.checkBox_RES_AO, 10, 5, 1, 1)

        #  -------------------CAPILLARY--------------------------
        self.label_RES_CAP_2 = QtWidgets.QLabel(self.tab_1)
        self.label_RES_CAP_2.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                           "color: rgb(255,255,255);")
        self.label_RES_CAP_2.setObjectName("label_RES_CAP_2")
        self.gridLayout.addWidget(self.label_RES_CAP_2, 11, 4, 1, 1)

        self.checkBox_RES_CAP = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_RES_CAP.sizePolicy().hasHeightForWidth())
        self.checkBox_RES_CAP.setSizePolicy(sizePolicy)
        self.checkBox_RES_CAP.setText("")
        self.checkBox_RES_CAP.setChecked(False)
        self.checkBox_RES_CAP.setObjectName("checkBox_RES_CAP")
        self.gridLayout.addWidget(self.checkBox_RES_CAP, 11, 5, 1, 1)

        self.doubleSpinBox_RES_CAP = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_RES_CAP.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_RES_CAP.setObjectName("doubleSpinBox_RES_CAP")
        self.gridLayout.addWidget(self.doubleSpinBox_RES_CAP, 11, 6, 1, 1)

        #=========================VISCOELASTANCE==========================
        self.label_VE = QtWidgets.QLabel(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_VE.sizePolicy().hasHeightForWidth())
        self.label_VE.setSizePolicy(sizePolicy)
        self.label_VE.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                    "background-color: rgb(35, 35, 35);\n"
                                    "color: rgb(255, 210, 119);")
        self.label_VE.setObjectName("label_VE")
        self.gridLayout.addWidget(self.label_VE, 0, 8, 1, 3)

        # --------------------------VENOUS INERTANCE---------------------------------
        self.label_VE_VI = QtWidgets.QLabel(self.tab_1)
        self.label_VE_VI.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_VE_VI.setObjectName("label_VE_VI_2")
        self.gridLayout.addWidget(self.label_VE_VI, 1, 8, 1, 1)


        self.checkBox_VE_VI = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_VE_VI.sizePolicy().hasHeightForWidth())
        self.checkBox_VE_VI.setSizePolicy(sizePolicy)
        self.checkBox_VE_VI.setText("")
        self.checkBox_VE_VI.setChecked(False)
        self.checkBox_VE_VI.setObjectName("checkBox_VE_VI")
        self.gridLayout.addWidget(self.checkBox_VE_VI, 1, 9, 1, 1)

        self.doubleSpinBox_VE_VI = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_VE_VI.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                               "color: rgb(255, 210, 119);\n"
                                               "selection-color: rgb(237, 85, 59);\n"
                                               "selection-background-color: rgb(33, 57, 86);\n"
                                               "\n"
                                               "font: 11pt \"Calibri\";")
        self.doubleSpinBox_VE_VI.setObjectName("doubleSpinBox_VE_VI")
        self.gridLayout.addWidget(self.doubleSpinBox_VE_VI, 1, 10, 1, 1)


        # ---------------------------VENA CAVA----------------------------
        self.label_VE_VC_ = QtWidgets.QLabel(self.tab_1)
        self.label_VE_VC_.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255,255,255);")
        self.label_VE_VC_.setObjectName("label_VE_VC_")
        self.gridLayout.addWidget(self.label_VE_VC_, 2, 8, 1, 1)

        self.checkBox_VE_VC = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_VE_VC.sizePolicy().hasHeightForWidth())
        self.checkBox_VE_VC.setSizePolicy(sizePolicy)
        self.checkBox_VE_VC.setText("")
        self.checkBox_VE_VC.setChecked(False)
        self.checkBox_VE_VC.setObjectName("checkBox_VE_VC")
        self.gridLayout.addWidget(self.checkBox_VE_VC, 2, 9, 1, 1)

        self.doubleSpinBox_VE_VC = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_VE_VC.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                               "color: rgb(255, 210, 119);\n"
                                               "selection-color: rgb(237, 85, 59);\n"
                                               "selection-background-color: rgb(33, 57, 86);\n"
                                               "\n"
                                               "font: 11pt \"Calibri\";")
        self.doubleSpinBox_VE_VC.setObjectName("doubleSpinBox_VE_VC")
        self.gridLayout.addWidget(self.doubleSpinBox_VE_VC, 2, 10, 1, 1)

        # -------------------------- TRICUSPID VALVE---------------------------
        self.label_VE_TV_2 = QtWidgets.QLabel(self.tab_1)
        self.label_VE_TV_2.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_VE_TV_2.setObjectName("label_VE_TV_2")
        self.gridLayout.addWidget(self.label_VE_TV_2, 3, 8, 1, 1)

        self.checkBox_VE_TV = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_VE_TV.sizePolicy().hasHeightForWidth())
        self.checkBox_VE_TV.setSizePolicy(sizePolicy)
        self.checkBox_VE_TV.setText("")
        self.checkBox_VE_TV.setChecked(False)
        self.checkBox_VE_TV.setObjectName("checkBox_VE_TV")
        self.gridLayout.addWidget(self.checkBox_VE_TV, 3, 9, 1, 1)

        self.doubleSpinBox_VE_TV = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_VE_TV.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                               "color: rgb(255, 210, 119);\n"
                                               "selection-color: rgb(237, 85, 59);\n"
                                               "selection-background-color: rgb(33, 57, 86);\n"
                                               "\n"
                                               "font: 11pt \"Calibri\";")
        self.doubleSpinBox_VE_TV.setObjectName("doubleSpinBox_VE_TV")
        self.gridLayout.addWidget(self.doubleSpinBox_VE_TV, 3, 10, 1, 1)

        # ------------------------ PULMONARY VALVE ----------------------------
        self.label_VE_PUVA = QtWidgets.QLabel(self.tab_1)
        self.label_VE_PUVA.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                         "color: rgb(255,255,255);")
        self.label_VE_PUVA.setObjectName("label_VE_PUVA")
        self.gridLayout.addWidget(self.label_VE_PUVA, 4, 8, 1, 1)

        self.checkBox_VE_PUVA = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_VE_PUVA.sizePolicy().hasHeightForWidth())
        self.checkBox_VE_PUVA.setSizePolicy(sizePolicy)
        self.checkBox_VE_PUVA.setText("")
        self.checkBox_VE_PUVA.setChecked(False)
        self.checkBox_VE_PUVA.setObjectName("checkBox_VE_PUVA")
        self.gridLayout.addWidget(self.checkBox_VE_PUVA, 4, 9, 1, 1)

        # ------------------------ PULMONARY ARTERY ----------------------------
        self.label_VE_PUA = QtWidgets.QLabel(self.tab_1)
        self.label_VE_PUA.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255,255,255);")
        self.label_VE_PUA.setObjectName("label_VE_PUA")
        self.gridLayout.addWidget(self.label_VE_PUA, 5, 8, 1, 1)


        self.checkBox_VE_PUA = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_VE_PUA.sizePolicy().hasHeightForWidth())
        self.checkBox_VE_PUA.setSizePolicy(sizePolicy)
        self.checkBox_VE_PUA.setText("")
        self.checkBox_VE_PUA.setChecked(False)
        self.checkBox_VE_PUA.setObjectName("checkBox_VE_PUA")
        self.gridLayout.addWidget(self.checkBox_VE_PUA, 5, 9, 1, 1)

        self.doubleSpinBox_VE_PUA = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_VE_PUA.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                "color: rgb(255, 210, 119);\n"
                                                "selection-color: rgb(237, 85, 59);\n"
                                                "selection-background-color: rgb(33, 57, 86);\n"
                                                "\n"
                                                "font: 11pt \"Calibri\";")
        self.doubleSpinBox_VE_PUA.setObjectName("doubleSpinBox_VE_PUA")
        self.gridLayout.addWidget(self.doubleSpinBox_VE_PUA, 5, 10, 1, 1)
        self.doubleSpinBox_VE_PUVA = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_VE_PUVA.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                 "color: rgb(255, 210, 119);\n"
                                                 "selection-color: rgb(237, 85, 59);\n"
                                                 "selection-background-color: rgb(33, 57, 86);\n"
                                                 "\n"
                                                 "font: 11pt \"Calibri\";")
        self.doubleSpinBox_VE_PUVA.setObjectName("doubleSpinBox_VE_PUVA")
        self.gridLayout.addWidget(self.doubleSpinBox_VE_PUVA, 4, 10, 1, 1)


        # ------------------------ PULMONARY CAPILLARY ----------------------------
        self.checkBox_VE_PUC = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_VE_PUC.sizePolicy().hasHeightForWidth())
        self.checkBox_VE_PUC.setSizePolicy(sizePolicy)
        self.checkBox_VE_PUC.setText("")
        self.checkBox_VE_PUC.setChecked(False)
        self.checkBox_VE_PUC.setObjectName("checkBox_VE_PUC")
        self.gridLayout.addWidget(self.checkBox_VE_PUC, 6, 9, 1, 1)
        self.doubleSpinBox_VE_PUC = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_VE_PUC.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                "color: rgb(255, 210, 119);\n"
                                                "selection-color: rgb(237, 85, 59);\n"
                                                "selection-background-color: rgb(33, 57, 86);\n"
                                                "\n"
                                                "font: 11pt \"Calibri\";")
        self.doubleSpinBox_VE_PUC.setObjectName("doubleSpinBox_VE_PUC")
        self.gridLayout.addWidget(self.doubleSpinBox_VE_PUC, 6, 10, 1, 1)
        self.label_VE_CAP_2 = QtWidgets.QLabel(self.tab_1)
        self.label_VE_CAP_2.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                          "color: rgb(255,255,255);")
        self.label_VE_CAP_2.setObjectName("label_VE_CAP_2")
        self.gridLayout.addWidget(self.label_VE_CAP_2, 6, 8, 1, 1)


        # ------------------------ PULMONARY VEIN ----------------------------
        self.checkBox_VE_PUV = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_VE_PUV.sizePolicy().hasHeightForWidth())
        self.checkBox_VE_PUV.setSizePolicy(sizePolicy)
        self.checkBox_VE_PUV.setText("")
        self.checkBox_VE_PUV.setChecked(False)
        self.checkBox_VE_PUV.setObjectName("checkBox_VE_PUV")
        self.gridLayout.addWidget(self.checkBox_VE_PUV, 7, 9, 1, 1)

        self.label_VE_PUV = QtWidgets.QLabel(self.tab_1)
        self.label_VE_PUV.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255,255,255);")
        self.label_VE_PUV.setObjectName("label_VE_PUV")
        self.gridLayout.addWidget(self.label_VE_PUV, 7, 8, 1, 1)

        self.doubleSpinBox_VE_PUV = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_VE_PUV.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                "color: rgb(255, 210, 119);\n"
                                                "selection-color: rgb(237, 85, 59);\n"
                                                "selection-background-color: rgb(33, 57, 86);\n"
                                                "\n"
                                                "font: 11pt \"Calibri\";")
        self.doubleSpinBox_VE_PUV.setObjectName("doubleSpinBox_VE_PUV")
        self.gridLayout.addWidget(self.doubleSpinBox_VE_PUV, 7, 10, 1, 1)
        # ------------------------ MITRAL VALVE ----------------------------
        self.label_VE_MV = QtWidgets.QLabel(self.tab_1)
        self.label_VE_MV.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                       "color: rgb(255,255,255);")
        self.label_VE_MV.setObjectName("label_VE_MV")
        self.gridLayout.addWidget(self.label_VE_MV, 8, 8, 1, 1)

        self.checkBox_VE_MV = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_VE_MV.sizePolicy().hasHeightForWidth())
        self.checkBox_VE_MV.setSizePolicy(sizePolicy)
        self.checkBox_VE_MV.setText("")
        self.checkBox_VE_MV.setChecked(False)
        self.checkBox_VE_MV.setObjectName("checkBox_VE_MV")
        self.gridLayout.addWidget(self.checkBox_VE_MV, 8, 9, 1, 1)

        self.doubleSpinBox_VE_MV = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_VE_MV.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                               "color: rgb(255, 210, 119);\n"
                                               "selection-color: rgb(237, 85, 59);\n"
                                               "selection-background-color: rgb(33, 57, 86);\n"
                                               "\n"
                                               "font: 11pt \"Calibri\";")
        self.doubleSpinBox_VE_MV.setObjectName("doubleSpinBox_VE_MV")
        self.gridLayout.addWidget(self.doubleSpinBox_VE_MV, 8, 10, 1, 1)
        # ------------------------ AORTIC VALVE ----------------------------

        self.label_VE_AV = QtWidgets.QLabel(self.tab_1)
        self.label_VE_AV.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                       "color: rgb(255,255,255);")
        self.label_VE_AV.setObjectName("label_VE_AV")
        self.gridLayout.addWidget(self.label_VE_AV, 9, 8, 1, 1)

        self.checkBox_VE_AV = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_VE_AV.sizePolicy().hasHeightForWidth())
        self.checkBox_VE_AV.setSizePolicy(sizePolicy)
        self.checkBox_VE_AV.setText("")
        self.checkBox_VE_AV.setChecked(False)
        self.checkBox_VE_AV.setObjectName("checkBox_VE_AV")
        self.gridLayout.addWidget(self.checkBox_VE_AV, 9, 9, 1, 1)

        self.doubleSpinBox_VE_AV = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_VE_AV.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                               "color: rgb(255, 210, 119);\n"
                                               "selection-color: rgb(237, 85, 59);\n"
                                               "selection-background-color: rgb(33, 57, 86);\n"
                                               "\n"
                                               "font: 11pt \"Calibri\";")
        self.doubleSpinBox_VE_AV.setObjectName("doubleSpinBox_VE_AV")
        self.gridLayout.addWidget(self.doubleSpinBox_VE_AV, 9, 10, 1, 1)

        # -------------------------- AORTA  ----------------------------
        self.label_VE_AO = QtWidgets.QLabel(self.tab_1)
        self.label_VE_AO.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                       "color: rgb(255,255,255);")
        self.label_VE_AO.setObjectName("label_VE_AO")
        self.gridLayout.addWidget(self.label_VE_AO, 10, 8, 1, 1)

        self.checkBox_VE_AO = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_VE_AO.sizePolicy().hasHeightForWidth())
        self.checkBox_VE_AO.setSizePolicy(sizePolicy)
        self.checkBox_VE_AO.setText("")
        self.checkBox_VE_AO.setChecked(False)
        self.checkBox_VE_AO.setObjectName("checkBox_VE_AO")
        self.gridLayout.addWidget(self.checkBox_VE_AO, 10, 9, 1, 1)

        self.doubleSpinBox_VE_AO = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_VE_AO.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                               "color: rgb(255, 210, 119);\n"
                                               "selection-color: rgb(237, 85, 59);\n"
                                               "selection-background-color: rgb(33, 57, 86);\n"
                                               "\n"
                                               "font: 11pt \"Calibri\";")
        self.doubleSpinBox_VE_AO.setObjectName("doubleSpinBox_VE_AO")
        self.gridLayout.addWidget(self.doubleSpinBox_VE_AO, 10, 10, 1, 1)

        # ------------------------ CAPILLARY ----------------------------
        self.label_VE_CAP = QtWidgets.QLabel(self.tab_1)
        self.label_VE_CAP.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255,255,255);")
        self.label_VE_CAP.setObjectName("label_VE_CAP")
        self.gridLayout.addWidget(self.label_VE_CAP, 11, 8, 1, 1)

        self.doubleSpinBox_VE_CAP = QtWidgets.QDoubleSpinBox(self.tab_1)
        self.doubleSpinBox_VE_CAP.setStyleSheet("background-color: rgb(35, 35, 35);\n"
                                                "color: rgb(255, 210, 119);\n"
                                                "selection-color: rgb(237, 85, 59);\n"
                                                "selection-background-color: rgb(33, 57, 86);\n"
                                                "\n"
                                                "font: 11pt \"Calibri\";")
        self.doubleSpinBox_VE_CAP.setObjectName("doubleSpinBox_VE_CAP")
        self.gridLayout.addWidget(self.doubleSpinBox_VE_CAP, 11, 10, 1, 1)

        self.checkBox_VE_CAP = QtWidgets.QCheckBox(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_VE_CAP.sizePolicy().hasHeightForWidth())
        self.checkBox_VE_CAP.setSizePolicy(sizePolicy)
        self.checkBox_VE_CAP.setText("")
        self.checkBox_VE_CAP.setChecked(False)
        self.checkBox_VE_CAP.setObjectName("checkBox_VE_CAP")
        self.gridLayout.addWidget(self.checkBox_VE_CAP, 11, 9, 1, 1)

        # =====================SPACER ITEM=====================
        # spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        # self.gridLayout.addItem(spacerItem3, 5, 7, 1, 1)
        # ===ADD TAB WIDGET TO THE WINDOW======================
        self.tabWidget.addTab(self.tab_0, "")
        self.tabWidget.addTab(self.tab_1, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.heart_ok, 1, 1, 1,1)

        self.retranslateUi(self.widget_1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self.widget_1)

        # ==============CHECKBOX ENABLE SIGNAL

        # =========BERNOULI'S RESISTANCE
        self.checkBox_BR_MV.clicked.connect(self.enable)
        self.checkBox_BR_PV.clicked.connect(self.enable)
        self.checkBox_BR_TV.clicked.connect(self.enable)
        self.checkBox_BR_AV.clicked.connect(self.enable)
        # ==========COMPLIANCE
        self.checkBox_CMP_CAP.clicked.connect(self.enable)
        self.checkBox_CMP_ART.clicked.connect(self.enable)
        self.checkBox_CMP_AO.clicked.connect(self.enable)
        self.checkBox_CMP_VC.clicked.connect(self.enable)
        self.checkBox_CMP_VCO.clicked.connect(self.enable)
        # ===========ELASTANCE
        self.checkBox_ELA_PUV.clicked.connect(self.enable)
        self.checkBox_ELA_PUA.clicked.connect(self.enable)
        self.checkBox_ELA_PUC.clicked.connect(self.enable)
        self.checkBox_ELA_LVb.clicked.connect(self.enable)
        self.checkBox_ELA_RAa.clicked.connect(self.enable)
        self.checkBox_ELA_RAb.clicked.connect(self.enable)
        self.checkBox_ELA_RVa.clicked.connect(self.enable)
        self.checkBox_ELA_RVb.clicked.connect(self.enable)
        self.checkBox_ELA_LAa.clicked.connect(self.enable)
        self.checkBox_ELA_LAb.clicked.connect(self.enable)
        self.checkBox_ELA_LVa.clicked.connect(self.enable)
        # ===========INDUCTANCE
        self.checkBox_IND_VI.clicked.connect(self.enable)
        self.checkBox_IND_VC.clicked.connect(self.enable)
        self.checkBox_IND_TV.clicked.connect(self.enable)
        self.checkBox_IND_PUVA.clicked.connect(self.enable)
        self.checkBox_IND_PUC.clicked.connect(self.enable)
        self.checkBox_IND_PUA.clicked.connect(self.enable)
        self.checkBox_IND_PUV.clicked.connect(self.enable)
        self.checkBox_IND_AO.clicked.connect(self.enable)
        self.checkBox_IND_MV.clicked.connect(self.enable)
        self.checkBox_IND_AV.clicked.connect(self.enable)
        self.checkBox_IND_CAP.clicked.connect(self.enable)
        # ============RESISTANCE
        self.checkBox_RES_VI.clicked.connect(self.enable)
        self.checkBox_RES_VC.clicked.connect(self.enable)
        self.checkBox_RES_TV.clicked.connect(self.enable)
        self.checkBox_RES_PUVA.clicked.connect(self.enable)
        self.checkBox_RES_PUC.clicked.connect(self.enable)
        self.checkBox_RES_PUA.clicked.connect(self.enable)
        self.checkBox_RES_PUV.clicked.connect(self.enable)
        self.checkBox_RES_AO.clicked.connect(self.enable)
        self.checkBox_RES_MV.clicked.connect(self.enable)
        self.checkBox_RES_AV.clicked.connect(self.enable)
        self.checkBox_RES_CAP.clicked.connect(self.enable)
        # =========== VISCO ELASTANCE
        self.checkBox_VE_VI.clicked.connect(self.enable)
        self.checkBox_VE_VC.clicked.connect(self.enable)
        self.checkBox_VE_TV.clicked.connect(self.enable)
        self.checkBox_VE_PUVA.clicked.connect(self.enable)
        self.checkBox_VE_PUC.clicked.connect(self.enable)
        self.checkBox_VE_PUA.clicked.connect(self.enable)
        self.checkBox_VE_PUV.clicked.connect(self.enable)
        self.checkBox_VE_AO.clicked.connect(self.enable)
        self.checkBox_VE_MV.clicked.connect(self.enable)
        self.checkBox_VE_AV.clicked.connect(self.enable)
        self.checkBox_VE_CAP.clicked.connect(self.enable)

    def retranslateUi(self, widget_1):
        _translate = QtCore.QCoreApplication.translate
        widget_1.setWindowTitle(_translate("widget_1", "HEART PARAMETERS"))
        self.label_ELA_LVb.setText(_translate("widget_1", "Left Vent (base)"))
        self.label_CMP.setText(_translate("widget_1", "COMPLIANCE :"))
        self.label_ELA_RAa.setText(_translate("widget_1", "Right Atrium (amplitude)"))
        self.label_ELA_RAb.setText(_translate("widget_1", "Right Atrium (base)"))
        self.label_ELA_RVa.setText(_translate("widget_1", "Right Vent (amplitude)"))
        self.label_ELA_RVb.setText(_translate("widget_1", "Right Vent (base)"))
        self.label_ELAS.setText(_translate("widget_1", "ELASTANCE :"))
        self.label_BR.setText(_translate("widget_1", "BERNOULI\"S RESISTANCE :"))
        self.label_CMP_PUV.setText(_translate("widget_1", "Pul vein (0 VOL)"))
        self.label_BR_MV.setText(_translate("widget_1", "Mitral Valve"))
        self.label_BR_PV.setText(_translate("widget_1", "Pul Valve"))
        self.label_CMP_PUA.setText(_translate("widget_1", "Pul artery (0 VOL)"))
        self.label_BR_TV.setText(_translate("widget_1", "Tricuspid Valve"))
        self.label_ELA_PUC.setText(_translate("widget_1", "Pul capillary (0 VOL)"))
        self.label_CMP_CAP.setText(_translate("widget_1", "Capillary"))
        self.label_CMP_ART.setText(_translate("widget_1", "Artery"))
        self.label_CMP_AO.setText(_translate("widget_1", "Aorta"))
        self.label_CMP_VC.setText(_translate("widget_1", "Vena Cava"))
        self.label_BR_AV.setText(_translate("widget_1", "Aortic Valve"))
        self.label_ELA_LAa.setText(_translate("widget_1", "Left Atrium (amplitude)"))
        self.label_ELA_LAb.setText(_translate("widget_1", "Left Atrium (base)"))
        self.label_CMP_VCO.setText(_translate("widget_1", "Venous Compli."))
        self.label_ELA_LVa.setText(_translate("widget_1", "Left Vent (amplitude)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_0), _translate("widget_1", "Parameters-1"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_0), _translate("widget_1", "Parameters list"))
        self.label_VE_VI.setText(_translate("widget_1", "Venous inertance"))
        self.label_RES.setText(_translate("widget_1", "RESISTANCE :"))
        self.label_IND_VI.setText(_translate("widget_1", "Venous inertance"))
        self.label_IND_VC.setText(_translate("widget_1", "Vena Cava"))
        self.label_IND.setText(_translate("widget_1", "INDUCTANCE :"))
        self.label_VE.setText(_translate("widget_1", "VISCOELASTANCE :"))
        self.label_RES_VI.setText(_translate("widget_1", "Venous inertance"))
        self.label_RES_TV.setText(_translate("widget_1", "Tricuspid Valve"))
        self.label_IND_TV.setText(_translate("widget_1", "Tricuspid Valve"))
        self.label_VE_TV_2.setText(_translate("widget_1", "Tricuspid Valve"))
        self.label_VE_VC_.setText(_translate("widget_1", "Vena Cava"))
        self.label_RES_VC.setText(_translate("widget_1", "Vena Cava"))
        self.label_IND_PUVA.setText(_translate("widget_1", "Pul Valve"))
        self.label_VE_PUVA.setText(_translate("widget_1", "Pul Valve"))
        self.label_RES_PUVA.setText(_translate("widget_1", "Pul Valve"))
        self.label_RES_PUA.setText(_translate("widget_1", "Pul Artery"))
        self.label_IND_PUA.setText(_translate("widget_1", "Pul Artery"))
        self.label_RES_CAP.setText(_translate("widget_1", "Pul Capillary"))
        self.label_IND_PUC.setText(_translate("widget_1", "Pul Capillary"))
        self.label_VE_PUA.setText(_translate("widget_1", "Pul Artery"))
        self.label_VE_CAP_2.setText(_translate("widget_1", "Pul Capillary"))
        self.label_RES_PUV.setText(_translate("widget_1", "Pul Vein"))
        self.label_IND_PUV.setText(_translate("widget_1", "Pul Vein"))
        self.label_IND_AO.setText(_translate("widget_1", "Aorta"))
        self.label_IND_MV.setText(_translate("widget_1", "Mitral Valve"))
        self.label_IND_AV.setText(_translate("widget_1", "Aortic Valve"))
        self.label_VE_PUV.setText(_translate("widget_1", "Pul Vein"))
        self.label_VE_MV.setText(_translate("widget_1", "Mitral Valve"))
        self.label_RES_AV.setText(_translate("widget_1", "Aortic Valve"))
        self.label_VE_AV.setText(_translate("widget_1", "Aortic Valve"))
        self.label_RES_MV.setText(_translate("widget_1", "Mitral Valve"))
        self.label_VE_AO.setText(_translate("widget_1", "Aorta"))
        self.label_IND_CAP.setText(_translate("widget_1", "Capillary"))
        self.label_RES_AO.setText(_translate("widget_1", "Aorta"))
        self.label_RES_CAP_2.setText(_translate("widget_1", "Capillary"))
        self.label_VE_CAP.setText(_translate("widget_1", "Capillary"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("widget_1", "Parameters-2"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_1), _translate("widget_1", "Parameters List"))

    def enable(self):
        # Bernouli's Resistance
        if self.checkBox_BR_MV.isChecked():
            self.doubleSpinBox_BR_MV.setEnabled(True)
        else:
            self.doubleSpinBox_BR_MV.setEnabled(False)

        if self.checkBox_BR_PV.isChecked():
            self.doubleSpinBox_BR_PV.setEnabled(True)
        else:
            self.doubleSpinBox_BR_PV.setEnabled(False)

        if self.checkBox_BR_TV.isChecked():
            self.doubleSpinBox_BR_TV.setEnabled(True)
        else:
            self.doubleSpinBox_BR_TV.setEnabled(False)

        if self.checkBox_BR_AV.isChecked():
            self.doubleSpinBox_BR_AV.setEnabled(True)
        else:
            self.doubleSpinBox_BR_AV.setEnabled(False)


        # COMPLIANCE
        if self.checkBox_CMP_CAP.isChecked():
            self.doubleSpinBox_CMP_CAP.setEnabled(True)
        else:
            self.doubleSpinBox_CMP_CAP.setEnabled(False)

        if self.checkBox_CMP_ART.isChecked():
            self.doubleSpinBox_CMP_ART.setEnabled(True)
        else:
            self.doubleSpinBox_CMP_ART.setEnabled(False)

        if self.checkBox_CMP_AO.isChecked():
            self.doubleSpinBox_CMP_AO.setEnabled(True)
        else:
            self.doubleSpinBox_CMP_AO.setEnabled(False)

        if self.checkBox_CMP_VC.isChecked():
            self.doubleSpinBox_CMP_VC.setEnabled(True)
        else:
            self.doubleSpinBox_CMP_VC.setEnabled(False)

        if self.checkBox_CMP_VCO.isChecked():
            self.doubleSpinBox_CMP_VCO.setEnabled(True)
        else:
            self.doubleSpinBox_CMP_VCO.setEnabled(False)


        # ELASTANCE
        if self.checkBox_ELA_LVb.isChecked():
            self.doubleSpinBox_ELA_LVb.setEnabled(True)
        else:
            self.doubleSpinBox_ELA_LVb.setEnabled(False)

        if self.checkBox_ELA_RAa.isChecked():
            self.doubleSpinBox_ELA_RAa.setEnabled(True)
        else:
            self.doubleSpinBox_ELA_RAa.setEnabled(False)

        if self.checkBox_ELA_RAb.isChecked():
            self.doubleSpinBox_ELA_RAb.setEnabled(True)
        else:
            self.doubleSpinBox_ELA_RAb.setEnabled(False)

        if self.checkBox_ELA_RVa.isChecked():
            self.doubleSpinBox_ELA_RVa.setEnabled(True)
        else:
            self.doubleSpinBox_ELA_RVa.setEnabled(False)

        if self.checkBox_ELA_RVb.isChecked():
            self.doubleSpinBox_ELA_RVb.setEnabled(True)
        else:
            self.doubleSpinBox_ELA_RVb.setEnabled(False)

        if self.checkBox_ELA_PUV.isChecked():
            self.doubleSpinBox_ELA_PUV.setEnabled(True)
        else:
            self.doubleSpinBox_ELA_PUV.setEnabled(False)

        if self.checkBox_ELA_PUA.isChecked():
            self.doubleSpinBox_ELA_PUA.setEnabled(True)
        else:
            self.doubleSpinBox_ELA_PUA.setEnabled(False)

        if self.checkBox_ELA_PUC.isChecked():
            self.doubleSpinBox_ELA_PUC.setEnabled(True)
        else:
            self.doubleSpinBox_ELA_PUC.setEnabled(False)

        if self.checkBox_ELA_LAa.isChecked():
            self.doubleSpinBox_ELA_LAa.setEnabled(True)
        else:
            self.doubleSpinBox_ELA_LAa.setEnabled(False)

        if self.checkBox_ELA_LAb.isChecked():
            self.doubleSpinBox_ELA_LAb.setEnabled(True)
        else:
            self.doubleSpinBox_ELA_LAb.setEnabled(False)

        if self.checkBox_ELA_LVa.isChecked():
            self.doubleSpinBox_ELA_LVa.setEnabled(True)
        else:
            self.doubleSpinBox_ELA_LVa.setEnabled(False)


        # INDUCTANCE
        if self.checkBox_IND_VI.isChecked():
            self.doubleSpinBox_IND_VI.setEnabled(True)
        else:
            self.doubleSpinBox_IND_VI.setEnabled(False)

        if self.checkBox_IND_VC.isChecked():
            self.doubleSpinBox_IND_VC.setEnabled(True)
        else:
            self.doubleSpinBox_IND_VC.setEnabled(False)

        if self.checkBox_IND_TV.isChecked():
            self.doubleSpinBox_IND_TV.setEnabled(True)
        else:
            self.doubleSpinBox_IND_TV.setEnabled(False)

        if self.checkBox_IND_PUVA.isChecked():
            self.doubleSpinBox_IND_PUVA.setEnabled(True)
        else:
            self.doubleSpinBox_IND_PUVA.setEnabled(False)

        if self.checkBox_IND_PUA.isChecked():
            self.doubleSpinBox_IND_PUA.setEnabled(True)
        else:
            self.doubleSpinBox_IND_PUA.setEnabled(False)

        if self.checkBox_IND_PUC.isChecked():
            self.doubleSpinBox_IND_PUC.setEnabled(True)
        else:
            self.doubleSpinBox_IND_PUC.setEnabled(False)

        if self.checkBox_IND_PUV.isChecked():
            self.doubleSpinBox_IND_PUV.setEnabled(True)
        else:
            self.doubleSpinBox_IND_PUV.setEnabled(False)

        if self.checkBox_IND_MV.isChecked():
            self.doubleSpinBox_IND_MV.setEnabled(True)
        else:
            self.doubleSpinBox_IND_MV.setEnabled(False)

        if self.checkBox_IND_AV.isChecked():
            self.doubleSpinBox_IND_AV.setEnabled(True)
        else:
            self.doubleSpinBox_IND_AV.setEnabled(False)

        if self.checkBox_IND_AO.isChecked():
            self.doubleSpinBox_IND_AO.setEnabled(True)
        else:
            self.doubleSpinBox_IND_AO.setEnabled(False)

        if self.checkBox_IND_CAP.isChecked():
            self.doubleSpinBox_IND_CAP.setEnabled(True)
        else:
            self.doubleSpinBox_IND_CAP.setEnabled(False)

        # RESISTANCE
        if self.checkBox_RES_VI.isChecked():
            self.doubleSpinBox_RES_VI.setEnabled(True)
        else:
            self.doubleSpinBox_RES_VI.setEnabled(False)

        if self.checkBox_RES_VC.isChecked():
            self.doubleSpinBox_RES_VC.setEnabled(True)
        else:
            self.doubleSpinBox_RES_VC.setEnabled(False)

        if self.checkBox_RES_TV.isChecked():
            self.doubleSpinBox_RES_TV.setEnabled(True)
        else:
            self.doubleSpinBox_RES_TV.setEnabled(False)

        if self.checkBox_RES_PUVA.isChecked():
            self.doubleSpinBox_RES_PUVA.setEnabled(True)
        else:
            self.doubleSpinBox_RES_PUVA.setEnabled(False)

        if self.checkBox_RES_PUA.isChecked():
            self.doubleSpinBox_RES_PUA.setEnabled(True)
        else:
            self.doubleSpinBox_RES_PUA.setEnabled(False)

        if self.checkBox_RES_PUC.isChecked():
            self.doubleSpinBox_RES_PUC.setEnabled(True)
        else:
            self.doubleSpinBox_RES_PUC.setEnabled(False)

        if self.checkBox_RES_PUV.isChecked():
            self.doubleSpinBox_RES_PUV.setEnabled(True)
        else:
            self.doubleSpinBox_RES_PUV.setEnabled(False)

        if self.checkBox_RES_MV.isChecked():
            self.doubleSpinBox_RES_MV.setEnabled(True)
        else:
            self.doubleSpinBox_RES_MV.setEnabled(False)

        if self.checkBox_RES_AV.isChecked():
            self.doubleSpinBox_RES_AV.setEnabled(True)
        else:
            self.doubleSpinBox_RES_AV.setEnabled(False)

        if self.checkBox_RES_AO.isChecked():
            self.doubleSpinBox_RES_AO.setEnabled(True)
        else:
            self.doubleSpinBox_RES_AO.setEnabled(False)

        if self.checkBox_RES_CAP.isChecked():
            self.doubleSpinBox_RES_CAP.setEnabled(True)
        else:
            self.doubleSpinBox_RES_CAP.setEnabled(False)

        # VISCO ELASTANCE
        if self.checkBox_VE_VI.isChecked():
            self.doubleSpinBox_VE_VI.setEnabled(True)
        else:
            self.doubleSpinBox_VE_VI.setEnabled(False)

        if self.checkBox_VE_VC.isChecked():
            self.doubleSpinBox_VE_VC.setEnabled(True)
        else:
            self.doubleSpinBox_VE_VC.setEnabled(False)

        if self.checkBox_VE_TV.isChecked():
            self.doubleSpinBox_VE_TV.setEnabled(True)
        else:
            self.doubleSpinBox_VE_TV.setEnabled(False)

        if self.checkBox_VE_PUVA.isChecked():
            self.doubleSpinBox_VE_PUVA.setEnabled(True)
        else:
            self.doubleSpinBox_VE_PUVA.setEnabled(False)

        if self.checkBox_VE_PUA.isChecked():
            self.doubleSpinBox_VE_PUA.setEnabled(True)
        else:
            self.doubleSpinBox_VE_PUA.setEnabled(False)

        if self.checkBox_VE_PUC.isChecked():
            self.doubleSpinBox_VE_PUC.setEnabled(True)
        else:
            self.doubleSpinBox_VE_PUC.setEnabled(False)

        if self.checkBox_VE_PUV.isChecked():
            self.doubleSpinBox_VE_PUV.setEnabled(True)
        else:
            self.doubleSpinBox_VE_PUV.setEnabled(False)

        if self.checkBox_VE_MV.isChecked():
            self.doubleSpinBox_VE_MV.setEnabled(True)
        else:
            self.doubleSpinBox_VE_MV.setEnabled(False)

        if self.checkBox_VE_AV.isChecked():
            self.doubleSpinBox_VE_AV.setEnabled(True)
        else:
            self.doubleSpinBox_VE_AV.setEnabled(False)

        if self.checkBox_VE_AO.isChecked():
            self.doubleSpinBox_VE_AO.setEnabled(True)
        else:
            self.doubleSpinBox_VE_AO.setEnabled(False)

        if self.checkBox_VE_CAP.isChecked():
            self.doubleSpinBox_VE_CAP.setEnabled(True)
        else:
            self.doubleSpinBox_VE_CAP.setEnabled(False)

    def clicked(self):
        path = os.path.join("DBS", "bloodsim.sqlite")
        connection = create_connection(path)
        css = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
              0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # BERNOUL'S RESISTANCE
        BR_MV = self.doubleSpinBox_BR_MV.value()
        BR_PV = self.doubleSpinBox_BR_PV.value()
        BR_AV = self.doubleSpinBox_BR_AV.value()
        BR_TV = self.doubleSpinBox_BR_TV.value()

        # COMPLIANCE
        CMP_CAP = self.doubleSpinBox_CMP_CAP.value()
        CMP_ART = self.doubleSpinBox_CMP_ART.value()
        CMP_AO = self.doubleSpinBox_CMP_AO.value()
        CMP_VC = self.doubleSpinBox_CMP_VC.value()
        CMP_VCO = self.doubleSpinBox_CMP_VCO.value()

        # ELASTANCE
        ELA_PUV = self.doubleSpinBox_ELA_PUV.value()
        ELA_PUA = self.doubleSpinBox_ELA_PUA.value()
        ELA_PUC = self.doubleSpinBox_ELA_PUC.value()
        ELA_LVb = self.doubleSpinBox_ELA_LVb.value()
        ELA_RAa = self.doubleSpinBox_ELA_RAa.value()
        ELA_RAb = self.doubleSpinBox_ELA_RAb.value()
        ELA_RVa = self.doubleSpinBox_ELA_RVa.value()
        ELA_RVb = self.doubleSpinBox_ELA_RVb.value()
        ELA_LAa = self.doubleSpinBox_ELA_LAa.value()
        ELA_LAb = self.doubleSpinBox_ELA_LAb.value()
        ELA_LVa = self.doubleSpinBox_ELA_LVa.value()

        # INDUCTANCE
        IND_VI = self.doubleSpinBox_IND_VI.value()
        IND_VC = self.doubleSpinBox_IND_VC.value()
        IND_TV = self.doubleSpinBox_IND_TV.value()
        IND_PUVA = self.doubleSpinBox_IND_PUVA.value()
        IND_PUA = self.doubleSpinBox_IND_PUA.value()
        IND_PUC = self.doubleSpinBox_IND_PUC.value()
        IND_PUV = self.doubleSpinBox_IND_PUV.value()
        IND_MV = self.doubleSpinBox_IND_MV.value()
        IND_AV = self.doubleSpinBox_IND_AV.value()
        IND_AO = self.doubleSpinBox_IND_AO.value()
        IND_CAP = self.doubleSpinBox_IND_CAP.value()

        # RESISTANCE
        RES_VI = self.doubleSpinBox_RES_VI.value()
        RES_VC = self.doubleSpinBox_RES_VC.value()
        RES_TV = self.doubleSpinBox_RES_TV.value()
        RES_PUVA = self.doubleSpinBox_RES_PUVA.value()
        RES_PUA = self.doubleSpinBox_RES_PUA.value()
        RES_PUC = self.doubleSpinBox_RES_PUC.value()
        RES_PUV = self.doubleSpinBox_RES_PUV.value()
        RES_MV = self.doubleSpinBox_RES_MV.value()
        RES_AV = self.doubleSpinBox_RES_AV.value()
        RES_AO = self.doubleSpinBox_RES_AO.value()
        RES_CAP = self.doubleSpinBox_RES_CAP.value()

        # VISCO ELASTANCE
        VE_VI = self.doubleSpinBox_VE_VI.value()
        VE_VC = self.doubleSpinBox_VE_VC.value()
        VE_TV = self.doubleSpinBox_VE_TV.value()
        VE_PUVA = self.doubleSpinBox_VE_PUVA.value()
        VE_PUA = self.doubleSpinBox_VE_PUA.value()
        VE_PUC = self.doubleSpinBox_VE_PUC.value()
        VE_PUV = self.doubleSpinBox_VE_PUV.value()
        VE_MV = self.doubleSpinBox_VE_MV.value()
        VE_AV = self.doubleSpinBox_VE_AV.value()
        VE_AO = self.doubleSpinBox_VE_AO.value()
        VE_CAP = self.doubleSpinBox_VE_CAP.value()

        # VARIABLES VALUE
        heart_br_para = [BR_MV,BR_PV, BR_AV, BR_TV]
        heart_cmp_para = [CMP_CAP, CMP_ART, CMP_AO, CMP_VC, CMP_VCO]
        heart_ela_para = [ELA_PUV, ELA_PUA, ELA_PUC, ELA_LVb, ELA_RAa,
                          ELA_RAb, ELA_RVa, ELA_RVb, ELA_LAa, ELA_LAb, ELA_LVa]
        heart_ind_para = [IND_VI,IND_VC,IND_TV, IND_PUVA,IND_PUA, IND_PUC,
                               IND_PUV, IND_MV, IND_AV, IND_AO, IND_CAP]
        heart_res_para = [RES_VI, RES_VC, RES_TV, RES_PUVA, RES_PUA, RES_PUC,
                               RES_PUV, RES_MV, RES_AV, RES_AO, RES_CAP]
        heart_ve_para = [VE_VI, VE_VC, VE_TV, VE_PUVA, VE_PUA, VE_PUC,
                              VE_PUV, VE_MV, VE_AV, VE_AO, VE_CAP]

        query = "Update CARDI set val = ? where id = ?"
        query_list = [(BR_MV, 0), (BR_PV, 1), (BR_AV, 2), (BR_TV, 3), \
                      (CMP_CAP, 4), (CMP_ART, 5), (CMP_AO, 6), (CMP_VC, 7), (CMP_VCO, 8), \
                      (ELA_PUV, 9), (ELA_PUA, 10), (ELA_PUC, 11), (ELA_LVb, 12), (ELA_RAa, 13), \
                      (ELA_RAb, 14), (ELA_RVa, 15), (ELA_RVb, 16), (ELA_LAa, 17), (ELA_LAb, 18), (ELA_LVa, 19), \
                      (IND_VI, 20), (IND_VC, 21), (IND_TV, 22), (IND_PUVA, 23), (IND_PUA, 24), \
                      (IND_PUC, 25), (IND_PUV, 26), (IND_MV, 27), (IND_AV, 28), (IND_AO, 29), (IND_CAP, 30), \
                      (RES_VI, 31), (RES_VC, 32), (RES_TV, 33), (RES_PUVA, 34), (RES_PUA, 35), (RES_PUC, 36), \
                      (RES_PUV, 37), (RES_MV, 38), (RES_AV, 39), (RES_AO, 40), (RES_CAP, 41), \
                      (VE_VI, 42), (VE_VC, 43), (VE_TV, 44), (VE_PUVA, 45), (VE_PUA, 46), (VE_PUC, 47), \
                      (VE_PUV, 48), (VE_MV, 49), (VE_AV, 50), (VE_AO, 51), (VE_CAP, 52)]
        execute_many_query(connection, query, query_list)

        # CHECK STATE
        # BERNOUL'S RESISTANCE
        css[0] = BR_MV = self.doubleSpinBox_BR_MV.isEnabled()
        css[1] = BR_PV = self.doubleSpinBox_BR_PV.isEnabled()
        css[2] = BR_AV = self.doubleSpinBox_BR_AV.isEnabled()
        css[3] = BR_TV = self.doubleSpinBox_BR_TV.isEnabled()

        # COMPLIANCE
        css[4] = CMP_CAP = self.doubleSpinBox_CMP_CAP.isEnabled()
        css[5] = CMP_ART = self.doubleSpinBox_CMP_ART.isEnabled()
        css[6] = CMP_AO = self.doubleSpinBox_CMP_AO.isEnabled()
        css[7] = CMP_VC = self.doubleSpinBox_CMP_VC.isEnabled()
        css[8] = CMP_VCO = self.doubleSpinBox_CMP_VCO.isEnabled()

        # ELASTANCE
        css[9] = ELA_PUV = self.doubleSpinBox_ELA_PUV.isEnabled()
        css[10] = ELA_PUA = self.doubleSpinBox_ELA_PUA.isEnabled()
        css[11] = ELA_PUC = self.doubleSpinBox_ELA_PUC.isEnabled()
        css[12] = ELA_LVb = self.doubleSpinBox_ELA_LVb.isEnabled()
        css[13] = ELA_RAa = self.doubleSpinBox_ELA_RAa.isEnabled()
        css[14] = ELA_RAb = self.doubleSpinBox_ELA_RAb.isEnabled()
        css[15] = ELA_RVa = self.doubleSpinBox_ELA_RVa.isEnabled()
        css[16] = ELA_RVb = self.doubleSpinBox_ELA_RVb.isEnabled()
        css[17] = ELA_LAa = self.doubleSpinBox_ELA_LAa.isEnabled()
        css[18] = ELA_LAb = self.doubleSpinBox_ELA_LAb.isEnabled()
        css[19] = ELA_LVa = self.doubleSpinBox_ELA_LVa.isEnabled()

        # INDUCTANCE
        css[20] = IND_VI = self.doubleSpinBox_IND_VI.isEnabled()
        css[21] = IND_VC = self.doubleSpinBox_IND_VC.isEnabled()
        css[22] = IND_TV = self.doubleSpinBox_IND_TV.isEnabled()
        css[23] = IND_PUVA = self.doubleSpinBox_IND_PUVA.isEnabled()
        css[24] = IND_PUA = self.doubleSpinBox_IND_PUA.isEnabled()
        css[25] = IND_PUC = self.doubleSpinBox_IND_PUC.isEnabled()
        css[26] = IND_PUV = self.doubleSpinBox_IND_PUV.isEnabled()
        css[27] = IND_MV = self.doubleSpinBox_IND_MV.isEnabled()
        css[28] = IND_AV = self.doubleSpinBox_IND_AV.isEnabled()
        css[29] = IND_AO = self.doubleSpinBox_IND_AO.isEnabled()
        css[30] = IND_CAP = self.doubleSpinBox_IND_CAP.isEnabled()

        # RESISTANCE
        css[31] = RES_VI = self.doubleSpinBox_RES_VI.isEnabled()
        css[32] = RES_VC = self.doubleSpinBox_RES_VC.isEnabled()
        css[33] = RES_TV = self.doubleSpinBox_RES_TV.isEnabled()
        css[34] = RES_PUVA = self.doubleSpinBox_RES_PUVA.isEnabled()
        css[35] = RES_PUA = self.doubleSpinBox_RES_PUA.isEnabled()
        css[36] = RES_PUC = self.doubleSpinBox_RES_PUC.isEnabled()
        css[37] = RES_PUV = self.doubleSpinBox_RES_PUV.isEnabled()
        css[38] = RES_MV = self.doubleSpinBox_RES_MV.isEnabled()
        css[39] = RES_AV = self.doubleSpinBox_RES_AV.isEnabled()
        css[40] = RES_AO = self.doubleSpinBox_RES_AO.isEnabled()
        css[41] = RES_CAP = self.doubleSpinBox_RES_CAP.isEnabled()

        # VISCO ELASTANCE
        css[42] = VE_VI = self.doubleSpinBox_VE_VI.isEnabled()
        css[43] = VE_VC = self.doubleSpinBox_VE_VC.isEnabled()
        css[44] = VE_TV = self.doubleSpinBox_VE_TV.isEnabled()
        css[45] = VE_PUVA = self.doubleSpinBox_VE_PUVA.isEnabled()
        css[46] = VE_PUA = self.doubleSpinBox_VE_PUA.isEnabled()
        css[47] = VE_PUC = self.doubleSpinBox_VE_PUC.isEnabled()
        css[48] = VE_PUV = self.doubleSpinBox_VE_PUV.isEnabled()
        css[49] = VE_MV = self.doubleSpinBox_VE_MV.isEnabled()
        css[50] = VE_AV = self.doubleSpinBox_VE_AV.isEnabled()
        css[51] = VE_AO = self.doubleSpinBox_VE_AO.isEnabled()
        css[52] = VE_CAP = self.doubleSpinBox_VE_CAP.isEnabled()

        for i in range(53):
            if css[i] == True:
                css[i] = 1
            else:
                css[i] = 0


        query = "Update CARDI set state = ? where id = ?"
        query_list = [(css[0], 0), (css[1], 1), (css[2], 2), (css[3], 3), (css[4], 4), (css[5], 5), (css[6], 6),\
                      (css[7], 7), (css[8], 8), (css[9], 9), (css[10], 10), (css[11], 11), (css[12], 12), (css[13], 13),\
                      (css[14], 14), (css[15], 15), (css[16], 16), (css[17], 17), (css[18], 18), (css[19], 19),\
                      (css[20], 20),(css[21], 21),(css[22], 22),(css[23], 23),(css[24], 24),(css[25], 25),(css[26], 26),\
                      (css[27], 27),(css[28], 28),(css[29], 29),(css[30], 30),(css[31], 31),(css[32], 32),\
                      (css[33], 33),(css[34], 34),(css[35], 35),(css[36], 36),(css[37], 37),(css[38], 38),(css[39], 39),\
                      (css[40], 40),(css[41], 41),(css[42], 42),(css[43], 43),(css[44], 44),(css[45], 45),(css[46], 46),\
                      (css[47], 47),(css[48], 48),(css[49], 49),(css[50], 50),(css[51], 51),(css[52], 52)]
        execute_many_query(connection, query, query_list)
        self.widget_1.close()

    def state(self):
        path = os.path.join("DBS", "bloodsim.sqlite")
        connection = create_connection(path)

        C = []
        query = "SELECT val FROM CARDI"
        bdat = execute_read_query(connection, query)
        C = sum(bdat, ())

        # =============UPDATE BOX VALUE
        self.doubleSpinBox_BR_MV.setValue(C[0])
        self.doubleSpinBox_BR_PV.setValue(C[1])
        self.doubleSpinBox_BR_AV.setValue(C[2])
        self.doubleSpinBox_BR_TV.setValue(C[3])

        # =========COMPLIANCE
        self.doubleSpinBox_CMP_CAP.setValue(C[4])
        self.doubleSpinBox_CMP_ART.setValue(C[5])
        self.doubleSpinBox_CMP_AO.setValue(C[6])
        self.doubleSpinBox_CMP_VC.setValue(C[7])
        self.doubleSpinBox_CMP_VCO.setValue(C[8])

        # ==========ELASTANCE
        self.doubleSpinBox_ELA_PUV.setValue(C[9])
        self.doubleSpinBox_ELA_PUA.setValue(C[10])
        self.doubleSpinBox_ELA_PUC.setValue(C[11])
        self.doubleSpinBox_ELA_LVb.setValue(C[12])
        self.doubleSpinBox_ELA_RAa.setValue(C[13])
        self.doubleSpinBox_ELA_RAb.setValue(C[14])
        self.doubleSpinBox_ELA_RVa.setValue(C[15])
        self.doubleSpinBox_ELA_RVb.setValue(C[16])
        self.doubleSpinBox_ELA_LAa.setValue(C[17])
        self.doubleSpinBox_ELA_LAb.setValue(C[18])
        self.doubleSpinBox_ELA_LVa.setValue(C[19])

        # ==========INDUCTANCE
        self.doubleSpinBox_IND_VI.setValue(C[20])
        self.doubleSpinBox_IND_VC.setValue(C[21])
        self.doubleSpinBox_IND_TV.setValue(C[22])
        self.doubleSpinBox_IND_PUVA.setValue(C[23])
        self.doubleSpinBox_IND_PUA.setValue(C[24])
        self.doubleSpinBox_IND_PUC.setValue(C[25])
        self.doubleSpinBox_IND_PUV.setValue(C[26])
        self.doubleSpinBox_IND_MV.setValue(C[27])
        self.doubleSpinBox_IND_AV.setValue(C[28])
        self.doubleSpinBox_IND_AO.setValue(C[29])
        self.doubleSpinBox_IND_CAP.setValue(C[30])

        # ===========RESISTANCE
        self.doubleSpinBox_RES_VI.setValue(C[31])
        self.doubleSpinBox_RES_VC.setValue(C[32])
        self.doubleSpinBox_RES_TV.setValue(C[33])
        self.doubleSpinBox_RES_PUVA.setValue(C[34])
        self.doubleSpinBox_RES_PUA.setValue(C[35])
        self.doubleSpinBox_RES_PUC.setValue(C[36])
        self.doubleSpinBox_RES_PUV.setValue(C[37])
        self.doubleSpinBox_RES_MV.setValue(C[38])
        self.doubleSpinBox_RES_AV.setValue(C[39])
        self.doubleSpinBox_RES_AO.setValue(C[40])
        self.doubleSpinBox_RES_CAP.setValue(C[41])

        # ==========VISCO ELASTANCE
        self.doubleSpinBox_VE_VI.setValue(C[42])
        self.doubleSpinBox_VE_VC.setValue(C[43])
        self.doubleSpinBox_VE_TV.setValue(C[44])
        self.doubleSpinBox_VE_PUVA.setValue(C[45])
        self.doubleSpinBox_VE_PUA.setValue(C[46])
        self.doubleSpinBox_VE_PUC.setValue(C[47])
        self.doubleSpinBox_VE_PUV.setValue(C[48])
        self.doubleSpinBox_VE_MV.setValue(C[49])
        self.doubleSpinBox_VE_AV.setValue(C[50])
        self.doubleSpinBox_VE_AO.setValue(C[51])
        self.doubleSpinBox_VE_CAP.setValue(C[52])

        # ==================DISABLE DOUBLESPINBOX
        C1 = []
        query = "SELECT state FROM CARDI"
        state = execute_read_query(connection, query)
        C1 = sum(state, ())
        # ========BERNOULI'S RESISTANCE
        self.doubleSpinBox_BR_MV.setEnabled(C1[0])
        self.doubleSpinBox_BR_PV.setEnabled(C1[1])
        self.doubleSpinBox_BR_AV.setEnabled(C1[2])
        self.doubleSpinBox_BR_TV.setEnabled(C1[3])

        # =========COMPLIANCE
        self.doubleSpinBox_CMP_CAP.setEnabled(C1[4])
        self.doubleSpinBox_CMP_ART.setEnabled(C1[5])
        self.doubleSpinBox_CMP_AO.setEnabled(C1[6])
        self.doubleSpinBox_CMP_VC.setEnabled(C1[7])
        self.doubleSpinBox_CMP_VCO.setEnabled(C1[8])

        # ==========ELASTANCE
        self.doubleSpinBox_ELA_PUV.setEnabled(C1[9])
        self.doubleSpinBox_ELA_PUA.setEnabled(C1[10])
        self.doubleSpinBox_ELA_PUC.setEnabled(C1[11])
        self.doubleSpinBox_ELA_LVb.setEnabled(C1[12])
        self.doubleSpinBox_ELA_RAa.setEnabled(C1[13])
        self.doubleSpinBox_ELA_RAb.setEnabled(C1[14])
        self.doubleSpinBox_ELA_RVa.setEnabled(C1[15])
        self.doubleSpinBox_ELA_RVb.setEnabled(C1[16])
        self.doubleSpinBox_ELA_LAa.setEnabled(C1[17])
        self.doubleSpinBox_ELA_LAb.setEnabled(C1[18])
        self.doubleSpinBox_ELA_LVa.setEnabled(C1[19])

        # ==========INDUCTANCE
        self.doubleSpinBox_IND_VI.setEnabled(C1[20])
        self.doubleSpinBox_IND_VC.setEnabled(C1[21])
        self.doubleSpinBox_IND_TV.setEnabled(C1[22])
        self.doubleSpinBox_IND_PUVA.setEnabled(C1[23])
        self.doubleSpinBox_IND_PUA.setEnabled(C1[24])
        self.doubleSpinBox_IND_PUC.setEnabled(C1[25])
        self.doubleSpinBox_IND_PUV.setEnabled(C1[26])
        self.doubleSpinBox_IND_MV.setEnabled(C1[27])
        self.doubleSpinBox_IND_AV.setEnabled(C1[28])
        self.doubleSpinBox_IND_AO.setEnabled(C1[29])
        self.doubleSpinBox_IND_CAP.setEnabled(C1[30])

        # ===========RESISTANCE
        self.doubleSpinBox_RES_VI.setEnabled(C1[31])
        self.doubleSpinBox_RES_VC.setEnabled(C1[32])
        self.doubleSpinBox_RES_TV.setEnabled(C1[33])
        self.doubleSpinBox_RES_PUVA.setEnabled(C1[34])
        self.doubleSpinBox_RES_PUA.setEnabled(C1[35])
        self.doubleSpinBox_RES_PUC.setEnabled(C1[36])
        self.doubleSpinBox_RES_PUV.setEnabled(C1[37])
        self.doubleSpinBox_RES_MV.setEnabled(C1[38])
        self.doubleSpinBox_RES_AV.setEnabled(C1[39])
        self.doubleSpinBox_RES_AO.setEnabled(C1[40])
        self.doubleSpinBox_RES_CAP.setEnabled(C1[41])

        # ==========VISCO ELASTANCE
        self.doubleSpinBox_VE_VI.setEnabled(C1[42])
        self.doubleSpinBox_VE_VC.setEnabled(C1[43])
        self.doubleSpinBox_VE_TV.setEnabled(C1[44])
        self.doubleSpinBox_VE_PUVA.setEnabled(C1[45])
        self.doubleSpinBox_VE_PUA.setEnabled(C1[46])
        self.doubleSpinBox_VE_PUC.setEnabled(C1[47])
        self.doubleSpinBox_VE_PUV.setEnabled(C1[48])
        self.doubleSpinBox_VE_MV.setEnabled(C1[49])
        self.doubleSpinBox_VE_AV.setEnabled(C1[50])
        self.doubleSpinBox_VE_AO.setEnabled(C1[51])
        self.doubleSpinBox_VE_CAP.setEnabled(C1[52])

        # ==================CHECKBOX STATE
        # ========BERNOULI'S RESISTANCE
        self.checkBox_BR_MV.setChecked(C1[0])
        self.checkBox_BR_PV.setChecked(C1[1])
        self.checkBox_BR_AV.setChecked(C1[2])
        self.checkBox_BR_TV.setChecked(C1[3])

        # =========COMPLIANCE
        self.checkBox_CMP_CAP.setChecked(C1[4])
        self.checkBox_CMP_ART.setChecked(C1[5])
        self.checkBox_CMP_AO.setChecked(C1[6])
        self.checkBox_CMP_VC.setChecked(C1[7])
        self.checkBox_CMP_VCO.setChecked(C1[8])

        # ==========ELASTANCE
        self.checkBox_ELA_PUV.setChecked(C1[9])
        self.checkBox_ELA_PUA.setChecked(C1[10])
        self.checkBox_ELA_PUC.setChecked(C1[11])
        self.checkBox_ELA_LVb.setChecked(C1[12])
        self.checkBox_ELA_RAa.setChecked(C1[13])
        self.checkBox_ELA_RAb.setChecked(C1[14])
        self.checkBox_ELA_RVa.setChecked(C1[15])
        self.checkBox_ELA_RVb.setChecked(C1[16])
        self.checkBox_ELA_LAa.setChecked(C1[17])
        self.checkBox_ELA_LAb.setChecked(C1[18])
        self.checkBox_ELA_LVa.setChecked(C1[19])

        # ==========INDUCTANCE
        self.checkBox_IND_VI.setChecked(C1[20])
        self.checkBox_IND_VC.setChecked(C1[21])
        self.checkBox_IND_TV.setChecked(C1[22])
        self.checkBox_IND_PUVA.setChecked(C1[23])
        self.checkBox_IND_PUA.setChecked(C1[24])
        self.checkBox_IND_PUC.setChecked(C1[25])
        self.checkBox_IND_PUV.setChecked(C1[26])
        self.checkBox_IND_MV.setChecked(C1[27])
        self.checkBox_IND_AV.setChecked(C1[28])
        self.checkBox_IND_AO.setChecked(C1[29])
        self.checkBox_IND_CAP.setChecked(C1[30])

        # ===========RESISTANCE
        self.checkBox_RES_VI.setChecked(C1[31])
        self.checkBox_RES_VC.setChecked(C1[32])
        self.checkBox_RES_TV.setChecked(C1[33])
        self.checkBox_RES_PUVA.setChecked(C1[34])
        self.checkBox_RES_PUA.setChecked(C1[35])
        self.checkBox_RES_PUC.setChecked(C1[36])
        self.checkBox_RES_PUV.setChecked(C1[37])
        self.checkBox_RES_MV.setChecked(C1[38])
        self.checkBox_RES_AV.setChecked(C1[39])
        self.checkBox_RES_AO.setChecked(C1[40])
        self.checkBox_RES_CAP.setChecked(C1[41])

        # ==========VISCO ELASTANCE
        self.checkBox_VE_VI.setChecked(C1[42])
        self.checkBox_VE_VC.setChecked(C1[43])
        self.checkBox_VE_TV.setChecked(C1[44])
        self.checkBox_VE_PUVA.setChecked(C1[45])
        self.checkBox_VE_PUA.setChecked(C1[46])
        self.checkBox_VE_PUC.setChecked(C1[47])
        self.checkBox_VE_PUV.setChecked(C1[48])
        self.checkBox_VE_MV.setChecked(C1[49])
        self.checkBox_VE_AV.setChecked(C1[50])
        self.checkBox_VE_AO.setChecked(C1[51])
        self.checkBox_VE_CAP.setChecked(C1[52])


if __name__ == "__main__":
    # import threading
    import sys
    # def printit():
    #    threading.Timer(5.0, printit).start()
    # printit()
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QMainWindow()
    # form = QtWidgets.QWidget()
    ui = Ui_MainWindow(form)
    form.show()
    sys.exit(app.exec_())


