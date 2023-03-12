import ui
import controller as c
import json

def check_action(n, menu):
    '''
    Функция проверяет на корректность ввода цифры, соответствующей команды.
    n -  количество команд в меню
    menu - конкретное меню
    '''    
    while True:
        try:
            action = ui.action(menu)
            if action > 0 and action < n + 1:
                break
            else:
                ui.print_color('Вы ввели не корректное значение!', "red")
        except ValueError:
            ui.print_color('Вы ввели не число!', "red")
    return action  

def check_list_empty():
    '''
    Функция проверяет наличие заметок в файле. Если файл пуст, 
    выводит соответствующее сообщение. Возвращает список заметок, если они есть.
    '''
    
    with open('f.json', 'r', encoding='utf-8') as file:
            try:
                array_all = json.load(file) 
                if len(array_all) > 0:
                    return array_all    
                else:     
                    ui.print_color("Список пуст! Переводим в основное меню.", "red")
                    c.button_click()                
            except ValueError:            
                ui.print_color("Список пуст! Переводим в основное меню.", "red")
                c.button_click() 
 
def check_id(array_all):
    '''
    Функция проверяет корректность ввода ID. 
    1. Должно быть введено целое число.
    2. ID должен быть из списка найденых заметок.
    '''
    array_id = []
    while True:
        try:
           ID = ui.get_id()
           for i in array_all:
            array_id.append(i["id"])
           if ID in array_id:                           
                return ID                
           else:
                ui.print_color('Вы ввели не корректный ID!', "red")
        except ValueError:
            ui.print_color('Вы ввели не число!', "red")
     