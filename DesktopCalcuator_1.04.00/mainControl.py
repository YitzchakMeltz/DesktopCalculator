from DesktopCalculatorGUI140 import*

#--------------------------------- Main Program ---------------------------------------
if __name__ == "__main__":
    import sys
    

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()

    if not ui.check_for_updates():
        sys.exit(app.exec_())

   
    
    #--------------------------------------------------------------------------------------