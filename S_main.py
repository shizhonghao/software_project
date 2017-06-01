import sys

from views.servent import mainwindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from client import c

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = mainwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())