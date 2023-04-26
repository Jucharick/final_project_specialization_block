from datetime import datetime
from Note import Note

def add_new_note(id: str, name: str, body: str):
    date_note = datetime.now
    new_note = Note(id, name, date_note, body)
    print(new_note)

