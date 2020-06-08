from Mainwindow import Ui_MainWindow, Steno_para, Heart_para
from HomeWindow import Ui_HomeWindow
from PyQt5 import QtGui, QtCore, QtWidgets
import os
import sys

class Controller():

    def Show_HomeWindow(self):
        self.HomeWindow = QtWidgets.QMainWindow()
        self.ui = Ui_HomeWindow(self.HomeWindow)
        self.ui.pushButton_1.clicked.connect(self.Show_SecondWindow)
        self.ui.pushButton_2.clicked.connect(self.manual)
        self.ui.pushButton_3.clicked.connect(self.exit)
        self.HomeWindow.show()

    def exit(self):
        self.HomeWindow.close()

    def manual(self):
        path = os.path.join('images', 'User_Manual.pdf')
        os.system(path)

    def Show_SecondWindow(self):
        try:
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow(self.MainWindow)
            self.ui.actionQuit.triggered.connect(self.exit1)
            self.ui.pushButton_HP.clicked.connect(self.heart_para)
            self.ui.pushButton_STENO.clicked.connect(self.Steno_para)
            self.MainWindow.show()
            self.HomeWindow.close()
        except Exception as e:
            alert = QtWidgets.QMessageBox()
            alert.setText(str(e))
            alert.exec_()

    def exit1(self):
        self.MainWindow.close()

    def heart_para(self):
        self.widget_1 = QtWidgets.QWidget()
        self.wui = Heart_para(self.widget_1)
        self.widget_1.show()

    def Steno_para(self):
        self.Form = QtWidgets.QWidget()
        self.sui = Steno_para(self.Form)
        self.Form.show()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Controller = Controller()
    Controller.Show_HomeWindow()
    sys.exit(app.exec_())
