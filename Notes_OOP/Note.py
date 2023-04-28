from datetime import datetime

class Note():
    '''Заметка'''

    ID = 1 # уникальное значение, даже при удалении

    def __init__(self, id_note: int, name: str, body: str, date_note: datetime):
            self.id = id_note
            self.name = name
            self.body = body
            self.date_note = date_note

            Note.ID+=1

    def get_descriptive_long(self):
        long_str = f"{self.id} {self.name} {self.date_note.strftime('%Y-%m-%d %H:%M:%S')} {self.body}"
        return long_str.title()

    def get_descriptive_short(self):
        short_str = f"{self.id} {self.name} {self.date_note.strftime('%Y-%m-%d %H:%M:%S')}" 
        return short_str.title()

    def get_id_note():
        return Note.ID
    
    def get_date():
         return datetime.now()

    def __getstate__(self) -> dict:  # "сохранить" объект класса
        state = {}
        state["id"] = self.id
        state["name"] = self.name
        state["body"] = self.body
        state["date_note"] = self.date_note
        return state

    def __setstate__(self, state: dict):  # "восстановить" объект класса из байтов
        state["id"] = self.id
        state["name"] = self.name
        state["body"] = self.body
        state["date_note"] = self.date_note