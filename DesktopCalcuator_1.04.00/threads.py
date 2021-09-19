from PyQt5.QtCore import QObject, QThread, pyqtSignal
from updateProgramCode140 import updateCalc
import updateProgramCode140
import time

# Create a worker class
class DownloadThread(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        """Long-running task."""
        updateProgramCode140.updateCalc()
        self.finished.emit()