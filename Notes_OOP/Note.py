from datetime import datetime

class Note():
    def __init__(self, id_note: str, name: str, body: str, date_note: datetime):
            self.id = id_note
            self.name = name
            self.body = body
            self.date_note = date_note

    def get_descriptive_long(self):
        long_str = f"{self.id} {self.name} {self.date_note.strftime('%Y-%m-%d %H:%M:%S')} {self.body}"
        return long_str.title()

    def get_descriptive_short(self):
        short_str = f"{self.id} {self.name} {self.date_note.strftime('%Y-%m-%d %H:%M:%S')}" 
        return short_str.title()

    def get_id_note():
        return 1
    
    def get_date():
         return datetime.now()
