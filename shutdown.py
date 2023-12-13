from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QWidget, QApplication
from QtDesignWindow import Ui_MainWindow
import sys




class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj = None, **kwargs):
        super(Window, self,).__init__(*args, **kwargs)
        self.setupUi(self)
        self.scheduleButton.clicked.connect(self.timeToSec)

    def timeToSec(self):
        # 1hr:3600s   |   1min:60s    |    1s:1s
        totalSec = (self.hoursInput.value() * 3600) + (self.minutesInput.value() * 60) + self.secondsInput.value()
        print(totalSec)
        return totalSec
    

    
    
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()