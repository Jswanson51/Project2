from gui import *
import sys

def main():
        app = QtWidgets.QApplication(sys.argv)
        QMainWindow = QtWidgets.QMainWindow()
        ui = Ui_QMainWindow()
        ui.setupUi(QMainWindow)
        QMainWindow.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    main()
