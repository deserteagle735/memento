from interface.qt import *


class DB(object):
    
    def __init__(self, path, first_run=False):
        self.connection = QSqlDatabase.addDatabase("QSQLITE")
        self.connection.setDatabaseName(path)
        self.connection.open()
        if first_run:
            self.create_database()

    def create_database(self): 
        query = QSqlQuery(self.connection)
        query.exec_("""
            create table word (
                vocabulary text not null,                
                category text not null,
                phonetic text,
                hint text,
                definition text not null,
                tag text,
                picture_name text,
                record_name text,
                level int default 1,
                create_at text default current_timestamp,
                constraint constraint_pk primary key (vocabulary, definition)
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
        
    def close(self):
        self.connection.close()
        self.connection.removeDatabase()



