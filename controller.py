import ui 
import check
import mod

def button_click():  
    '''
    Функция запускает основное меню и в зависимиости от выбора пользователя реализует дальнейший алгоритм.
    '''  
    ui.print_color("Основное меню.", "green")
    action = check.check_action(5, "menu1")
    if action == 1:  # Поиск     
        mod.search_note(ui.input_search())
    elif action == 2: # Запись
        title, text = ui.input_note()
        mod.add_note(title, text)
    elif action == 3: # Печать
        mod.print_notes()    
    elif action == 4: # Редакция/Удаление
        ui.print_color("Какую заметку Вы хотите редактировать/удалить? Воспользуйтесь поиском!", "yellow")
        mod.search_note(ui.input_search())
    elif action == 5: # Выход
        ui.print_color("До свидания!", "green")
        exit

def choose_action(array_found):
    '''
    Функция запускает дополнительное меню и в зависимиости от выбора пользователя реализует дальнейший алгоритм.
    '''
    action = check.check_action(3, "menu2")    
    if action == 1: # Редактировать
        if len(array_found) > 1:
            ID = check.check_id(array_found)
        else:
            ID = array_found[0]["id"]
        choose_key(ID)
    elif action == 2: #Удалить
        if len(array_found) > 1:
            ID = check.check_id(array_found)
        else:
            ID = array_found[0]["id"]
        mod.delete_note(ID)    
    elif action == 3: #Выход в меню
        button_click()

def choose_key(ID):
    '''
    Функция запускает дополнительное меню и в зависимиости от выбора пользователя реализует дальнейший алгоритм.
    '''
    action = check.check_action(3, "menu3")
    if action == 1:  # title
        title = str(input("\033[43mВведите новый заголовок: \033[0m"))
        mod.redaction(ID, title, "title") 
    elif action == 2:  # text
        text = str(input("\033[43mВведите новый текст: \033[0m")) 
        mod.redaction(ID, text, "text") 
    elif action == 3: #Выход в меню
        button_click()
        