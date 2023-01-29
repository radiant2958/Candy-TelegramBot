number_class=''
def show_menu() -> int:
    print("Меню журнала")
    print('Припервом запуске необходимо вначале открыть журнал нужного класса')
    menu_list = [
        "Открыть журнал класса",
        "Открыть предмет",
        "Открыть оценки ученика по всем предметам",
        "Начать урок",
        "Выход",
        
    ]
    for i in range(len(menu_list)):
        print(f"  {i+1}. {menu_list[i]}")
    user_input = int(input("Введите команду:> "))
    return user_input


def input_class():
    global number_class
    number_class = input("Введите номер и букву класса без пробела: ").upper()
    number_class += ".txt"
    return number_class


def print_journal(data: dict):
    for k, v in data.items():
        print(k, ":")
        for key, value in v.items():
            print(key, "оценки", value)
        print()


def open_lesson(data: dict):
    if len(data) < 0:
        print("Журнал не открыт, откройте журнал класса")
    else:
        lesson = input("Введите названия предмета: ").lower()
    for k, v in data.items():
        if k == lesson:
            print(k, ":")
            for key, value in v.items():
                print(key, "оценки", value)
        print()
    return lesson


def exit_journal():
    print("Завершение программы")
    exit()


def open_popil(data: dict):
    if len(data) < 0:
        print("Журнал не открыт, откройте журнал класса")
    else:
        popil = input("Введите фамилию и имя ученика: ").upper()
        for k, v in data.items():
            print(k, ":")
            for key, value in v.items():
                if key == popil:
                    print(key, "оценки", value)
    print()


def new_lesson(data: str)->str:
    if len(data)>0:
        lesson=input('введите урок: ').lower()
        return lesson
    else:
        print('Журнал не открыт, откройте журнал нужного класса')

def who_answer():
    student=input('Кто отвечает: ').upper()
    return student

def what_mark():
    grand=input('что поставим? ')
    return grand
