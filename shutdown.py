from PyQt6 import QtWidgets
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QSpinBox
from QtMainWindow import Ui_MainWindow
from QtCountdownWindow import Ui_Dialog
import sys
import os

class Countdown(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self, *args, obj = None, **kwargs):
        super(Countdown, self,).__init__(*args, **kwargs)
        self.setupUi(self)
        

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj = None, **kwargs):
        super(Window, self,).__init__(*args, **kwargs)
        self.setupUi(self)
        self.removeSpinButtons()
        self.scheduleButton.clicked.connect(self.scheduleButtonClicked)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateCountdown)
        self.remainingtime = -1
        self.countdown = Countdown()
        
    def removeSpinButtons(self):
        self.hoursInput.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.minutesInput.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.secondsInput.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
    def scheduleButtonClicked(self):
        if self.scheduleButton.text() == "Schedule":
            self.startCountdown()
            if self.remainingtime > 0:
                self.scheduleButton.setText("Reset")
        else:
            self.resetCountdown()
            self.scheduleButton.setText("Schedule")

    def startCountdown(self):
        self.remainingtime = timeToSec(self.hoursInput.value(), self.minutesInput.value(), self.secondsInput.value())
        self.countdown.show()
        self.updateCountdown()

        self.timer.start(1000)
    def resetCountdown(self):
        self.timer.stop()
        self.countdown.lcdHours.display(0)
        self.countdown.lcdMinutes.display(0)
        self.countdown.lcdSeconds.display(0)
        remainingtime = -1

    def updateCountdown(self):
        if self.remainingtime > 0:
            hours, r = divmod(self.remainingtime, 3600)
            minutes, seconds = divmod(r, 60)
            self.countdown.lcdHours.display(hours)
            self.countdown.lcdMinutes.display(minutes)
            self.countdown.lcdSeconds.display(seconds)
            self.remainingtime -= 1
        elif self.remainingtime == 0: 
            self.countdown.lcdSeconds.display(0) # cleans up the display
            self.timer.stop()
            self.countdown.hide()
            self.scheduleButton.setText("Schedule")
            self.shutdown()
        
    def generateShutdownCommand(self):
        if sys.platform == "win32":
            return "shutdown -s -t " + str(0)
        else:
            return "shutdown -p"

    def shutdown(self):
        os.system(self.generateShutdownCommand())


def timeToSec(h, m, s):
    # 1hr:3600s   |   1min:60s    |    1s:1s
    totalSeconds = ((h * 3600) + (m * 60) + s)
    return totalSeconds

def main():
    # UI
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setStyleSheet("""
                            QWidget { 
                                color: rgb(255, 255, 255);
                                background-color: rgb(0, 0, 0); 
                            }
                            QPushButton { 
                                font-size: 25px;
                                background-color: rgb(20, 20, 20);
                                border-radius: 25px; 
                            }
                         """)
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
