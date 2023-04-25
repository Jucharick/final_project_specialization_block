commands = ['Создать новую заметку',
            'Сохранить',
            'Просмотр',
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



def end_prog():
    print()
    print('Работа в программе завершена')
    print()