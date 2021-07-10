# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\hmeltz\Documents\GitHub\DesktopCalculator\DesktopCalculatorGUI_1.1.0.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QApplication, QMessageBox
from PyQt5.QtGui import*
from PyQt5.QtCore import*


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        icon = QtGui.QIcon("CalculatorLogo(150p)_1.0.0.ico")
        MainWindow.setWindowIcon(icon)
        
        # set fixed size and disable resizing and maximizing window
        MainWindow.setFixedSize(331, 411)
       
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.button_equals = QtWidgets.QPushButton(self.centralwidget)
        self.button_equals.setGeometry(QtCore.QRect(260, 340, 51, 41))
        self.button_equals.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(255, 139, 85);\n"
"font: 20pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(230, 125, 76);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(217, 118, 72);\n"
"}\n"
"\n"
"")
        self.button_equals.setAutoDefault(True)
        self.button_equals.setDefault(False)
        self.button_equals.setFlat(True)
        self.button_equals.setObjectName("button_equals")
        self.button_equals.clicked.connect(self.equal_click)



        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setGeometry(QtCore.QRect(20, 190, 71, 41))
        self.button_7.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 20pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(212, 212, 212);\n"
"}\n"
"\n"
"")
        self.button_7.setAutoDefault(True)
        self.button_7.setDefault(False)
        self.button_7.setFlat(True)
        self.button_7.setObjectName("button_7")
        



        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.setGeometry(QtCore.QRect(100, 190, 71, 41))
        self.button_8.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 20pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(212, 212, 212);\n"
"}\n"
"\n"
"")
        self.button_8.setAutoDefault(True)
        self.button_8.setDefault(False)
        self.button_8.setFlat(True)
        self.button_8.setObjectName("button_8")


        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.button_9.setGeometry(QtCore.QRect(180, 190, 71, 41))
        self.button_9.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 20pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(212, 212, 212);\n"
"}\n"
"\n"
"")
        self.button_9.setAutoDefault(True)
        self.button_9.setDefault(False)
        self.button_9.setFlat(True)
        self.button_9.setObjectName("button_9")


        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.setGeometry(QtCore.QRect(20, 240, 71, 41))
        self.button_4.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 20pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(212, 212, 212);\n"
"}\n"
"\n"
"")
        self.button_4.setAutoDefault(True)
        self.button_4.setDefault(False)
        self.button_4.setFlat(True)
        self.button_4.setObjectName("button_4")


        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.setGeometry(QtCore.QRect(100, 240, 71, 41))
        self.button_5.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 20pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(212, 212, 212);\n"
"}\n"
"\n"
"")
        self.button_5.setAutoDefault(True)
        self.button_5.setDefault(False)
        self.button_5.setFlat(True)
        self.button_5.setObjectName("button_5")


        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setGeometry(QtCore.QRect(180, 240, 71, 41))
        self.button_6.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 20pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(212, 212, 212);\n"
"}\n"
"\n"
"")
        self.button_6.setAutoDefault(True)
        self.button_6.setDefault(False)
        self.button_6.setFlat(True)
        self.button_6.setObjectName("button_6")


        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setGeometry(QtCore.QRect(20, 290, 71, 41))
        self.button_1.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 20pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(212, 212, 212);\n"
"}\n"
"\n"
"")
        self.button_1.setAutoDefault(True)
        self.button_1.setDefault(False)
        self.button_1.setFlat(True)
        self.button_1.setObjectName("button_1")


        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(100, 290, 71, 41))
        self.button_2.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 20pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(212, 212, 212);\n"
"}\n"
"\n"
"")
        self.button_2.setAutoDefault(True)
        self.button_2.setDefault(False)
        self.button_2.setFlat(True)
        self.button_2.setObjectName("button_2")


        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.setGeometry(QtCore.QRect(180, 290, 71, 41))
        self.button_3.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 20pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(212, 212, 212);\n"
"}\n"
"\n"
"")
        self.button_3.setAutoDefault(True)
        self.button_3.setDefault(False)
        self.button_3.setFlat(True)
        self.button_3.setObjectName("button_3")


        self.button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear.setGeometry(QtCore.QRect(180, 340, 71, 41))
        self.button_clear.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 20pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(212, 212, 212);\n"
"}\n"
"\n"
"")
        self.button_clear.setAutoDefault(True)
        self.button_clear.setDefault(False)
        self.button_clear.setFlat(True)
        self.button_clear.setObjectName("button_clear")
        


        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.button_0.setGeometry(QtCore.QRect(20, 340, 71, 41))
        self.button_0.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 20pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(212, 212, 212);\n"
"}\n"
"\n"
"")
        self.button_0.setAutoDefault(True)
        self.button_0.setDefault(False)
        self.button_0.setFlat(True)
        self.button_0.setObjectName("button_0")


        self.button_dot = QtWidgets.QPushButton(self.centralwidget)
        self.button_dot.setGeometry(QtCore.QRect(100, 340, 71, 41))
        self.button_dot.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 20pt \"Calibri\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(212, 212, 212);\n"
"}\n"
"\n"
"")
        self.button_dot.setAutoDefault(True)
        self.button_dot.setDefault(False)
        self.button_dot.setFlat(True)
        self.button_dot.setObjectName("button_dot")


        self.button_minus = QtWidgets.QPushButton(self.centralwidget)
        self.button_minus.setGeometry(QtCore.QRect(260, 240, 51, 41))
        self.button_minus.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(217, 231, 245);\n"
"font: 20pt \"calibri\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(201, 213, 226);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(187, 199, 211);\n"
"}\n"
"\n"
"")
        self.button_minus.setAutoDefault(True)
        self.button_minus.setDefault(False)
        self.button_minus.setFlat(True)
        self.button_minus.setObjectName("button_minus")


        self.button_plus = QtWidgets.QPushButton(self.centralwidget)
        self.button_plus.setGeometry(QtCore.QRect(260, 290, 51, 41))
        self.button_plus.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(217, 231, 245);\n"
"font: 20pt \"calibri\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(201, 213, 226);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(187, 199, 211);\n"
"}\n"
"\n"
"")
        self.button_plus.setAutoDefault(True)
        self.button_plus.setDefault(False)
        self.button_plus.setFlat(True)
        self.button_plus.setObjectName("button_plus")


        self.button_openPar = QtWidgets.QPushButton(self.centralwidget)
        self.button_openPar.setGeometry(QtCore.QRect(20, 140, 71, 41))
        self.button_openPar.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(232, 232, 232);\n"
"font: 20pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(222, 222, 222);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(211, 211, 211);\n"
"}")
        self.button_openPar.setAutoDefault(True)
        self.button_openPar.setDefault(False)
        self.button_openPar.setFlat(True)
        self.button_openPar.setObjectName("button_openPar")


        self.button_closePar = QtWidgets.QPushButton(self.centralwidget)
        self.button_closePar.setGeometry(QtCore.QRect(100, 140, 71, 41))
        self.button_closePar.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(232, 232, 232);\n"
"font: 20pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(222, 222, 222);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(211, 211, 211);\n"
"}")
        self.button_closePar.setAutoDefault(True)
        self.button_closePar.setDefault(False)
        self.button_closePar.setFlat(True)
        self.button_closePar.setObjectName("button_closePar")


        self.button_backspace = QtWidgets.QPushButton(self.centralwidget)
        self.button_backspace.setGeometry(QtCore.QRect(180, 140, 71, 41))
        self.button_backspace.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(232, 232, 232);\n"
"font: 20pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(222, 222, 222);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(211, 211, 211);\n"
"}\n"
"\n"
"")
        self.button_backspace.setAutoDefault(True)
        self.button_backspace.setDefault(False)
        self.button_backspace.setFlat(True)
        self.button_backspace.setObjectName("button_backspace")


        self.button_div = QtWidgets.QPushButton(self.centralwidget)
        self.button_div.setGeometry(QtCore.QRect(260, 140, 51, 41))
        self.button_div.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(217, 231, 245);\n"
"font: 20pt \"calibri\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(201, 213, 226);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(187, 199, 211);\n"
"}\n"
"\n"
"")
        self.button_div.setAutoDefault(True)
        self.button_div.setDefault(False)
        self.button_div.setFlat(True)
        self.button_div.setObjectName("button_div")


        self.button_mult = QtWidgets.QPushButton(self.centralwidget)
        self.button_mult.setGeometry(QtCore.QRect(260, 190, 51, 41))
        self.button_mult.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(217, 231, 245);\n"
"font: 20pt \"calibri\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(201, 213, 226);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color: rgb(187, 199, 211);\n"
"}\n"
"\n"
"")
        self.button_mult.setAutoDefault(True)
        self.button_mult.setDefault(False)
        self.button_mult.setFlat(True)
        self.button_mult.setObjectName("button_mult")




        self.releaseLabel = QtWidgets.QLabel(self.centralwidget)
        self.releaseLabel.setGeometry(QtCore.QRect(20, 380, 161, 16))
        self.releaseLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.releaseLabel.setStyleSheet("font: 4pt \"MS Shell Dlg 2\";\n"
"color: rgb(197, 197, 197);")
        self.releaseLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.releaseLabel.setObjectName("releaseLabel")




        self.screenOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.screenOutput.setGeometry(QtCore.QRect(20, 30, 291, 20))
        self.screenOutput.setStyleSheet("border: none; background: transparent;"
        "font: 12pt \"MS Shell Dlg 2\";\n""color: rgb(190, 190, 190);")
        self.screenOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.screenOutput.setObjectName("eqInput")
        self.screenOutput.setContextMenuPolicy(Qt.NoContextMenu)        #disable menu pop up for cut/copy/paste
        self.screenOutput.selectionChanged.connect(lambda:self.screenOutput.deselect())  # disable selecting text


        self.decimalResultOutput = QtWidgets.QLabel(self.centralwidget)
        self.decimalResultOutput.setGeometry(QtCore.QRect(20, 100, 271, 31))
        self.decimalResultOutput.setStyleSheet("font: 11pt \"calibri\";\n"
"color: rgb(150, 150, 150);")
        self.decimalResultOutput.setText("")
        self.decimalResultOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.decimalResultOutput.setObjectName("decimalResultOutput")


        self.resultOutput = QtWidgets.QLabel(self.centralwidget)
        self.resultOutput.setGeometry(QtCore.QRect(20, 70, 271, 31))
        self.resultOutput.setStyleSheet("font: 23pt \"calibri\";\n"
"color: rgb(70, 70, 70);")
        self.resultOutput.setText("")
        self.resultOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.resultOutput.setObjectName("resultOutput")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 331, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " Sagy Calculator"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_clear.setText(_translate("MainWindow", "AC"))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_dot.setText(_translate("MainWindow", "."))
        self.button_minus.setText(_translate("MainWindow", "-"))
        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_openPar.setText(_translate("MainWindow", "("))
        self.button_closePar.setText(_translate("MainWindow", ")"))
        self.button_backspace.setText(_translate("MainWindow", "⌫"))
        self.button_div.setText(_translate("MainWindow", "÷"))
        self.button_mult.setText(_translate("MainWindow", "×"))
        self.button_equals.setText(_translate("MainWindow", "="))
        self.releaseLabel.setText(_translate("MainWindow", " YitzchakMeltz Release_1.03.05"))
        self.screenOutput.setText(_translate("MainWindow", "Enter Your Equation"))
#--------------------------------------------------------------------------------------