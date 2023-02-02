from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_main_menu=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)

btn_yes=KeyboardButton('/yes')
btn_help=KeyboardButton('/help')
btn_stop=KeyboardButton('/stop')

kb_main_menu.add(btn_yes,btn_help,btn_stop)

kb_menu=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True )
btn_not=KeyboardButton('/no')
kb_menu.add(btn_yes)
kb_menu.add(btn_not)