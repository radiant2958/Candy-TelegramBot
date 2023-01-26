my_list=[]
my_list_copy=[]
def read_data(path: str)->dict:
    global my_list
    global my_list_copy
    with open(path, 'r',encoding='UTF-8') as file:
        temp=file.readlines()
        for i in temp:
            id_dict={}
            i=i.strip().split(';')
            id_dict['lastname']=i[0]
            id_dict['fersttname']=i[1]
            id_dict['phone']=i[2]
            id_dict['comment']=i[3]
            my_list.append(id_dict)
    my_list_copy=my_list.copy()
    # return my_list


def set_db(new_contact: str):
    global my_list
    my_list.append(new_contact)
           
def get_db():
    global my_list
    return my_list
  
def save_file(db:list): #сохранение файла
    new_db=''
    for i in range(len (db)):
        if i==0:
            new_db+='\n'
            for v in db[i].values():
                new_db+=v+';'
        else:
            for v in db[i].values():
                new_db+=v+';'
        new_db+='\n'            
    with open('data.txt', 'a', encoding='UTF-8') as data:
        data.write(new_db)
        

def comparison(db: list, db_copy: list): #сравнивает контакты из файла с открытым списком
    new_data=[]
    for i in db:
        if i not in db_copy:
            new_data.append(i)
    return new_data

def change_contact(db: list,l: int, new_dict: dict): #изменить контакт
    db[l]=new_dict
    return db

def delte_contact(db: list, l: int): #удалить контакт
    db.pop(l)
    return db


