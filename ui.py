
def input_search():     
    '''
    Функция принимает от пользователя поисковый запрос.
    '''
    data = str(input('\033[43mВведите поисковый запрос: \033[0m')) 
    return data 

def get_id():
    '''
    Функция принимает от пользователя ID.
    '''
    ID = int(input("\033[43mУкажите ID заметки для редакции: \033[0m")) 
    return ID
 
def action(menu):
    '''
    Функция отправляет пользователю запрос на выбор пункта меню.
    menu - меню, которое функция предлагает пользователю. 
    '''
    if menu == "menu1":
        action = int(input('\033[43mВыберете цифру соответствующую операции и нажмите "ввод"\033[0m'
                             '\n 1: "Поиск заметки"'
                             '\n 2: "Добавить заметку"'
                             '\n 3: "Вывести все заметки"'                             
                             '\n 4: "Редактировать/Удалить заметку"'
                             '\n 5: "Выход из программы"\n')) 
    elif menu == "menu2":
        action = int(input('\033[43mЧто вы хотитете сделать с заметкой? Выберете цифру соответствующую операции и нажмите "ввод"\033[0m'
                             '\n 1: "Редактировать"' 
                             '\n 2: "Удалить"'
                             '\n 3: "Выход в основное меню"\n')) 
    elif menu == "menu3":
        action = int(input('\033[43mЧто вы хотитете отредактировать? Выберете цифру соответствующую операции и нажмите "ввод"\033[0m'
                             '\n 1: "Заголовок"'
                             '\n 2: "Текст"'
                             '\n 3: "Выход в основное меню"\n'))
    return action 

def input_note():   
    '''
    Функция принимает от пользователя заголовок и текст заметки.
    ''' 
    title = str(input('\033[43mВведите заголовок: \033[0m')) 
    text = str(input('\033[43mВведите текст: \033[0m'))     
    return title, text

def print_color(text, color):
    '''
    Функция отвечает за вывод текста в цветном фоне.
    text - текст для вывода
    color - цвет фона
    '''
    if color == "green":
        print("\033[42m{}\033[0m".format(text))
    if color == "red":
        print("\033[41m{}\033[0m".format(text))
    if color == "yellow":
        print("\033[43m{}\033[0m".format(text))
    if color == "white":
        print("\033[47m{}\033[0m".format(text))

def print_list(i):
    '''
    Функция реализует вывод заметок в определенном формате.
    i - заметка.
    '''
    print(f'\033[47m{i["title"]}\033[0m\n'
    f'ID: {i["id"]}\n'
    f'Дата: {i["data"]}\n'
    f'Текст: {i["text"]}\n')