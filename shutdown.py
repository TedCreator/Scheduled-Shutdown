from PyQt6 import QtWidgets, uic, QtCore
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtCore import QTimer

from QtMainWindow import Ui_MainWindow
import sys
import os
import time
import datetime

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj = None, **kwargs):
        super(Window, self,).__init__(*args, **kwargs)
        self.setupUi(self)
        # self.lcdHour.setHidden(True)
        # self.lcdMinute.setHidden(True)
        # self.lcdSecond.setHidden(True)
        self.scheduleButton.clicked.connect(self.scheduleButtonClicked)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateCountdown)
        self.remainingtime = 0

    def scheduleButtonClicked(self):
        self.shutdown(timeToSec(self.hoursInput.value(), self.minutesInput.value(), self.secondsInput.value()))
        self.lcdHour.setHidden(False)
        self.lcdMinute.setHidden(False)
        self.lcdSecond.setHidden(False)
        self.startCountdown()
        # self.updateCountdown(self.hoursInput.value(),self.minutesInput.value(),self.secondsInput.value())

    def startCountdown(self):
        self.remainingtime = timeToSec(self.hoursInput.value(), self.minutesInput.value(), self.secondsInput.value())
        
        self.updateCountdown()

        self.timer.start(1000)

    def updateCountdown(self):
        if self.remainingtime > 0:
            hours, r = divmod(self.remainingtime, 3600)
            minutes, seconds = divmod(r, 60)
            self.lcdHour.display(hours)
            self.lcdMinute.display(minutes)
            self.lcdSecond.display(seconds)
            self.remainingtime -= 1
        else: 
            self.timer.stop()
        
    def shutdown(self, seconds):
        # May transfer this to be a headless python internal counter instead of an OS command
        command = "shutdown -s -t " + str(seconds) + " -c " + "\"" + str(seconds) + "\""
        print(command)
        # self.logTime()
        err = os.system(command)
        if(err == 1190):
            # Shutdown Abort
            os.system("shutdown -a")


def timeToSec(h, m, s):
    # 1hr:3600s   |   1min:60s    |    1s:1s
    totalSeconds = ((h * 3600) + (m * 60) + s)
    return totalSeconds


def logTime():
    print("Log")

def main():
    # UI
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()