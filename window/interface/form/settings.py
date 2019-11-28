# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.setEnabled(True)
        Dialog.resize(400, 398)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(12)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resource/memento.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab = QtWidgets.QTabWidget(Dialog)
        self.tab.setObjectName("tab")
        self.test = QtWidgets.QWidget()
        self.test.setObjectName("test")
        self.gridLayout = QtWidgets.QGridLayout(self.test)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(167, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(167, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.test)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.combobox_field = QtWidgets.QComboBox(self.test)
        self.combobox_field.setObjectName("combobox_field")
        self.combobox_field.addItem("")
        self.combobox_field.addItem("")
        self.combobox_field.addItem("")
        self.gridLayout.addWidget(self.combobox_field, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.test)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.test)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(167, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.test)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 6, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.test)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.spinbox_test_level = QtWidgets.QSpinBox(self.test)
        self.spinbox_test_level.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinbox_test_level.setMinimum(1)
        self.spinbox_test_level.setMaximum(7)
        self.spinbox_test_level.setObjectName("spinbox_test_level")
        self.gridLayout.addWidget(self.spinbox_test_level, 1, 1, 1, 1)
        self.spinbox_hint_level = QtWidgets.QSpinBox(self.test)
        self.spinbox_hint_level.setMinimum(1)
        self.spinbox_hint_level.setMaximum(4)
        self.spinbox_hint_level.setObjectName("spinbox_hint_level")
        self.gridLayout.addWidget(self.spinbox_hint_level, 2, 1, 1, 1)
        self.spinbox_number_of_word = QtWidgets.QSpinBox(self.test)
        self.spinbox_number_of_word.setMinimum(1)
        self.spinbox_number_of_word.setMaximum(50)
        self.spinbox_number_of_word.setObjectName("spinbox_number_of_word")
        self.gridLayout.addWidget(self.spinbox_number_of_word, 4, 1, 1, 1)
        self.tab.addTab(self.test, "")
        self.data = QtWidgets.QWidget()
        self.data.setObjectName("data")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.data)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.data)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(13, 22, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.data)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 1, 1, 1)
        self.spinbox_old_level = QtWidgets.QSpinBox(self.data)
        self.spinbox_old_level.setMaximum(4)
        self.spinbox_old_level.setObjectName("spinbox_old_level")
        self.gridLayout_3.addWidget(self.spinbox_old_level, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(13, 22, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.data)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 1, 1, 1)
        self.spinbox_new_level = QtWidgets.QSpinBox(self.data)
        self.spinbox_new_level.setMaximum(4)
        self.spinbox_new_level.setObjectName("spinbox_new_level")
        self.gridLayout_3.addWidget(self.spinbox_new_level, 1, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 1, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem7 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.button_reset = QtWidgets.QPushButton(self.data)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.button_reset.setFont(font)
        self.button_reset.setStyleSheet("QPushButton{border-radius:10px;\n"
"border:1px solid gray;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"border: 1px solid #006080;\n"
"}")
        self.button_reset.setObjectName("button_reset")
        self.horizontalLayout.addWidget(self.button_reset)
        spacerItem8 = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem9 = QtWidgets.QSpacerItem(20, 217, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem9)
        self.tab.addTab(self.data, "")
        self.verticalLayout.addWidget(self.tab)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        self.button_cancel = QtWidgets.QPushButton(Dialog)
        self.button_cancel.setStyleSheet("QPushButton{border-radius:10px;\n"
"border:1px solid gray;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"border: 1px solid #006080;\n"
"}")
        self.button_cancel.setAutoDefault(True)
        self.button_cancel.setDefault(True)
        self.button_cancel.setObjectName("button_cancel")
        self.gridLayout_2.addWidget(self.button_cancel, 0, 2, 1, 1)
        self.button_save = QtWidgets.QPushButton(Dialog)
        self.button_save.setStyleSheet("QPushButton{border-radius:10px;\n"
"border:1px solid #3f8cc8;\n"
"padding: 0 8px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.494, y1:0.989, x2:0.494, y2:0.011, stop:0.863158 rgba(23, 132, 255, 250), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:focus{\n"
"border: 1px solid rgb(0, 255, 255);\n"
"}\n"
"QPushButton:disabled{\n"
"background-color: rgb(195, 203, 218);\n"
"border:1px solid rgb(195, 203, 218);\n"
"}")
        self.button_save.setAutoDefault(True)
        self.button_save.setDefault(False)
        self.button_save.setObjectName("button_save")
        self.gridLayout_2.addWidget(self.button_save, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)

        self.retranslateUi(Dialog)
        self.tab.setCurrentIndex(0)
        self.label.linkHovered['QString'].connect(self.combobox_field.setCurrentText)
        self.label_2.linkHovered['QString'].connect(self.spinbox_test_level.selectAll)
        self.label_3.linkHovered['QString'].connect(self.spinbox_hint_level.selectAll)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.tab, self.combobox_field)
        Dialog.setTabOrder(self.combobox_field, self.spinbox_test_level)
        Dialog.setTabOrder(self.spinbox_test_level, self.spinbox_hint_level)
        Dialog.setTabOrder(self.spinbox_hint_level, self.spinbox_number_of_word)
        Dialog.setTabOrder(self.spinbox_number_of_word, self.textBrowser)
        Dialog.setTabOrder(self.textBrowser, self.button_save)
        Dialog.setTabOrder(self.button_save, self.button_cancel)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cài đặt"))
        self.label_3.setText(_translate("Dialog", "Mức độ gợi ý"))
        self.combobox_field.setItemText(0, _translate("Dialog", "Tất cả"))
        self.combobox_field.setItemText(1, _translate("Dialog", "Thẻ"))
        self.combobox_field.setItemText(2, _translate("Dialog", "Thêm hôm nay"))
        self.label_2.setText(_translate("Dialog", "Mức độ câu hỏi"))
        self.label_4.setText(_translate("Dialog", "Số lượng từ mỗi lần"))
        self.label.setText(_translate("Dialog", "Tìm từ theo"))
        self.tab.setTabText(self.tab.indexOf(self.test), _translate("Dialog", "Kiểm tra"))
        self.label_5.setText(_translate("Dialog", "Đặt lại trình độ cho các từ:"))
        self.label_6.setText(_translate("Dialog", "Trình độ cũ"))
        self.label_7.setText(_translate("Dialog", "Trình độ mới"))
        self.button_reset.setText(_translate("Dialog", "Đặt lại"))
        self.tab.setTabText(self.tab.indexOf(self.data), _translate("Dialog", "Dữ liệu"))
        self.button_cancel.setToolTip(_translate("Dialog", "Esc"))
        self.button_cancel.setText(_translate("Dialog", "Hủy"))
        self.button_cancel.setShortcut(_translate("Dialog", "Esc"))
        self.button_save.setToolTip(_translate("Dialog", "Ctrl+S"))
        self.button_save.setText(_translate("Dialog", "Lưu"))
        self.button_save.setShortcut(_translate("Dialog", "Ctrl+S"))
import resource_rc
