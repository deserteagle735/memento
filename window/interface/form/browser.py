# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(939, 460)
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resource/memento.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("font: 12pt \"SF Pro Display\";")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(Dialog)
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
        self.text_search_box.setStyleSheet("QLineEdit{\n"
"border-radius:10px;\n"
"border:1px solid gray;\n"
"padding: 0 8px;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"    border: 1px solid #006080;\n"
"}")
        self.text_search_box.setObjectName("text_search_box")
        self.gridLayout.addWidget(self.text_search_box, 1, 1, 1, 1)
        self.button_search = QtWidgets.QPushButton(self.layoutWidget)
        self.button_search.setStyleSheet("\n"
"\n"
"QPushButton:focus{\n"
"border: 1px solid #006080;\n"
"}")
        self.button_search.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resource/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_search.setIcon(icon1)
        self.button_search.setAutoDefault(True)
        self.button_search.setObjectName("button_search")
        self.gridLayout.addWidget(self.button_search, 1, 2, 1, 1)
        self.comboBox_field = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_field.setStyleSheet("QComboBox{border: 1px solid gray;\n"
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
"QComboBox:focus{\n"
"border: 1px solid #006080;\n"
"}\n"
"\n"
"")
        self.comboBox_field.setObjectName("comboBox_field")
        self.comboBox_field.addItem("")
        self.comboBox_field.addItem("")
        self.comboBox_field.addItem("")
        self.comboBox_field.addItem("")
        self.comboBox_field.addItem("")
        self.comboBox_field.addItem("")
        self.gridLayout.addWidget(self.comboBox_field, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tableView = QtWidgets.QTableView(self.layoutWidget)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setAlternatingRowColors(False)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableView.setShowGrid(True)
        self.tableView.setGridStyle(QtCore.Qt.SolidLine)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView.horizontalHeader().setHighlightSections(False)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableView)
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
        self.combobox_category.setStyleSheet("QComboBox{border: 1px solid gray;\n"
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
"QComboBox:focus{\n"
"border: 1px solid #006080;\n"
"}\n"
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
        self.text_phonetic.setStyleSheet("QLineEdit{\n"
"border-radius:10px;\n"
"border:1px solid gray;\n"
"padding: 0 8px;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"    border: 1px solid #006080;\n"
"}")
        self.text_phonetic.setObjectName("text_phonetic")
        self.gridLayout_11.addWidget(self.text_phonetic, 3, 0, 1, 1)
        self.text_hint = QtWidgets.QLineEdit(self.editor)
        self.text_hint.setStyleSheet("QLineEdit{\n"
"border-radius:10px;\n"
"border:1px solid gray;\n"
"padding: 0 8px;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"    border: 1px solid #006080;\n"
"}")
        self.text_hint.setObjectName("text_hint")
        self.gridLayout_11.addWidget(self.text_hint, 3, 1, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.editor)
        self.label_38.setObjectName("label_38")
        self.gridLayout_11.addWidget(self.label_38, 2, 1, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.text_tag = QtWidgets.QLineEdit(self.editor)
        self.text_tag.setStyleSheet("QLineEdit{\n"
"border-radius:10px;\n"
"border:1px solid gray;\n"
"padding: 0 8px;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"    border: 1px solid #006080;\n"
"}")
        self.text_tag.setObjectName("text_tag")
        self.gridLayout_12.addWidget(self.text_tag, 1, 0, 1, 2)
        self.widget_12 = QtWidgets.QWidget(self.editor)
        self.widget_12.setObjectName("widget_12")
        self.gridLayout_12.addWidget(self.widget_12, 8, 1, 1, 1)
        self.button_delete_picture = QtWidgets.QPushButton(self.editor)
        self.button_delete_picture.setStyleSheet("QPushButton{border-radius:10px;\n"
"border:1px solid gray;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"border: 1px solid #006080;\n"
"}")
        self.button_delete_picture.setAutoDefault(True)
        self.button_delete_picture.setObjectName("button_delete_picture")
        self.gridLayout_12.addWidget(self.button_delete_picture, 4, 1, 1, 1)
        self.button_delete_record = QtWidgets.QPushButton(self.editor)
        self.button_delete_record.setStyleSheet("QPushButton{border-radius:10px;\n"
"border:1px solid gray;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"border: 1px solid #006080;\n"
"}")
        self.button_delete_record.setAutoDefault(True)
        self.button_delete_record.setObjectName("button_delete_record")
        self.gridLayout_12.addWidget(self.button_delete_record, 7, 1, 1, 1)
        self.button_record = QtWidgets.QPushButton(self.editor)
        self.button_record.setStyleSheet("QPushButton{border-radius:10px;\n"
"border:1px solid gray;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"border: 1px solid #006080;\n"
"}")
        self.button_record.setAutoDefault(True)
        self.button_record.setObjectName("button_record")
        self.gridLayout_12.addWidget(self.button_record, 7, 0, 1, 1)
        self.button_play_record = QtWidgets.QPushButton(self.editor)
        self.button_play_record.setStyleSheet("QPushButton{border-radius:10px;\n"
"border:1px solid gray;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"border: 1px solid #006080;\n"
"}")
        self.button_play_record.setAutoDefault(True)
        self.button_play_record.setObjectName("button_play_record")
        self.gridLayout_12.addWidget(self.button_play_record, 8, 0, 1, 1)
        self.label_52 = QtWidgets.QLabel(self.editor)
        self.label_52.setObjectName("label_52")
        self.gridLayout_12.addWidget(self.label_52, 6, 0, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.editor)
        self.label_51.setObjectName("label_51")
        self.gridLayout_12.addWidget(self.label_51, 2, 0, 1, 2)
        self.button_choose_picture = QtWidgets.QPushButton(self.editor)
        self.button_choose_picture.setStyleSheet("QPushButton{border-radius:10px;\n"
"border:1px solid gray;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"border: 1px solid #006080;\n"
"}")
        self.button_choose_picture.setAutoDefault(True)
        self.button_choose_picture.setObjectName("button_choose_picture")
        self.gridLayout_12.addWidget(self.button_choose_picture, 4, 0, 1, 1)
        self.label_54 = QtWidgets.QLabel(self.editor)
        self.label_54.setObjectName("label_54")
        self.gridLayout_12.addWidget(self.label_54, 0, 0, 1, 1)
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
        self.text_definition.setStyleSheet("QLineEdit{\n"
"border-radius:10px;\n"
"border:1px solid gray;\n"
"padding: 0 8px;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"    border: 1px solid #006080;\n"
"}")
        self.text_definition.setObjectName("text_definition")
        self.gridLayout_11.addWidget(self.text_definition, 6, 0, 1, 2)
        self.label_36 = QtWidgets.QLabel(self.editor)
        self.label_36.setObjectName("label_36")
        self.gridLayout_11.addWidget(self.label_36, 0, 0, 1, 1)
        self.picture = QtWidgets.QLabel(self.editor)
        self.picture.setText("")
        self.picture.setScaledContents(False)
        self.picture.setAlignment(QtCore.Qt.AlignCenter)
        self.picture.setObjectName("picture")
        self.gridLayout_11.addWidget(self.picture, 7, 0, 1, 1)
        self.text_vocabulary = QtWidgets.QLineEdit(self.editor)
        self.text_vocabulary.setStyleSheet("QLineEdit{\n"
"border-radius:10px;\n"
"border:1px solid gray;\n"
"padding: 0 8px;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"    border: 1px solid #006080;\n"
"}")
        self.text_vocabulary.setObjectName("text_vocabulary")
        self.gridLayout_11.addWidget(self.text_vocabulary, 1, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.editor)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_13.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.button_discard = QtWidgets.QPushButton(self.widget_3)
        self.button_discard.setStyleSheet("QPushButton{border-radius:10px;\n"
"border:1px solid gray;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"border: 1px solid #006080;\n"
"}")
        self.button_discard.setAutoDefault(True)
        self.button_discard.setObjectName("button_discard")
        self.gridLayout_13.addWidget(self.button_discard, 0, 4, 1, 1)
        self.button_delete = QtWidgets.QPushButton(self.widget_3)
        self.button_delete.setStyleSheet("QPushButton{border-radius:10px;\n"
"border:1px solid gray;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"border: 1px solid #006080;\n"
"}")
        self.button_delete.setAutoDefault(True)
        self.button_delete.setObjectName("button_delete")
        self.gridLayout_13.addWidget(self.button_delete, 0, 1, 1, 1)
        self.button_save = QtWidgets.QPushButton(self.widget_3)
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
        self.button_save.setFlat(False)
        self.button_save.setObjectName("button_save")
        self.gridLayout_13.addWidget(self.button_save, 0, 3, 1, 1)
        self.widget_11 = QtWidgets.QWidget(self.widget_3)
        self.widget_11.setObjectName("widget_11")
        self.gridLayout_13.addWidget(self.widget_11, 0, 2, 1, 1)
        self.gridLayout_11.addWidget(self.widget_3, 9, 0, 1, 2)
        self.label_bottom = QtWidgets.QLabel(self.editor)
        self.label_bottom.setText("")
        self.label_bottom.setAlignment(QtCore.Qt.AlignCenter)
        self.label_bottom.setObjectName("label_bottom")
        self.gridLayout_11.addWidget(self.label_bottom, 8, 0, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout_11)
        self.verticalLayout_3.addWidget(self.splitter)
        self.label_38.setBuddy(self.text_hint)
        self.label_52.setBuddy(self.button_record)
        self.label_51.setBuddy(self.button_choose_picture)
        self.label_54.setBuddy(self.text_tag)
        self.label_37.setBuddy(self.combobox_category)
        self.label_39.setBuddy(self.text_phonetic)
        self.label_36.setBuddy(self.text_vocabulary)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Danh sách"))
        self.label_2.setText(_translate("Dialog", "Từ khóa"))
        self.label_3.setText(_translate("Dialog", "Tìm theo"))
        self.button_search.setToolTip(_translate("Dialog", "Ctrl+F"))
        self.button_search.setShortcut(_translate("Dialog", "Ctrl+F"))
        self.comboBox_field.setItemText(0, _translate("Dialog", "Tất cả"))
        self.comboBox_field.setItemText(1, _translate("Dialog", "Từ mới"))
        self.comboBox_field.setItemText(2, _translate("Dialog", "Thẻ"))
        self.comboBox_field.setItemText(3, _translate("Dialog", "Trình độ"))
        self.comboBox_field.setItemText(4, _translate("Dialog", "Thêm hôm nay"))
        self.comboBox_field.setItemText(5, _translate("Dialog", "Ngày thêm"))
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
        self.button_record.setToolTip(_translate("Dialog", "Ctrl+R"))
        self.button_record.setText(_translate("Dialog", "Bắt đầu"))
        self.button_record.setShortcut(_translate("Dialog", "Ctrl+R"))
        self.button_play_record.setToolTip(_translate("Dialog", "Ctrl+P"))
        self.button_play_record.setText(_translate("Dialog", "Nghe lại"))
        self.button_play_record.setShortcut(_translate("Dialog", "Ctrl+P"))
        self.label_52.setText(_translate("Dialog", "Ghi âm"))
        self.label_51.setText(_translate("Dialog", "Hình ảnh gợi ý"))
        self.button_choose_picture.setToolTip(_translate("Dialog", "Ctrl+O"))
        self.button_choose_picture.setText(_translate("Dialog", "Chọn ảnh"))
        self.button_choose_picture.setShortcut(_translate("Dialog", "Ctrl+O"))
        self.label_54.setText(_translate("Dialog", "Gắn thẻ"))
        self.label_37.setText(_translate("Dialog", "Từ loại"))
        self.label_39.setText(_translate("Dialog", "Phiên âm"))
        self.label_40.setText(_translate("Dialog", "Dịch nghĩa"))
        self.label_36.setText(_translate("Dialog", "Từ mới"))
        self.button_discard.setToolTip(_translate("Dialog", "Ctrl+D"))
        self.button_discard.setText(_translate("Dialog", "Hủy"))
        self.button_discard.setShortcut(_translate("Dialog", "Ctrl+D"))
        self.button_delete.setToolTip(_translate("Dialog", "Delete"))
        self.button_delete.setText(_translate("Dialog", "Xóa"))
        self.button_delete.setShortcut(_translate("Dialog", "Del"))
        self.button_save.setToolTip(_translate("Dialog", "Ctrl+S"))
        self.button_save.setText(_translate("Dialog", "Lưu"))
        self.button_save.setShortcut(_translate("Dialog", "Ctrl+S"))
import resource_rc
