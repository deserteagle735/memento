import datetime
class Word(object):

    def __init__(self,
                id=None,
                vocabulary="test",
                category="test",
                phonetic = "",
                hint = "",
                definition="test",
                tag = "",
                picture_name = "",
                record_name = "",
                level= 0,
                met= 0,
                correct= 0):
        self.id = id
        self.vocabulary = vocabulary
        self.category = category
        self.phonetic = phonetic
        self.hint = hint
        self.definition = definition
        self.tag = tag
        self.picture_name = picture_name
        self.record_name = record_name
        self.level = level
        self.met = met
        self.correct = correct
    
    


