# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1440, 788)
        self.sideRect = QtWidgets.QLabel(Dialog)
        self.sideRect.setGeometry(QtCore.QRect(0, 0, 81, 851))
        self.sideRect.setText("")
        self.sideRect.setPixmap(QtGui.QPixmap("rectangle.png"))
        self.sideRect.setObjectName("sideRect")
        self.terminal = QtWidgets.QLabel(Dialog)
        self.terminal.setGeometry(QtCore.QRect(10, 720, 41, 51))
        self.terminal.setText("")
        self.terminal.setPixmap(QtGui.QPixmap("terminal.png"))
        self.terminal.setObjectName("terminal")
        self.orcaLogo = QtWidgets.QLabel(Dialog)
        self.orcaLogo.setGeometry(QtCore.QRect(10, 10, 51, 61))
        self.orcaLogo.setText("")
        self.orcaLogo.setPixmap(QtGui.QPixmap("orcalogo.png"))
        self.orcaLogo.setObjectName("orcaLogo")
        self.largeRect = QtWidgets.QLabel(Dialog)
        self.largeRect.setGeometry(QtCore.QRect(80, 0, 1361, 851))
        self.largeRect.setText("")
        self.largeRect.setPixmap(QtGui.QPixmap("bigrectangle.png"))
        self.largeRect.setObjectName("largeRect")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 0, 251, 101))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("red5.png"))
        self.label_5.setObjectName("label_5")
        self.docking = QtWidgets.QPushButton(Dialog)
        self.docking.setGeometry(QtCore.QRect(195, 240, 71, 61))
        self.docking.setStyleSheet("border: none ;\n"
"")
        self.docking.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Docking.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.docking.setIcon(icon)
        self.docking.setIconSize(QtCore.QSize(65, 65))
        self.docking.setObjectName("docking")
        self.photomosaic = QtWidgets.QPushButton(Dialog)
        self.photomosaic.setGeometry(QtCore.QRect(490, 240, 81, 61))
        self.photomosaic.setStyleSheet("border: none ;\n"
"")
        self.photomosaic.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Photomosaic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.photomosaic.setIcon(icon1)
        self.photomosaic.setIconSize(QtCore.QSize(65, 65))
        self.photomosaic.setObjectName("photomosaic")
        self.fishLength = QtWidgets.QPushButton(Dialog)
        self.fishLength.setGeometry(QtCore.QRect(420, 110, 71, 61))
        self.fishLength.setStyleSheet("border: none ;\n"
"")
        self.fishLength.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("fishLength.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fishLength.setIcon(icon2)
        self.fishLength.setIconSize(QtCore.QSize(65, 65))
        self.fishLength.setObjectName("fishLength")
        self.linefollower = QtWidgets.QPushButton(Dialog)
        self.linefollower.setGeometry(QtCore.QRect(120, 110, 65, 65))
        self.linefollower.setMaximumSize(QtCore.QSize(65, 65))
        self.linefollower.setStyleSheet("border: none ;\n"
"")
        self.linefollower.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("linefollower.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.linefollower.setIcon(icon3)
        self.linefollower.setIconSize(QtCore.QSize(65, 65))
        self.linefollower.setObjectName("linefollower")
        self.mortDetect = QtWidgets.QPushButton(Dialog)
        self.mortDetect.setGeometry(QtCore.QRect(270, 110, 81, 61))
        self.mortDetect.setStyleSheet("border: none ;\n"
"")
        self.mortDetect.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("mortdetection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mortDetect.setIcon(icon4)
        self.mortDetect.setIconSize(QtCore.QSize(65, 65))
        self.mortDetect.setObjectName("mortDetect")
        self.wreckLength = QtWidgets.QPushButton(Dialog)
        self.wreckLength.setGeometry(QtCore.QRect(570, 110, 71, 61))
        self.wreckLength.setStyleSheet("border: none ;\n"
"")
        self.wreckLength.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("WreckLength.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.wreckLength.setIcon(icon5)
        self.wreckLength.setIconSize(QtCore.QSize(65, 65))
        self.wreckLength.setObjectName("wreckLength")
        self.lfText = QtWidgets.QLineEdit(Dialog)
        self.lfText.setGeometry(QtCore.QRect(110, 180, 91, 21))
        self.lfText.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"color: white;")
        self.lfText.setObjectName("lfText")
        self.mdText = QtWidgets.QLineEdit(Dialog)
        self.mdText.setGeometry(QtCore.QRect(260, 180, 101, 21))
        self.mdText.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"color: white;")
        self.mdText.setObjectName("mdText")
        self.flText = QtWidgets.QLineEdit(Dialog)
        self.flText.setGeometry(QtCore.QRect(415, 180, 81, 21))
        self.flText.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"color: white;")
        self.flText.setObjectName("flText")
        self.dText = QtWidgets.QLineEdit(Dialog)
        self.dText.setGeometry(QtCore.QRect(202, 310, 61, 21))
        self.dText.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"color: white;")
        self.dText.setObjectName("dText")
        self.wlText = QtWidgets.QLineEdit(Dialog)
        self.wlText.setGeometry(QtCore.QRect(560, 180, 91, 21))
        self.wlText.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"color: white;")
        self.wlText.setObjectName("wlText")
        self.pText = QtWidgets.QLineEdit(Dialog)
        self.pText.setGeometry(QtCore.QRect(490, 310, 91, 21))
        self.pText.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"color: white;")
        self.pText.setObjectName("pText")
        self.sideRect.raise_()
        self.terminal.raise_()
        self.orcaLogo.raise_()
        self.largeRect.raise_()
        self.label_5.raise_()
        self.docking.raise_()
        self.photomosaic.raise_()
        self.linefollower.raise_()
        self.mortDetect.raise_()
        self.wreckLength.raise_()
        self.lfText.raise_()
        self.fishLength.raise_()
        self.mdText.raise_()
        self.flText.raise_()
        self.dText.raise_()
        self.wlText.raise_()
        self.pText.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lfText.setText(_translate("Dialog", "Line Follower"))
        self.mdText.setText(_translate("Dialog", "Mort Detection"))
        self.flText.setText(_translate("Dialog", "Fish Length"))
        self.dText.setText(_translate("Dialog", "Docking"))
        self.wlText.setText(_translate("Dialog", "Wreck Length"))
        self.pText.setText(_translate("Dialog", "Photomosaic"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

