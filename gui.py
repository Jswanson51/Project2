from PyQt5 import QtCore, QtGui, QtWidgets
import webcolors


class Ui_QMainWindow(object):
    def setupUi(self, QMainWindow):
        QMainWindow.setObjectName("QMainWindow")
        QMainWindow.resize(645, 452)
        self.centralwidget = QtWidgets.QWidget(QMainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Label_Hexidecimal = QtWidgets.QLabel(self.centralwidget)
        self.Label_Hexidecimal.setGeometry(QtCore.QRect(250, 300, 200, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Hexidecimal.setFont(font)
        self.Label_Hexidecimal.setObjectName("Label_Hexidecimal")

        self.Color_viewer = QtWidgets.QGraphicsView(self.centralwidget)
        self.Color_viewer.setGeometry(QtCore.QRect(200, 20, 231, 161))
        self.Color_viewer.setObjectName("Color_viewer")

        self.R_value = QtWidgets.QSpinBox(self.centralwidget)
        self.R_value.setGeometry(QtCore.QRect(220, 210, 51, 31))
        self.R_value.setMaximum(255)
        self.R_value.setObjectName("R_value")

        self.G_value = QtWidgets.QSpinBox(self.centralwidget)
        self.G_value.setGeometry(QtCore.QRect(290, 210, 51, 31))
        self.G_value.setMaximum(255)
        self.G_value.setObjectName("G_value")

        self.B_value = QtWidgets.QSpinBox(self.centralwidget)
        self.B_value.setGeometry(QtCore.QRect(360, 210, 51, 31))
        self.B_value.setMaximum(255)
        self.B_value.setObjectName("B_value")

        self.label_HexValue = QtWidgets.QLabel(self.centralwidget)
        self.label_HexValue.setGeometry(QtCore.QRect(200, 350, 221, 51))
        self.label_HexValue.setText("")
        self.label_HexValue.setObjectName("label_HexValue")
        QMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 21))
        self.menubar.setObjectName("menubar")
        QMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(QMainWindow)
        self.statusbar.setObjectName("statusbar")
        QMainWindow.setStatusBar(self.statusbar)

        self.button_select = QtWidgets.QPushButton(self.centralwidget)
        self.button_select.setText('Select Color')
        self.button_select.setGeometry(QtCore.QRect(200, 255, 231, 30))

        Spin1_value = 0
        Spin2_value = 0
        Spin3_value = 0

    def clicked_select(self):
        Spin1_value = int(self.R_value.value)
        Spin2_value = int(self.G_value.value)
        Spin3_value = int(self.B_value.value)

        RGB = (Spin1_value, Spin2_value, Spin3_value)

        self.label_HexValue.setText(webcolors.rgb_to_hex(RGB))

        print(Spin1_value)
        print(Spin2_value)
        print(Spin3_value)

        self.retranslateUi(QMainWindow)
        QtCore.QMetaObject.connectSlotsByName(QMainWindow)

    def retranslateUi(self, QMainWindow):
        _translate = QtCore.QCoreApplication.translate
        QMainWindow.setWindowTitle(_translate("QMainWindow", "Color Preview"))
        self.Label_Hexidecimal.setText(_translate("QMainWindow", "Hexidecimal:"))

