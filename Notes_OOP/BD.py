class BD():
    '''Работа с базой данных'''

    PATH = 'C:/Users/Юлия Чарикова/Desktop/GeekBrains/I четверть - блок 2/final_project_specialization_block/Notes_OOP/data.csv'

    def __init__(self):
        pass

    # def open_file():
    #     with open(BD.PATH, 'r', encoding='utf-8') as data:
    #         file = data.readlines()
    #     for note in file:
    #         BD.NOTES_BOOK.append(note.strip().split(','))
    #     return file

    def save_file(state: dict):
        try:
            with open(BD.PATH, 'a', encoding='utf-8') as data:
                for value in state.values():
                    data.write(str(value) + ',')  
        except:
            print("Ошибка при работе с файлом")
