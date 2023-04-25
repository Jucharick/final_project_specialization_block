import view
import model


def start():
    value =''
    model.open_file()
    while True:
        value = view.menu()
        match value:
            case 1:
                # Показать список заметок
                view.show_notes(model.get_notes_book())
            case 2:
                # Создать новую заметку
                new_note = list(view.create_note())
                model.add_new_note(new_note)
                view.information(f'\nНовая заметка добавлена\n')
            case 3:
                # Показать заметку
                show_select_note = view.select_note('Введите ID или тему заметки: ')
                view.view_note(model.get_note(show_select_note))
            case 4:
                # Изменить
                pass
            case 5:
                # Удалить
                pass
            case 6:
                # Выход из программы
                model.save_file()
                view.end_prog()
                break
