import interface
from interface.qt import *
import json

TEST_LEVEL_TEXT = {
    1 :""" - Cho biết số lượng từ, số lượng chữ cái, chứ cái đầu và cuối của mỗi từ
 - Hình ảnh minh họa
 - Dịch nghĩa
 - Phiên âm
 - Nghe phát âm
 - Gợi ý
 - Thẻ
""",
    2: """ - Cho biết số lượng từ, số lượng chữ cái, chứ cái đầu và cuối của mỗi từ
 - Hình ảnh minh họa
 - Dịch nghĩa
 - Nghe phát âm
 - Gợi ý
 - Thẻ
""",
    3: """ - Cho biết số lượng từ, số lượng chữ cái, chứ cái đầu và cuối của mỗi từ
 - Hình ảnh minh họa
 - Dịch nghĩa
 - Nghe phát âm
 - Thẻ
""",
    4: """ - Cho biết số lượng từ, số lượng chữ cái, chứ cái đầu và cuối của mỗi từ
 - Hình ảnh minh họa
 - Dịch nghĩa
 - Thẻ
""",
    5: """ - Cho biết số lượng từ, số lượng chữ cái
 - Hình ảnh minh họa
 - Dịch nghĩa
 - Thẻ
""",
    6: """ - Cho biết số lượng từ, số lượng chữ cái
 - Hình ảnh minh họa
 - Thẻ
""",
    7: """ - Hình ảnh minh họa
 - Thẻ
"""
}

HINT_LEVEL_TEXT = {
    1: """ - Cho biết các chữ cái sai
 - Nghe phát âm
""",
    2: """ - Cho biết dãy con chung dài nhất giữa đáp án và câu trả lời của bạn
 - Nghe phát âm
""",
    3: """ - Nghe phát âm
""",
    4: """ - Không có gợi ý
"""
}


class Settings(QDialog):
    def __init__(self, controller):
        QDialog.__init__(self, None, Qt.Window)
        self.controller = controller
        self.config = self.load_config()
        self.setup_ui()
        self.setup_button()
        self.setup_data()
        
    def setup_ui(self):
        self.setup_dialog()
        self.form.combobox_field.setCurrentIndex(self.config["field"])
        self.form.spinbox_test_level.setValue(self.config["test"])
        self.form.spinbox_hint_level.setValue(self.config["hint"])
        self.show()

    def setup_dialog(self):
        # main window
        from interface.form import settings
        self.form = interface.form.settings.Ui_Dialog()
        self.form.setupUi(self)
    
    def setup_button(self):
        self.form.button_save.clicked.connect(self.button_save_clicked)
        self.form.button_cancel.clicked.connect(self.button_cancel_click)
        self.form.spinbox_test_level.valueChanged.connect(self.spinbox_test_level_value_changed)
        self.form.spinbox_hint_level.valueChanged.connect(self.spinbox_hint_level_value_changed)

    def load_config(self):
        file = "./config.json"
        with open(file, "r") as config_file:
            config = json.load(config_file)

        return config

    def save_config(self):
        file = "./config.json"
        self.config["field"] = self.form.combobox_field.currentIndex()
        self.config["test"] = self.form.spinbox_test_level.value()
        self.config["hint"] = self.form.spinbox_hint_level.value()

        with open(file, "w") as config_file:
            json.dump(self.config, config_file)

    def spinbox_test_level_value_changed(self):
        self.setup_data()

    def spinbox_hint_level_value_changed(self):
        self.setup_data()

    def button_save_clicked(self):
        self.save_config()
        self.close()
  
    def button_cancel_click(self):
        self.close()

    def setup_data(self):
        test_level = self.form.spinbox_test_level.value()
        hint_level = self.form.spinbox_hint_level.value()

        text = "MỨC ĐỘ CÂU HỎI\n" + TEST_LEVEL_TEXT[test_level] + "MỨC ĐỘ GỢI Ý\n" + HINT_LEVEL_TEXT[hint_level]

        self.form.textBrowser.setText(text)



