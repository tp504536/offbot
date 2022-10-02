from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


start = ReplyKeyboardMarkup(resize_keyboard=True)
qiwi = KeyboardButton('Qiwi🥝')
sber = KeyboardButton('Sber🍀')
rai = KeyboardButton('Raifaisenbank⚔️')
tink = KeyboardButton('Tinkoff💂‍♀️')
info = KeyboardButton('Наши проекты❗️')
start.insert(qiwi).insert(sber).insert(rai).insert(tink).insert(info)
back = KeyboardButton('Назад🔙')

qiw_menu = ReplyKeyboardMarkup(resize_keyboard=True)
trans_qiwi = KeyboardButton('Перевод на другой на карту🥝')
blance_qiwi = KeyboardButton('Баланс Qiwi🥝')
up_qiwi = KeyboardButton('Получение денежных средст Qiwi🥝')
qiw_menu.add(blance_qiwi).add(trans_qiwi).add(up_qiwi).add(back)

sber_menu = ReplyKeyboardMarkup(resize_keyboard=True)
trans_sber = KeyboardButton('Перевод на сбербанк🍀')
blance_sber = KeyboardButton('Баланс сбербанк🍀')
sber_menu.add(blance_sber).add(trans_sber).add(back)

tink_menu = ReplyKeyboardMarkup(resize_keyboard=True)
trans_tink = KeyboardButton('Перевод на Тинькофф💂‍♀')
blance_tink = KeyboardButton('Баланс Тинькофф💂‍♀')
tink_menu.add(blance_tink).add(trans_tink).add(back)

rai_menu = ReplyKeyboardMarkup(resize_keyboard=True)
trans_rai = KeyboardButton('Перевод на Райфайзинг⚔️')
blance_rai = KeyboardButton('Баланс Райфайзинг⚔️')
rai_menu.add(blance_rai).add(trans_rai).add(back)

admin_menu = ReplyKeyboardMarkup(resize_keyboard=True)
spam = KeyboardButton('Рассылка')
stat = KeyboardButton('Статистика')
user_menu = KeyboardButton('Пользователькое меню')
admin_menu.add(spam).add(stat).add(user_menu)

spam_inline = InlineKeyboardMarkup(row_width=2)
ok = InlineKeyboardButton('Отправить',callback_data='ok')
no = InlineKeyboardButton('Отменить',callback_data='no')
spam_inline.add(ok).add(no)