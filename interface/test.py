from interface.qt import *
import interface
import interface.audio
from memento.word import Word
from difflib import SequenceMatcher
import json
import os

MAX_TEST_LEVEL = 7
MAX_HINT_LEVEL = 4

class Test(QDialog):
    
    def __init__(self, controller):
        QDialog.__init__(self, None, Qt.Window)
        self.controller = controller
        self.picture_name = ""
        self.record_name = ""

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

        self.config = self.load_config()
        self.setModal(True)
        self.setup_ui()   
        
        #get words
        self.words = self.get_words()
        self.current_index = 0
        if (len(self.words) == 0):
            pass
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

    def load_config(self):
        file = "./config.json"
        with open(file, "r") as config_file:
            config = json.load(config_file)

        return config     

    def setup_button(self):  
        self.form.button_play_record.clicked.connect(self.button_play_record_clicked)
        self.form.button_check.clicked.connect(self.button_check_clicked)
        self.form.button_next.clicked.connect(self.button_next_clicked)

        self.form.button_play_record.setDisabled(True)
        self.form.button_next.setDisabled(True)

    def button_check_clicked(self):
        self.check_answer(self.words[self.current_index])

    def button_next_clicked(self):
        self.form.button_next.setDisabled(True)
        self.current_index += 1
        if self.current_index == len(self.words):
            return
        else:
            self.form.button_play_record.setDisabled(True)

    def button_play_record_clicked(self):
        if self.record_name != "":
            interface.audio.play_audio(self.controller.media_folder_path, self.record_name)

    #Retrieve word from database
    def get_words(self):
         #test
        w = Word(
            id= 1,
            vocabulary= "cat",
            category="n - danh từ",
            phonetic="két",
            hint="meow meow",
            definition= "con mèo",
            tag= "động vật",
            picture_name= "1574131646.859594.png",
            record_name= "1574266730.578919.wav"
        )

        return [w]

    # Funtion to show word
    def show_phonetic(self, word):
        self.form.text_phonetic.setText(word.phonetic)

    def show_hint(self, word):
        self.form.text_hint.setText(word.hint)

    def set_record(self, word):
        self.record_name = word.record_name
        self.form.button_play_record.setEnabled(True)

    def show_encode_word1(self, word):
        """Encode every character by square
        except first and last character of each word
        """
        list_word = word.vocabulary.split()
        l_txt = []
        for item in list_word:
            txt = [item[0]] + ["\u20DE"] * (len(item) - 1)
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

    #Check base on hint level
    def check_incorrect_character(self, word, answer):
        if self.config["test"] > 6:
            list_word = word.vocabulary.split()
            l_txt = []
            for item in list_word:
                txt = ["\u20DE"] * len(item) 
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
            #cho biết các chữ cái sai
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
                        txt = "{}{}".format(red(answer[0:i]), txt)
                        break
                    else:
                        if voca[string_matcher.a - string_matcher.b + i] == answer[i]:
                            txt = "{}{}".format(answer[i], txt)
                        else: 
                            txt = "{}{}".format(red(answer[i]), txt)
            #txt = "<html>" + txt + "</html>"
            self.form.label_top.setText(txt)
            print(txt)

    def check_record(self, word, answer):
        if self.config["test"] > 4:
            self.form.label_bottom.setText("Bạn nghe phát âm nhé")
            self.record_name = word.record_name
            self.form.button_play_record.setEnabled(True)

    def check_nothing(self, word, answer):
        if answer == word.vocabulary:
            self.record_name = word.record_name
            self.form.button_play_record.setEnabled(True)

    def check_answer(self, word):

        def format_string(string):
            #invalid = "!@#$%^&*\"\|<>?-+()"

            result = string.strip()
            if result == "":
                return result
            w = []
            
            for i in range(len(result)-1):
                #if result[i] in invalid:
                #    continue
                if result[i] == " " and result[i+1] == " ":
                    continue
                w.append(result[i])

            w.append(result[-1])
            result = "".join(w)
            return result

        answer = format_string(self.form.text_answer.displayText())
        if answer == word.vocabulary:
            self.form.button_next.setEnabled(True)
            self.form.label_bottom.setText("<p style='color:green'>Chính xác")
            return
        else:
            self.form.label_bottom.setText("<p style='color:Red'>Chưa chính xác")
        for c in range(MAX_HINT_LEVEL-1, self.config["hint"]-2, -1):
            self.check_function[c](word, answer)
        
        
 
        