#imports

from view import *
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ShapesCalculator()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())