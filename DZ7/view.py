def show_menu() -> int:
    print("Меню")
    menu_list = [
        "Показать все контакты",
        "Открыть файл",
        "Сохранить файл",
        "Создать контакт",
        "Изменить контакт",
        "Удалить контакт",
        "Найти контакт",
        "Выход",
    ]
    for i in range(len(menu_list)):
        print(f"  {i+1}. {menu_list[i]}")
    user_input = int(input("Введите команду:> "))
    return user_input


def show_all(db: list):
    if len(db) > 0:
        for i in range(len(db)):
            user_id = i + 1
            print(user_id, end=". ")
            for v in db[i].values():
                print(v, end=" ")
            print()
    else:
        print("Телефоная книга не открыта")


def db_success(db: list):
    if db:
        print("телефонная книга открыта")
        return True
    else:
        print("Телефоная книга не открыта")
        return False


def exit_pro():
    print("Завершение программы")
    exit()


def create_contact():
    print("Создаем новый контакт в телефонной книге")
    new_contact = {}
    new_contact["lastname"] = input("ВВедите фамилию: ")
    new_contact["fersttname"] = input("ВВедите имя: ")
    new_contact["phone"] = input("ВВедите номер телефона: ")
    new_contact["comment"] = input("ВВедите коментарий: ")
    return new_contact

def input_contact(db: list): 
    lasN=input('Введите фамилию контакта c заглавной буквы, который необходим для дальнейших действий: ')
    l=None
    for i in range(len(db)):
            if lasN in db[i].values():
                l=int(i)
    return l

def output_seach_contact(db: list): #вывод нужного контакта
    l=input_contact(db) 
    if l != None:
        for c in db[l].values():
            print(c, end=' ')
    else:
        print('Такого контакта нет ')
    print()
                        

def change_new_data():
    new_contact = {}
    print('Введите новые данные для изменения или повторите прежние')
    new_contact["lastname"] = input("ВВедите фамилию: ")
    new_contact["fersttname"] = input("ВВедите имя: ")
    new_contact["phone"] = input("ВВедите номер телефона: ")
    new_contact["comment"] = input("ВВедите коментарий: ")
    return new_contact
    
    


                


    
    