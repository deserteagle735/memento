import interface
import interface.audio
import shutil
import time
import datetime

from interface.qt import *
from memento import utils
from memento.db import DB
from memento.word import Word

class Add(QDialog):
    def __init__(self, controller):
        QDialog.__init__(self, None, Qt.Window)
        self.controller = controller
        self.picture_name = ""
        self.record_name = ""
        self.hitory = []
        self.timer = QTimer()
        self.setModal(True)
        self.setup_ui() 
        
    def setup_ui(self):
        self.setup_dialog()
        self.setup_button()
        self.show()

    def setup_dialog(self):
        # main window
        from interface.form import add
        self.form = interface.form.add.Ui_Dialog()
        self.form.setupUi(self)

    def setup_button(self):        
        #disable dialog accept role
        # picture
        self.form.button_choose_picture.clicked.connect(self.choose_picture)
        self.form.button_delete_picture.clicked.connect(self.delete_picture)
        # record
        self.form.button_record.clicked.connect(self.record)
        self.form.button_play_record.clicked.connect(self.play_record)
        self.form.button_delete_record.clicked.connect(self.delete_record)
        # add word
        self.form.button_add.clicked.connect(self.add)
        # exit
        self.form.button_exit.clicked.connect(self.exit_)

    def choose_picture(self):
        picture_before = (self.picture_name != "")
        picture_name_before = self.picture_name
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self,"Chọn ảnh minh họa", "","Ảnh (*.jpg *.png *.jpeg)", options=options)
        if filename:
            pixmap = QPixmap(filename)
            width = pixmap.width()
            height = pixmap.height()
            if height > self.form.picture.height() or width > self.form.picture.width():
                pixmap = pixmap.scaled(self.form.picture.width(), self.form.picture.height(), Qt.KeepAspectRatio)
            self.form.picture.setPixmap(pixmap)
            
            self.picture_name = str(datetime.datetime.today().timestamp())
            if filename.endswith(".jpg"):
                self.picture_name += ".jpg"
            elif filename.endswith(".jpeg"):
                self.picture_name += ".jpeg"
            elif filename.endswith(".png"):
                self.picture_name += ".png"
            self.form.button_delete_picture.setEnabled(True)
            shutil.copy2(filename,os.path.join(self.controller.media_folder_path, self.picture_name))
            
            #delete before file
            if picture_before:
                try:
                    os.remove(os.path.join(self.controller.media_folder_path, picture_name_before))
                    print("delete", picture_name_before)
                except:
                    print("File " + picture_name_before + " not found")

    def delete_picture(self):
        if self.picture_name != "":
            self.form.button_delete_picture.setEnabled(False)
            self.form.picture.clear()
            try:
                os.remove(os.path.join(self.controller.media_folder_path, self.picture_name))
            except:
                print("File " + self.picture_name + " not found")

            self.picture_name = ""

    def record(self):
        recorded_before = (self.record_name != "")
        recorded_file_name = self.record_name
        temp_file = interface.audio.record_audio(self, self.controller.media_folder_path)
        if temp_file != "":
            self.record_name = temp_file
            self.form.button_delete_record.setEnabled(True)
            self.form.button_play_record.setEnabled(True)
            
            if recorded_before:
                try:
                    os.remove(os.path.join(self.controller.media_folder_path, recorded_file_name))
                except:
                    print("File " + recorded_file_name + " not found")

    def play_record(self):
        # if form.button_play_record.displayText() == "Nghe lại":
        #     self.form.button_play_record.setText("Dừng")
        #     state = interface.audio.play_audio(self, self.controller.media_folder_path, self.record_name)
        # if state == QMediaPlayer.StoppedState:
        #     self.form.button_play_record.setText("Nghe Lại")
        #     print("playing record")
        # else:
        #     if self.form.button_play_record
        #     state = interface.audio.pause_audio()
        #     if state == QMediaPlayer.StoppedState:
        #interface.audio.play_audio(self.form.button_play_record, self.controller.media_folder_path, self.record_name)
        #QSound.play("/home/deserteagle735/Desktop/PyQt-audio-record/test.wav")
        if self.record_name != "":
            interface.audio.play_audio(self.controller.media_folder_path, self.record_name)
        
    def delete_record(self):
        if self.record_name != "":
            self.form.button_delete_record.setEnabled(False)
            self.form.button_play_record.setEnabled(False)
            try:
                os.remove(os.path.join(self.controller.media_folder_path,self.record_name))
            except:
                print("File " + self.record_name + " not found")
            
            self.record_name = ""

    def add(self):

        def is_null(textbox):
            return textbox.displayText().strip() == "" 

        if is_null(self.form.text_vocabulary):
            QMessageBox.critical(self, "Lỗi", "Bạn chưa điền Từ mới", QMessageBox.Ok)
            return  
        if (self.form.combobox_category.currentIndex() == 0):
            QMessageBox.critical(self, "Lỗi", "Bạn chưa chọn Từ loại", QMessageBox.Ok)
            return    
        if is_null(self.form.text_definition):
            QMessageBox.critical(self, "Lỗi", "Bạn chưa điền Dịch nghĩa", QMessageBox.Ok)
            return

        if not utils.is_invalid_string(self.form.text_vocabulary.displayText()):
            self.form.label_bottom.setText("<p style='color:red'>Kí tự không hợp lệ `~!@#$%^&*()+=_<>?/\|[]{};</p>")
            self.form.text_vocabulary.setFocus()
            return
        if not utils.is_invalid_string(self.form.text_phonetic.displayText()):
            self.form.label_bottom.setText("<p style='color:red'>Kí tự không hợp lệ `~!@#$%^&*()+=_<>?/\|;[]{}</p>")
            self.form.text_phonetic.setFocus()
            return
        if not utils.is_invalid_string(self.form.text_hint.displayText()):
            self.form.label_bottom.setText("<p style='color:red'>Kí tự không hợp lệ `~!@#$%^&*()+=_<>?/\|;[]{}</p>")
            self.form.text_hint.setFocus()
            return
        if not utils.is_invalid_string(self.form.text_definition.displayText()):
            self.form.label_bottom.setText("<p style='color:red'>Kí tự không hợp lệ `~!@#$%^&*()+=_<>?/\|;[]{}</p>")
            self.form.text_definition.setFocus()
            return
        if not utils.is_invalid_string(self.form.text_tag.displayText()):
            self.form.label_bottom.setText("<p style='color:red'>Kí tự không hợp lệ `~!@#$%^&*()+=_<>?/\|;[]{}</p>")
            self.form.text_tag.setFocus()            
            return
        self.form.label_bottom.setText("")

        word = Word(
            id= None,
            vocabulary= utils.format_string(self.form.text_vocabulary.displayText()),
            category= utils.format_string(self.form.combobox_category.currentText()),
            phonetic= utils.format_string(self.form.text_phonetic.displayText()),
            hint= utils.format_string(self.form.text_hint.displayText()),
            definition= utils.format_string(self.form.text_definition.displayText()),
            tag= utils.format_string(self.form.text_tag.displayText()),
            picture_name= self.picture_name,
            record_name= self.record_name
        )

        self.controller.db.add_word(word)
        self.show_popup()
        self.clear_text()
        
    def show_popup(self):
        self.form.label_bottom.setText("<p style = 'color:green'>Đã thêm<p>")    
        self.timer.timeout.connect(self.close_popup)
        self.timer.start(1000)
    
    def close_popup(self):
        self.form.label_bottom.setText("")

    def clear_text(self):
        self.form.text_vocabulary.clear()
        self.form.combobox_category.setCurrentIndex(0)
        self.form.text_phonetic.clear()
        self.form.text_hint.clear()
        self.form.text_definition.clear()
        self.form.text_tag.clear()
        self.picture_name = ""
        self.record_name = ""
        self.form.picture.clear()
        self.form.text_vocabulary.setFocus()
        self.form.button_delete_picture.setDisabled(True)
        self.form.button_delete_record.setDisabled(True)
        self.form.button_play_record.setDisabled(True)
        
    def closeEvent(self,e):
        if self.picture_name != "":
            try:
                os.remove(os.path.join(self.controller.media_folder_path,self.picture_name))
            except:
                print("File " + self.picture_name + " not found")
        if self.record_name != "":            
            try:
                os.remove(os.path.join(self.controller.media_folder_path,self.record_name))
            except:
                print("File " + self.record_name + " not found")
        e.accept()

    def exit_(self):
        self.close()

        
        
    
        