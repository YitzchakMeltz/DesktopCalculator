import MainWindowGUI
import mainBackend140
from MainWindowGUI import*
from mainBackend140 import*
from settings import*
from updateProgramCode140 import checkForUpdates, updateCalc
import sys, os
from threads import DownloadThread
from PyQt5.uic import loadUi
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QListView
from PyQt5.QtWidgets import QLabel, QDialogButtonBox

initializeCalculatorSettings()

displayValue = get_HR_Display_Value()
# Handle high resolution displays:
if hasattr(displayValue == "Auto" and QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(displayValue == "Auto" and QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

# manual settings
if hasattr(not displayValue == "Auto" and QtCore.Qt, 'AA_EnableHighDpiScaling'):
        os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
        os.environ["QT_SCALE_FACTOR"] = displayValue
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

resultStyleChanged = False
placeholderThere = True
   
class mainControl(QMainWindow, Ui_MainWindow):
    def __init__(self, Window, parent=None):
        super(mainControl, self).__init__(parent)

        self.bl = SagyLogic()

        self.settings = retrieveSettings()

        self.setupUi(Window)
    
        self.stackedWidget.setCurrentIndex(0)

        icon = QtGui.QIcon("icons/CalculatorLogo(150p)_1.0.0.ico")
        Window.setWindowIcon(icon)

        undoIcon = QtGui.QIcon("icons/undo_icon.png")
        self.undoButton.setIcon(undoIcon)
        redoIcon = QtGui.QIcon("icons/redo_icon.png")
        self.redoButton.setIcon(redoIcon)
        settingsIcon = QtGui.QIcon("icons/icons8-settings-50.png")
        self.settingsButton.setIcon(settingsIcon)
        
        # set fixed size and disable resizing and maximizing window
        Window.setFixedSize(331, 468)

        # needed to allow extrra spacing in between setting comboBox items
        self.zoom_comboBox.setView(QListView())

        self.screenOutput.setReadOnly(True)
        self.screenOutput.setContextMenuPolicy(Qt.NoContextMenu)        #disable menu pop up for cut/copy/paste
        self.screenOutput.selectionChanged.connect(lambda:self.screenOutput.deselect())  # disable selecting text
        self.button_equals.setFocus()   # set focus to equals button so that if you press enter it doesn't press a different button

        # disable undo and redo buttons when opened
        if len(self.bl.undo_stack) < 2:
                self.undoButton.setEnabled(False)
        if not self.bl.redo_stack:
                self.redoButton.setEnabled(False)
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
        self.button_ans.clicked.connect(lambda:self.click_and_update(self.bl.get_previous_answer()))
        self.button_clear.clicked.connect(self.click_and_clear)
        self.button_dot.clicked.connect(lambda:self.click_and_update("."))
        self.button_plus.clicked.connect(lambda:self.click_and_update(" + "))
        self.button_minus.clicked.connect(lambda:self.click_and_update(" - "))
        self.button_div.clicked.connect(lambda:self.click_and_update(" ÷ "))
        self.button_mult.clicked.connect(lambda:self.click_and_update(" × "))
        self.button_percent.clicked.connect(lambda:self.click_and_update("% "))
        self.button_openPar.clicked.connect(lambda:self.click_and_update("("))
        self.button_closePar.clicked.connect(lambda:self.click_and_update(")"))
        self.button_backspace.clicked.connect(self.backspace_click)
        self.button_equals.clicked.connect(self.equal_click)
        self.settingsButton.clicked.connect(self.Open_Settings_Screen)
        self.save_button.clicked.connect(self.initiate_save_settings)
        self.discard_button.clicked.connect(self.discard_settings)
        self.decimalPoints_slider.valueChanged.connect(self.update_clipboard_num_display)
        self.clipboard_checkbox.stateChanged.connect(self.toggle_clipboard_settings)
        self.undoButton.clicked.connect(lambda: self.history("undo"))
        self.redoButton.clicked.connect(lambda: self.history("redo"))

    #-------------------------------- Shortcuts -------------------------------------


        self.undoButton.setShortcut(QKeySequence("Ctrl+Z"))
        self.redoButton.setShortcut(QKeySequence("Ctrl+Y"))
        self.button_0.setShortcut(Qt.Key_0)
        self.button_1.setShortcut(Qt.Key_1)
        self.button_2.setShortcut(Qt.Key_2)
        self.button_3.setShortcut(Qt.Key_3)
        self.button_4.setShortcut(Qt.Key_4)
        self.button_5.setShortcut(Qt.Key_5)
        self.button_6.setShortcut(Qt.Key_6)
        self.button_7.setShortcut(Qt.Key_7)
        self.button_8.setShortcut(Qt.Key_8)
        self.button_9.setShortcut(Qt.Key_9)
        self.button_ans.setShortcut(Qt.Key_A)
        self.button_plus.setShortcut(Qt.Key_Plus)
        self.button_minus.setShortcut(Qt.Key_Minus)
        self.button_mult.setShortcut(Qt.Key_Asterisk)
        self.button_div.setShortcut(Qt.Key_Slash)
        self.button_dot.setShortcut(Qt.Key_Period)
        self.button_openPar.setShortcut(Qt.Key_ParenLeft)
        self.button_closePar.setShortcut(Qt.Key_ParenRight)
        self.button_equals.setShortcut(Qt.Key_Return)
        self.button_clear.setShortcut(Qt.Key_Delete)
        self.button_backspace.setShortcut(Qt.Key_Backspace)
        self.button_percent.setShortcut(Qt.Key_Percent)

        # set keyPressEvent to current widgets that we'd like it to be overridden
        self.centralwidget.keyPressEvent = self.keyPressEvent
        self.screenOutput.keyPressEvent = self.keyPressEvent
    #--------------------------------------------------------------------------------------    

    #------------------------------ Tool Tips --------------------------------------------- 

        self.redoButton.setToolTip("Redo (Ctrl+Y)")
        self.undoButton.setToolTip("Undo (Ctrl+Z)")
        self.button_clear.setToolTip("Clear (Del)")
        self.button_backspace.setToolTip("Backspace")
        self.button_ans.setToolTip("Previous Answer (A)")

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
                self.button_equals.animateClick()
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
        global placeholderThere
        if(self.bl.last_equal):
                self.clear_results()
        newCursorPos = self.bl.button_click(userClick,self.screenOutput.cursorPosition(), not self.screenOutput.hasFocus())
        placeholderThere = False
        self.update_screen()
        self.screenOutput.setCursorPosition(newCursorPos)
        self.button_equals.setFocus()
        self.undoButton.setEnabled(True)
        self.redoButton.setEnabled(False)
        return
    
    def update_screen(self):
        global placeholderThere
        self.screenOutput.setText(self.bl.math_equation)
        
        if self.bl.math_equation == "":
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
        self.bl.button_clear_click()
        self.update_screen()
        self.update_result_screen()
        self.resultOutput.setText("")
        return

        # clear the results screens
    def clear_results(self):
        self.resultOutput.setText("")
        self.decimalResultOutput.setText("")
        return

        # is this function ever used????
        # another copy paste of the same function?????
    def equal_click(self):
        self.bl.button_equals_click()
        self.update_screen()
        self.update_result_screen()
        return

    def update_result_screen(self):
        global resultStyleChanged
   
        self.bl.button_equals_click()

        if resultStyleChanged:
               self.resultOutput.setStyleSheet("font: 23pt \"calibri\";\n""color: rgb(70, 70, 70);")          # reset the style to large
        
        if len(str((self.bl.sum)))>15:
                self.resultOutput.setStyleSheet("font: 13pt \"calibri\";\n""color: rgb(70, 70, 70);")
                resultStyleChanged = True

        if isinstance(self.bl.sum,int) or isinstance(self.bl.sum,Fraction):
                self.resultOutput.setText("= " + str(self.bl.sum))
                self.decimalResultOutput.setText(self.bl.decimal_sum)
        else:
                self.resultOutput.setText(self.bl.sum)
        return

        # is this function extra (there's another function with the same name)???
    def backspace_click(self):
        newCursorPos = self.bl.button_backspace_click(self.screenOutput.cursorPosition())
        self.update_screen()
        self.resultOutput.setText("")
        self.decimalResultOutput.setText("")
        self.screenOutput.setCursorPosition(newCursorPos)

    def arrow_click(self,direction):
        newCursorPos = self.bl.button_arrow_click(self.screenOutput.cursorPosition(),direction)
        self.screenOutput.setCursorPosition(newCursorPos)    

    def update_screen(self):
        global placeholderThere
        self.screenOutput.setText(self.bl.math_equation)
        if self.bl.math_equation == "":
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
        self.bl.button_clear_click()
        self.update_screen()
        self.update_result_screen()
        self.resultOutput.setText("")
        self.redoButton.setEnabled(False)       # disable redo button
        return

        # clear the results screens
    def clear_results(self):
        self.resultOutput.setText("")
        self.decimalResultOutput.setText("")
        return

    def equal_click(self):
        if self.bl.button_equals_click(self.settings):
                self.undoButton.setEnabled(True)
        self.update_screen()
        self.update_result_screen()
        return

    def update_result_screen(self):
        global resultStyleChanged

        if resultStyleChanged:
               self.resultOutput.setStyleSheet("font: 23pt \"calibri\";\n""color: rgb(70, 70, 70);")          # reset the style to large
        
        if len(str((self.bl.sum)))>15:
                self.resultOutput.setStyleSheet("font: 13pt \"calibri\";\n""color: rgb(70, 70, 70);")
                resultStyleChanged = True

        if isinstance(self.bl.sum,int) or isinstance(self.bl.sum,Fraction) or isinstance(self.bl.sum,float):
                self.resultOutput.setText("= " + str(self.bl.sum))
                self.decimalResultOutput.setText(self.bl.decimal_sum)
        else:
                self.resultOutput.setText(self.bl.sum)
        return

    def backspace_click(self):
        newCursorPos = self.bl.button_backspace_click(self.screenOutput.cursorPosition())
        self.update_screen()
        self.resultOutput.setText("")
        self.decimalResultOutput.setText("")
        self.screenOutput.setCursorPosition(newCursorPos)
        if self.bl.math_equation == "":
                self.undoButton.setEnabled(False)

    def question_msgbox(self, title, msg, width):
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


        self.msg.setWindowTitle(title)
        self.msg.setText(msg)
        self.msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        self.msg.setStyleSheet(width)
        self.msg.setWindowIcon(QtGui.QIcon("icons/CalculatorLogo(150p)_1.0.0.ico"))

        if self.msg.exec_() == QMessageBox.Ok:
                return True

        else: 
                return False


    def check_for_updates(self):
        if self.bl.have_internet():
                self.initiate_update_proccess()    

    def initiate_update_proccess(self):
        print("check for updates")
        if checkForUpdates():
                self.request_update_permission()

    def request_update_permission(self):
        title = "  Software Update"
        msg = "A software update is available.<br>Do you want to update now?<br>"
        width = "QLabel{min-width: 200px;}"
        if self.question_msgbox(title, msg, width):
                Dlg = UpdatingDlgBox(self)
                Dlg.UpdatingDlgProgressBar.setValue(0)
                self.start_update_proccess(Dlg)
                Dlg.exec()

    def start_update_proccess(self, dlg):
        # Create a QThread object
        self.thread = QThread()
        self.download_thread = DownloadThread(dlg)
        # Move worker to the thread
        self.download_thread.moveToThread(self.thread)
        # Connect signals and slots
        self.thread.started.connect(self.download_thread.run)
        self.download_thread.finished.connect(self.close_program)
        self.download_thread.finished.connect(self.thread.quit)
        self.download_thread.finished.connect(self.download_thread.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # Start the thread
        self.thread.start()

    def close_program(self):
        MainWindow.close()

    def showUpdatingDlgBox(self):
        Dlg = UpdatingDlgBox(self)
        Dlg.exec()

    def Handle_Progress(dlg, blocknum, blocksize, totalsize):
        ## calculate the progress
        readed_data = blocknum * blocksize
 
        if totalsize > 0:
            download_percentage = readed_data * 100 / totalsize
            dlg.progressBar.setValue(download_percentage)
            QApplication.processEvents() 

    def Open_Settings_Screen(self):
            self.settings = retrieveSettings() 
            self.display_saved_settings()
            self.stackedWidget.setCurrentIndex(1)

    def display_saved_settings(self):
        self.zoom_comboBox.setCurrentText(self.bl.decimal_to_percent(self.settings.get("HR-Display")))
            
        if self.settings.get("CopyToClipboard"):
                self.clipboard_checkbox.setChecked(True)
                self.decimalPoints_slider.setValue(self.settings.get("decimalsToCopy"))
        else:
                self.decimalPoints_slider.setEnabled(False)

        if self.settings.get("display_as_fraction"):
                self.display_fraction_radio_button.setChecked(True)
        else:
                self.display_decimal_radio_button.setChecked(True)  
        
    def update_clipboard_num_display(self):
            num = self.decimalPoints_slider.value()
            self.clipboardDecimalPointDisplay.setText(str(num))

    def initiate_save_settings(self):
        if self.restart_needed():
                self.restart()
        else:
                self.stackedWidget.setCurrentIndex(0)  
                self.save_settings()

    def save_settings(self): 
        self.copy_settings_from_gui()
        saveSettingsToFile(self.settings)  
           
    def discard_settings(self):
            self.stackedWidget.setCurrentIndex(0) 

    def copy_settings_from_gui(self):
        self.settings["HR-Display"] = self.bl.percent_to_decimal(self.zoom_comboBox.currentText())

        if self.clipboard_checkbox.isChecked():
                self.settings["CopyToClipboard"] = True
        else:
                self.settings["CopyToClipboard"] = False
        self.settings["decimalsToCopy"] = self.decimalPoints_slider.value()

        if self.display_fraction_radio_button.isChecked():
                self.settings["display_as_fraction"] = True
        else:
                self.settings["display_as_fraction"] = False

    def toggle_clipboard_settings(self):
        if self.clipboard_checkbox.isChecked():
                self.decimalPoints_slider.setEnabled(True)
                self.clipboardDecimalPointDisplay.setEnabled(True)
                self.decimalPoints_label.setEnabled(True)
                self.clipboard_checkbox.setText("Enabled")
        else:
                self.decimalPoints_slider.setEnabled(False)
                self.clipboardDecimalPointDisplay.setEnabled(False)
                self.decimalPoints_label.setEnabled(False)
                self.clipboard_checkbox.setText("Disabled")

    def history(self, value):
        global placeholderThere
        self.bl.handle_history(value)
        if value == "undo":
                self.redoButton.setEnabled(True)
        # disable undo and redo buttons when opened
        if len(self.bl.undo_stack) < 2:
                self.undoButton.setEnabled(False)
        else:
                self.undoButton.setEnabled(True)
                placeholderThere = False
        if not self.bl.redo_stack:
                self.redoButton.setEnabled(False)
        else:
                self.redoButton.setEnabled(True) 
        self.update_screen()
        self.clear_results()

    def restart(self):
        title = "  Restart Needed"
        msg = "Sagy Calculator must be restarted to see changes.<br>Do you want to retart now?<br>"
        width = "QLabel{min-width: 270px;}"
        if self.question_msgbox(title, msg, width):
                self.save_settings()
                os.execl(sys.executable, f'"{sys.executable}"', *sys.argv)
        else:
                self.zoom_comboBox.setCurrentText(self.bl.decimal_to_percent(self.settings.get("HR-Display")))
                self.save_settings()

    def restart_needed(self):
        return self.settings["HR-Display"] != self.bl.percent_to_decimal(self.zoom_comboBox.currentText())

class UpdatingDlgBox(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/UpdatingDlgBox.ui", self)
        icon = QtGui.QIcon("icons/CalculatorLogo(150p)_1.0.0.ico")
        self.setWindowIcon(icon)
#--------------------------------------------------------------------------------------

#--------------------------------- Main Program ---------------------------------------
if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = mainControl(MainWindow)

    MainWindow.show()

    ui.check_for_updates()

    sys.exit(app.exec_())
#--------------------------------------------------------------------------------------