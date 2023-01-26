import modell
import view



def handler(inp: int):
    match inp:
        case 1:
            view.show_all(modell.get_db())
        case 2:
            modell.read_data("data.txt")
            view.db_success(modell.get_db())
        case 3:
            modell.save_file(modell.comparison(modell.get_db,modell.my_list_copy))
        case 4:
            modell.set_db(view.create_contact())
        case 5:
            modell.change_contact(modell.my_list,view.input_contact(modell.my_list), view.change_new_data())
        case 6:
            modell.delte_contact(modell.my_list,view.input_contact(modell.my_list))
        case 7:
            view.output_seach_contact(modell.my_list)

        case 8:
            view.exit_pro()

def start():
    while True:
        user_inp = view.show_menu()
        handler(user_inp)
