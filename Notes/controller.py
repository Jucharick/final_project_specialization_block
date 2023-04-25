# 'Показать список заметок',
# 'Создать новую заметку',
# 'Показать заметку',
# 'Изменить',
# 'Удалить',
# 'Выход из программы'

import view
import model


def start():
    value =''
    model.open_file()
    while True:
        value = view.menu()
        match value:
            case 1:
                view.show_notes(model.get_notes_book())
            case 2:
                new_note = list(view.create_note())
                model.add_new_note(new_note)
                view.information(f'\nНовая заметка добавлена\n')
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                model.save_file()
                view.end_prog()
                break
