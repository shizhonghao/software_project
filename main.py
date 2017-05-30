import sys
import lxy_mainwindow
from PyQt5.QtWidgets import QApplication, QDialog,QWidget,QMainWindow
from M_database import db_close

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = lxy_mainwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    db_close()