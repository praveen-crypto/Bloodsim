from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import MAIN
import numpy as np
import STENOSIS
import os
import CARDIAC


class Ui_MainWindow(object):
    try:          
        def init(self, MainWindow):

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
            self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.groupBox_1)
            self.label_1 = QtWidgets.QLabel(self.groupBox_1)
            self.label_2 = QtWidgets.QLabel(self.groupBox_1)
            self.label_3 = QtWidgets.QLabel(self.groupBox_1)
            self.label_4 = QtWidgets.QLabel(self.groupBox_1)
            self.label_5 = QtWidgets.QLabel(self.groupBox_1)
            self.label_6 = QtWidgets.QLabel(self.groupBox_1)
            self.label_7 = QtWidgets.QLabel(self.groupBox_1)
            self.comboBox_1 = QtWidgets.QComboBox(self.groupBox_1)
            self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_1)
            self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_1)
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
            self.cv =0
            self.labelStyle = {'color': '#ED553B', 'font-size': '9pt'}
            self.dockWidget_3 = QtWidgets.QDockWidget(MainWindow)
            self.dockWidgetContents_3 = QtWidgets.QWidget()
            self.gridLayout_11 = QtWidgets.QGridLayout(self.dockWidgetContents_3)
            self.groupBox_5 = QtWidgets.QGroupBox(self.dockWidgetContents_3)
            self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_5)
            self.label_heart = QtWidgets.QLabel(self.groupBox_5)
            self.groupBox_6 = QtWidgets.QGroupBox(self.dockWidgetContents_3)
            self.text_heartinfo = QtWidgets.QTextBrowser(self.groupBox_6)
            self.labelEdit_1.setPixmap(QtGui.QPixmap(os.path.join( "images/artery tree images","art_tree_img.png" )))
            self.textBrowser_2.setText("The primary function of the heart is to serve as a muscular pump propelling blood"
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

        def setupUi(self, MainWindow):
            self.init(MainWindow)
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
            ####GRAPH_WIDGET - 1 ======================================================================================================
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
            #####GRAPH_WIDGET - 2 ============================================================================
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
            #####FIRST GRAPH =================================================================================
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
            ####SECOND GRAPH=====================================================================================================
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
            ####THIRD GRAPH=====================================================================================================
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
            #####LEFT SIDE DOCK WIDGET====================================================================================
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
            ###groupBox_1========================================================================================
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
            # label_6
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
            self.label_6.setSizePolicy(sizePolicy)
            self.label_6.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                       "color: rgb(255,255,255);")
            self.label_6.setObjectName("label_6")
            self.gridLayout_3.addWidget(self.label_6, 4, 0, 1, 1)
            # comboBox_1
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
            self.gridLayout_3.addWidget(self.comboBox_1, 4, 2, 1, 1)
            # label_7
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
            self.label_7.setSizePolicy(sizePolicy)
            self.label_7.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";\n"
                                       "color: rgb(255,255,255);")
            self.label_7.setObjectName("label_7")
            self.gridLayout_3.addWidget(self.label_7, 5, 0, 1, 1)
            # doubleSpinBox_3
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
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
            self.gridLayout_3.addWidget(self.doubleSpinBox_3, 6, 2, 1, 1)
            # PushButton-1
            self.pushButton_1 = QtWidgets.QPushButton(self.groupBox_1)
            self.pushButton_1.setStyleSheet("background-color: rgb(35, 35, 35);")
            self.pushButton_1.setObjectName("pushButton_1")
            self.gridLayout_3.addWidget(self.pushButton_1, 7, 0, 1, 3)
            self.pushButton_1.clicked.connect(self.store)
            # comboBox_2
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
            self.gridLayout_3.addWidget(self.comboBox_2, 5, 2, 1, 1)
            # comboBox_3
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
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
            ############## groupBox_4
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
            #pushButton_5
            self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_4)
            self.pushButton_5.setStyleSheet("background-color: rgb(35, 35, 35);")
            self.pushButton_5.setObjectName("pushButton_2")
            self.gridLayout_5.addWidget(self.pushButton_5, 0, 0, 1, 1)
            self.pushButton_5.clicked.connect(self.button_graph_1)
            #pushButton_6
            self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_4)
            self.pushButton_6.setStyleSheet("background-color: rgb(35, 35, 35);")
            self.pushButton_6.setObjectName("pushButton_3")
            self.gridLayout_5.addWidget(self.pushButton_6, 0, 1, 1, 1)
            self.pushButton_6.clicked.connect(self.button_graph_2)
            #pushButton_7
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
            #pushButton_2
            self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_6)
            self.pushButton_2.setStyleSheet("background-color: rgb(35, 35, 35);")
            self.pushButton_2.setObjectName("pushButton_2")
            self.gridLayout_13.addWidget(self.pushButton_2, 0, 0, 1, 1)
            self.pushButton_2.clicked.connect(self.button_chambers)
            #pushButton_3
            self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_6)
            self.pushButton_3.setStyleSheet("background-color: rgb(35, 35, 35);")
            self.pushButton_3.setObjectName("pushButton_3")
            self.gridLayout_13.addWidget(self.pushButton_3, 0, 1, 1, 1)
            self.pushButton_3.clicked.connect(self.button_valves)
            #pushButton_4
            self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_6)
            self.pushButton_4.setStyleSheet("background-color: rgb(35, 35, 35);")
            self.pushButton_4.setObjectName("pushButton_4")
            self.pushButton_4.clicked.connect(self.button_iandolet)
            self.gridLayout_13.addWidget(self.pushButton_4, 0, 2, 1, 1)
            self.gridLayout_11.addWidget(self.groupBox_6, 1, 0, 1, 1)
            self.dockWidget_3.setWidget(self.dockWidgetContents_3)
            MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_3)
            self.dockWidget_3.hide()
    ##########################END OF DOCKWIDGET_3
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
            #self.actionQuit.triggered.connect()
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
            # setBuddy
            self.label_10.setBuddy(self.checkBox_3)
            self.label_11.setBuddy(self.checkBox_4)
            self.label_12.setBuddy(self.checkBox_5)
            self.label_6.setBuddy(self.comboBox_1)
            self.label_7.setBuddy(self.comboBox_2)
            self.label_4.setBuddy(self.checkBox_2)
            self.label_3.setBuddy(self.checkBox_1)
            # TabOrder
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
            self.pushButton_1.setText(self._translate("MainWindow", "OK"))
            self.pushButton_2.setText(self._translate("MainWindow", "CHAMBERS"))
            self.pushButton_3.setText(self._translate("MainWindow", "VALVES"))
            self.pushButton_4.setText(self._translate("MainWindow", "INLET/OUTLET"))
            self.pushButton_5.setText(self._translate("MainWindow", "GRAPH-1"))
            self.pushButton_6.setText(self._translate("MainWindow", "GRAPH-2"))
            self.pushButton_7.setText(self._translate("MainWindow", "ANALYSE"))
            self.radioButton_2.setText(self._translate("MainWindow", "Flow"))
            self.radioButton_4.setText(self._translate("MainWindow", "Flow"))
            self.radioButton_3.setText(self._translate("MainWindow", "Pressure"))
            self.radioButton_1.setText(self._translate("MainWindow", "Pressure"))
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
            self.label_6.setText(self._translate("MainWindow", "Number of Arteries"))
            self.label_7.setText(self._translate("MainWindow", "Select Artery"))
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
            self.comboBox_1.setItemText(0, self._translate("MainWindow", "1"))
            self.comboBox_1.setItemText(1, self._translate("MainWindow", "2"))
            self.comboBox_1.setItemText(2, self._translate("MainWindow", "3"))
            self.comboBox_1.setItemText(3, self._translate("MainWindow", "4"))
            self.comboBox_1.setItemText(4, self._translate("MainWindow", "5"))
            self.comboBox_1.setItemText(5, self._translate("MainWindow", "6"))
            self.comboBox_1.setItemText(6, self._translate("MainWindow", "7"))
            self.comboBox_1.setItemText(7, self._translate("MainWindow", "8"))
            self.comboBox_1.setItemText(8, self._translate("MainWindow", "9"))
            self.comboBox_1.setItemText(9, self._translate("MainWindow", "10"))
            self.comboBox_1.setItemText(10, self._translate("MainWindow", "11"))
            self.comboBox_1.setItemText(11, self._translate("MainWindow", "12"))
            self.comboBox_1.setItemText(12, self._translate("MainWindow", "13"))
            self.comboBox_1.setItemText(13, self._translate("MainWindow", "14"))
            self.comboBox_1.setItemText(14, self._translate("MainWindow", "15"))
            self.comboBox_1.setItemText(15, self._translate("MainWindow", "16"))
            self.comboBox_1.setItemText(16, self._translate("MainWindow", "17"))
            self.comboBox_1.setItemText(17, self._translate("MainWindow", "18"))
            self.comboBox_1.setItemText(18, self._translate("MainWindow", "19"))
            self.comboBox_1.setItemText(19, self._translate("MainWindow", "20"))
            self.comboBox_3.setItemText(0, self._translate("MainWindow", "Ascending aorta"))
            self.comboBox_3.setItemText(1, self._translate("MainWindow", "Aortic arch"))
            self.comboBox_3.setItemText(2, self._translate("MainWindow", "Subclavian artery left"))
            self.comboBox_3.setItemText(3, self._translate("MainWindow", "Subclavian artery right"))
            self.comboBox_3.setItemText(4, self._translate("MainWindow", "Common carotid(L)"))
            self.comboBox_3.setItemText(5, self._translate("MainWindow", "Common carotid(R)"))
            self.comboBox_3.setItemText(6, self._translate("MainWindow", "Thoracic aorta"))
            self.comboBox_3.setItemText(7, self._translate("MainWindow", "Cerebral artery right"))
            self.comboBox_3.setItemText(8, self._translate("MainWindow", "Cerebral artery left"))
            self.comboBox_3.setItemText(9, self._translate("MainWindow", "Abdominal aorta"))
            self.comboBox_3.setItemText(10, self._translate("MainWindow", "Brachial artery right"))
            self.comboBox_3.setItemText(11, self._translate("MainWindow", "Brachial artery left"))
            self.comboBox_3.setItemText(12, self._translate("MainWindow", "Hepatic artery"))
            self.comboBox_3.setItemText(13, self._translate("MainWindow", "Renal artery"))
            self.comboBox_3.setItemText(14, self._translate("MainWindow", "Femoral artery left"))
            self.comboBox_3.setItemText(15, self._translate("MainWindow", "Femoral artery right"))
            self.comboBox_3.setItemText(16, self._translate("MainWindow", "Ulnar artery left"))
            self.comboBox_3.setItemText(17, self._translate("MainWindow", "Ulnar artery right"))
            self.comboBox_3.setItemText(18, self._translate("MainWindow", "Radial artery left"))
            self.comboBox_3.setItemText(19, self._translate("MainWindow", "Radial artery right"))
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

        def val(self):
            data = self.comboBox_1.currentIndex()
            data = int(data)
            self.comboBox_2.clear()
            for i in range(data + 1):
                j = i + 1
                j = str(j)
                self.comboBox_2.addItem(j)
            self.c = 0

        def store(self):
            self.c = self.c + 1
            if self.c - 1 == 0: ck = [];self.cbnew = {}
            cb1 = int(self.comboBox_1.currentText())
            cb2 = self.comboBox_2.currentIndex()
            pos = self.comboBox_3.currentIndex()
            cn = self.comboBox_2.count()
            cbdic = {cb2: pos}
            if self.c <= cn:
                self.cbnew.update(cbdic)
                position = [0, 1, 7, 13, 3, 11, 10, 51, 46, 74, 56, 70, 62, 63, 108, 109, 102, 107, 96, 92]
                if self.cbnew.items() not in self.cbnew.items():
                    u_Pos = position[pos]
                    val = self.doubleSpinBox_3.value()
                    for dat in self.stn_dat:
                        if dat == u_Pos:
                            self.stn_dat[u_Pos] = val
                            del cbdic
                            self.statusbar.showMessage('UPDATED', msecs=5000)
            else:
                self.alert("can't update")

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
                    "The heart is comprised of two atria and two ventricles. Blood enters the heart through the two atria and exits through the two ventricles. Deoxygenated blood enters the right atrium through the inferior and superior vena cava. The right side of the heart then pumps this deoxygenated blood into the pulmonary arteries around the lungs. There, fresh oxygen enters the blood stream, and the blood moves to the left side of the heart. From the lungs, blood is brought to the left atrium through the pulmonary vein, and then to the left ventricle through the mitral valve, from where it is pumped to the rest of the body.")
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
                Index = self.comboBox_3.currentIndex()
                if Index == 1:
                    Pos = 0
                    self.plot_p = 1
                    self.plot_f = 0
                elif Index == 2:  # Index value in combo_box
                    Pos = 1  # Initalize position
                    self.plot_p = 3
                    self.plot_f = 2
                elif Index == 3:
                    Pos = 7
                    self.plot_p = 7 #5
                    self.plot_f = 6 #4
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
                datas = self.stn_dat
                m = self.doubleSpinBox_4.value()
                r = self.doubleSpinBox_5.value()
                g = self.doubleSpinBox_6.value()
                STENOSIS.steno(m, r, g, **datas)
                self.clock, self.pulse = MAIN.calc(H, P)
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
            plt.plot(self.clock, self.pulse[self.plot_f,:], pen=pg.mkPen(2, width=2), name=Txt)
            self.statusbar.showMessage('PLOTTED', msecs=5000)

        def alert(self, msg):
            alert = QtWidgets.QMessageBox()
            alert.setWindowTitle("Warning!!")
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
            about = QtWidgets.QMessageBox()
            about.setWindowIcon(QtGui.QIcon('images/logo.png'))
            about.setWindowTitle("About")
            about.setText(
                'BloodSim is an open-source software to simulate blood pressure, flow and volume waveforms in the cardiovascular system. Effect of stenosis on the pressure and flow of blood in the arterial tree is modelled.\n'
                '\nThe model is based on the following authors works,\n'
                '\nDr.Suganthi L             (Associate professor, Department of Biomedical Engineering, SSN college of Engineering)\n'
                '\nDr,Manivannan M     (Professor, Department of Applied Mechanics, Indian Institute of Technology, Madras)\n'
                '\nDr. Hemalatha K\n'
                'The model is based on thefollowing works,\n'
                '1.  HYBRID CARDIOPULMONARY INTERACTION MODEL TOWARDS NOVEL DIGNOSTIC TECHNIQUES\n'
                '2.  TAKAYASUS ARTERITIS – CLINICAL ANALYSIS, MODELING AND SIMULATION TOWARDS NOVEL DIAGNOSTIC TECHNIQUE\n'
                '\n The software is developed in Python using Qt designer\n'
                '\nDevelopers\n\n'
                'Praveen Kumar S\n' 
                'Arvindh Swaminathan MB\n')
            about.exec_()

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
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(os.path.join('images/artery tree images', 'aortic_arch.png')))
                    self.textBrowser_2.setText('The aortic arch s the part of the aorta between the ascending and descending '
                                               'aorta. The arch travels backward, so that it ultimately runs to the left of the'
                                               'trachea. The aortic arch has three branches,'
                                               '1.     brachiocephalic trunk'
                                               '2.     left common carotid artery'
                                               '3.     left subclavian artery'
                                                'The aortic arch is the connection between the ascending and descending aorta,'
                                                'and its central part is formed by the left 4th aortic arch during early '
                                                'development.')
                elif index == 3:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(os.path.join('images/artery tree images', 'subclavian_left.png')))
                    self.textBrowser_2.setText('The subclavian arteries are paired major arteries of the upper thorax, below'
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
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(os.path.join('images/artery tree images', 'subclavian_right.png')))
                    self.textBrowser_2.setText('The subclavian arteries are paired major arteries of the upper thorax, below'
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
                elif index == 6:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'common_carotid_right.png')))
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
                    self.textBrowser_2.setText('The renal arteries normally arise off the left interior side of the abdominal'
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
                elif index == 16:
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
                elif index == 17:
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
                elif index == 18:
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
                elif index == 19:
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
                elif index == 20:
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
                    self.textBrowser_2.setText('The aortic arch s the part of the aorta between the ascending and descending '
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
                    self.textBrowser_2.setText('The subclavian arteries are paired major arteries of the upper thorax, below'
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
                    self.textBrowser_2.setText('The subclavian arteries are paired major arteries of the upper thorax, below'
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
                elif index == 6:
                    self.labelEdit_1.setPixmap(QtGui.QPixmap(
                        os.path.join('images/artery tree images',
                                     'common_carotid_right.png')))
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
                    self.textBrowser_2.setText('The renal arteries normally arise off the left interior side of the abdominal'
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
                elif index == 16:
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
                elif index == 17:
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
                elif index == 18:
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
                elif index == 19:
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
                elif index == 20:
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
                
                self.textBrowser_2.setText('This section displays the features extracted from the blood pressure and flow waveforms simulated.'
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
                                           % (self.comboBox_G1.currentText(), self.pressure_max, self.pressure_min, self.flowmax, self.flowmin, self.comboBox_G2.currentText(), self.pressure_max_2, self.pressure_min_2, self.flowmax_2, self.flowmin_2))

        def art_text_display(self, a):
            if a == 1:
                Id = self.comboBox_G1.currentIndex()
            elif a == 2:
                Id = self.comboBox_G2.currentIndex()
            if Id == 0:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images', 'art_tree_img.png')))
                self.textBrowser_2.setText('The primary function of the heart is to serve as a muscular pump propelling blood into and through vessels to and from all parts of the body. The arteries, which receive this blood at high pressure and velocity and conduct it throughout the body, have thick walls that are composed of elastic fibrous tissue and muscle cells. The arterial tree—the branching system of arteries—terminates in short, narrow, muscular vessels called arterioles, from which blood enters simple endothelial tubes (i.e., tubes formed of endothelial, or lining, cells) known as capillaries. These thin, microscopic capillaries are permeable to vital cellular nutrients and waste products that they receive and distribute. From the capillaries, the blood, now depleted of oxygen and burdened with waste products, moving more slowly and under low pressure, enters small vessels called venules that converge to form veins, ultimately guiding the blood on its way back to the heart.')

            elif Id == 1:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'ascending_aorta.png')))
                self.textBrowser_2.setText('The ascending aorta  is a portion of the commencing at the upper part of the base of the left ventricle, on a level with the lower border of the third costal cartilage behind the left half of the sternum. The upper limit of standard reference range of the ascending aorta may be up to 4.3 cm among large, elderly individuals. The ascending aorta is contained within the pericardium, and is enclosed in a tube of the serous pericardium, common to it and the pulmonary artery. The only branches of the ascending aorta are the two coronary arteries which supply the heart; they arise near the commencement of the aorta from the aortic sinuses which are opposite the aortic valve.')

            elif Id == 2:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'aortic_arch.png')))
                self.textBrowser_2.setText('The aortic arch s the part of the aorta between the ascending and descending aorta. The arch travels backward, so that it ultimately runs to the left of the trachea. \n'
                                           '\nThe aortic arch has three branches,\n\n1.    brachiocephalic trunk\n2.  left common carotid artery\n3. left subclavian artery\n\nThe aortic arch is the connection between the ascending and descending aorta, and its central part is formed by the left 4th aortic arch during early development.')

            elif Id == 3:
                self.labelEdit_1.setPixmap(QtGui.QPixmap(
                    os.path.join('images/artery tree images',
                                 'subclavian_left.png')))
                self.textBrowser_2.setText('The subclavian arteries are paired major arteries of the upper thorax, below'
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
                self.textBrowser_2.setText('The subclavian arteries are paired major arteries of the upper thorax, below'
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
                    os.path.join('images/artery tree images','common_carotid_right.png')))
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
                self.textBrowser_2.setText('The renal arteries normally arise off the left interior side of the abdominal'
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
            if self.cv == 1 :
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
            else: self.alert("Run Heart Model!!")

        def button_iandolet(self):
            self.bc = 3
            self.radioButton_6.setDisabled(False)
            if self.cv ==1:
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
                self.label_heart.setPixmap(QtGui.QPixmap( os.path.join('images', 'left_ventricle.png')))
                self.text_heartinfo.setText(
                    "The left Ventricle is located on the left side of the heart, below the left atrium. It is separated from the atrium by the mitral valve. Of all the chambers, the left ventricle has the thickest wall. The blood coming from the left atrium is pumped by this chamber to the rest of the body through the aorta. The valve between the left ventricle and the aorta is the aortic valve. The left ventricle is separated from the right by the intra ventricular septum. The contraction of the left ventricle corresponds to the QRS complex in the electrocardiogram.")
                if self.radioButton_5.isChecked():
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 22], pen=pg.mkPen('#3CAEA3', width=2))
                elif self.radioButton_6.isChecked():
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 21], pen=pg.mkPen('#3CAEA3', width=2))

            elif self.comboBox_G3.currentIndex() == 3:
                self.label_heart.setPixmap(QtGui.QPixmap( os.path.join('images', 'right_atrium.png')))
                self.text_heartinfo.setText(
                    "The right atrium is located superior to the right ventricle and anteromedial to the left atrium. The right atrium receives the vena cava and coronary sinus, has an appendage, and directs blood into the right ventricle through the tricuspid valve. The right atrium is the first chamber of the heart to receive deoxygenated and carbon dioxide-rich systemic blood from the body through the superior and inferior vena cava. The right atrium also houses the first part of the conduction system, the sinoatrial node (SAN), which is located in the upper section near the superior vena cava. The SAN is made up of pacemaker cells which polarize to generate an action potential.")
                if self.radioButton_5.isChecked():
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 5], pen=pg.mkPen('#3CAEA3', width=2))
                elif self.radioButton_6.isChecked():
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 4], pen=pg.mkPen('#3CAEA3', width=2))

            elif self.comboBox_G3.currentIndex() == 4:
                self.label_heart.setPixmap(QtGui.QPixmap(   os.path.join('images', 'right_ventricle.png')))
                self.text_heartinfo.setText(
                    "The right ventricle lies anterior to the other heart chambers. Posteriorly and to the left, it is related to the left ventricle from which it is separated by the interventricular septum. The right ventricle is a unique, asymmetric, crescent-shape structure that is designed to accommodate the entire venous return while maintaining a low atrial pressure. The right ventricle is separated from the right atrium by the tricuspid valve. And the right atrium pumps blood to the lungs through the pulmonary artery gated by the pulmonary valve.")
                if self.radioButton_5.isChecked():
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total,  7], pen=pg.mkPen('#3CAEA3', width=2))
                elif self.radioButton_6.isChecked():
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 6], pen=pg.mkPen('#3CAEA3', width=2))

        def valve_plot(self):
            
            self.graphWidget_2.plotItem.clear()
            total = len(self.ctime)
            if self.comboBox_G3.currentIndex() == 1:
                self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 20], pen=pg.mkPen('#3CAEA3', width=2))
                self.graphWidget_2.setLabel('left', 'Volume', **self.labelStyle)
                self.graphWidget_2.setLabel('bottom', 'Time (s)', **self.labelStyle)
                self.label_heart.setPixmap(QtGui.QPixmap(   os.path.join('images', 'mitral_valve.png')))
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
                self.label_heart.setPixmap(QtGui.QPixmap(  os.path.join('images', 'aortic_valve.png')))
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
                else: self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 25], pen=pg.mkPen('#3CAEA3', width=2))
                self.graphWidget_2.setLabel('left', 'Volume', **self.labelStyle)
                self.graphWidget_2.setLabel('bottom', 'Time (s)', **self.labelStyle)
                self.label_heart.setPixmap(QtGui.QPixmap(  os.path.join('images', 'aorta.png')))
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
                else: self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 8], pen=pg.mkPen('#3CAEA3', width=2))
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
                else: self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 2], pen=pg.mkPen('#3CAEA3', width=2))
                self.graphWidget_2.setLabel('left', 'Volume', **self.labelStyle)
                self.graphWidget_2.setLabel('bottom', 'Time (s)', **self.labelStyle)
                self.label_heart.setPixmap(QtGui.QPixmap(
                    os.path.join('images', 'vena_cava.png')))
                self.text_heartinfo.setText(
                    "The venae cavae, singular 'vena cava' are two large veins that return deoxygenated blood from the body into the heart. In humans there are the superior vena cava and the inferior vena cava, and both empty into the right atrium. The inferior vena cava (or caudal vena cava in some animals) travels up alongside the abdominal aorta with blood from the lower part of the body. It is the largest vein in the human body. The superior vena cava (or cranial vena cava in animals) is above the heart, and forms from a convergence of the left and right brachiocephalic veins, which contain blood from the head and the arms. ")
            elif self.comboBox_G3.currentIndex() == 4:
                if self.radioButton_5.isChecked():
                    self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 13], pen=pg.mkPen('#3CAEA3', width=2))
                else: self.graphWidget_2.plot(self.ctime, self.cardiac[:total, 12], pen=pg.mkPen('#3CAEA3', width=2))
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
            self.textBrowser_2.setText("The primary function of the heart is to serve as a muscular pump propelling blood"
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

class Ui_HomeWindow(object):

    def setupUi(self, MainWin):
        MainWin.setObjectName("MainWindow")
        MainWin.resize(800, 400)
        MainWin.setMinimumSize(QtCore.QSize(800, 400))
        MainWin.setMaximumSize(QtCore.QSize(1000, 500))
        MainWin.setStyleSheet("background-color: rgb(37, 118, 184);\n")
        MainWin.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWin.setDocumentMode(False)
        MainWin.setTabShape(QtWidgets.QTabWidget.Triangular)
        MainWin.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.centralwidget = QtWidgets.QWidget(MainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 260, 191, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(23, 63, 95);\n"
                                        "color: rgb(246, 213, 92);\n")
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setIcon(QtGui.QIcon(os.path.join('images', 'Homebutton2.png')    ))
        self.pushButton_2.setIconSize(QtCore.QSize(190, 41))
        self.pushButton_2.setFlat(True)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 320, 191, 41))
        self.pushButton_3.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_3.setStyleSheet("background-color: rgb(23, 63, 95);\n"
                                        "color: rgb(246, 213, 92);\n")
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setIcon(QtGui.QIcon(os.path.join('images', 'Homebutton3.png')  ))
        self.pushButton_3.setIconSize(QtCore.QSize(190, 41))
        self.pushButton_3.setFlat(True)

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(570, 200, 191, 41))
        self.pushButton_1.setStyleSheet("border-color: rgb(0, 0, 0);\n"
                                        "color: rgb(246, 213, 92);\n"
                                        "background-color: rgb(23, 63, 95);\n")
        self.pushButton_1.setDefault(False)
        self.pushButton_1.setFlat(False)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.setIcon(QtGui.QIcon(os.path.join('images', 'Homebutton1.png')   ))
        self.pushButton_1.setIconSize(QtCore.QSize(190,41))
        self.pushButton_1.setFlat(True)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 0, 491, 296))
        self.label.setObjectName("label")
        self.label.setPixmap(QtGui.QPixmap(os.path.join('images', 'icon.jpeg')))

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(72, 290, 491, 81))
        self.label_2.setObjectName("label_2")
        self.label_2.setPixmap(QtGui.QPixmap( os.path.join('images', 'title.jpeg')))

        MainWin.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWin)
        QtCore.QMetaObject.connectSlotsByName(MainWin)

    def retranslateUi(self, OthrMainWindow):
        _translate = QtCore.QCoreApplication.translate
        OthrMainWindow.setWindowTitle(_translate("MainWindow", "BloodSim"))

class Controller:

    def Show_HomeWindow(self):
        self.HomeWindow = QtWidgets.QMainWindow()
        self.ui = Ui_HomeWindow()
        self.ui.setupUi(self.HomeWindow)
        self.ui.pushButton_1.clicked.connect(self.Show_SecondWindow)
        self.ui.pushButton_2.clicked.connect(self.manual)
        self.ui.pushButton_3.clicked.connect(self.exit)
        self.HomeWindow.show()

    def Show_SecondWindow(self):
        try :
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.MainWindow)
            #self.ui.pushButton.clicked.connect(self.Print)
            self.ui.actionQuit.triggered.connect(self.exit1)
            self.MainWindow.show()
            self.HomeWindow.close()
        except:
            alert = QtWidgets.QMessageBox()
            alert.setText('Error occured')
            alert.exec_()

    def exit(self):
        self.HomeWindow.close()

    def manual(self):
        path = os.path.join('images','User_Manual.pdf')
        os.system(path)
    
    def exit1(self):
        self.MainWindow.close()    

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Controller = Controller()
    Controller.Show_HomeWindow()
    sys.exit(app.exec_())
