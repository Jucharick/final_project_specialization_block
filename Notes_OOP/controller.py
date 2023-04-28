from Note import Note
from View import View
from Commands import Commands
from BD import BD

def start():
    value =''
    while True:
        value = View.menu()
        BD.open_file()
        match value:
            case 1:
                # Show a list of notes
                print(BD.open_file())
            case 2:
                # Create a new note
                new_note = Commands.add_note(View.create_note())
                print(Note.get_descriptive_long(new_note))
                BD.save_file(Note.__getstate__(new_note))
                View.information(f'\nНовая заметка добавлена\n')
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
                View.end_prog()
                break