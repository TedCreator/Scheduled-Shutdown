# Form implementation generated from reading ui file 'pyqt.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(621, 235)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_11.addItem(spacerItem)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.Prompt = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Prompt.setFont(font)
        self.Prompt.setObjectName("Prompt")
        self.horizontalLayout_8.addWidget(self.Prompt, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_13.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.hoursInput = QtWidgets.QSpinBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hoursInput.sizePolicy().hasHeightForWidth())
        self.hoursInput.setSizePolicy(sizePolicy)
        self.hoursInput.setMaximum(8760)
        self.hoursInput.setObjectName("hoursInput")
        self.horizontalLayout_10.addWidget(self.hoursInput, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.hoursLabel = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hoursLabel.sizePolicy().hasHeightForWidth())
        self.hoursLabel.setSizePolicy(sizePolicy)
        self.hoursLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.hoursLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hoursLabel.setFont(font)
        self.hoursLabel.setObjectName("hoursLabel")
        self.horizontalLayout_10.addWidget(self.hoursLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.minutesInput = QtWidgets.QSpinBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minutesInput.sizePolicy().hasHeightForWidth())
        self.minutesInput.setSizePolicy(sizePolicy)
        self.minutesInput.setMaximum(525600)
        self.minutesInput.setObjectName("minutesInput")
        self.horizontalLayout_10.addWidget(self.minutesInput)
        self.minutesLabel = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minutesLabel.sizePolicy().hasHeightForWidth())
        self.minutesLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.minutesLabel.setFont(font)
        self.minutesLabel.setObjectName("minutesLabel")
        self.horizontalLayout_10.addWidget(self.minutesLabel)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.secondsInput = QtWidgets.QSpinBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.secondsInput.sizePolicy().hasHeightForWidth())
        self.secondsInput.setSizePolicy(sizePolicy)
        self.secondsInput.setMinimum(0)
        self.secondsInput.setMaximum(31536000)
        self.secondsInput.setObjectName("secondsInput")
        self.horizontalLayout_10.addWidget(self.secondsInput)
        self.secondsLabel = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.secondsLabel.sizePolicy().hasHeightForWidth())
        self.secondsLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.secondsLabel.setFont(font)
        self.secondsLabel.setObjectName("secondsLabel")
        self.horizontalLayout_10.addWidget(self.secondsLabel)
        spacerItem4 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.verticalLayout_13.addLayout(self.horizontalLayout_10)
        self.verticalLayout_11.addLayout(self.verticalLayout_13)
        spacerItem5 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_11.addItem(spacerItem5)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.scheduleButton = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scheduleButton.sizePolicy().hasHeightForWidth())
        self.scheduleButton.setSizePolicy(sizePolicy)
        self.scheduleButton.setMinimumSize(QtCore.QSize(300, 50))
        self.scheduleButton.setStyleSheet("background-color: rgb(12, 12, 12);")
        self.scheduleButton.setObjectName("scheduleButton")
        self.horizontalLayout_11.addWidget(self.scheduleButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.verticalLayout_11.addLayout(self.horizontalLayout_11)
        spacerItem8 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.verticalLayout_11.addItem(spacerItem8)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lcdHour = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.lcdHour.setObjectName("lcdHour")
        self.horizontalLayout.addWidget(self.lcdHour, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.lcdMinute = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.lcdMinute.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Filled)
        self.lcdMinute.setObjectName("lcdMinute")
        self.horizontalLayout.addWidget(self.lcdMinute, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.lcdSecond = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.lcdSecond.setObjectName("lcdSecond")
        self.horizontalLayout.addWidget(self.lcdSecond, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_12.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setEnabled(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 621, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Schedule A Shutdown!"))
        self.Prompt.setText(_translate("MainWindow", "Input an amount of time before shutdown occurs:"))
        self.hoursLabel.setText(_translate("MainWindow", "Hours"))
        self.minutesLabel.setText(_translate("MainWindow", "Minutes"))
        self.secondsLabel.setText(_translate("MainWindow", "Seconds"))
        self.scheduleButton.setText(_translate("MainWindow", "Schedule"))