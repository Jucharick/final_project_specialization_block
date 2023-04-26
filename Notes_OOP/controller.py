import notes_view
import model

def start():
    value =''
    while True:
        value = notes_view.menu()
        match value:
            case 1:
                # Показать список заметок
                pass
            case 2:
                # Создать новую заметку
                print(notes_view.create_note())
                # model.add_new_note(notes_view.create_note())
                notes_view.information(f'\nНовая заметка добавлена\n')
            case 3:
                # Показать заметку
                pass
            case 4:
                # Изменить
                pass
            case 5:
                # Удалить
                pass
            case 6:
                # Выход из программы
                notes_view.end_prog()
                break