from create import dp 
from aiogram import types
from random import randint


total=None


@dp.message_handler(commands=['start', 'старт'])
async def mes_star(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}!Сейчас мы сыграем с тобой в игру "КОНФЕТЫ".Победит тот, кто возьмет последнюю конфету со стола. Введи: "/set колличество конфет"')

@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('Я пока ничего не умею, но научусь')

@dp.message_handler(commands=['set'])
async def mes_setsetting(message: types.Message):
    global total
    count=int(message.text.split()[1])
    total=count
    await message.answer(f'На столе лежит {total} конфет, ты можешь взять за раз не больше 28 конфет.Игра началась! Введи чило конфет> ')

@dp.message_handler(commands=['stop', 'стоп'])
async def mes_stop(message: types.Message):
    await message.answer('Игра закончена')
    exit()

@dp.message_handler()
async def mes_all(message: types.Message):
    global total
    if message.text.isdigit():
        x = int(message.text)

        if x <= 28:
            total -= x
            if total >28:

                await message.answer(f'на столе осталось {total} конфет, дальше ходит бот')

                if total < 50:
                    c = total-29
                    if c == 0:
                        c += 1
                        total -= c
                        if total >28:
                            await message.answer(f'бот взял {c} конфет, на столе осталось {total} конфет, твой ход')
                        else:
                            await message.answer(f'на столе осталось {total} конфет,выйграл {message.from_user.first_name}')
                else:
                    c = randint(1, 28)
                    total -= c
                    if total > 28:

                        await message.answer(f'бот взял {c} конфет, на столе осталось {total} конфет, твой ход')
                    else:
                        await message.answer(f'на столе осталось {total} конфет, выйграл {message.from_user.first_name}')

            else:
                await message.answer(f'на столе осталось {total} конфет, выйграл бот')

        else:
            await message.answer('введите корректное число конфет')
    else:
        await message.answer('введите целое число ')






    


