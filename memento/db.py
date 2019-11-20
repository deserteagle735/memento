from interface.qt import *
           
            
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
        query.exec_("""
            create table word (
                id integer primary key autoincrement,
                vocabulary text not null,                
                category text not null,
                phonetic text,
                hint text,
                definition text not null,
                tag text,
                picture_name text,
                record_name text,
                level int default 1,
                count int defautt 0,
                create_at text default current_timestamp
            );
        """)
    
    def add_word(self, word):
        query = QSqlQuery(self.connection)
        query.prepare(
            """
            insert into word 
            (vocabulary, category, phonetic, 
            hint, definition, tag,
            picture_name, record_name )
            values
            (?,?,?,?,?,?,?,?) 
            """)
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
            """
            update word 
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
        self.model = QSqlTableModel(parent=None, db=self.connection)
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.setTable("word")
        self.model.setQuery(QSqlQuery("""
            select id,
                    vocabulary,
                    category,
                    phonetic,
                    hint,
                    definition,
                    tag,
                    picture_name,
                    record_name,
                    level,
                    date(create_at,'localtime') as created from word;
        """, self.connection))

        #setup model
        record = self.model.record(0)
        self.model.setHeaderData(record.indexOf("vocabulary"), Qt.Horizontal, "Từ mới")
        self.model.setHeaderData(record.indexOf("category"), Qt.Horizontal, "Từ loại")
        self.model.setHeaderData(record.indexOf("definition"), Qt.Horizontal, "Dịch nghĩa")
        self.model.setHeaderData(record.indexOf("tag"), Qt.Horizontal, "Thẻ")
        self.model.setHeaderData(record.indexOf("Level"), Qt.Horizontal, "Trình độ")
        self.model.setHeaderData(record.indexOf("created"), Qt.Horizontal, "Ngày thêm")
        return self.model
        
    def search(self, field, text):
        if field == "all":
            self.model.setFilter(" 1 = 1")
        elif field == "level":
            if text == "":
                return
            sql = field + " = " + text
            #print(sql)
            self.model.setFilter(sql)
            self.model.select()
        elif field == "today":
            sql =  "date(create_at,'localtime') = date('now','localtime')"
            #print(sql)
            self.model.setFilter(sql)
            self.model.select()
        elif field == "create_at":
            if text == "":
                return
            sql = "date(create_at,'localtime') like '%" + text + "%'"
            #print(sql)
            self.model.setFilter(sql)
            self.model.select()
        else:
            if text == "":
                return
            sql = field + " like \'%" + text + "%\'"
            #print(sql)
            self.model.setFilter(sql)
            self.model.select()
        return self.model
        

    def close(self):
        self.connection.close()
        self.connection.removeDatabase()



