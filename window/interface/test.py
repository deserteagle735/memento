import interface
import interface.audio
import json
import os
import random

from difflib import SequenceMatcher
from interface.qt import *
from memento import utils
from memento.word import Word

MAX_TEST_LEVEL = 7
MAX_HINT_LEVEL = 4
MAX_LEVEL = 5
RATIO = [4, 2, 2, 1, 1]
TOTAL = 10
HIDDEN_CHARACTER = '?'

class Tag(QDialog):
    def __init__(self):
        QDialog.__init__(self, None, Qt.Dialog | Qt.WindowTitleHint | Qt.CustomizeWindowHint)
        from interface.form import tag
        self.form = interface.form.tag.Ui_Dialog()
        self.form.setupUi(self)
        self.show()
        self.setModal(True)

class Test(QDialog):
    
    def __init__(self, controller):
        QDialog.__init__(self, None, Qt.Window)
        self.controller = controller
        self.picture_name = ""
        self.record_name = ""
        self.is_correct_answer = False
        self.learn_value = 0
        self.tag = ""
        self.tag_dialog = None
        #Function base on test level
        self.show_function = [self.show_phonetic,
                self.show_hint,
                self.set_record,
                self.show_encode_word1,
                self.show_definition,
                self.show_encode_word2,
                self.show_picture_and_tag]
        #Function base on hint level
        self.check_function = [self.check_nothing,
                self.check_record,
                self.check_longest_common_string,
                self.check_incorrect_character]

        self.config = utils.load_config()
        #quantity of word for each level
        self.quantity = [int(RATIO[i] * self.config["num"] / TOTAL) for i in range(5)]
        self.quantity[0] = self.config["num"] - sum([self.quantity[i] for i in range(4,0,-1)])
        self.setModal(True)
        self.setup_ui()
        self.words = []
        self.current_index = 0
        # if test by tag -> ask for tag
        if self.config["field"] == 1:
            self.tag_dialog = Tag()
            self.tag_dialog.form.button_back.clicked.connect(self.close_tag)
            self.tag_dialog.form.button_find.clicked.connect(self.find_tag)            
        elif self.config["field"] == 2:
            self.words = self.get_words()
            self.current_index = 0
            if (len(self.words) == 0):
                QMessageBox.critical(self, "Không tìm thấy từ mới", "Hôm nay bạn chưa thêm từ mới", QMessageBox.Ok)
                self.close()
            else:
                self.show_word(self.words[self.current_index])           
        elif self.config["field"] == 0:
            self.words = self.get_words()
            self.current_index = 0
            if (len(self.words) == 0):
                QMessageBox.critical(self, "Không tìm thấy từ mới", "Memento không tìm thấy từ của bạn", QMessageBox.Ok)
                self.close()
            else:
                self.show_word(self.words[self.current_index])           

    def setup_ui(self):
        self.setup_dialog()
        self.setup_button()
        self.show()

    def setup_dialog(self):
        # main window
        from interface.form import test
        self.form = interface.form.test.Ui_Dialog()
        self.form.setupUi(self)
        self.form.text_answer.setFocus()

        

    def setup_button(self):  
        self.form.button_play_record.clicked.connect(self.button_play_record_clicked)
        self.form.button_check.clicked.connect(self.button_check_clicked)
        self.form.button_next.clicked.connect(self.button_next_clicked)
        self.form.button_show_answer.clicked.connect(self.button_show_answer_clicked)

        self.form.button_play_record.setDisabled(True)

    def button_check_clicked(self):
        self.check_answer(self.words[self.current_index])
        if self.is_correct_answer == True:
            if self.learn_value == 0:
                self.update_learn_data(self.words[self.current_index], True)
            self.form.button_check.setDisabled(True)
            self.form.button_show_answer.setDisabled(True)
        else: 
            self.learn_value = -1

    def update_learn_data(self, word, correct=False):
        self.controller.db.update_learn_data(word, correct)

    def button_next_clicked(self):
        next_word = False
        if self.is_correct_answer == False:
            dialog_next = QMessageBox(self)
            dialog_next.setStyleSheet("font: 12pt \"SF Pro Display\";")
            dialog_next.setWindowTitle("Tiếp theo")
            dialog_next.setInformativeText("""Bạn chưa trả lời đúng.\nBạn có chắc chắn muốn chuyến sang câu tiếp theo?""")
            #icon
            dialog_next.setIcon(QMessageBox.Icon(QMessageBox.Question))
            #button
            button_cancel = QPushButton("Hủy")
            button_cancel.setDefault(True)
            button_ok = QPushButton("Tiếp theo")
            dialog_next.addButton(button_ok, QMessageBox.AcceptRole)
            dialog_next.addButton(button_cancel, QMessageBox.RejectRole)
            dialog_next.setEscapeButton(button_cancel)
            result = dialog_next.exec_()
            if result == QMessageBox.AcceptRole:
                next_word = True
                self.update_learn_data(self.words[self.current_index], False)
            elif result == QMessageBox.RejectRole: 
                next_word = False
        else:
            next_word = True
        if next_word == True:
            self.current_index += 1
            if self.current_index == len(self.words):
                QMessageBox.information(self, "Xong", "Bạn đã hoàn thành kiểm tra", QMessageBox.Ok)
                self.close()
            else:
                self.form.button_play_record.setDisabled(True)
                self.show_word(self.words[self.current_index])
                self.form.text_answer.clear()
                self.form.text_answer.setFocus()

    def button_play_record_clicked(self):
        if self.record_name != "":
            interface.audio.play_audio(self.controller.media_folder_path, self.record_name)

    def button_show_answer_clicked(self):
        dialog_show_answer = QMessageBox(self)
        dialog_show_answer.setStyleSheet("font: 12pt \"SF Pro Display\";")
        dialog_show_answer.setWindowTitle("Đáp")
        dialog_show_answer.setInformativeText("""Bạn có muốn hiện đáp án?""")
        #icon
        dialog_show_answer.setIcon(QMessageBox.Icon(QMessageBox.Question))
        #button
        button_cancel = QPushButton("Hủy")
        button_cancel.setDefault(True)
        button_ok = QPushButton("Hiện đáp án")
        dialog_show_answer.addButton(button_ok, QMessageBox.AcceptRole)
        dialog_show_answer.addButton(button_cancel, QMessageBox.RejectRole)
        dialog_show_answer.setEscapeButton(button_cancel)
        result = dialog_show_answer.exec_()
        if result == QMessageBox.AcceptRole:
            txt = "<p style = 'color:green'>" + self.words[self.current_index].vocabulary +"</p>"
            self.form.label_top.setText(txt)
            self.form.label_bottom.setText("")
            self.form.button_check.setDisabled(True)
            self.form.button_play_record.setEnabled(True)
            self.is_correct_answer = True
            self.update_learn_data(self.words[self.current_index], True)

    def close_tag(self):
        self.tag_dialog.close() 
        self.close()

    def find_tag(self):
        if not utils.is_invalid_string(self.tag_dialog.form.text_tag.displayText()):
            self.tag_dialog.form.label_bottom.setText("<p style='color:red'>Kí tự không hợp lệ `~!@#$%^&*()+=_<>?/\|;[]{}</p>")
            self.tag_dialog.form.text_tag.setFocus()
            return
        self.tag = utils.format_string(self.tag_dialog.form.text_tag.displayText())
        if self.tag == "":
            self.tag_dialog.form.label_bottom.setText("Bạn chưa điền thẻ")
            self.tag_dialog.form.text_tag.setFocus()
            return
        self.words = self.get_words()
        if len(self.words) == 0:
            self.tag_dialog.form.label_bottom.setText("Không tìm thấy thẻ bạn vừa nhập")
            self.tag_dialog.form.text_tag.setFocus()
            return
        self.show_word(self.words[self.current_index])
        self.tag_dialog.close()
    #Retrieve word from database
    def get_words(self):
        #test
        # w = Word(
        #     id= 1,
        #     vocabulary= "cat",
        #     category="n - danh từ",
        #     phonetic="két",
        #     hint="meow meow",
        #     definition= "con mèo",
        #     tag= "động vật",
        #     picture_name= "1574131646.859594.png",
        #     record_name= "1574266730.578919.wav"
        # )

        # 0 = all, 1 = by tag , 2 = added today
        if self.config["field"] == 0:
            words = self.controller.db.get_words(MAX_LEVEL, self.quantity, 0)
        elif self.config["field"] == 1:
            words = self.controller.db.get_words(MAX_LEVEL, self.quantity, 1, self.tag)
        elif self.config["field"] == 2:
            words = self.controller.db.get_words(MAX_LEVEL, self.quantity, 2)
        random.shuffle(words)
        return words

    # Funtion to show word
    def show_phonetic(self, word):
        self.form.text_phonetic.setText(word.phonetic)

    def show_hint(self, word):
        self.form.text_hint.setText(word.hint)

    def set_record(self, word):
        self.form.button_play_record.setEnabled(True)

    def show_encode_word1(self, word):
        """Encode every character by square
        except first and last character of each word
        """
        list_word = word.vocabulary.split()
        l_txt = []
        for item in list_word:
            txt = [item[0]] + [HIDDEN_CHARACTER] * (len(item) - 1)
            if len(item) > 2:
                txt[-1] = item[-1]
            l_txt.append("".join(txt))

        encoded_txt = "  ".join(l_txt)
        self.form.text_vocabulary.setText(encoded_txt)

    def show_definition(self, word):
        self.form.text_definition.setText(word.definition)

    def show_encode_word2(self, word):
        """Encode every character by square
        """
        list_word = word.vocabulary.split()
        l_txt = []
        for item in list_word:
            txt = ["\u20DE"] * len(item) 
            l_txt.append("".join(txt))

        encoded_txt = " ".join(l_txt)
        self.form.text_vocabulary.setText(encoded_txt)

    def show_picture_and_tag(self, word):
        self.picture_name = word.picture_name
        
        pixmap = QPixmap(os.path.join(self.controller.media_folder_path, self.picture_name))
        width = pixmap.width()
        height = pixmap.height()
        if height > self.form.picture.height() or width > self.form.picture.width():
            pixmap = pixmap.scaled(self.form.picture.width(), self.form.picture.height(), Qt.KeepAspectRatio)
        self.form.picture.setPixmap(pixmap)

        self.form.text_tag.setText(word.tag)

    def show_word(self, word):
        """Show information depend on test level and hint level
        """
        for l in range(MAX_TEST_LEVEL-1, self.config["test"]-2, -1):
            self.show_function[l](word)

        self.is_correct_answer = False
        self.form.button_check.setEnabled(True)
        self.form.button_show_answer.setEnabled(True)
        self.form.label_top.setText("Đáp án của bạn là")
        self.form.label_bottom.setText("")
        self.learn_value = 0
        self.record_name = word.record_name

    #Check base on hint level
    def check_incorrect_character(self, word, answer):
        if self.config["test"] > 6:
            list_word = word.vocabulary.split()
            l_txt = []
            for item in list_word:
                txt = [HIDDEN_CHARACTER] * len(item) 
                l_txt.append("".join(txt))

            encoded_txt = " ".join(l_txt)
            self.form.label_top.setText(encoded_txt)

    def check_longest_common_string(self, word, answer):
        
        def red(char):
            return "<span style='color:red'>" + char + "</span>"

        voca = word.vocabulary
        string_matcher = SequenceMatcher(None, voca, answer).find_longest_match(0, len(voca), 0, len(answer))
        if self.config["test"] > 6:
            if self.config["hint"] == 2:
                txt = "Xâu chung dài nhất là: " + answer[string_matcher.b:string_matcher.b + string_matcher.size]
                self.form.label_top.setText(txt)                
        else:
            #highlight incorrect character in red
            if string_matcher.size == 0:
                txt = red(answer)
            else:
                txt = voca[string_matcher.a: string_matcher.a + string_matcher.size]
                l = len(voca)-1
                for i in range(string_matcher.b+ string_matcher.size, len(answer),1):
                    if string_matcher.a - string_matcher.b + i > l:
                        txt = "{}{}".format(txt,red(answer[i:len(answer)]))
                        break
                    else:
                        if voca[string_matcher.a - string_matcher.b + i] == answer[i]:
                            txt = "{}{}".format(txt,answer[i])
                        else: 
                            txt = "{}{}".format(txt, red(answer[i]))  
                for i in range(string_matcher.b-1, -1, -1):
                    if string_matcher.a - string_matcher.b + i < 0:
                        txt = "{}{}".format(red(answer[0:i+1]), txt)
                        break
                    else:
                        if voca[string_matcher.a - string_matcher.b + i] == answer[i]:
                            txt = "{}{}".format(answer[i], txt)
                        else: 
                            txt = "{}{}".format(red(answer[i]), txt)
            #txt = "<html>" + txt + "</html>"
            self.form.label_top.setText(txt)
            #print(txt)

    def check_record(self, word, answer):
        if self.config["test"] > 3:
            self.form.label_bottom.setText("Bạn nghe phát âm nhé")
            self.form.button_play_record.setEnabled(True)

    def check_nothing(self, word, answer):
        if answer == word.vocabulary:
            self.record_name = word.record_name
            self.form.button_play_record.setEnabled(True)

    def check_answer(self, word):

        self.form.label_top.setText("")
        self.form.label_bottom.setText("")
        answer = utils.format_string(self.form.text_answer.displayText())
        if (answer == ""):            
            self.form.label_bottom.setText("<p style='color:red'>Bạn chưa điền đáp án</p>")
            return
        if answer == word.vocabulary:
            self.form.button_next.setEnabled(True)
            self.form.label_bottom.setText("<p style='color:green'>Chính xác")
            self.is_correct_answer = True
            return
        if not utils.is_invalid_string(answer):
            self.form.label_bottom.setText("<p style='color:red'>Kí tự không hợp lệ `~!@#$%^&*()+=_<>?/\|;[]{}</p>")
            return
        else:
            self.form.label_bottom.setText("<p style='color:red'>Chưa chính xác")
        for c in range(MAX_HINT_LEVEL-1, self.config["hint"]-2, -1):
            self.check_function[c](word, answer)
        
 
        