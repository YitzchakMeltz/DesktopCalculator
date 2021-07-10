from DesktopCalculatorGUI140 import*

class mainControl(Ui_MainWindow):
    def __init__(self, Window):
        self.setupUi(Window)
    
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
        self.decimalResultOutput.setText(mainBackend140.decimalSum)
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

def check_for_updates():
    if have_internet():
            print("check for updates")
            from updateProgramCode140 import checkForUpdates, updateCalc, openUpdateInstaller
            if checkForUpdates():
                    if update_msgbox():
                            updating_dlgbox()
                            if updateCalc():
                                    import atexit, sys, os
                                    installer = os.path.join('C:\ProgramData\SasyOwl\SagyCalculator','Updates',
                                                            'SagyCalculatorSetup.exe')
                                    atexit.register(os.execl, installer, installer)
                                    dlg.close()
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

    if not check_for_updates():
        sys.exit(app.exec_())

    #--------------------------------------------------------------------------------------