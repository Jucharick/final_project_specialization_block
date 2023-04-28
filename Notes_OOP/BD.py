import pickle


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

    # def save_file():
    #     create_str = []
    #     for note in BD.NOTES_BOOK:
    #         create_str.append(','.join(note)) 
    #     with open(BD.PATH, 'w', encoding='utf-8') as data:
    #         data.write('\n'.join(create_str))  
    
    def save_file(state: dict):
        try:
            with open(BD.PATH, "wb") as fp:
                pickle.dump(state, fp)
            fp.close()
        except:
            print("Ошибка при работе с файлом")

    def open_file():
        try:
            with open(BD.PATH, "rb") as fp:
                    file = pickle.load(fp)
                    return file
        except:
            print("Ошибка при работе с файлом")