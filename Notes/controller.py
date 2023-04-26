import view
import model


def start():
    value =''
    model.open_file()
    while True:
        value = view.menu()
        match value:
            case 1:
                # Show a list of notes
                view.show_notes(model.get_notes_book())
            case 2:
                # Create a new note
                new_note = list(view.create_note())
                model.add_new_note(new_note)
                view.information(f'\nНовая заметка добавлена\n')
            case 3:
                # Show a note
                show_select_note = model.get_note(view.select_note('Введите ID или тему заметки: '))
                if show_select_note:
                    view.view_note(show_select_note)
                elif show_select_note == []:
                    view.empty_request()
                else:
                    view.many_request()
            case 4:
                # Update a note
                upd_select_note = model.get_note(view.select_note('Для редактирования заметки введите ее ID или тему: '))
                if upd_select_note:
                    upd_student = view.change_note_input()
                    model.update_note(upd_select_note[1], list(upd_student))
                    view.information(f'\nРедактирование заметки {upd_select_note[0][0]} завершено\n')
                elif upd_select_note == []:
                    view.empty_request()
                else:
                    view.many_request()
            case 5:
                # Delete a note
                del_select_note = model.get_note(view.select_note('Введите ID или тему заметки для удаления: '))
                if del_select_note:
                    confirm = view.delete_confirm(del_select_note[0][0])
                    if confirm:
                        model.del_note(del_select_note[0])  
                        view.information(f'\nЗаметка {del_select_note[0][0]} удалена\n')
                elif del_select_note == []:
                    view.empty_request()
                else:
                    view.many_request()
            case 6:
                # Exit
                model.save_file()
                view.end_prog()
                break
