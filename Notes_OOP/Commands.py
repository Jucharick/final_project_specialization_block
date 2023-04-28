from Note import Note
from BD import BD

class Commands():
    '''Комманды для работы с заметками'''

    def add_note(new_note: list):
        create_new_note = Note(Note.get_id_note(), new_note[0], new_note[1], Note.get_date())
        return create_new_note
    

    