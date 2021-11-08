# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DesktopCalculatorGUI_1.06.01.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(331, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, -10, 331, 431))
        self.stackedWidget.setObjectName("stackedWidget")
        self.calculatorPage = QtWidgets.QWidget()
        self.calculatorPage.setObjectName("calculatorPage")
        self.button_8 = QtWidgets.QPushButton(self.calculatorPage)
        self.button_8.setGeometry(QtCore.QRect(100, 200, 71, 41))
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
        self.button_equals = QtWidgets.QPushButton(self.calculatorPage)
        self.button_equals.setGeometry(QtCore.QRect(260, 350, 51, 41))
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
        self.button_dot = QtWidgets.QPushButton(self.calculatorPage)
        self.button_dot.setGeometry(QtCore.QRect(100, 350, 71, 41))
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
        self.button_6 = QtWidgets.QPushButton(self.calculatorPage)
        self.button_6.setGeometry(QtCore.QRect(180, 250, 71, 41))
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
        self.button_7 = QtWidgets.QPushButton(self.calculatorPage)
        self.button_7.setGeometry(QtCore.QRect(20, 200, 71, 41))
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
        self.button_backspace = QtWidgets.QPushButton(self.calculatorPage)
        self.button_backspace.setGeometry(QtCore.QRect(180, 150, 71, 41))
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
        self.button_closePar = QtWidgets.QPushButton(self.calculatorPage)
        self.button_closePar.setGeometry(QtCore.QRect(100, 150, 71, 41))
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
        self.button_clear = QtWidgets.QPushButton(self.calculatorPage)
        self.button_clear.setGeometry(QtCore.QRect(180, 350, 71, 41))
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
        self.button_3 = QtWidgets.QPushButton(self.calculatorPage)
        self.button_3.setGeometry(QtCore.QRect(180, 300, 71, 41))
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
        self.button_9 = QtWidgets.QPushButton(self.calculatorPage)
        self.button_9.setGeometry(QtCore.QRect(180, 200, 71, 41))
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
        self.button_4 = QtWidgets.QPushButton(self.calculatorPage)
        self.button_4.setGeometry(QtCore.QRect(20, 250, 71, 41))
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
        self.button_minus = QtWidgets.QPushButton(self.calculatorPage)
        self.button_minus.setGeometry(QtCore.QRect(260, 250, 51, 41))
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
        self.settingsButton = QtWidgets.QPushButton(self.calculatorPage)
        self.settingsButton.setGeometry(QtCore.QRect(120, 400, 75, 21))
        self.settingsButton.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(232, 232, 232);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255,255,255);\n"
"border-radius : 8px; \n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/icons8-settings-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsButton.setIcon(icon)
        self.settingsButton.setIconSize(QtCore.QSize(10, 10))
        self.settingsButton.setObjectName("settingsButton")
        self.resultOutput = QtWidgets.QLabel(self.calculatorPage)
        self.resultOutput.setGeometry(QtCore.QRect(20, 80, 271, 31))
        self.resultOutput.setStyleSheet("font: 23pt \"calibri\";\n"
"color: rgb(94, 94, 94);")
        self.resultOutput.setText("")
        self.resultOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.resultOutput.setObjectName("resultOutput")
        self.screenOutput = QtWidgets.QLineEdit(self.calculatorPage)
        self.screenOutput.setGeometry(QtCore.QRect(20, 40, 291, 20))
        self.screenOutput.setStyleSheet("border: none; background: transparent;\n"
"font: 12pt MS Shell Dlg 2;\n"
"color: rgb(190, 190, 190);")
        self.screenOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.screenOutput.setObjectName("screenOutput")
        self.button_mult = QtWidgets.QPushButton(self.calculatorPage)
        self.button_mult.setGeometry(QtCore.QRect(260, 200, 51, 41))
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
        self.button_5 = QtWidgets.QPushButton(self.calculatorPage)
        self.button_5.setGeometry(QtCore.QRect(100, 250, 71, 41))
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
        self.button_0 = QtWidgets.QPushButton(self.calculatorPage)
        self.button_0.setGeometry(QtCore.QRect(20, 350, 71, 41))
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
        self.button_2 = QtWidgets.QPushButton(self.calculatorPage)
        self.button_2.setGeometry(QtCore.QRect(100, 300, 71, 41))
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
        self.button_openPar = QtWidgets.QPushButton(self.calculatorPage)
        self.button_openPar.setGeometry(QtCore.QRect(20, 150, 71, 41))
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
        self.releaseLabel = QtWidgets.QLabel(self.calculatorPage)
        self.releaseLabel.setGeometry(QtCore.QRect(2, 415, 81, 16))
        self.releaseLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.releaseLabel.setStyleSheet("font: 4pt \"MS Shell Dlg 2\";\n"
"color: rgb(197, 197, 197);")
        self.releaseLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.releaseLabel.setObjectName("releaseLabel")
        self.button_1 = QtWidgets.QPushButton(self.calculatorPage)
        self.button_1.setGeometry(QtCore.QRect(20, 300, 71, 41))
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
        self.button_div = QtWidgets.QPushButton(self.calculatorPage)
        self.button_div.setGeometry(QtCore.QRect(260, 150, 51, 41))
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
        self.button_plus = QtWidgets.QPushButton(self.calculatorPage)
        self.button_plus.setGeometry(QtCore.QRect(260, 300, 51, 41))
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
        self.decimalResultOutput = QtWidgets.QLabel(self.calculatorPage)
        self.decimalResultOutput.setGeometry(QtCore.QRect(20, 110, 271, 31))
        self.decimalResultOutput.setStyleSheet("border: none; background: transparent;\n"
"font: 11pt calibri;\n"
"color: rgb(150, 150, 150);")
        self.decimalResultOutput.setText("")
        self.decimalResultOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.decimalResultOutput.setObjectName("decimalResultOutput")
        self.redoButton = QtWidgets.QPushButton(self.calculatorPage)
        self.redoButton.setGeometry(QtCore.QRect(198, 400, 21, 21))
        self.redoButton.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(232, 232, 232);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255,255,255);\n"
"border-radius : 8px; \n"
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
        self.redoButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/redo_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redoButton.setIcon(icon1)
        self.redoButton.setIconSize(QtCore.QSize(10, 10))
        self.redoButton.setObjectName("redoButton")
        self.undoButton = QtWidgets.QPushButton(self.calculatorPage)
        self.undoButton.setGeometry(QtCore.QRect(96, 400, 21, 21))
        self.undoButton.setStyleSheet("QPushButton\n"
"{\n"
"border: none;\n"
"background-color: rgb(232, 232, 232);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255,255,255);\n"
"border-radius : 8px; \n"
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
        self.undoButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/undo_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undoButton.setIcon(icon2)
        self.undoButton.setIconSize(QtCore.QSize(10, 10))
        self.undoButton.setObjectName("undoButton")
        self.stackedWidget.addWidget(self.calculatorPage)
        self.settingsPage = QtWidgets.QWidget()
        self.settingsPage.setObjectName("settingsPage")
        self.decimalPoints_slider = QtWidgets.QSlider(self.settingsPage)
        self.decimalPoints_slider.setGeometry(QtCore.QRect(90, 270, 141, 21))
        self.decimalPoints_slider.setMinimum(1)
        self.decimalPoints_slider.setMaximum(10)
        self.decimalPoints_slider.setPageStep(1)
        self.decimalPoints_slider.setSliderPosition(6)
        self.decimalPoints_slider.setOrientation(QtCore.Qt.Horizontal)
        self.decimalPoints_slider.setInvertedAppearance(False)
        self.decimalPoints_slider.setInvertedControls(False)
        self.decimalPoints_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.decimalPoints_slider.setTickInterval(1)
        self.decimalPoints_slider.setObjectName("decimalPoints_slider")
        self.clipboard_checkbox = QtWidgets.QCheckBox(self.settingsPage)
        self.clipboard_checkbox.setGeometry(QtCore.QRect(70, 220, 171, 18))
        self.clipboard_checkbox.setObjectName("clipboard_checkbox")
        self.decimalPoints_label = QtWidgets.QLabel(self.settingsPage)
        self.decimalPoints_label.setGeometry(QtCore.QRect(90, 250, 181, 16))
        self.decimalPoints_label.setObjectName("decimalPoints_label")
        self.discard_button = QtWidgets.QPushButton(self.settingsPage)
        self.discard_button.setGeometry(QtCore.QRect(90, 340, 71, 31))
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
        self.save_button = QtWidgets.QPushButton(self.settingsPage)
        self.save_button.setGeometry(QtCore.QRect(170, 340, 71, 31))
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
        self.releaseLabel_2 = QtWidgets.QLabel(self.settingsPage)
        self.releaseLabel_2.setGeometry(QtCore.QRect(2, 415, 161, 16))
        self.releaseLabel_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.releaseLabel_2.setStyleSheet("font: 4pt \"MS Shell Dlg 2\";\n"
"color: rgb(197, 197, 197);")
        self.releaseLabel_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.releaseLabel_2.setObjectName("releaseLabel_2")
        self.clipboardDecimalPointDisplay = QtWidgets.QLabel(self.settingsPage)
        self.clipboardDecimalPointDisplay.setGeometry(QtCore.QRect(240, 270, 16, 16))
        self.clipboardDecimalPointDisplay.setStyleSheet("QLabel\n"
"{\n"
"background-color: rgb(255,255,255);\n"
"}")
        self.clipboardDecimalPointDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.clipboardDecimalPointDisplay.setObjectName("clipboardDecimalPointDisplay")
        self.reportLinkLabel = QtWidgets.QLabel(self.settingsPage)
        self.reportLinkLabel.setGeometry(QtCore.QRect(120, 380, 91, 20))
        self.reportLinkLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.reportLinkLabel.setWordWrap(False)
        self.reportLinkLabel.setOpenExternalLinks(True)
        self.reportLinkLabel.setObjectName("reportLinkLabel")
        self.zoom150RadioButton = QtWidgets.QRadioButton(self.settingsPage)
        self.zoom150RadioButton.setGeometry(QtCore.QRect(70, 80, 83, 18))
        self.zoom150RadioButton.setObjectName("zoom150RadioButton")
        self.zoom50RadioButton = QtWidgets.QRadioButton(self.settingsPage)
        self.zoom50RadioButton.setGeometry(QtCore.QRect(70, 160, 83, 18))
        self.zoom50RadioButton.setObjectName("zoom50RadioButton")
        self.zoom80RadioButton = QtWidgets.QRadioButton(self.settingsPage)
        self.zoom80RadioButton.setGeometry(QtCore.QRect(70, 140, 83, 18))
        self.zoom80RadioButton.setObjectName("zoom80RadioButton")
        self.zoom100RadioButton = QtWidgets.QRadioButton(self.settingsPage)
        self.zoom100RadioButton.setGeometry(QtCore.QRect(70, 120, 83, 18))
        self.zoom100RadioButton.setObjectName("zoom100RadioButton")
        self.zoom120RadioButton = QtWidgets.QRadioButton(self.settingsPage)
        self.zoom120RadioButton.setGeometry(QtCore.QRect(70, 100, 83, 18))
        self.zoom120RadioButton.setObjectName("zoom120RadioButton")
        self.zoomAutoRadioButton = QtWidgets.QRadioButton(self.settingsPage)
        self.zoomAutoRadioButton.setGeometry(QtCore.QRect(70, 60, 83, 18))
        self.zoomAutoRadioButton.setObjectName("zoomAutoRadioButton")
        self.zoomSettingsLeftLine = QtWidgets.QFrame(self.settingsPage)
        self.zoomSettingsLeftLine.setGeometry(QtCore.QRect(30, 40, 91, 16))
        self.zoomSettingsLeftLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.zoomSettingsLeftLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.zoomSettingsLeftLine.setObjectName("zoomSettingsLeftLine")
        self.zoomSettingsLabel = QtWidgets.QLabel(self.settingsPage)
        self.zoomSettingsLabel.setGeometry(QtCore.QRect(130, 40, 71, 16))
        self.zoomSettingsLabel.setStyleSheet("QLabel\n"
"{\n"
"color: Grey;\n"
"}\n"
"")
        self.zoomSettingsLabel.setObjectName("zoomSettingsLabel")
        self.zoomSettingsRightLine = QtWidgets.QFrame(self.settingsPage)
        self.zoomSettingsRightLine.setGeometry(QtCore.QRect(210, 40, 91, 16))
        self.zoomSettingsRightLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.zoomSettingsRightLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.zoomSettingsRightLine.setObjectName("zoomSettingsRightLine")
        self.cilpboardSettingsLabel = QtWidgets.QLabel(self.settingsPage)
        self.cilpboardSettingsLabel.setGeometry(QtCore.QRect(120, 190, 91, 20))
        self.cilpboardSettingsLabel.setStyleSheet("QLabel\n"
"{\n"
"color: Grey;\n"
"}\n"
"")
        self.cilpboardSettingsLabel.setObjectName("cilpboardSettingsLabel")
        self.clipboardSettingsRightLine = QtWidgets.QFrame(self.settingsPage)
        self.clipboardSettingsRightLine.setGeometry(QtCore.QRect(220, 190, 81, 20))
        self.clipboardSettingsRightLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.clipboardSettingsRightLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.clipboardSettingsRightLine.setObjectName("clipboardSettingsRightLine")
        self.clipboardSettingsLeftLine = QtWidgets.QFrame(self.settingsPage)
        self.clipboardSettingsLeftLine.setGeometry(QtCore.QRect(30, 190, 81, 20))
        self.clipboardSettingsLeftLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.clipboardSettingsLeftLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.clipboardSettingsLeftLine.setObjectName("clipboardSettingsLeftLine")
        self.zoomNoteLabel = QtWidgets.QLabel(self.settingsPage)
        self.zoomNoteLabel.setGeometry(QtCore.QRect(160, 80, 121, 71))
        self.zoomNoteLabel.setStyleSheet("QLabel\n"
"{\n"
"color: Grey;\n"
"}")
        self.zoomNoteLabel.setObjectName("zoomNoteLabel")
        self.stackedWidget.addWidget(self.settingsPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 331, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " Sagy Calculator"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_equals.setText(_translate("MainWindow", "="))
        self.button_dot.setText(_translate("MainWindow", "."))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_backspace.setText(_translate("MainWindow", "⌫"))
        self.button_closePar.setText(_translate("MainWindow", ")"))
        self.button_clear.setText(_translate("MainWindow", "AC"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_minus.setText(_translate("MainWindow", "-"))
        self.settingsButton.setText(_translate("MainWindow", "Settings"))
        self.screenOutput.setText(_translate("MainWindow", "Enter Your Equation"))
        self.button_mult.setText(_translate("MainWindow", "×"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_openPar.setText(_translate("MainWindow", "("))
        self.releaseLabel.setText(_translate("MainWindow", "  YitzchakMeltz Release_1.07.00"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_div.setText(_translate("MainWindow", "÷"))
        self.button_plus.setText(_translate("MainWindow", "+"))
        self.clipboard_checkbox.setText(_translate("MainWindow", "Copy answer to clipboard"))
        self.decimalPoints_label.setText(_translate("MainWindow", "Decimal points to copy to clipboard"))
        self.discard_button.setText(_translate("MainWindow", "Discard"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.releaseLabel_2.setText(_translate("MainWindow", "  YitzchakMeltz Release_1.07.00"))
        self.clipboardDecimalPointDisplay.setText(_translate("MainWindow", "6"))
        self.reportLinkLabel.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://yitzchakmeltz.github.io/SassyOwlWebsite/support.html\"><span style=\" color:#0000ff;\">report a problem</span></a></p></body></html>"))
        self.zoom150RadioButton.setText(_translate("MainWindow", " 150%"))
        self.zoom50RadioButton.setText(_translate("MainWindow", " 50%"))
        self.zoom80RadioButton.setText(_translate("MainWindow", " 80%"))
        self.zoom100RadioButton.setText(_translate("MainWindow", " 100%"))
        self.zoom120RadioButton.setText(_translate("MainWindow", " 120%"))
        self.zoomAutoRadioButton.setText(_translate("MainWindow", " Auto"))
        self.zoomSettingsLabel.setText(_translate("MainWindow", "Zoom Settings"))
        self.cilpboardSettingsLabel.setText(_translate("MainWindow", "Clipboard Settings"))
        self.zoomNoteLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Note: Changes made to<br>the  zoom settings will <br>not be noticed until <br>the program is restarted</p></body></html>"))
