from PySide6.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
       super().__init__()
       self.resize(960, 720)

    
    def closeEvent(self, event):
        event.accept()
