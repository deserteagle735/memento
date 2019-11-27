# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(400, 441)
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(12)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resource/memento.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.picture = QtWidgets.QLabel(Dialog)
        self.picture.setMinimumSize(QtCore.QSize(190, 190))
        self.picture.setAlignment(QtCore.Qt.AlignCenter)
        self.picture.setObjectName("picture")
        self.horizontalLayout.addWidget(self.picture)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.text_phonetic = QtWidgets.QLineEdit(Dialog)
        self.text_phonetic.setEnabled(True)
        self.text_phonetic.setStyleSheet("border-radius:10px;\n"
"border:1px solid white;\n"
"padding: 0 8px;")
        self.text_phonetic.setText("")
        self.text_phonetic.setAlignment(QtCore.Qt.AlignCenter)
        self.text_phonetic.setReadOnly(True)
        self.text_phonetic.setObjectName("text_phonetic")
        self.verticalLayout_4.addWidget(self.text_phonetic)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.text_hint = QtWidgets.QLineEdit(Dialog)
        self.text_hint.setStyleSheet("border-radius:10px;\n"
"border:1px solid white;\n"
"padding: 0 8px;")
        self.text_hint.setText("")
        self.text_hint.setAlignment(QtCore.Qt.AlignCenter)
        self.text_hint.setReadOnly(True)
        self.text_hint.setObjectName("text_hint")
        self.verticalLayout_5.addWidget(self.text_hint)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.text_tag = QtWidgets.QLineEdit(Dialog)
        self.text_tag.setEnabled(True)
        self.text_tag.setStyleSheet("border-radius:10px;\n"
"border:1px solid white;\n"
"padding: 0 8px;")
        self.text_tag.setText("")
        self.text_tag.setAlignment(QtCore.Qt.AlignCenter)
        self.text_tag.setReadOnly(True)
        self.text_tag.setObjectName("text_tag")
        self.verticalLayout_3.addWidget(self.text_tag)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.text_definition = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_definition.sizePolicy().hasHeightForWidth())
        self.text_definition.setSizePolicy(sizePolicy)
        self.text_definition.setStyleSheet("border-radius:10px;\n"
"border:1px solid white;\n"
"padding: 0 8px;")
        self.text_definition.setText("")
        self.text_definition.setAlignment(QtCore.Qt.AlignCenter)
        self.text_definition.setReadOnly(True)
        self.text_definition.setObjectName("text_definition")
        self.verticalLayout_2.addWidget(self.text_definition)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.text_vocabulary = QtWidgets.QLineEdit(Dialog)
        self.text_vocabulary.setStyleSheet("border-radius:10px;\n"
"border:1px solid white;\n"
"padding: 0 8px;")
        self.text_vocabulary.setText("")
        self.text_vocabulary.setAlignment(QtCore.Qt.AlignCenter)
        self.text_vocabulary.setReadOnly(True)
        self.text_vocabulary.setClearButtonEnabled(False)
        self.text_vocabulary.setObjectName("text_vocabulary")
        self.verticalLayout.addWidget(self.text_vocabulary)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_9.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_top = QtWidgets.QLabel(Dialog)
        self.label_top.setAlignment(QtCore.Qt.AlignCenter)
        self.label_top.setObjectName("label_top")
        self.verticalLayout_8.addWidget(self.label_top)
        self.text_answer = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_answer.sizePolicy().hasHeightForWidth())
        self.text_answer.setSizePolicy(sizePolicy)
        self.text_answer.setStyleSheet("QLineEdit{\n"
"border-radius:10px;\n"
"border:1px solid gray;\n"
"padding: 0 8px;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"    border: 1px solid #006080;\n"
"}")
        self.text_answer.setAlignment(QtCore.Qt.AlignCenter)
        self.text_answer.setReadOnly(False)
        self.text_answer.setPlaceholderText("")
        self.text_answer.setClearButtonEnabled(False)
        self.text_answer.setObjectName("text_answer")
        self.verticalLayout_8.addWidget(self.text_answer)
        self.label_bottom = QtWidgets.QLabel(Dialog)
        self.label_bottom.setText("")
        self.label_bottom.setAlignment(QtCore.Qt.AlignCenter)
        self.label_bottom.setObjectName("label_bottom")
        self.verticalLayout_8.addWidget(self.label_bottom)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_show_answer = QtWidgets.QPushButton(Dialog)
        self.button_show_answer.setStyleSheet("QPushButton{border-radius:10px;\n"
"border:1px solid gray;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"border: 1px solid #006080;\n"
"}")
        self.button_show_answer.setIconSize(QtCore.QSize(20, 20))
        self.button_show_answer.setAutoDefault(True)
        self.button_show_answer.setFlat(False)
        self.button_show_answer.setObjectName("button_show_answer")
        self.horizontalLayout_3.addWidget(self.button_show_answer)
        self.button_play_record = QtWidgets.QPushButton(Dialog)
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
        self.button_play_record.setIconSize(QtCore.QSize(20, 20))
        self.button_play_record.setAutoDefault(True)
        self.button_play_record.setFlat(False)
        self.button_play_record.setObjectName("button_play_record")
        self.horizontalLayout_3.addWidget(self.button_play_record)
        self.button_check = QtWidgets.QPushButton(Dialog)
        self.button_check.setEnabled(True)
        self.button_check.setStyleSheet("QPushButton{border-radius:10px;\n"
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
        self.button_check.setAutoDefault(True)
        self.button_check.setDefault(True)
        self.button_check.setObjectName("button_check")
        self.horizontalLayout_3.addWidget(self.button_check)
        self.button_next = QtWidgets.QPushButton(Dialog)
        self.button_next.setEnabled(True)
        self.button_next.setStyleSheet("QPushButton{border-radius:10px;\n"
"border:1px solid gray;\n"
"padding: 0 8px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"border: 1px solid #006080;\n"
"}")
        self.button_next.setAutoDefault(True)
        self.button_next.setObjectName("button_next")
        self.horizontalLayout_3.addWidget(self.button_next)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.text_answer, self.button_show_answer)
        Dialog.setTabOrder(self.button_show_answer, self.button_play_record)
        Dialog.setTabOrder(self.button_play_record, self.button_check)
        Dialog.setTabOrder(self.button_check, self.button_next)
        Dialog.setTabOrder(self.button_next, self.text_phonetic)
        Dialog.setTabOrder(self.text_phonetic, self.text_hint)
        Dialog.setTabOrder(self.text_hint, self.text_tag)
        Dialog.setTabOrder(self.text_tag, self.text_definition)
        Dialog.setTabOrder(self.text_definition, self.text_vocabulary)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kiểm tra"))
        self.picture.setText(_translate("Dialog", "Picture"))
        self.label.setText(_translate("Dialog", "Phiên âm"))
        self.label_2.setText(_translate("Dialog", "Gợi ý"))
        self.label_3.setText(_translate("Dialog", "Thẻ"))
        self.label_5.setText(_translate("Dialog", " Dịch nghĩa"))
        self.label_4.setText(_translate("Dialog", " Từ mới"))
        self.label_top.setText(_translate("Dialog", "Đáp án của bạn là"))
        self.button_show_answer.setToolTip(_translate("Dialog", "Ctrl+K"))
        self.button_show_answer.setText(_translate("Dialog", "Đáp án"))
        self.button_show_answer.setShortcut(_translate("Dialog", "Ctrl+K"))
        self.button_play_record.setToolTip(_translate("Dialog", "Ctrl+P"))
        self.button_play_record.setText(_translate("Dialog", "Nghe"))
        self.button_play_record.setShortcut(_translate("Dialog", "Ctrl+P"))
        self.button_check.setToolTip(_translate("Dialog", "Ctrl+Enter"))
        self.button_check.setText(_translate("Dialog", "Kiểm tra"))
        self.button_check.setShortcut(_translate("Dialog", "Ctrl+Return"))
        self.button_next.setToolTip(_translate("Dialog", "Ctrl+N"))
        self.button_next.setText(_translate("Dialog", "Tiếp theo"))
        self.button_next.setShortcut(_translate("Dialog", "Ctrl+N"))
import resource_rc
