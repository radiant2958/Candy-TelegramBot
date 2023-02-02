from create import dp 
from aiogram import types
from keyboards import kb_main_menu, kb_menu
from random import randint


total=None
game=False
@dp.message_handler(commands='start')
async def mes_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}!👋Я предлагаю тебе сыграть со мной в игру "Конфеты", если согласен выбери "yes"', reply_markup=kb_main_menu)


@dp.message_handler(commands=['yes'])
async def mes_yes(message: types.Message):
    await message.answer('Я рад,что ты решил со мной сыграть!😁\n'
                        'Сейчас о правилах:\n'
                        '1.🏆Победит тот, кто возьмет последнюю конфету со стола\n'
                        '2.❗️За раз нельзя взять больше 28 конфет❗️\n'
                        'Чтобы продалжить-введи: "/set колличество конфет"')

@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('Я пока ничего не умею, но научусь')

@dp.message_handler(commands=['set'])
async def mes_setsetting(message: types.Message):
    global total
    global game
    count=int(message.text.split()[1])
    total=count
    game=True
    await message.answer(f'На столе лежит {total} конфет🍭. Введи число конфет которое возьмешь> ')

@dp.message_handler(commands=['stop'])
async def mes_stop(message: types.Message):
    await message.answer('Я пошел спать😴')
    exit()

@dp.message_handler(commands=['no'])
async def mes_stop(message: types.Message):
    global game
    game=False
    await message.answer('Очень жаль,что ты не хочешь играть😭')
    
   

@dp.message_handler()
async def mes_all(message: types.Message):
    global total
    global game
    if game==True:

        if message.text.isdigit():
            x = int(message.text)

            if x <= 28:
                total -= x
                if total >28:

                    await message.answer(f'на столе осталось {total} конфет, дальше ходит бот')

                    if total <= 50:
                        c = total-29
                        if c == 0:
                            c += 1
                        total -= c
                        if total > 28:
                            await message.answer(f'бот взял {c} конфет, на столе осталось {total} конфет, твой ход')
                        else:
                            await message.answer(f'бот взял {c} конфет,на столе осталось {total} конфет,выйграл🏆{message.from_user.first_name}')
                            game==False
                            await message.answer('Игра закончена!Поиграем еще?', reply_markup=kb_menu)
                            
                                
                    else:
                        c = randint(1, 28)
                        total -= c
                        if total > 28:

                            await message.answer(f'бот взял {c} конфет, на столе осталось {total} конфет, твой ход')
                        else:
                            await message.answer(f'бот взял {c} конфет,на столе осталось {total} конфет, выйграл🏆{message.from_user.first_name}')
                            game==False
                            await message.answer('Игра закончена!Поиграем еще?', reply_markup=kb_menu)
                            
                            
                else:
                    await message.answer(f'на столе осталось {total} конфет, выйграл 🏆 бот')
                    game==False
                    await message.answer('Игра закончена!Поиграем еще?', reply_markup=kb_menu)

            else:
                await message.answer('введите корректное число конфет')
        else:
            await message.answer('введите целое число ')
    elif game==False:
        await message.answer('Выбери команду: \yes - начать игру, \help - помощь,\stop - отключить бота', reply_markup=kb_main_menu)


    


    


