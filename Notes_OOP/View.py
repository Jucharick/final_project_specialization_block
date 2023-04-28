class View():
    '''UI'''

    COMMANDS = ['Показать список заметок',
                'Создать новую заметку',
                'Показать заметку',
                'Изменить',
                'Удалить',
                'Выход из программы']

    def __init__(self):
        pass

    def menu():
        print('Главное меню:')
        for i, item in enumerate(View.COMMANDS, 1):
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

    def create_note():
        name = input('Тема: ')
        body = input('Заметка: ')
        return name, body

    def end_prog():
        print()
        print('Работа в программе завершена')
        print()

    def information(message):
        print(message)