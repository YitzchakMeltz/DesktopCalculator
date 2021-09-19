from PyQt5.QtCore import QObject, QThread, pyqtSignal
from updateProgramCode140 import updateCalc
import updateProgramCode140
import atexit, sys, os

# Create a worker class
class DownloadThread(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        """Long-running task."""
        updateProgramCode140.updateCalc()
        installer = os.path.join('C:\ProgramData\SasyOwl\SagyCalculator','Updates',
                                'SagyCalculatorSetup.exe')
        atexit.register(os.execl, installer, installer)
        self.finished.emit()