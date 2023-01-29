my_class = {}

def read_data(path: str) -> dict:
    global my_class
    with open(path, "r", encoding="UTF-8") as file:
        temp = file.readlines()
        my_list = []
        for i in temp:
            i = i.strip().split("|")
            my_list.append(i)
    for j, e in enumerate(my_list):
        item = e[1].split(";")
        grades = [item[k] for k in range(1, len(item), 2)]
        names = [item[w] for w in range(0, len(item), 2)]
        pupils = dict(zip(names, grades))
        my_class[e[0]] = pupils
  
    return my_class




def student_grade(date: dict, l: str, s: str, g: str):
    for k, v in date.items():
        if k == l:
            for key, value in v.items():
                if key == s:
                    v[key] = value + "," + g
    return date

def save_journal(date: dict, name_class: str): #сохранить файл
    new_str=''
    for k,v in date.items():
        new_str+=k+'|'
        for i,j in v.items():
            new_str+=i+";"+j+";"
        new_str+='\n'

    with open(name_class, 'w', encoding='UTF-8') as data:
        data.write(new_str)


def open_lesson(date: dict, lesson: str):
    if len(date)>0:
        my_dict={}
        for k,v in date.items():
            if k==lesson:
                my_dict[k]=v
        return my_dict
    

