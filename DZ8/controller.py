import model
import view


def start():
    while True:
        user_inp = view.show_menu()
        handler(user_inp)


def handler(n: int):
    match n:
        case 1:
            view.print_journal(model.read_data(view.input_class()))
        case 2:
            view.open_lesson(model.my_class)
        case 3:
            view.open_popil(model.my_class)

        case 4:
            lesson=view.new_lesson(model.my_class)
            journal=model.open_lesson(model.my_class,lesson)
            while True:
                view.print_journal(journal)
                student=view.who_answer()
                if student=='EXIT':
                    break
                grad=view.what_mark()
                model.student_grade(model.my_class, lesson,student,grad)
            model.save_journal(model.my_class,view.number_class)


        case 5:
            view.exit_journal()
