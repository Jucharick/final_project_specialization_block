commands = ['Показать список заметок',
            'Создать новую заметку',
            'Показать заметку',
            'Изменить',
            'Удалить',
            'Выход из программы']

def menu():
    print('Главное меню:')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}. {item}') # \t табуляция 
    while True:
        try: # try except пробует преобразовать input в int и если пользователь вводит букву или символ => ValueError: print('Введите корректное значение')
            request = int(input('Выберите пункт меню: '))
            if 0 < request < 7:
                return request
            else:
                print('Введите значение от 1 до 7')
        except ValueError:
            print('Введите корректное значение')

def show_notes(note_list: list):
    if len(note_list) < 1:
        print()
        print('Заметок нет')
    else:
        print()
        for i, note in enumerate(note_list, 1):
            # print(f'\t{i}. {note[0][0]:7} {note[0][1]:15} {note[1].strftime("%Y-%m-%d %H:%M:%S")}') # [0][0] - id, [0][1] - name, [0][2] - body, [1] - date
            # print(f'\t{i}. {note[0][0]:7} {note[0][1]:15} {note[1][0:19]}') # [0][0] - id, [0][1] - name, [0][2] - body, [1] - date
            print(f'\t{i}. {note[0]:7} {note[1]:15} {note[3][0:19]}') # 0 - id, 1 - name, 2 - body, 3 - date
    print()

def create_note():
    id = input('ID: ')
    name = input('Тема: ')
    body = input('Заметка: ')
    return id, name, body

def end_prog():
    print()
    print('Работа в программе завершена')
    print()

def information(message):
    print(message)