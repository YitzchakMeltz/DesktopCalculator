from DesktopCalculatorGUI140 import*
from mainBackend140 import*

# Handle high resolution displays:
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


resultStyleChanged = False
placeholderThere = True

    
class mainControl(Ui_MainWindow):
    def __init__(self, Window):
        self.setupUi(Window)
    
        icon = QtGui.QIcon("CalculatorLogo(150p)_1.0.0.ico")
        Window.setWindowIcon(icon)

        # set fixed size and disable resizing and maximizing window
        Window.setFixedSize(331, 411)

        self.screenOutput.setContextMenuPolicy(Qt.NoContextMenu)        #disable menu pop up for cut/copy/paste
        self.screenOutput.selectionChanged.connect(lambda:self.screenOutput.deselect())  # disable selecting text

    #-------------------------------- Connect Buttons -------------------------------------
        self.button_0.clicked.connect(lambda:self.click_and_update("0"))
        self.button_1.clicked.connect(lambda:self.click_and_update("1"))
        self.button_2.clicked.connect(lambda:self.click_and_update("2"))
        self.button_3.clicked.connect(lambda:self.click_and_update("3"))
        self.button_4.clicked.connect(lambda:self.click_and_update("4"))
        self.button_5.clicked.connect(lambda:self.click_and_update("5"))
        self.button_6.clicked.connect(lambda:self.click_and_update("6"))
        self.button_7.clicked.connect(lambda:self.click_and_update("7"))
        self.button_8.clicked.connect(lambda:self.click_and_update("8"))
        self.button_9.clicked.connect(lambda:self.click_and_update("9"))
        self.button_clear.clicked.connect(self.click_and_clear)
        self.button_dot.clicked.connect(lambda:self.click_and_update("."))
        self.button_plus.clicked.connect(lambda:self.click_and_update(" + "))
        self.button_minus.clicked.connect(lambda:self.click_and_update(" - "))
        self.button_div.clicked.connect(lambda:self.click_and_update(" ÷ "))
        self.button_mult.clicked.connect(lambda:self.click_and_update(" × "))
        self.button_openPar.clicked.connect(lambda:self.click_and_update("("))
        self.button_closePar.clicked.connect(lambda:self.click_and_update(")"))
        self.button_backspace.clicked.connect(self.backspace_click)

        # set keyPressEvent to current widgets that we'd like it to be overridden
        self.centralwidget.keyPressEvent = self.keyPressEvent
        self.screenOutput.keyPressEvent = self.keyPressEvent
    #--------------------------------------------------------------------------------------    

#---------------------------------- Key Press -----------------------------------------

    # override when key is pressed and treat key like on-screen pushbutton
    def keyPressEvent(self,e):

        if e.key() == Qt.Key_0:
                self.click_and_update("0")

        if e.key() == Qt.Key_1:
                self.click_and_update("1")

        if e.key() == Qt.Key_2:
                self.click_and_update("2")

        if e.key() == Qt.Key_3:
                self.click_and_update("3")

        if e.key() == Qt.Key_4:
                self.click_and_update("4")

        if e.key() == Qt.Key_5:
                self.click_and_update("5")

        if e.key() == Qt.Key_6:
                self.click_and_update("6")

        if e.key() == Qt.Key_7:
                self.click_and_update("7")

        if e.key() == Qt.Key_8:
                self.click_and_update("8")

        if e.key() == Qt.Key_9:
                self.click_and_update("9")

        if e.key() == Qt.Key_Plus:
                self.click_and_update(" + ")

        if e.key() == Qt.Key_Minus:
                self.click_and_update(" - ")

        if e.key() == Qt.Key_Asterisk:
                self.click_and_update(" × ")

        if e.key() == Qt.Key_Slash:
                self.click_and_update(" ÷ ")

        if e.key() == Qt.Key_Period:
                self.click_and_update(".")

        if e.key() == Qt.Key_ParenLeft:
                self.click_and_update("(")

        if e.key() == Qt.Key_ParenRight:
                self.click_and_update(")")

        if e.key() in (Qt.Key_Return,Qt.Key_Enter):
                self.equal_click()

        if e.key() == Qt.Key_Equal:
                self.equal_click()

        if e.key() == Qt.Key_Delete:
                self.click_and_clear()
        
        if e.key() == Qt.Key_Backspace:
                self.backspace_click()

        if e.key() == Qt.Key_Right:
                self.arrow_click('R')

        if e.key() == Qt.Key_Left:
                self.arrow_click('L')
#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------
#----------------------------------- Functions ----------------------------------------
    def click_and_update(self,userClick):
        import mainBackend140
        global placeholderThere
        if(mainBackend140.lastEqual):
                self.clear_results()
        newCursorPos = button_click(userClick,self.screenOutput.cursorPosition(), not self.screenOutput.hasFocus())
        placeholderThere = False
        self.update_screen()
        self.screenOutput.setCursorPosition(newCursorPos)
        self.button_equals.setFocus()
        return
    
    def update_screen(self):
        import mainBackend140
        global placeholderThere
        self.screenOutput.setText(mainBackend140.mathEq)
        
        if mainBackend140.mathEq == "":
                self.screenOutput.setText("Enter Your Equation")
                placeholderThere = True

        if placeholderThere:
                self.screenOutput.setStyleSheet("border: none; background: transparent;""font: 12pt \"MS Shell Dlg 2\";\n""color: rgb(190, 190, 190);")
                self.screenOutput.setReadOnly(True)
        else:
               self.screenOutput.setStyleSheet("border: none; background: transparent;""font: 12pt \"MS Shell Dlg 2\";\n""color: rgb(110, 110, 110);") 
               self.screenOutput.setReadOnly(False)
        return

    def click_and_clear(self):
        button_clear_click()
        self.update_screen()
        self.update_result_screen()
        self.resultOutput.setText("")
        return

        # clear the results screens
    def clear_results(self):
        self.resultOutput.setText("")
        self.decimalResultOutput.setText("")
        return

    def equal_click(self):
        button_equals_click()
        self.update_screen()
        self.update_result_screen()
        return

    def update_result_screen(self):
        import mainBackend140
        global resultStyleChanged
   
        button_equals_click()

        if resultStyleChanged:
               self.resultOutput.setStyleSheet("font: 23pt \"calibri\";\n""color: rgb(70, 70, 70);")          # reset the style to large
        
        if len(str((mainBackend140.sum)))>15:
                self.resultOutput.setStyleSheet("font: 13pt \"calibri\";\n""color: rgb(70, 70, 70);")
                resultStyleChanged = True

        if isinstance(mainBackend140.sum,int) or isinstance(mainBackend140.sum,Fraction):
                self.resultOutput.setText("= " + str(mainBackend140.sum))
                self.decimalResultOutput.setText(mainBackend140.decimalSum)
        else:
                self.resultOutput.setText(mainBackend140.sum)
        return

    def backspace_click(self):
        import mainBackend140
        newCursorPos = button_backspace_click(self.screenOutput.cursorPosition())
        self.update_screen()
        self.resultOutput.setText("")
        self.decimalResultOutput.setText("")
        self.screenOutput.setCursorPosition(newCursorPos)

    def arrow_click(self,direction):
        newCursorPos = button_arrow_click(self.screenOutput.cursorPosition(),direction)
        self.screenOutput.setCursorPosition(newCursorPos)    

    def update_screen(self):
        import mainBackend140
        global placeholderThere
        self.screenOutput.setText(mainBackend140.mathEq)
        #self.decimalResultOutput.setText(mainBackend140.decimalSum)
        if mainBackend140.mathEq == "":
                self.screenOutput.setText("Enter Your Equation")
                placeholderThere = True

        if placeholderThere:
                self.screenOutput.setStyleSheet("border: none; background: transparent;""font: 12pt \"MS Shell Dlg 2\";\n""color: rgb(190, 190, 190);")
                self.screenOutput.setReadOnly(True)
        else:
               self.screenOutput.setStyleSheet("border: none; background: transparent;""font: 12pt \"MS Shell Dlg 2\";\n""color: rgb(110, 110, 110);") 
               self.screenOutput.setReadOnly(False)
        return

    def click_and_clear(self):
        button_clear_click()
        self.update_screen()
        self.update_result_screen()
        self.resultOutput.setText("")
        
        return

        # clear the results screens
    def clear_results(self):
        self.resultOutput.setText("")
        self.decimalResultOutput.setText("")
        return

    def equal_click(self):
        button_equals_click()
        self.update_screen()
        self.update_result_screen()
        return

    def update_result_screen(self):
        import mainBackend140
        global resultStyleChanged
   
        button_equals_click()

        if resultStyleChanged:
               self.resultOutput.setStyleSheet("font: 23pt \"calibri\";\n""color: rgb(70, 70, 70);")          # reset the style to large
        
        if len(str((mainBackend140.sum)))>15:
                self.resultOutput.setStyleSheet("font: 13pt \"calibri\";\n""color: rgb(70, 70, 70);")
                resultStyleChanged = True

        if isinstance(mainBackend140.sum,int) or isinstance(mainBackend140.sum,Fraction):
                self.resultOutput.setText("= " + str(mainBackend140.sum))
                self.decimalResultOutput.setText(mainBackend140.decimalSum)
        else:
                self.resultOutput.setText(mainBackend140.sum)
        return

    def backspace_click(self):
        import mainBackend140
        newCursorPos = button_backspace_click(self.screenOutput.cursorPosition())
        self.update_screen()
        self.resultOutput.setText("")
        self.decimalResultOutput.setText("")
        self.screenOutput.setCursorPosition(newCursorPos)

    def update_msgbox(self):
        from PyQt5.QtWidgets import QLabel, QDialogButtonBox
        self.msg = QMessageBox()
        self.grid_layout = self.msg.layout()

        self.qt_msgboxex_icon_label = self.msg.findChild(QLabel, "qt_msgboxex_icon_label")
        self.qt_msgboxex_icon_label.deleteLater()

        self.qt_msgbox_label = self.msg.findChild(QLabel, "qt_msgbox_label")
        self.qt_msgbox_label.setAlignment(Qt.AlignCenter)
        self.grid_layout.removeWidget(self.qt_msgbox_label)

        self.qt_msgbox_buttonbox = self.msg.findChild(QDialogButtonBox, "qt_msgbox_buttonbox")
        self.grid_layout.removeWidget(self.qt_msgbox_buttonbox)

        self.grid_layout.addWidget(self.qt_msgbox_label, 0, 0, alignment=Qt.AlignCenter)
        self.grid_layout.addWidget(self.qt_msgbox_buttonbox, 1, 0, alignment=Qt.AlignCenter)


        self.msg.setWindowTitle("  Software Update")
        self.msg.setText("A software update is available.<br>Do you want to update now?<br>")
        self.msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        self.msg.setStyleSheet("QLabel{min-width: 200px;}")
        self.msg.setWindowIcon(QtGui.QIcon("CalculatorLogo(150p)_1.0.0.ico"))

        if self.msg.exec_() == QMessageBox.Ok:
                return True

        else: 
                return False


    def updating_dlgbox(self):
        from PyQt5.QtWidgets import QLabel, QDialog
        self.dlg = QDialog()
        self.dlg.setWindowTitle(" Updating")
        self.dlg.setWindowIcon(QtGui.QIcon("CalculatorLogo(150p)_1.0.0.ico"))
        self.dlg.setModal(True)
        label = QLabel(self.dlg)
        label.setText("Program is updating.\nPlease do not turn off your computer.")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setGeometry(QtCore.QRect(20, 30, 200, 27))
        self.dlg.show()

    def check_for_updates(self):
        if have_internet():
                print("check for updates")
                from updateProgramCode140 import checkForUpdates, updateCalc, openUpdateInstaller
                if checkForUpdates():
                        if self.update_msgbox():
                                self.updating_dlgbox()
                                if updateCalc():
                                        import atexit, sys, os
                                        installer = os.path.join('C:\ProgramData\SasyOwl\SagyCalculator','Updates',
                                                                 'SagyCalculatorSetup.exe')
                                        atexit.register(os.execl, installer, installer)
                                        self.dlg.close()
                                        MainWindow.close()
                                        return True
        return False
#--------------------------------------------------------------------------------------

#--------------------------------- Main Program ---------------------------------------
if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = mainControl(MainWindow)
    
    MainWindow.show()

    if not ui.check_for_updates():
        sys.exit(app.exec_())
#--------------------------------------------------------------------------------------