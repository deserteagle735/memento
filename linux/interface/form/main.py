# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(300, 300)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resource/memento.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_logo.setFont(font)
        self.label_logo.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label_logo.setStyleSheet("")
        self.label_logo.setTextFormat(QtCore.Qt.AutoText)
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setWordWrap(False)
        self.label_logo.setObjectName("label_logo")
        self.verticalLayout.addWidget(self.label_logo)
        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("SF Pro Rounded")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_add.setFont(font)
        self.button_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_add.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.button_add.setAutoFillBackground(False)
        self.button_add.setStyleSheet("background-color: rgb(65, 148, 254);\n"
"font: 12pt \"SF Pro Display\";\n"
"font: 12pt \"SF Pro Rounded\";\n"
"color:white;\n"
"border-style:outset;\n"
"border-color:black;\n"
"border-radius:10px;\n"
"padding:6px;\n"
"\n"
"")
        self.button_add.setObjectName("button_add")
        self.verticalLayout.addWidget(self.button_add)
        self.button_test = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_test.setFont(font)
        self.button_test.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_test.setStyleSheet("border-style:outset;\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"SF Pro Display\";\n"
"border-color:black;\n"
"border-radius:10px;\n"
"padding:6px;\n"
"background-color: rgb(65, 148, 254);")
        self.button_test.setObjectName("button_test")
        self.verticalLayout.addWidget(self.button_test)
        self.button_browser = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_browser.setFont(font)
        self.button_browser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_browser.setAutoFillBackground(False)
        self.button_browser.setStyleSheet("font: 12pt \"SF Pro Display\";\n"
"color:white;\n"
"border-style:outset;\n"
"border-color:black;\n"
"border-radius:10px;\n"
"padding:6px;\n"
"\n"
"background-color: rgb(65, 148, 254);")
        self.button_browser.setObjectName("button_browser")
        self.verticalLayout.addWidget(self.button_browser)
        self.button_settings = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.button_settings.setFont(font)
        self.button_settings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_settings.setAcceptDrops(False)
        self.button_settings.setStyleSheet("font: 12pt \"SF Pro Display\";\n"
"color:white;\n"
"border-style:outset;\n"
"border-color:black;\n"
"border-radius:10px;\n"
"padding:6px;\n"
"\n"
"background-color: rgb(65, 148, 254);")
        self.button_settings.setFlat(False)
        self.button_settings.setObjectName("button_settings")
        self.verticalLayout.addWidget(self.button_settings)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Memento"))
        self.label_logo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#4194fe;\">Memento</span></p></body></html>"))
        self.button_add.setToolTip(_translate("MainWindow", "F1"))
        self.button_add.setText(_translate("MainWindow", "Thêm từ"))
        self.button_add.setShortcut(_translate("MainWindow", "F1"))
        self.button_test.setToolTip(_translate("MainWindow", "F2"))
        self.button_test.setText(_translate("MainWindow", "Kiểm tra"))
        self.button_test.setShortcut(_translate("MainWindow", "F2"))
        self.button_browser.setToolTip(_translate("MainWindow", "F3"))
        self.button_browser.setText(_translate("MainWindow", "Danh sách từ"))
        self.button_browser.setShortcut(_translate("MainWindow", "F3"))
        self.button_settings.setToolTip(_translate("MainWindow", "F4"))
        self.button_settings.setText(_translate("MainWindow", "Cài đặt"))
        self.button_settings.setShortcut(_translate("MainWindow", "F4"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
import resource_rc
