from PyQt6 import QtWidgets
from PyQt6.QtCore import QTimer, QFile, QTextStream
from PyQt6.QtWidgets import QSpinBox
from QtMainWindow import Ui_MainWindow
from QtCountdownWindow import Ui_Dialog
import sys
import os

# Tried really hard to use relative file names for easy cross-platform building
# but I was never able to open file to load stylesheets using PyInstaller
# For now, using absolute windows style paths
CountdownWindowStylesPath = r"C:\Code\Python\Scheduled-Shutdown\Styles\CountdownWindow.qss"
MainWindowStylesPath = r"C:\Code\Python\Scheduled-Shutdown\Styles\MainWindow.qss"

class Countdown(QtWidgets.QWidget, Ui_Dialog):
    # Method has to be above _init_ so it exists before object is destroyed
    def stopTimer(self):
        self.timer.stop()
        self.lcdHours.display(0)
        self.lcdMinutes.display(0)
        self.lcdSeconds.display(0)

    def __init__(self, *args, obj = None, **kwargs):
        super(Countdown, self,).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setStyleSheet(getStylesFromPath(CountdownWindowStylesPath))
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateCountdown)
        self.destroyed.connect(self.stopTimer)
        self.remainingtime = -1

    def startTimer(self, time):
        self.remainingtime = time
        self.show()
        self.updateCountdown()
        self.timer.start(1000) # countdown every 1000ms

    def updateCountdown(self):
        if self.remainingtime > 0:
            hours, r = divmod(self.remainingtime, 3600)
            minutes, seconds = divmod(r, 60)
            self.lcdHours.display(hours)
            self.lcdMinutes.display(minutes)
            self.lcdSeconds.display(seconds)
            self.remainingtime -= 1
        elif self.remainingtime == 0: 
            self.stopTimer()
            shutdown()
            self.destroy()

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj = None, **kwargs):
        super(Window, self,).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setStyleSheet(getStylesFromPath(MainWindowStylesPath))
        self.removeSpinButtons()
        self.scheduleButton.clicked.connect(self.scheduleButtonClicked)
        self.countdown = Countdown()

    def removeSpinButtons(self):
        self.hoursInput.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.minutesInput.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)
        self.secondsInput.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)

    def scheduleButtonClicked(self):
        self.startCountdown()

    def startCountdown(self):
        self.countdown.startTimer(timeToSec(self.hoursInput.value(), self.minutesInput.value(), self.secondsInput.value()))

def getStylesFromPath(path):
    stylesheet = QFile(path)
    # Err checking
    if not stylesheet.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
        print(f"Could not open stylesheet: {stylesheet}")
        return
    # open -> read all lines
    stream = QTextStream(stylesheet)
    stylesheet = stream.readAll()
    
    return stylesheet

def timeToSec(h, m, s):
    # 1hr:3600s   |   1min:60s    |    1s:1s
    totalSeconds = ((h * 3600) + (m * 60) + s)
    return totalSeconds

def generateShutdownCommand():
    # Windows specific "Locking" function for testing
    # # return "rundll32.exe user32.dll,LockWorkStation"
    if sys.platform.startswith('win32'):
        return "shutdown -s -t " + str(0)
    elif sys.platform.startswith('linux'):
        return "shutdown -P 0"
    else:
        # Supports Linux and Windows right now
        return ""

def shutdown():
    os.system(generateShutdownCommand())

def main():
    
    # UI
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    if sys.platform.startswith('linux'):
        window.Prompt.setText("Linux Users should run this with su permissions!\n" + window.Prompt.text())
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
