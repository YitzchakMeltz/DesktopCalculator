# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\hmeltz\Documents\GitHub\DesktopCalculator\ui\SettingsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(331, 418)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(170, 330, 71, 31))
        self.save_button.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(232, 232, 232);\n"
"font: 8pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(222, 222, 222);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(211, 211, 211);\n"
"}")
        self.save_button.setAutoDefault(True)
        self.save_button.setDefault(False)
        self.save_button.setFlat(True)
        self.save_button.setObjectName("save_button")
        self.releaseLabel = QtWidgets.QLabel(self.centralwidget)
        self.releaseLabel.setGeometry(QtCore.QRect(10, 400, 161, 16))
        self.releaseLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.releaseLabel.setStyleSheet("font: 4pt \"MS Shell Dlg 2\";\n"
"color: rgb(197, 197, 197);")
        self.releaseLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.releaseLabel.setObjectName("releaseLabel")
        self.decimalPoints_label = QtWidgets.QLabel(self.centralwidget)
        self.decimalPoints_label.setGeometry(QtCore.QRect(90, 130, 181, 16))
        self.decimalPoints_label.setObjectName("decimalPoints_label")
        self.decimalPoints_slider = QtWidgets.QSlider(self.centralwidget)
        self.decimalPoints_slider.setGeometry(QtCore.QRect(90, 150, 171, 16))
        self.decimalPoints_slider.setOrientation(QtCore.Qt.Horizontal)
        self.decimalPoints_slider.setObjectName("decimalPoints_slider")
        self.settings_label = QtWidgets.QLabel(self.centralwidget)
        self.settings_label.setGeometry(QtCore.QRect(130, 20, 71, 20))
        self.settings_label.setStyleSheet("QLabel\n"
"{\n"
"font-size: 16px;\n"
"color: rgb(180,180,180);\n"
"}")
        self.settings_label.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_label.setObjectName("settings_label")
        self.discard_button = QtWidgets.QPushButton(self.centralwidget)
        self.discard_button.setGeometry(QtCore.QRect(90, 330, 71, 31))
        self.discard_button.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(232, 232, 232);\n"
"font: 8pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(222, 222, 222);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(211, 211, 211);\n"
"}")
        self.discard_button.setAutoDefault(True)
        self.discard_button.setDefault(False)
        self.discard_button.setFlat(True)
        self.discard_button.setObjectName("discard_button")
        self.scaling_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.scaling_checkbox.setGeometry(QtCore.QRect(70, 70, 191, 18))
        self.scaling_checkbox.setObjectName("scaling_checkbox")
        self.clipboard_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.clipboard_checkbox.setGeometry(QtCore.QRect(70, 100, 171, 18))
        self.clipboard_checkbox.setObjectName("clipboard_checkbox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 331, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.releaseLabel.setText(_translate("MainWindow", "  YitzchakMeltz   Release_1.6.0"))
        self.decimalPoints_label.setText(_translate("MainWindow", "Decimal points to copy to clipboard"))
        self.settings_label.setText(_translate("MainWindow", "Settings"))
        self.discard_button.setText(_translate("MainWindow", "Discard"))
        self.scaling_checkbox.setText(_translate("MainWindow", "Handle high resolution displays"))
        self.clipboard_checkbox.setText(_translate("MainWindow", "Copy answer to clipboard"))
