# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdatingDlgBox.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

class Ui_UpdatingDlgBox(object):
    def setupUi(self, UpdatingDlgBox):
        UpdatingDlgBox.setObjectName("UpdatingDlgBox")
        UpdatingDlgBox.resize(291, 124)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Logos/CalculatorLogo(150p)_1.0.0.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UpdatingDlgBox.setWindowIcon(icon)
        self.UpdatingDlgProgressBar = QtWidgets.QProgressBar(UpdatingDlgBox)
        self.UpdatingDlgProgressBar.setGeometry(QtCore.QRect(30, 70, 251, 23))
        self.UpdatingDlgProgressBar.setProperty("value", 24)
        self.UpdatingDlgProgressBar.setObjectName("UpdatingDlgProgressBar")
        self.UpdatingDlgLabel = QtWidgets.QLabel(UpdatingDlgBox)
        self.UpdatingDlgLabel.setGeometry(QtCore.QRect(0, 30, 291, 20))
        self.UpdatingDlgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.UpdatingDlgLabel.setObjectName("UpdatingDlgLabel")

        self.retranslateUi(UpdatingDlgBox)
        QtCore.QMetaObject.connectSlotsByName(UpdatingDlgBox)

    def retranslateUi(self, UpdatingDlgBox):
        _translate = QtCore.QCoreApplication.translate
        UpdatingDlgBox.setWindowTitle(_translate("UpdatingDlgBox", "Updating Sagy Calculator"))
        self.UpdatingDlgLabel.setText(_translate("UpdatingDlgBox", "Downloading Updates"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UpdatingDlgBox = QtWidgets.QDialog()
    ui = Ui_UpdatingDlgBox()
    ui.setupUi(UpdatingDlgBox)
    UpdatingDlgBox.show()
    sys.exit(app.exec_())