from datetime import datetime

notes_book = []
path = 'C:/Users/Юлия Чарикова/Desktop/GeekBrains/I четверть - блок 2/final_project_specialization_block/Notes/data.csv'

def get_notes_book():
    global notes_book
    return notes_book

def open_file():
    global path
    global notes_book
    with open(path, 'r', encoding='utf-8') as data:
        file = data.readlines()
    for note in file:
        notes_book.append(note.strip().split(','))
    return file

def save_file():
    global notes_book
    create_str = []
    for note in notes_book:
        create_str.append(','.join(note))
    with open(path, 'w', encoding='utf-8') as data:
        data.write('\n'.join(create_str))

def add_new_note(new_note: list):
    global notes_book
    new_note.append(str(datetime.now()))
    notes_book.append(new_note)

def get_note(find_note: str):
    global notes_book
    result = []
    for i, note in enumerate(notes_book):
        for field in note:
            if find_note in field:
                result.append((note, i)) 
                break
    if len(result) > 1: # если в список по поиску для удаления добавились больше 1 строки, то мы не можем удалить
        return False
    elif result == []:
        return result
    else:
        return result[0]