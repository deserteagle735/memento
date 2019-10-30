# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 460)
        Dialog.setMinimumSize(QtCore.QSize(900, 460))
        Dialog.setMaximumSize(QtCore.QSize(16777215, 11111111))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(12)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resource/icon/memento.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("font: 12pt \"SF Pro Display\";")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(11, 10, 878, 445))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.text_search_box = QtWidgets.QLineEdit(self.layoutWidget)
        self.text_search_box.setMinimumSize(QtCore.QSize(430, 0))
        self.text_search_box.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;")
        self.text_search_box.setObjectName("text_search_box")
        self.gridLayout.addWidget(self.text_search_box, 1, 1, 1, 1)
        self.button_search = QtWidgets.QPushButton(self.layoutWidget)
        self.button_search.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resource/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_search.setIcon(icon1)
        self.button_search.setObjectName("button_search")
        self.gridLayout.addWidget(self.button_search, 1, 2, 1, 1)
        self.comboBox_field = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_field.setStyleSheet("QComboBox{border: 2px solid gray;\n"
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
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow{image: url(:/resource/drop-down-arrow.png);}\n"
"\n"
"")
        self.comboBox_field.setObjectName("comboBox_field")
        self.comboBox_field.addItem("")
        self.comboBox_field.addItem("")
        self.comboBox_field.addItem("")
        self.comboBox_field.addItem("")
        self.gridLayout.addWidget(self.comboBox_field, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.editor = QtWidgets.QGroupBox(self.splitter)
        self.editor.setTitle("")
        self.editor.setFlat(False)
        self.editor.setObjectName("editor")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.editor)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.combobox_category = QtWidgets.QComboBox(self.editor)
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
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QComboBox::down-arrow{image: url(:/resource/drop-down-arrow.png);}\n"
"\n"
"")
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
        self.text_phonetic = QtWidgets.QLineEdit(self.editor)
        self.text_phonetic.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;")
        self.text_phonetic.setObjectName("text_phonetic")
        self.gridLayout_11.addWidget(self.text_phonetic, 3, 0, 1, 1)
        self.text_hint = QtWidgets.QLineEdit(self.editor)
        self.text_hint.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;")
        self.text_hint.setObjectName("text_hint")
        self.gridLayout_11.addWidget(self.text_hint, 3, 1, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.editor)
        self.label_38.setObjectName("label_38")
        self.gridLayout_11.addWidget(self.label_38, 2, 1, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.widget_12 = QtWidgets.QWidget(self.editor)
        self.widget_12.setObjectName("widget_12")
        self.label_53 = QtWidgets.QLabel(self.widget_12)
        self.label_53.setEnabled(False)
        self.label_53.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.label_53.setText("")
        self.label_53.setPixmap(QtGui.QPixmap("../resource/speaker.png"))
        self.label_53.setObjectName("label_53")
        self.gridLayout_12.addWidget(self.widget_12, 5, 1, 1, 1)
        self.button_delete_picture = QtWidgets.QPushButton(self.editor)
        self.button_delete_picture.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.button_delete_picture.setObjectName("button_delete_picture")
        self.gridLayout_12.addWidget(self.button_delete_picture, 1, 1, 1, 1)
        self.button_delete_record = QtWidgets.QPushButton(self.editor)
        self.button_delete_record.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.button_delete_record.setObjectName("button_delete_record")
        self.gridLayout_12.addWidget(self.button_delete_record, 4, 1, 1, 1)
        self.button_record = QtWidgets.QPushButton(self.editor)
        self.button_record.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.button_record.setObjectName("button_record")
        self.gridLayout_12.addWidget(self.button_record, 4, 0, 1, 1)
        self.button_play_record = QtWidgets.QPushButton(self.editor)
        self.button_play_record.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.button_play_record.setObjectName("button_play_record")
        self.gridLayout_12.addWidget(self.button_play_record, 5, 0, 1, 1)
        self.label_52 = QtWidgets.QLabel(self.editor)
        self.label_52.setObjectName("label_52")
        self.gridLayout_12.addWidget(self.label_52, 3, 0, 1, 1)
        self.text_tag = QtWidgets.QLineEdit(self.editor)
        self.text_tag.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;")
        self.text_tag.setObjectName("text_tag")
        self.gridLayout_12.addWidget(self.text_tag, 7, 0, 1, 2)
        self.label_51 = QtWidgets.QLabel(self.editor)
        self.label_51.setObjectName("label_51")
        self.gridLayout_12.addWidget(self.label_51, 0, 0, 1, 2)
        self.label_54 = QtWidgets.QLabel(self.editor)
        self.label_54.setObjectName("label_54")
        self.gridLayout_12.addWidget(self.label_54, 6, 0, 1, 2)
        self.button_choose_picture = QtWidgets.QPushButton(self.editor)
        self.button_choose_picture.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.button_choose_picture.setObjectName("button_choose_picture")
        self.gridLayout_12.addWidget(self.button_choose_picture, 1, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_12, 7, 1, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.editor)
        self.label_37.setObjectName("label_37")
        self.gridLayout_11.addWidget(self.label_37, 0, 1, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.editor)
        self.label_39.setObjectName("label_39")
        self.gridLayout_11.addWidget(self.label_39, 2, 0, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.editor)
        self.label_40.setObjectName("label_40")
        self.gridLayout_11.addWidget(self.label_40, 5, 0, 1, 1)
        self.text_definition = QtWidgets.QLineEdit(self.editor)
        self.text_definition.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;")
        self.text_definition.setObjectName("text_definition")
        self.gridLayout_11.addWidget(self.text_definition, 6, 0, 1, 2)
        self.label_36 = QtWidgets.QLabel(self.editor)
        self.label_36.setObjectName("label_36")
        self.gridLayout_11.addWidget(self.label_36, 0, 0, 1, 1)
        self.picture = QtWidgets.QLabel(self.editor)
        self.picture.setText("")
        self.picture.setObjectName("picture")
        self.gridLayout_11.addWidget(self.picture, 7, 0, 1, 1)
        self.text_vocalubary = QtWidgets.QLineEdit(self.editor)
        self.text_vocalubary.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;")
        self.text_vocalubary.setObjectName("text_vocalubary")
        self.gridLayout_11.addWidget(self.text_vocalubary, 1, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.editor)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_13.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.butto_discard = QtWidgets.QPushButton(self.widget_3)
        self.butto_discard.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.butto_discard.setObjectName("butto_discard")
        self.gridLayout_13.addWidget(self.butto_discard, 0, 4, 1, 1)
        self.button_delete = QtWidgets.QPushButton(self.widget_3)
        self.button_delete.setStyleSheet("border-radius:10px;\n"
"border:2px solid gray;\n"
"padding: 0 8px;\n"
" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);")
        self.button_delete.setObjectName("button_delete")
        self.gridLayout_13.addWidget(self.button_delete, 0, 1, 1, 1)
        self.button_save = QtWidgets.QPushButton(self.widget_3)
        self.button_save.setStyleSheet("border-radius:10px;\n"
"border:2px solid #3f8cc8;\n"
"padding: 0 8px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.494, y1:0.989, x2:0.494, y2:0.011, stop:0.863158 rgba(23, 132, 255, 250), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.button_save.setAutoDefault(False)
        self.button_save.setFlat(False)
        self.button_save.setObjectName("button_save")
        self.gridLayout_13.addWidget(self.button_save, 0, 3, 1, 1)
        self.widget_11 = QtWidgets.QWidget(self.widget_3)
        self.widget_11.setObjectName("widget_11")
        self.gridLayout_13.addWidget(self.widget_11, 0, 2, 1, 1)
        self.gridLayout_11.addWidget(self.widget_3, 8, 0, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout_11)
        self.label_38.setBuddy(self.text_hint)
        self.label_52.setBuddy(self.button_record)
        self.label_51.setBuddy(self.button_choose_picture)
        self.label_54.setBuddy(self.text_tag)
        self.label_37.setBuddy(self.combobox_category)
        self.label_39.setBuddy(self.text_phonetic)
        self.label_36.setBuddy(self.text_vocalubary)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Danh sách"))
        self.label_2.setText(_translate("Dialog", "Tìm kiếm"))
        self.label_3.setText(_translate("Dialog", "Trường"))
        self.comboBox_field.setItemText(0, _translate("Dialog", "Từ mới"))
        self.comboBox_field.setItemText(1, _translate("Dialog", "Thẻ"))
        self.comboBox_field.setItemText(2, _translate("Dialog", "Trình độ"))
        self.comboBox_field.setItemText(3, _translate("Dialog", "Ngày thêm"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Từ mới"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Thẻ"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Trình độ"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Ngày thêm"))
        self.combobox_category.setItemText(0, _translate("Dialog", "chưa xác định"))
        self.combobox_category.setItemText(1, _translate("Dialog", "n - danh từ"))
        self.combobox_category.setItemText(2, _translate("Dialog", "v - động từ"))
        self.combobox_category.setItemText(3, _translate("Dialog", "adj - tính từ"))
        self.combobox_category.setItemText(4, _translate("Dialog", "adv - trạng từ"))
        self.combobox_category.setItemText(5, _translate("Dialog", "np - cụm danh từ"))
        self.combobox_category.setItemText(6, _translate("Dialog", "vp - cụm động từ"))
        self.combobox_category.setItemText(7, _translate("Dialog", "idiom - thành ngữ"))
        self.combobox_category.setItemText(8, _translate("Dialog", "clause - mệnh đề"))
        self.label_38.setText(_translate("Dialog", "Gợi ý"))
        self.button_delete_picture.setText(_translate("Dialog", "Xóa"))
        self.button_delete_record.setText(_translate("Dialog", "Xóa"))
        self.button_record.setText(_translate("Dialog", "Bắt đầu"))
        self.button_play_record.setText(_translate("Dialog", "Nghe lại"))
        self.label_52.setText(_translate("Dialog", "Ghi âm"))
        self.label_51.setText(_translate("Dialog", "Hình ảnh gợi ý"))
        self.label_54.setText(_translate("Dialog", "Gắn thẻ"))
        self.button_choose_picture.setText(_translate("Dialog", "Chọn ảnh"))
        self.label_37.setText(_translate("Dialog", "Từ loại"))
        self.label_39.setText(_translate("Dialog", "Phiên âm"))
        self.label_40.setText(_translate("Dialog", "Dịch nghĩa"))
        self.label_36.setText(_translate("Dialog", "Từ mới"))
        self.butto_discard.setToolTip(_translate("Dialog", "F2"))
        self.butto_discard.setText(_translate("Dialog", "Hủy"))
        self.butto_discard.setShortcut(_translate("Dialog", "F2"))
        self.button_delete.setToolTip(_translate("Dialog", "F3"))
        self.button_delete.setText(_translate("Dialog", "Xóa"))
        self.button_delete.setShortcut(_translate("Dialog", "F3"))
        self.button_save.setToolTip(_translate("Dialog", "F1"))
        self.button_save.setText(_translate("Dialog", "Lưu"))
        self.button_save.setShortcut(_translate("Dialog", "F1"))
import resource_rc
