from datetime import datetime as dt
import json
import check
import controller as c
import ui

def add_note(title, text):
    '''
    Функция добавляет новые заметки в файл. Присваивает новой заметке ID, указывает дату создания заметки.
    '''
             
    with open('f.json', 'r', encoding='utf-8') as file:
        try:
            array_all = json.load(file) 
            if len(array_all) > 0:
                id = array_all[-1]["id"]
            else: id = 0
        except ValueError:
            array_all = []
            id = 0
    entry = {"id":id + 1,
             "data":dt.now().strftime('%d.%m.%y'), 
             "title":title, 
             "text":text}   
    array_all.append(entry)     
    write_file(array_all)
    ui.print_color("Заметка добавлена! Переводим в основное меню", "green")
    
    c.button_click()

def print_notes():   
    '''
    Функция выводит на экран весь список заметок из файла
    '''           
    array_all = check.check_list_empty() 
    ui.print_color("Список заметок", "green")
    for i in array_all:
        ui.print_list(i)  
    c.button_click()        

def search_note(data):
    '''
    Функция определяет вхождение элемента поиска в список заметок. Проверка происходит одновременно по ключам
    "data", "title" и "text". Если указать в качестве элемента поиска дату, то функция выведет список всех
    заметок с соответстветствующей датой.
    data - элемент для поиска.
    '''
    array_all = check.check_list_empty()
    array_found = []
    for i in array_all:
        if data in i["title"] or data in i["data"] or data in i["text"]:
            array_found.append(i)
    if len(array_found) == 0:
        ui.print_color("Такой заметки не найдено! Переводим Вас в основное меню.", "red")
        c.button_click()
    else:
        for i in array_found:
            ui.print_list(i)
    c.choose_action(array_found)

def delete_note(ID):
    '''
    Функция удаляет из списка заметку с указанным ID
    ID - ID заметки которую необходимо удалить
    '''
    array_all = check.check_list_empty()
    for i in array_all:
        if i["id"] == ID:
            array_all.remove(i)           
    write_file(array_all)
    ui.print_color("Заметка удалена! Переводим Вас в основное меню.", "green")
    c.button_click()

def redaction(ID, value, key):
    '''
    Функция осуществляет редактирование заметки. 
    ID - ID заметки, которую необходимо отредактировать
    value - новый заголовок или текст заметки
    key - ключ, указывающий, что конкретно необходимо перезаписать
    '''
    array_all = check.check_list_empty()
    if key == "title":
        for i in array_all:
            if i["id"] == ID:
                i["title"] = value   
                i["data"] = dt.now().strftime('%d.%m.%y')
    elif key == "text":
        for i in array_all:
            if i["id"] == ID:
                i["text"] = value   
                i["data"] = dt.now().strftime('%d.%m.%y')
    write_file(array_all)
    ui.print_color("Заметка отредактирована! Переводим Вас в основное меню.", "green")
    c.button_click()

def write_file(array_all):
    '''
    Функция осуществляет запись в файл
    array - массив для записи 
    '''
    with open('f.json', 'w', encoding='utf-8') as file:        
        json.dump(array_all, file, indent=2)
