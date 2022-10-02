import aiogram
import logging
import fakedraw

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import keyboard
from sql import Database
from config import *

logging.basicConfig(level=logging.INFO)

db = Database('base.db')
bot = Bot(token=TOKEN)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)


# Классы, которые нам понадаюятся
class Settings(StatesGroup):
    qiwi = State()
    qiwi_balance = State()
    qiwi_transfer = State()
    qiwi_up = State()
    sber = State()
    sber_balance = State()
    sber_transfer = State()
    rai_trans = State()
    rai_balance = State()
    tin_trans = State()
    tin_balance = State()
    spam_text = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if not db.users(message.from_user.id):
        db.add_user(message.from_user.id)
    await message.answer('Привет, друг! В этом боте ты сможешь создать точную копию скриншотов переводов,'
                         ' чеков по операциям и истории переводов и покупок.', reply_markup=keyboard.start)


@dp.message_handler(commands=['admin'])
async def admin(message:types.Message):
    await message.answer('Привет!',reply_markup=keyboard.admin_menu)

@dp.message_handler(content_types='text')
async def main(message: types.Message):
    if message.text == 'Qiwi🥝':
        await message.answer('Выберите из списка', reply_markup=keyboard.qiw_menu)
    elif message.text == 'Баланс Qiwi🥝':
        await message.answer_photo(fakedraw.fake_qiwi_balance(message), caption="""Введите необходимые данные:
        
1 - баланс
2 - время

Пример:
500
17:33
""")
        await Settings.qiwi_balance.set()
    elif message.text == 'Перевод на другой на карту🥝':
        await message.answer_photo(fakedraw.fake_qiwi_transfer(message), caption="""
        Введите необходимые данные:

        1 - сумма перевода
        2 - дату и время
        3 - дату 
        4 - последние 4 цифры карты

        Пример:
        53000
        08.03.2021 в 21:30
        21:30
        4513
        """)
        await Settings.qiwi_transfer.set()
    elif message.text == 'Получение денежных средст Qiwi🥝':
        await message.answer_photo(fakedraw.fake_qiwi_up(message),caption="""
        Введите необходимые данные:
        
        1 - Сумма
        2 - дату и время  
        3 - Время телефон
        4 - Номер телефона
        
        Пример:
        
        1000
        08.03.2021 в 21:30
        17:30
        +79045580813
        """)
        await Settings.qiwi_up.set()
    elif message.text == 'Sber🍀':
        await message.answer('Выберите из списка', reply_markup=keyboard.sber_menu)
    elif message.text == 'Баланс сбербанк🍀':
        await message.answer_photo(fakedraw.fake_sber_balance(message), caption="""
        Введите необходимые данные:
        
        1 - Сумма
        2 - имя владельца карты
        3 - последние 4 цифры карты
        4 - дату и время
        5 - Заряд устройства
        
        Пример:
        
        1000
        Владимир
        4577
        21:30
        50
        """)
        await Settings.sber_balance.set()
    elif message.text == 'Перевод на сбербанк🍀':
        await message.answer_photo(fakedraw.fake_sber_transfer(message), caption="""
        Введите необходимые данные:
        
        1 - сумма перевода
        2 - имя кому перевод
        3 - дату и время
        4 - Заряд устройства

        Пример:
        1000
        Владимир Владимирович П
        21:30
        20
        """)
        await Settings.sber_transfer.set()
    elif message.text == 'Raifaisenbank⚔️':
        await message.answer('Выберите из списка', reply_markup=keyboard.rai_menu)
    elif message.text == 'Перевод на Райфайзинг⚔️':
        await message.answer_photo(fakedraw.fake_rai_transfer(message), caption="""
        Введите необходимые данные:
        
        1 - Сумма перевода
        2 - номер счета
        3 - Имя кому перевод
        4 - Номер телефона
        5 - Банк
        6 - дату и время

        Пример:
        1000
        0675867
        Владимир Владимирович П
        +79125560613
        Сбербанк
        21:30
        """)
        await Settings.rai_trans.set()
    elif message.text == 'Баланс Райфайзинг⚔️':
        await message.answer_photo(fakedraw.fake_rai_balance(message), caption="""
        Введите необходимые данные:
        
        1 - Баланс
        2 - номер счета
        3 - дату и время

        Пример:
        1000
        0675867
        21:30
        """)
        await Settings.rai_balance.set()
    elif message.text == 'Tinkoff💂‍♀️':
        await message.answer('Выберите из списка', reply_markup=keyboard.tink_menu)
    elif message.text == 'Баланс Тинькофф💂‍♀':
        await message.answer_photo(fakedraw.fake_tin_balance(message), caption="""
        Введите необходимые данные:
        
        1 - Баланс
        2 - Имя владельца карты
        3 - Месяц
        4 - дату и время

        Пример:
        1000
        Дмитрий
        Ноябре
        21:30
        """)
        await Settings.tin_balance.set()
    elif message.text == 'Перевод на Тинькофф💂‍♀':
        await message.answer_photo(fakedraw.fake_tin_transfer(message), caption="""
        Введите необходимые данные:
        
        1 - Баланс карты
        2 - Сумму перевода
        3 - Имя получателя
        4 - Телефон получателя
        5 - дату и время

        Пример:
        15600
        25566
        Владимир П
        +7 (912) 445-05-32
        21:30
        """)
        await Settings.tin_trans.set()
    elif message.text == 'Назад🔙':
        await message.answer('Главное меню',reply_markup=keyboard.start)
    elif message.text == 'Пользователькое меню':
        await message.answer('Главное меню',reply_markup=keyboard.start)
    elif message.text == 'Статистика':
        count = db.coun_user()
        await message.answer('В бота заходило:\n' + str(count))
    elif message.text == 'Рассылка':
        await message.answer("Жду текст рассылки")
        await Settings.spam_text.set()
    elif message.text == 'Наши проекты❗️':
        await message.answer('🥤 Самая большая библиотека фильмов в Telegaram!\n\nhttps://t.me/Kinoozal_bot\n\n'
                             'Бот для скачивания медиа с instagram\n\nhttps://t.me/Instagramdownloader495_bot\n\n'
                             'По вопросам разработки ботов @vladimirr223 ')
    else:
        await message.answer('Используй клавиатуру')
@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Settings.qiwi_balance)
async def qiwi(message: types.Message, state: FSMContext):
    try:
        await message.answer_photo(fakedraw.fake_qiwi_balance(message), reply_markup=keyboard.start)
        await state.finish()
    except:
        await state.finish()
        await message.answer('Упс, что то не так!',reply_markup=keyboard.start)


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Settings.qiwi_up)
async def qiwi_up(message: types.Message, state: FSMContext):
    try:
        await message.answer_photo(fakedraw.fake_qiwi_up(message), reply_markup=keyboard.start)
        await state.finish()
    except:
        await state.finish()
        await message.answer('Упс, что то не так!',reply_markup=keyboard.start)

@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Settings.qiwi_transfer)
async def qiwi_transfer(message: types.Message, state: FSMContext):
    try:
        await message.answer_photo(fakedraw.fake_qiwi_transfer(message), reply_markup=keyboard.start)
        await state.finish()
    except:
        await state.finish()
        await message.answer('Упс, что то не так!',reply_markup=keyboard.start)


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Settings.sber_balance)
async def sber(message: types.Message, state: FSMContext):
    try:
        await message.answer_photo(fakedraw.fake_sber_balance(message), reply_markup=keyboard.start)
        await state.finish()
    except:
        await state.finish()
        await message.answer('Упс, что то не так!',reply_markup=keyboard.start)


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Settings.sber_transfer)
async def sber_trans(message: types.Message, state: FSMContext):
    try:
        await message.answer_photo(fakedraw.fake_sber_transfer(message), reply_markup=keyboard.start)
        await state.finish()
    except:
        await state.finish()
        await message.answer('Упс, что то не так!', reply_markup=keyboard.start)


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Settings.rai_balance)
async def rai_balance(message: types.Message, state: FSMContext):
    try:
        await message.answer_photo(fakedraw.fake_rai_balance(message), reply_markup=keyboard.start)
        await state.finish()
    except:
        await state.finish()
        await message.answer('Упс, что то не так!', reply_markup=keyboard.start)


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Settings.rai_trans)
async def rai_trans(message: types.Message, state: FSMContext):
    try:
        await message.answer_photo(fakedraw.fake_rai_transfer(message), reply_markup=keyboard.start)
        await state.finish()
    except:
        await state.finish()
        await message.answer('Упс, что то не так!', reply_markup=keyboard.start)

@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Settings.tin_trans)
async def tin_trans(message: types.Message, state: FSMContext):
    try:
        await message.answer_photo(fakedraw.fake_tin_transfer(message), reply_markup=keyboard.start)
        await state.finish()
    except:
        await state.finish()
        await message.answer('Упс, что то не так!', reply_markup=keyboard.start)


@dp.message_handler(content_types=types.ContentTypes.TEXT, state=Settings.tin_balance)
async def tin_trans(message: types.Message, state: FSMContext):
    try:
        await message.answer_photo(fakedraw.fake_tin_balance(message), reply_markup=keyboard.start)
        await state.finish()
    except:
        await state.finish()
        await message.answer('Упс, что то не так!', reply_markup=keyboard.start)


@dp.message_handler(content_types='text', state=Settings.spam_text.state)
async def login(message: types.Message, state: FSMContext):
    global spam
    async with state.proxy() as spam:
        spam['text'] = message.text
        await state.finish()
        await message.answer('Ваш текст для рассылки:\n\n' + spam['text'], reply_markup=keyboard.spam_inline)


@dp.callback_query_handler(text='ok')
async def no_date(call: types.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    all_users = db.all_user()
    for i in all_users:
        print(i)
        try:
            await bot.send_message(i,spam['text'])
        except:
            await call.message.answer('Упс! во время рассылки, что то пошло не так')

@dp.callback_query_handler(text='no')
async def no_date(call: types.CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer('Вы отменили рассылку')
if __name__ == "__main__":
    # Запускаем бота
    executor.start_polling(dp, skip_updates=True)
