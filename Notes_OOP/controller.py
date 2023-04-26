import notes_view
import model
from Note import Note

def start():
    value =''
    while True:
        value = notes_view.menu()
        match value:
            case 1:
                # Show a list of notes
                pass
            case 2:
                # Create a new note
                new_note = model.add_new_note(notes_view.create_note()) # notes_view.create_note() => ('', '')
                print(Note.get_descriptive_long(new_note))
                print(Note.get_descriptive_short(new_note))
                notes_view.information(f'\nНовая заметка добавлена\n')
            case 3:
                # Show a note
                pass
            case 4:
                # Update a note
                pass
            case 5:
                # Delete a note
                pass
            case 6:
                # Exit
                notes_view.end_prog()
                break