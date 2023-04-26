from datetime import datetime

class Note():
    def __init__(self, id_note: str, name: str, date_note: datetime, body: str):
            self.id = id_note
            self.name = name
            self.body = body
            self.date_note = date_note
