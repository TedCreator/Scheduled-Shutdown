from PyQt6 import QtWidgets
from PyQt6.QtCore import QTimer

from QtMainWindow import Ui_MainWindow
import sys
import os

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
        self.remainingtime = -1

    def scheduleButtonClicked(self):
        if self.scheduleButton.text() == "Schedule":
            self.lcdHour.setHidden(False)
            self.lcdMinute.setHidden(False)
            self.lcdSecond.setHidden(False)
            self.startCountdown()
            if self.remainingtime > 0:
                self.scheduleButton.setText("Reset")
        else:
            self.lcdHour.setHidden(True)
            self.lcdMinute.setHidden(True)
            self.lcdSecond.setHidden(True)
            self.resetCountdown()
            self.scheduleButton.setText("Schedule")

    def startCountdown(self):
        self.remainingtime = timeToSec(self.hoursInput.value(), self.minutesInput.value(), self.secondsInput.value())
        
        self.updateCountdown()

        self.timer.start(1000)
    def resetCountdown(self):
        self.timer.stop()
        self.lcdHour.display(0)
        self.lcdMinute.display(0)
        self.lcdSecond.display(0)
        remainingtime = -1

    def updateCountdown(self):
        if self.remainingtime > 0:
            hours, r = divmod(self.remainingtime, 3600)
            minutes, seconds = divmod(r, 60)
            self.lcdHour.display(hours)
            self.lcdMinute.display(minutes)
            self.lcdSecond.display(seconds)
            self.remainingtime -= 1
        elif self.remainingtime == 0: 
            self.lcdSecond.display(0) # cleans up the display
            # self.shutdown()
            self.timer.stop()
            self.lcdHour.setHidden(True)
            self.lcdMinute.setHidden(True)
            self.lcdSecond.setHidden(True)
            self.scheduleButton.setText("Schedule")
        
    def generateShutdownCommand(self):
        if sys.platform == "win32":
            return "shutdown -s -t " + str(0)
        else:
            return "shutdown -p"

    def shutdown(self):
        # self.logTime()
        os.system(self.generateShutdownCommand())


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