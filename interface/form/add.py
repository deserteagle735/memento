# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(400, 440)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resource/icon/memento.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("font: 12pt \"SF Pro Display\";")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_37 = QtWidgets.QLabel(Dialog)
        self.label_37.setObjectName("label_37")
        self.gridLayout_11.addWidget(self.label_37, 0, 1, 1, 1)
        self.label_39 = QtWidgets.QLabel(Dialog)
        self.label_39.setObjectName("label_39")
        self.gridLayout_11.addWidget(self.label_39, 2, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(Dialog)
        self.label_36.setObjectName("label_36")
        self.gridLayout_11.addWidget(self.label_36, 0, 0, 1, 1)
        self.picture = QtWidgets.QLabel(Dialog)
        self.picture.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.picture.setText("")
        self.picture.setScaledContents(False)
        self.picture.setAlignment(QtCore.Qt.AlignCenter)
        self.picture.setObjectName("picture")
        self.gridLayout_11.addWidget(self.picture, 7, 0, 1, 1)
        self.text_vocabulary = QtWidgets.QLineEdit(Dialog)
        self.text_vocabulary.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;")
        self.text_vocabulary.setObjectName("text_vocabulary")
        self.gridLayout_11.addWidget(self.text_vocabulary, 1, 0, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.widget_12 = QtWidgets.QWidget(Dialog)
        self.widget_12.setObjectName("widget_12")
        self.label_53 = QtWidgets.QLabel(self.widget_12)
        self.label_53.setEnabled(False)
        self.label_53.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.label_53.setText("")
        self.label_53.setPixmap(QtGui.QPixmap("../resource/speaker.png"))
        self.label_53.setObjectName("label_53")
        self.gridLayout_12.addWidget(self.widget_12, 7, 1, 1, 1)
        self.button_delete_picture = QtWidgets.QPushButton(Dialog)
        self.button_delete_picture.setEnabled(False)
        self.button_delete_picture.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.button_delete_picture.setAutoDefault(False)
        self.button_delete_picture.setObjectName("button_delete_picture")
        self.gridLayout_12.addWidget(self.button_delete_picture, 3, 1, 1, 1)
        self.button_delete_record = QtWidgets.QPushButton(Dialog)
        self.button_delete_record.setEnabled(False)
        self.button_delete_record.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.button_delete_record.setAutoDefault(False)
        self.button_delete_record.setObjectName("button_delete_record")
        self.gridLayout_12.addWidget(self.button_delete_record, 6, 1, 1, 1)
        self.button_record = QtWidgets.QPushButton(Dialog)
        self.button_record.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.button_record.setAutoDefault(False)
        self.button_record.setFlat(False)
        self.button_record.setObjectName("button_record")
        self.gridLayout_12.addWidget(self.button_record, 6, 0, 1, 1)
        self.button_play_record = QtWidgets.QPushButton(Dialog)
        self.button_play_record.setEnabled(False)
        self.button_play_record.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.button_play_record.setAutoDefault(False)
        self.button_play_record.setFlat(False)
        self.button_play_record.setObjectName("button_play_record")
        self.gridLayout_12.addWidget(self.button_play_record, 7, 0, 1, 1)
        self.label_52 = QtWidgets.QLabel(Dialog)
        self.label_52.setObjectName("label_52")
        self.gridLayout_12.addWidget(self.label_52, 5, 0, 1, 1)
        self.label_51 = QtWidgets.QLabel(Dialog)
        self.label_51.setObjectName("label_51")
        self.gridLayout_12.addWidget(self.label_51, 2, 0, 1, 2)
        self.button_choose_picture = QtWidgets.QPushButton(Dialog)
        self.button_choose_picture.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.button_choose_picture.setAutoDefault(False)
        self.button_choose_picture.setObjectName("button_choose_picture")
        self.gridLayout_12.addWidget(self.button_choose_picture, 3, 0, 1, 1)
        self.text_tag = QtWidgets.QLineEdit(Dialog)
        self.text_tag.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;")
        self.text_tag.setObjectName("text_tag")
        self.gridLayout_12.addWidget(self.text_tag, 1, 0, 1, 2)
        self.label_54 = QtWidgets.QLabel(Dialog)
        self.label_54.setObjectName("label_54")
        self.gridLayout_12.addWidget(self.label_54, 0, 0, 1, 2)
        self.gridLayout_11.addLayout(self.gridLayout_12, 7, 1, 1, 1)
        self.text_hint = QtWidgets.QLineEdit(Dialog)
        self.text_hint.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;")
        self.text_hint.setObjectName("text_hint")
        self.gridLayout_11.addWidget(self.text_hint, 3, 1, 1, 1)
        self.label_38 = QtWidgets.QLabel(Dialog)
        self.label_38.setObjectName("label_38")
        self.gridLayout_11.addWidget(self.label_38, 2, 1, 1, 1)
        self.combobox_category = QtWidgets.QComboBox(Dialog)
        self.combobox_category.setStyleSheet("QComboBox{border: 2px solid gray;\n"
"border-radius:10px; \n"
"padding: 1px 18px 1px 3px;\n"
"min-width: 6em;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 10px; \n"
"    border-bottom-right-radius: 10px;\n"
"}\n"
"QComboBox::down-arrow{image: url(:/resource/drop-down-arrow.png);}")
        self.combobox_category.setObjectName("combobox_category")
        self.combobox_category.addItem("")
        self.combobox_category.addItem("")
        self.combobox_category.addItem("")
        self.combobox_category.addItem("")
        self.combobox_category.addItem("")
        self.combobox_category.addItem("")
        self.combobox_category.addItem("")
        self.combobox_category.addItem("")
        self.combobox_category.addItem("")
        self.gridLayout_11.addWidget(self.combobox_category, 1, 1, 1, 1)
        self.text_phonetic = QtWidgets.QLineEdit(Dialog)
        self.text_phonetic.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;")
        self.text_phonetic.setObjectName("text_phonetic")
        self.gridLayout_11.addWidget(self.text_phonetic, 3, 0, 1, 1)
        self.label_40 = QtWidgets.QLabel(Dialog)
        self.label_40.setObjectName("label_40")
        self.gridLayout_11.addWidget(self.label_40, 5, 0, 1, 1)
        self.text_definition = QtWidgets.QLineEdit(Dialog)
        self.text_definition.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;")
        self.text_definition.setObjectName("text_definition")
        self.gridLayout_11.addWidget(self.text_definition, 6, 0, 1, 2)
        self.verticalLayout_4.addLayout(self.gridLayout_11)
        self.widget_3 = QtWidgets.QWidget(Dialog)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_13.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.button_add = QtWidgets.QPushButton(self.widget_3)
        self.button_add.setStyleSheet("border-radius:10px;\n"
"border:2px solid #3f8cc8;\n"
"padding: 0 8px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.494, y1:0.989, x2:0.494, y2:0.011, stop:0.863158 rgba(23, 132, 255, 250), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.button_add.setAutoDefault(False)
        self.button_add.setFlat(False)
        self.button_add.setObjectName("button_add")
        self.gridLayout_13.addWidget(self.button_add, 0, 3, 1, 1)
        self.widget_11 = QtWidgets.QWidget(self.widget_3)
        self.widget_11.setObjectName("widget_11")
        self.gridLayout_13.addWidget(self.widget_11, 0, 2, 1, 1)
        self.button_history = QtWidgets.QPushButton(self.widget_3)
        self.button_history.setEnabled(False)
        self.button_history.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.button_history.setAutoDefault(False)
        self.button_history.setObjectName("button_history")
        self.gridLayout_13.addWidget(self.button_history, 0, 1, 1, 1)
        self.button_exit = QtWidgets.QPushButton(self.widget_3)
        self.button_exit.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.button_exit.setAutoDefault(False)
        self.button_exit.setObjectName("button_exit")
        self.gridLayout_13.addWidget(self.button_exit, 0, 4, 1, 1)
        self.verticalLayout_4.addWidget(self.widget_3)
        self.label_37.setBuddy(self.combobox_category)
        self.label_39.setBuddy(self.text_phonetic)
        self.label_36.setBuddy(self.text_vocabulary)
        self.label_52.setBuddy(self.button_record)
        self.label_51.setBuddy(self.button_choose_picture)
        self.label_54.setBuddy(self.text_tag)
        self.label_38.setBuddy(self.text_hint)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.text_vocabulary, self.combobox_category)
        Dialog.setTabOrder(self.combobox_category, self.text_phonetic)
        Dialog.setTabOrder(self.text_phonetic, self.text_hint)
        Dialog.setTabOrder(self.text_hint, self.text_definition)
        Dialog.setTabOrder(self.text_definition, self.text_tag)
        Dialog.setTabOrder(self.text_tag, self.button_choose_picture)
        Dialog.setTabOrder(self.button_choose_picture, self.button_delete_picture)
        Dialog.setTabOrder(self.button_delete_picture, self.button_record)
        Dialog.setTabOrder(self.button_record, self.button_play_record)
        Dialog.setTabOrder(self.button_play_record, self.button_delete_record)
        Dialog.setTabOrder(self.button_delete_record, self.button_add)
        Dialog.setTabOrder(self.button_add, self.button_exit)
        Dialog.setTabOrder(self.button_exit, self.button_history)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Thêm từ mới"))
        self.label_37.setText(_translate("Dialog", "Từ loại"))
        self.label_39.setText(_translate("Dialog", "Phiên âm"))
        self.label_36.setText(_translate("Dialog", "Từ mới"))
        self.button_delete_picture.setText(_translate("Dialog", "Xóa"))
        self.button_delete_record.setText(_translate("Dialog", "Xóa"))
        self.button_record.setText(_translate("Dialog", "Bắt đầu"))
        self.button_play_record.setText(_translate("Dialog", "Nghe lại"))
        self.label_52.setText(_translate("Dialog", "Ghi âm"))
        self.label_51.setText(_translate("Dialog", "Hình ảnh gợi ý"))
        self.button_choose_picture.setText(_translate("Dialog", "Chọn ảnh"))
        self.label_54.setText(_translate("Dialog", "Gắn thẻ"))
        self.label_38.setText(_translate("Dialog", "Gợi ý"))
        self.combobox_category.setItemText(0, _translate("Dialog", "chưa xác định"))
        self.combobox_category.setItemText(1, _translate("Dialog", "n - danh từ"))
        self.combobox_category.setItemText(2, _translate("Dialog", "v - động từ"))
        self.combobox_category.setItemText(3, _translate("Dialog", "adj - tính từ"))
        self.combobox_category.setItemText(4, _translate("Dialog", "adv - trạng từ"))
        self.combobox_category.setItemText(5, _translate("Dialog", "np - cụm danh từ"))
        self.combobox_category.setItemText(6, _translate("Dialog", "vp - cụm động từ"))
        self.combobox_category.setItemText(7, _translate("Dialog", "idiom - thành ngữ"))
        self.combobox_category.setItemText(8, _translate("Dialog", "clause - mệnh đề"))
        self.label_40.setText(_translate("Dialog", "Dịch nghĩa"))
        self.button_add.setToolTip(_translate("Dialog", "F1"))
        self.button_add.setText(_translate("Dialog", "Thêm"))
        self.button_add.setShortcut(_translate("Dialog", "F1"))
        self.button_history.setToolTip(_translate("Dialog", "F3"))
        self.button_history.setText(_translate("Dialog", "Lịch sử"))
        self.button_history.setShortcut(_translate("Dialog", "F3"))
        self.button_exit.setToolTip(_translate("Dialog", "F2"))
        self.button_exit.setText(_translate("Dialog", "Thoát"))
        self.button_exit.setShortcut(_translate("Dialog", "F2"))
import resource_rc
