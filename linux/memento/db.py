from interface.qt import *
from memento.word import Word           

MAX_CORRECT = 3     
MAX_LEVEL = 5      

class DB(object):
    
    def __init__(self, path, first_run=False):
        try:
            QSqlDatabase.drivers().index("QSQLITE")
        except:
            QMessageBox.critical(None, "Unable to load databse", "Memento needs SQLITE driver")

        self.connection = QSqlDatabase.addDatabase("QSQLITE")
        self.connection.setDatabaseName(path)
        try:
            self.connection.open()
        except err:
            if err != QSqlError.NoError():
                QMessageBox.critical(None, "Unable to initialize database", "Error while initializing database " + str(err)          )
                return

        
        if first_run:
            self.create_database()

    def create_database(self): 
        query = QSqlQuery(self.connection)
        query.exec_("""create table word (
id integer primary key autoincrement,
vocabulary text not null,                
category text not null,
phonetic text,
hint text,
definition text not null,
tag text,
picture_name text,
record_name text,
level int default 0,
met int default 0,
correct int default 0,
create_at text default (date('now', 'localtime'))
);""")
    
    def add_word(self, word):
        query = QSqlQuery(self.connection)
        query.prepare(
"""insert into word 
(vocabulary, category, phonetic, 
hint, definition, tag,
picture_name, record_name )
values
(?,?,?,?,?,?,?,?)""")
        query.addBindValue(word.vocabulary)
        query.addBindValue(word.category)
        query.addBindValue(word.phonetic)
        query.addBindValue(word.hint)
        query.addBindValue(word.definition)
        query.addBindValue(word.tag)
        query.addBindValue(word.picture_name)
        query.addBindValue(word.record_name)
        query.exec_()
    
    def edit_word(self, word):
        query = QSqlQuery(self.connection)
        query.prepare(
"""update word 
set 
vocabulary = ?, 
category = ?, 
phonetic = ?, 
hint = ?, 
definition = ?,
tag = ?,
picture_name = ?, 
record_name = ?
where id = ? 
""")
        query.submitAlladdBindValue(word.vocabulary)
        query.addBindValue(word.category)
        query.addBindValue(word.phonetic)
        query.addBindValue(word.hint)
        query.addBindValue(word.definition)
        query.addBindValue(word.tag)
        query.addBindValue(word.picture_name)
        query.addBindValue(word.record_name)
        query.addBindValue(word.id)
        query.exec_()

    def start_model(self):
        model = QSqlTableModel(parent=None, db=self.connection)
        model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        model.setTable("word")
        model.setQuery(QSqlQuery(
"""select id,
vocabulary,
category,
phonetic,
hint,
definition,
tag,
picture_name,
record_name,
level,
met,
correct,
create_at from word""", 
        self.connection))

        #setup model
        record = model.record(0)
        model.setHeaderData(record.indexOf("vocabulary"), Qt.Horizontal, "Từ mới")
        model.setHeaderData(record.indexOf("category"), Qt.Horizontal, "Từ loại")
        model.setHeaderData(record.indexOf("definition"), Qt.Horizontal, "Dịch nghĩa")
        model.setHeaderData(record.indexOf("tag"), Qt.Horizontal, "Thẻ")
        model.setHeaderData(record.indexOf("level"), Qt.Horizontal, "Trình độ")
        model.setHeaderData(record.indexOf("met"), Qt.Horizontal, "Gặp")
        model.setHeaderData(record.indexOf("correct"), Qt.Horizontal, "Đúng")
        #model.setHeaderData(12, Qt.Horizontal, "Ngày thêm")
        model.setHeaderData(record.indexOf("create_at"), Qt.Horizontal, "Ngày thêm")
        return model
        
    def search(self, field, text):
        sql = ""
        if field == "all":
            sql = " 1 = 1"
        elif field == "level":
            if text == "":
                return
            sql = field + " = " + text
            
        elif field == "today":
            #sql =  "date(create_at,'localtime') = date('now','localtime')"
            sql =  "create_at = date('now','localtime')"
        elif field == "create_at":
            if text == "":
                return
            #sql = "date(create_at,'localtime') like '%" + text + "%'"
            sql = "create_at like '%" + text + "%'"
        else:
            if text == "":
                return
            sql = field + " like \'%" + text + "%\'"
        return self.search_db(sql)
        
    def search_db(self, condition):
        model = QSqlTableModel(parent=None, db=self.connection)
        model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        model.setTable("word")
        sql = """select id,
vocabulary,
category,
phonetic,
hint,
definition,
tag,
picture_name,
record_name,
level,
met,
correct,
create_at from word """ + "where " + condition
        #print(sql)
        model.setQuery(QSqlQuery(sql, self.connection))
        record = model.record(0)
        model.setHeaderData(record.indexOf("vocabulary"), Qt.Horizontal, "Từ mới")
        model.setHeaderData(record.indexOf("category"), Qt.Horizontal, "Từ loại")
        model.setHeaderData(record.indexOf("definition"), Qt.Horizontal, "Dịch nghĩa")
        model.setHeaderData(record.indexOf("tag"), Qt.Horizontal, "Thẻ")
        model.setHeaderData(record.indexOf("level"), Qt.Horizontal, "Trình độ")
        model.setHeaderData(record.indexOf("met"), Qt.Horizontal, "Gặp")
        model.setHeaderData(record.indexOf("correct"), Qt.Horizontal, "Đúng")
        model.setHeaderData(record.indexOf("create_at"), Qt.Horizontal, "Ngày thêm")
        
        return model


    def get_words(self, maxlevel, quantity, field, tag=""):
        list_words = []
        if field == 0:
        # for all
            short = 0
            for level in range(maxlevel-1, -1, -1):
                query = QSqlQuery(db=self.connection)
                query.prepare(
"""select 
id,
vocabulary,
category,
phonetic,
hint,
definition,
tag,
picture_name,
record_name,
level,
met,
correct from word
where level = ? 
order by correct asc, met asc
limit ?""")
                query.addBindValue(level)
                query.addBindValue(quantity[level] + short)
                query.exec_()
                count = 0        
                while(query.next()):
                    count += 1
                    w = Word(
                        id= query.value(0),
                        vocabulary= query.value(1),
                        category= query.value(2),
                        phonetic= query.value(3),
                        hint= query.value(4),
                        definition= query.value(5),
                        tag= query.value(6),
                        picture_name= query.value(7),
                        record_name= query.value(8),
                        level= query.value(9),
                        met= query.value(10),
                        correct= query.value(11)
                    )
                    list_words.append(w)
                short = quantity[level] + short - count

        elif field == 1:
            # by tag
            short = 0
            for level in range(maxlevel-1, -1, -1):
                query = QSqlQuery(db=self.connection)
                query.prepare(
"""select 
id,
vocabulary,
category,
phonetic,
hint,
definition,
tag,
picture_name,
record_name,
level,
met,
correct from word
where level = ? and tag like ?
order by correct asc, met asc
limit ?""")
                query.addBindValue(level)
                query.addBindValue("%"+ tag + "%")
                query.addBindValue(quantity[level] + short)
                query.exec_()
                count = 0        
                while(query.next()):
                    count += 1
                    w = Word(
                        id= query.value(0),
                        vocabulary= query.value(1),
                        category= query.value(2),
                        phonetic= query.value(3),
                        hint= query.value(4),
                        definition= query.value(5),
                        tag= query.value(6),
                        picture_name= query.value(7),
                        record_name= query.value(8),
                        level= query.value(9),
                        met= query.value(10),
                        correct= query.value(11)
                    )
                    list_words.append(w)
                short = quantity[level] + short - count
        elif field == 2:
            # added today
            short = 0
            for level in range(maxlevel-1, -1, -1):
                query = QSqlQuery(db=self.connection)
                query.prepare(
"""select 
id,
vocabulary,
category,
phonetic,
hint,
definition,
tag,
picture_name,
record_name,
level,
met,
correct from word
where level = ? and create_at = date('now', 'localtime')
order by correct asc, met asc
limit ?""")
                query.addBindValue(level)
                query.addBindValue(quantity[level] + short)
                query.exec_()
                count = 0        
                while(query.next()):
                    count += 1
                    w = Word(
                        id= query.value(0),
                        vocabulary= query.value(1),
                        category= query.value(2),
                        phonetic= query.value(3),
                        hint= query.value(4),
                        definition= query.value(5),
                        tag= query.value(6),
                        picture_name= query.value(7),
                        record_name= query.value(8),
                        level= query.value(9),
                        met= query.value(10),
                        correct= query.value(11)
                    )
                    list_words.append(w)
                short = quantity[level] + short - count
        return list_words

    def update_learn_data(self, word, correct=False):
        if correct == True:
            if word.correct == MAX_CORRECT:
                if word.level < MAX_LEVEL - 1:
                    word.level += 1
                    word.correct = 0
            else:
                word.correct += 1
        else: 
            word.level -= 1
            if word.level < 0:
                word.level = 0
        word.met += 1
        query = QSqlQuery(db=self.connection)
        query.prepare(
"""update word
set level = ?, met = ?, correct = ?
where id = ?""")
        query.addBindValue(word.level)
        query.addBindValue(word.met)
        query.addBindValue(word.correct)
        query.addBindValue(word.id)
        query.exec_()

    def close(self):
        self.connection.close()
        self.connection.removeDatabase("SQLITE")



