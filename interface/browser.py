import interface
import os
import datetime
import shutil
from interface.qt import *
from memento.word import Word
from memento import utils

class Browser(QDialog):
    def __init__(self, controller):
        QDialog.__init__(self, None, Qt.Window)
        self.controller = controller
        self.picture_name = ""
        self.record_name = ""
        self.id = None
        self.current_row = 0
        self.name = {
            "Từ mới" : "vocabulary",
            "Từ loại" : "category",
            "Phiên âm" : "phonetic",
            "Gợi ý" : "hint",
            "Dịch nghĩa" : "definition",
            "Thẻ" : "tag",
            "Ảnh" : "picture_name",
            "Ghi âm" : "record_name",
            "Ngày thêm" : "create_at",
            "Tất cả" : "all",
            "Thêm hôm nay" : "today",
            "Trình độ" : "level"
        }

        self.pics = []
        self.recs = []
        self.last_pic = ""
        self.last_rec = ""
        self.setModal(True)
        self.setup_ui()
        self.setup_data()   
        self.setup_button()
        
    def setup_ui(self):
        self.setup_dialog()
        self.show()

    def setup_dialog(self):
        # main window
        from interface.form import browser
        self.form = interface.form.browser.Ui_Dialog()
        self.form.setupUi(self)

    def setup_data(self):
        #connect to database
        self.model = self.controller.db.start_model() 

        #setup view
        record = self.model.record(0)
        self.form.tableView.setModel(self.model)
        self.form.tableView.setColumnHidden(record.indexOf("id"), True)
        self.form.tableView.setColumnHidden(record.indexOf("hint"), True)
        self.form.tableView.setColumnHidden(record.indexOf("phonetic"), True)
        self.form.tableView.setColumnHidden(record.indexOf("picture_name"), True)
        self.form.tableView.setColumnHidden(record.indexOf("record_name"), True)
        self.form.tableView.setColumnHidden(record.indexOf("met"), True)
        self.form.tableView.setColumnHidden(record.indexOf("correct"), True)
        self.form.tableView.selectionModel()
        
        #change data mapper when user change row
        self.form.tableView.selectionModel().currentRowChanged.connect(self.on_row_changed)
        self.form.tableView.setCurrentIndex(self.model.index(0,0))

    def on_row_changed(self, current, previous):
        record = self.model.record(current.row())

        #id
        self.id = record.value("id")

        #text
        self.form.text_vocabulary.setText(record.value("vocabulary"))
        self.form.combobox_category.setCurrentText(record.value("category"))
        self.form.text_phonetic.setText(record.value("phonetic"))
        self.form.text_hint.setText(record.value("hint"))
        self.form.text_definition.setText(record.value("definition"))
        self.form.text_tag.setText(record.value("tag"))

        #picture
        self.picture_name = str(record.value("picture_name"))
        self.last_pic = self.picture_name
        if self.picture_name != "":
            pixmap = QPixmap(os.path.join(self.controller.media_folder_path,self.picture_name))
            height = pixmap.height()
            width = pixmap.width()
            if height > self.form.picture.height() or width > self.form.picture.width():
                pixmap = pixmap.scaled(self.form.picture.width(), self.form.picture.height(), Qt.KeepAspectRatio)
            self.form.picture.setPixmap(pixmap)
            self.form.button_delete_picture.setEnabled(True)
        else:
            self.form.picture.clear()
            self.form.button_delete_picture.setEnabled(False)
        
        #record
        self.record_name = str(record.value("record_name"))
        self.last_rec = self.record_name
        if self.record_name != "":
            self.form.button_delete_record.setEnabled(True)
            self.form.button_play_record.setEnabled(True)
        else:
            self.form.button_delete_record.setEnabled(False)
            self.form.button_play_record.setEnabled(False)

        self.form.label_bottom.setText("")

    def setup_button(self):
        #save
        self.form.button_save.clicked.connect(self.button_save_clicked)
        #search
        self.form.button_search.clicked.connect(self.button_search_clicked)
        # picture
        self.form.button_choose_picture.clicked.connect(self.choose_picture)
        self.form.button_delete_picture.clicked.connect(self.delete_picture)
        # record
        self.form.button_record.clicked.connect(self.record)
        self.form.button_delete_record.clicked.connect(self.delete_record)
        self.form.button_play_record.clicked.connect(self.play_record)
        #discard
        self.form.button_discard.clicked.connect(self.button_discard_clicked)
        #delete
        self.form.button_delete.clicked.connect(self.delete_word)

    def button_save_clicked(self):
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
            self.form.label_bottom.setText("<p style='color:red'>Kí tự không hợp lệ `~!@#$%^&*()+=_<>?/\|;</p>")
            self.form.text_vocabulary.setFocus()
            return
        if not utils.is_invalid_string(self.form.text_phonetic.displayText()):
            self.form.label_bottom.setText("<p style='color:red'>Kí tự không hợp lệ `~!@#$%^&*()+=_<>?/\|;</p>")
            self.form.text_phonetic.setFocus()
            return
        if not utils.is_invalid_string(self.form.text_hint.displayText()):
            self.form.label_bottom.setText("<p style='color:red'>Kí tự không hợp lệ `~!@#$%^&*()+=_<>?/\|;</p>")
            self.form.text_hint.setFocus()
            return
        if not utils.is_invalid_string(self.form.text_definition.displayText()):
            self.form.label_bottom.setText("<p style='color:red'>Kí tự không hợp lệ `~!@#$%^&*()+=_<>?/\|;</p>")
            self.form.text_definition.setFocus()
            return
        if not utils.is_invalid_string(self.form.text_tag.displayText()):
            self.form.label_bottom.setText("<p style='color:red'>Kí tự không hợp lệ `~!@#$%^&*()+=_<>?/\|;</p>")
            self.form.text_tag.setFocus()            
            return
        self.form.label_bottom.setText("")

        self.current_row = self.form.tableView.currentIndex().row()
        current_index = self.form.tableView.currentIndex().row()
        self.model.setData(
            self.model.index(self.current_row, self.model.fieldIndex("vocabulary")),
            utils.format_string(self.form.text_vocabulary.displayText()))
        self.model.setData(
            self.model.index(self.current_row, self.model.fieldIndex("category")),
            utils.format_string(self.form.combobox_category.currentText()))
        self.model.setData(
            self.model.index(self.current_row, self.model.fieldIndex("phonetic")),
            utils.format_string(self.form.text_phonetic.displayText()))
        self.model.setData(
            self.model.index(self.current_row, self.model.fieldIndex("hint")),
            utils.format_string(self.form.text_hint.displayText()))
        self.model.setData(
            self.model.index(self.current_row, self.model.fieldIndex("definition")),
            utils.format_string(self.form.text_definition.displayText()))
        self.model.setData(
            self.model.index(self.current_row, self.model.fieldIndex("tag")),
            utils.format_string(self.form.text_tag.displayText()))
        self.model.setData(
            self.model.index(self.current_row, self.model.fieldIndex("picture_name")),
            self.picture_name)
        self.model.setData(
            self.model.index(self.current_row, self.model.fieldIndex("record_name")),
            self.record_name)
        
        for file in self.pics:
            if file != self.picture_name:
                try:
                    os.remove(os.path.join(self.controller.media_folder_path, file))
                except: 
                    print("File " + file + "not found")
        for file in self.recs:
            if file != self.record_name:
                try:
                    os.remove(os.path.join(self.controller.media_folder_path, file))
                except:
                    print("File " + file + " not found")

        self.model.submitAll()
        self.form.tableView.setCurrentIndex(self.model.index(self.current_row, 0))
        print("Saved " + self.form.text_vocabulary.displayText())

    def button_search_clicked(self):
        result = self.controller.db.search(
                                        self.name[self.form.comboBox_field.currentText()],
                                        self.form.text_search_box.displayText().strip())
        if result == None:
            QMessageBox.critical(self, "Lỗi", "Bạn chưa điền Từ khóa", QMessageBox.Ok)
            return
        self.model = result
        #self.model.select()
        self.form.tableView.setModel(self.model)
        self.form.tableView.selectionModel()
        self.form.tableView.setCurrentIndex(self.model.index(0,0))
    
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
                self.pics.append(picture_before)

    def delete_picture(self):
        if self.picture_name != "":
            self.form.button_delete_picture.setEnabled(False)
            self.form.picture.clear()
            self.pics.append(self.picture_name)

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
                self.recs.append(recorded_before)
                

    def play_record(self):
        if self.record_name != "":
            interface.audio.play_audio(self.controller.media_folder_path, self.record_name)
        
    def delete_record(self):
        if self.record_name != "":            
            self.form.button_delete_record.setEnabled(False)
            self.form.button_play_record.setEnabled(False)
            self.recs.append(self.record_name)
            self.record_name = ""
    
    def button_discard_clicked(self):
        self.form.label_bottom.setText("")
        #restore info
        for file in self.pics:
            if file != self.last_pic:
                try:
                    os.remove(os.path.join(self.controller.media_folder_path, file))
                except:
                    print("File " + file + " not found")

        for file in self.recs:
            if file != self.last_rec:
                try:
                    os.remove(os.path.join(self.controller.media_folder_path, file))
                except:
                    print("File " + file + " not found")

        index = self.form.tableView.currentIndex()
        self.on_row_changed(index, index)

    def delete_word(self):
        self.form.label_bottom.setText("")
        temp_word = self.form.text_vocabulary.displayText()
        delete_dialog = QMessageBox(self)
        txt = "Bạn có chắc chắn xóa " + temp_word + "?"
        delete_dialog.setText(txt)
        delete_dialog.setWindowTitle("Xóa từ")
        #button
        button_delete = QPushButton("Xóa")
        
        button_cancel = QPushButton("Quay lại")
        button_cancel.setDefault(True)
        delete_dialog.addButton(button_delete, QMessageBox.AcceptRole)
        delete_dialog.addButton(button_cancel, QMessageBox.RejectRole)
        delete_dialog.setEscapeButton(button_cancel)
        QApplication.instance().processEvents()

        while not delete_dialog.clickedButton():
            delete_dialog.show()
            QApplication.instance().processEvents()

        if delete_dialog.clickedButton() == delete_dialog.escapeButton() :
            print("Back")
        else:
            index = self.form.tableView.currentIndex().row()
            #remove picture
            temp_picture_name = self.model.record(index).value("picture_name")
            if  temp_picture_name != "":
                try:
                    os.remove(os.path.join(self.controller.media_folder_path, temp_picture_name))
                    print("Deleted picture: ", temp_picture_name)
                except:
                    print("File " + temp_picture_name + " not found")
            #remove record
            temp_record_name = self.model.record(index).value("record_name")
            if temp_record_name != "":
                try:
                    os.remove(os.path.join(self.controller.media_folder_path, temp_record_name))
                    print("Deleted record: ", temp_record_name)
                except:
                    print("File " + temp_record_name + " not found")
            self.model.deleteRowFromTable(index)
            self.model.submitAll()
            self.form.tableView.setCurrentIndex(self.model.index(0,0))
            print("Deleted word: ", temp_word)
            