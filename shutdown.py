from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QWidget, QApplication
from QtDesignWindow import Ui_MainWindow
import sys

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj = None, **kwargs):
        super(Window, self,).__init__(*args, **kwargs)
        self.setupUi(self)
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()