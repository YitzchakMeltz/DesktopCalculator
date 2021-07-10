from DesktopCalculatorGUI140 import*

button_7.clicked.connect(lambda:click_and_update("7"))

#--------------------------------------------------------------------------------------
#----------------------------------- Functions ----------------------------------------
def click_and_update(userClick):
    import mainBackend140
    global placeholderThere
    if(mainBackend140.lastEqual):
            clear_results()
    newCursorPos = button_click(userClick,screenOutput.cursorPosition(), not screenOutput.hasFocus())
    placeholderThere = False
    update_screen()
    screenOutput.setCursorPosition(newCursorPos)
    button_equals.setFocus()
    return

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
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()

    if not check_for_updates():
        sys.exit(app.exec_())

    #--------------------------------------------------------------------------------------