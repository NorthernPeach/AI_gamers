from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 461, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
        # setting its geometry
        self.label = QtWidgets.QLabel("Select folder:\t\nTop Predict:\t\n1)\t\n2)\t\n3)\t\n4)\t\n5)", self.centralwidget)
        self.label.setStyleSheet("")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label)
  

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(16, 10, 451, 20))
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setFont(QtGui.QFont('Arial', 12))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 476, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pbar = QProgressBar(self.centralwidget)
  
        self.pbar.setGeometry(10, 250, 450, 25)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ai Gamers Bowhead whale "))
        MainWindow.setWindowIcon(QtGui.QIcon('ico3.ico'))
        self.pushButton_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>CVS from Folder with folders</p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "CVS"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Predict Dir</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Predict"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Dir image</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Load"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p>Top area</p></body></html>"))
        self.label_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Photo prediction area</p></body></html>"))
