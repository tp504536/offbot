import os

from PIL import Image, ImageFont, ImageDraw


def fake_qiwi_balance(message):
    if message.text == "Баланс Qiwi🥝":
        text = ["5,78", "17:10","20"]
    else:
        text = message.text.split("\n")
    spam = '{0:,}'.format(float(text[0].replace(',','.'))).replace(',', ' ')
    if float(spam) - int(float(spam)) > 0:
        spam = spam.replace('.',',') + " ₽"
    else:
        spam = str(int(float(spam))) + " ₽"
    time_n = text[1]
    qiwi = Image.open("Image source/Qiwi/balance(2).png")
    fnt = ImageFont.truetype("Fonts/SF-Pro-Text-Bold.otf", 100)
    fnt_time = ImageFont.truetype("Fonts/SF-Pro-Text-Bold.otf", 40)
    W = 562.5
    w, h = fnt.getsize(spam)
    d = ImageDraw.Draw(qiwi)
    d.text((W - w / 2, 405), spam, font=fnt, fill=(255,255,255,255))
    d.text(((83, 53)), time_n, font=fnt_time, fill=(0, 0, 0))
    battery_percetage = int(round(int(text[2]) / 100, 1) * 100)
    battery = Image.open(f'Image source/battery_qiwi_main/{battery_percetage}.png')
    qiwi.paste(battery, (1009, 52))
    del d
    qiwi.save(f"ForScreen/{message.chat.id}_q_balance.png.png", "PNG")
    return open(f"ForScreen/{message.chat.id}_q_balance.png.png", "rb")


def fake_qiwi_send_phone(message):
    if message.text == "Чек перевод по номеру🥝":
        text = ["10000", "17:10",'+79045580813',"20"]
    else:
        text = message.text.split("\n")
    money = '{0:,}'.format(int(text[0])).replace(',', ' ')
    money = '- ' + str(money) + " ₽"
    phone = text[2]
    time_n = text[1]
    qiwi_phone = Image.open("Image source/Qiwi/qiwi_send_phone.png")
    fnt = ImageFont.truetype("Fonts/SF-Pro-Display-Medium.otf", 60)
    fnt_time = ImageFont.truetype("Fonts/SF-Pro-Text-Bold.otf", 40)
    phone_n = ImageFont.truetype("Fonts/SF-Pro-Display-Light.otf", 40)
    W = 270
    w1, h1 = fnt.getsize(money)
    w2, h2 = phone_n.getsize(phone)
    d = ImageDraw.Draw(qiwi_phone)
    d.text((562.5 - w1 / 2, 825), money, font=fnt, fill=(0, 0, 0))
    d.text(((83, 53)), time_n, font=fnt_time, fill=(0, 0, 0))
    d.text((562.5 - w2 / 2, 717), phone, font=phone_n, fill=(155, 155, 155))
    battery_percetage = int(round(int(text[3]) / 100, 1) * 100)
    battery = Image.open(f'Image source/battery_qiwi_transfer/{battery_percetage}.png')
    qiwi_phone.paste(battery, (1009, 52))
    del d
    qiwi_phone.save(f"ForScreen/{message.chat.id}_q_send_phone.png.png", "PNG")
    return open(f"ForScreen/{message.chat.id}_q_send_phone.png.png", "rb")

def fake_qiwi_transfer(message):
    if message.text == "Перевод на другой на карту🥝":
        text = ["53161,40", "08.03.2021 в 21:30", "17:30", "4341","20"]
    else:
        text = message.text.split("\n")
    b = text[0].split(',')
    finish = '{0:,}'.format(int(b[0])).replace(',', ' ')
    if len(b) > 1:
        money = '- ' + str(finish) + ',' + b[1] + " ₽"
    else:
        money = '- ' + str(finish) + " ₽"

    card = text[3]
    date_time = text[1].strip()
    data_n = text[2]
    qiwi = Image.open("Image source/Qiwi/qiwi_visa.png")
    font1 = ImageFont.truetype("Fonts/Roboto-Bold.ttf", 53)
    font2 = ImageFont.truetype("Fonts/Roboto-Regular.ttf", 38)
    font3 = ImageFont.truetype("Fonts/Roboto-Regular.ttf", 40)
    font4 = ImageFont.truetype("Fonts/Roboto-Bold.ttf", 60)
    fnt_time = ImageFont.truetype("Fonts/SF-Pro-Text-Bold.otf", 40)
    card_n = ImageFont.truetype("Fonts/SF-Pro-Display-Light.otf", 40)
    W = 1080
    w1, h1 = font4.getsize(money)
    d = ImageDraw.Draw(qiwi)
    print(w1)
    # d.text(((W - w1) / 2, 685), money2, font=font1, fill=(0, 0, 0, 255))
    # d.text(((W - w2) / 2 + 60, 614), phone, font=font2, fill=(153, 153, 153, 255))
    d.text((631, 626), card, font=card_n, fill=(155, 155, 155))
    d.text((63, 2215), date_time, font=font3, fill=(0, 0, 0))
    d.text((562.5 - w1 / 2, 743), money, font=font4, fill=(0, 0, 0))
    d.text((83, 53), data_n, font=fnt_time, fill=(0, 0, 0))
    battery_percetage = int(round(int(text[4]) / 100, 1) * 100)
    battery = Image.open(f'Image source/battery_qiwi_transfer/{battery_percetage}.png')
    qiwi.paste(battery, (1009, 52))
    if message.text == "Перевод на другой на карту🥝":
        qiwi.save(f"ForScreen/example_fakeqiwitransfer.png", "PNG")
        return open(f"ForScreen/example_fakeqiwitransfer.png", "rb")
    else:
        qiwi.save(f"ForScreen/{message.chat.id}_q_transfer.png", "PNG")
        return open(f"ForScreen/{message.chat.id}_q_transfer.png", "rb")


def fake_qiwi_up(message):
    if message.text == "Получение денежных средст Qiwi🥝":
        text = ["105005", "08.03.2021 в 21:30", "17:30", "+79045580813", "20"]
    else:
        text = message.text.split("\n")
    b = text[0].split(',')
    finish = '{0:,}'.format(int(b[0])).replace(',', ' ')
    if len(b) > 1:
        money = '+ ' + str(finish) + ',' + b[1] + " ₽"
    else:
        money = '+ ' + str(finish) + " ₽"
    # money_two = text[0]
    # if money_two.replace('')
    # money_two = '{0:,}'.format(float(money_two)).replace(',', ' ')
    phone = text[3]
    phone_two = text[3]
    date_time = text[1].strip()
    data_n = text[2]
    qiwi = Image.open("Image source/Qiwi/up_qiwi.png")
    font1 = ImageFont.truetype("Fonts/Roboto-Regular.ttf", 46)
    font2 = ImageFont.truetype("Fonts/Roboto-Regular.ttf", 38)
    font3 = ImageFont.truetype("Fonts/Roboto-Regular.ttf", 40)
    font4 = ImageFont.truetype("Fonts/SF-Pro-Display-Medium.otf", 60)
    fnt_time = ImageFont.truetype("Fonts/SF-Pro-Text-Bold.otf", 40)
    card_n = ImageFont.truetype("Fonts/Roboto-Regular.ttf", 40)
    W = 1080
    w1, h1 = font4.getsize(money)
    w2, h2 = font1.getsize(phone_two)
    d = ImageDraw.Draw(qiwi)
    d.text((64, 1882), money.replace('+ ',''), font=font2, fill=(0,0,0))
    d.text((562.5-w2 /2, 717), phone_two, font=font1, fill=(155,155, 155))
    d.text((62, 1679), phone, font=card_n, fill=(0,0,0))
    d.text((63, 1474), date_time, font=font3, fill=(0, 0, 0))
    d.text((562.5 - w1 / 2, 824), money, font=font4, fill=(75, 188, 92))
    d.text((83, 53), data_n, font=fnt_time, fill=(0, 0, 0))
    d.text((64, 2290), money.replace('+ ',''), font=font2, fill=(0,0,0))
    battery_percetage = int(round(int(text[4]) / 100, 1) * 100)
    battery = Image.open(f'Image source/battery_qiwi_transfer/{battery_percetage}.png')
    qiwi.paste(battery, (1009, 52))
    if message.text == "Получение денежных средст Qiwi🥝":
        qiwi.save(f"ForScreen/example_fakeqiwitransfer.png", "PNG")
        return open(f"ForScreen/example_fakeqiwitransfer.png", "rb")
    else:
        qiwi.save(f"ForScreen/{message.chat.id}_q_up.png", "PNG")
        return open(f"ForScreen/{message.chat.id}_q_up.png", "rb")


def fake_sber_balance(message):
    if message.text == "Баланс сбербанк🍀":
        text = ["15000", "Ярик", "4569", "23:40","100"]
    else:
        text = message.text.split("\n")
    b = text[0].split(',')
    finish = '{0:,}'.format(int(b[0])).replace(',', ' ')
    if len(b) > 1:
        money = str(finish) + ',' + b[1] + " ₽"
    else:
        money = str(finish) + " ₽"
    name = text[1] + ','
    number_card = text[2]
    time_n = text[3]
    battery_percetage = int(round(int(text[4])/100, 1)*100)
    sber = Image.open("Image source/Sber/sber_balance.png")
    fnt = ImageFont.truetype("Fonts/SF-Pro-Display-Medium.otf", 60)
    fnt_name = ImageFont.truetype("Fonts/SF-Pro-Display-Bold.otf", 70)
    fnt_card = ImageFont.truetype("Fonts/SF-Pro-Display-Semibold.otf", 40)
    fnt_time = ImageFont.truetype("Fonts/SF-Pro-Display-Medium.otf", 43)
    W = 243
    H = 1140
    W1 = 53
    H1 = 317
    W2 = 510
    H2 = 1217
    W3 = 57
    H3 = 42
    battery = Image.open(f'Image source/battery_sber_main/{battery_percetage}.png')
    d = ImageDraw.Draw(sber)
    d.text(((W), H), money, font=fnt, fill=(255, 255, 255, 255))
    d.text((W1, H1), name, font=fnt_name, fill=(255, 255, 255, 255))
    d.text((W2, H2), number_card, font=fnt_card, fill=(155, 155, 155))
    d.text((W3, H3), time_n, font=fnt_time, fill=(255, 255, 255, 255))
    sber.paste(battery, (1009, 52))
    if message.text == "Перевод на другой кошелек🍀":
        sber.save(f"ForScreen/example_fakeqsberbalance.png", "PNG")
        return open(f"ForScreen/example_fakesberbalance.png", "rb")
    else:
        sber.save(f"ForScreen/{message.chat.id}_sberbalance.png", "PNG")
        return open(f"ForScreen/{message.chat.id}_sberbalance.png", "rb")


def fake_sber_transfer(message):
    if message.text == "Перевод на сбербанк🍀":
        text = ["1", "Кристина Артуровна С", "21:30","20"]
    else:
        text = message.text.split("\n")
    b = text[0].split(',')
    finish = '{0:,}'.format(int(b[0])).replace(',', ' ')
    if len(b) > 1:
        money = str(finish) + ',' + b[1] + " ₽"
    else:
        money = str(finish) + " ₽"
    name = text[1] + '.'
    time_n = text[2]
    battery_percetage = int(round(int(text[3]) / 100, 1) * 100)
    # 20 = 0.2
    # 55 = 0.55 = 0.6 = 60
    # 044 = 04
    sber = Image.open("Image source/Sber/sber_trans.png")
    fnt = ImageFont.truetype("Fonts/SF-Pro-Text-Bold.otf", 75)
    fnt_name = ImageFont.truetype("Fonts/SF-Pro-Display-Medium.otf", 41)
    fnt_time = ImageFont.truetype("Fonts/SF-Pro-Display-Medium.otf", 43)
    W = 562.5
    H = 662
    W1 = 562.5
    H1 = 807
    W3 = 57
    H3 = 42
    w1, h1 = fnt.getsize(money)
    w, h = fnt_name.getsize(name)
    battery = Image.open(f'Image source/battery_send_sber/{battery_percetage}.png')
    d = ImageDraw.Draw(sber)
    d.text(((W - w1 / 2), H), money, font=fnt, fill=(255, 255, 255, 255))
    d.text(((W1 - w / 2), H1), name, font=fnt_name, fill=(255, 255, 255, 255))
    d.text((W3, H3), time_n, font=fnt_time, fill=(255, 255, 255, 255))
    sber.paste(battery, (1009, 52))
    if message.text == "Перевод на сбербанк🍀":
        sber.save(f"ForScreen/example_fakesbertransfer.png", "PNG")
        return open(f"ForScreen/example_fakesbertransfer.png", "rb")
    else:
        sber.save(f"ForScreen/{message.chat.id}_fakesbertransfer.png", "PNG")
        return open(f"ForScreen/{message.chat.id}_fakesbertransfer.png", "rb")


def fake_rai_transfer(message):
    if message.text == "Перевод на Райфайзинг⚔️":
        text = ["5", "0953697", "Кристина Артуровна С", "+78954328507", "Сбербанк", "21:30", "20"]
    else:
        text = message.text.split("\n")
    b = text[0].split(',')
    finish = '{0:,}'.format(int(b[0])).replace(',', ' ')
    if len(b) > 1:
        money = str(finish) + ',' + b[1] + " ₽"
    else:
        money = str(finish) + " ₽"
    name = text[2] + '.'
    time_n = text[5]
    card = "*" + text[1]
    iphone = text[3]
    bank = text[4]
    rai = Image.open("Image source/rai/trans.PNG")
    fnt = ImageFont.truetype("Fonts/SF-Pro-Text-Bold.otf", 60)
    fnt_name = ImageFont.truetype("Fonts/SF-Pro-Text-Bold.otf", 40)
    fnt_time = ImageFont.truetype("Fonts/SF-Pro-Text-Bold.otf", 40)
    fnt_card = ImageFont.truetype("Fonts/SF-Pro-Text-Bold.otf", 40)
    fnt_bank = ImageFont.truetype("Fonts/SF-Pro-Text-Bold.otf", 40)
    fnt_phone = ImageFont.truetype("Fonts/SF-Pro-Text-Bold.otf", 40)
    W = 562.5
    H = 1288
    W1 = 562.5
    H1 = 1820
    W3 = 78
    H3 = 52
    W4 = 562.5
    H4 = 1641
    W5 = 568.5
    H5 = 1933
    W6 = 568.5
    H6 = 1877
    w1, h1 = fnt.getsize(money)
    w, h = fnt_name.getsize(name)
    w2, h2 = fnt_name.getsize(card)
    w3, h3 = fnt_name.getsize(bank)
    w4, h4 = fnt_name.getsize(iphone)
    d = ImageDraw.Draw(rai)
    d.text(((W - w1 / 2), H), money, font=fnt, fill=(0, 0, 0))
    d.text(((W1 - w / 2), H1), name, font=fnt_name, fill=(255, 255, 255, 255))
    d.text((W3, H3), time_n, font=fnt_time, fill=(255, 255, 255, 255))
    d.text(((W4 - w2 / 2), H4), card, font=fnt_card, fill=(255, 255, 255, 255))
    d.text(((W5 - w3 / 2), H5), bank, font=fnt_bank, fill=(255, 255, 255, 255))
    d.text(((W6 - w4 / 2), H6), iphone, font=fnt_phone, fill=(255, 255, 255, 255))
    battery_percetage = int(round(int(text[6]) / 100, 1) * 100)
    battery = Image.open(f'Image source/battery_raifaz_transfer/{battery_percetage}.png')
    rai.paste(battery, (1009, 52))
    if message.text == "Перевод на Райфайзинг⚔️":
        rai.save(f"ForScreen/example_fakeraitransfer.png", "PNG")
        return open(f"ForScreen/example_fakeraitransfer.png", "rb")
    else:
        rai.save(f"ForScreen/{message.chat.id}_raitransfer.png", "PNG")
        return open(f"ForScreen/{message.chat.id}_raitransfer.png", "rb")


def fake_rai_balance(message):
    if message.text == "Баланс Райфайзинг⚔️":
        text = ["4500,35", "0953697", "21:50", "20"]
    else:
        text = message.text.split("\n")
    b = text[0].split(',')
    finish = '{0:,}'.format(int(b[0])).replace(',', ' ')
    if len(b) > 1:
        money = str(finish) + ',' + b[1] + " ₽"
    else:
        money = str(finish) + " ₽"
    # name = text[1] + ','
    number_card = '*' + text[1]
    time_n = text[2]
    raifazen_main = Image.open("Image source/rai/balance2.PNG ")
    fnt = ImageFont.truetype("Fonts/SF-Pro-Text-Bold.otf", 50)
    fnt_name = ImageFont.truetype("Fonts/SF-Pro-Display-Bold.otf", 39)
    fnt_card = ImageFont.truetype("Fonts/SF-Pro-Display-Medium.otf", 35)
    fnt_time = ImageFont.truetype("Fonts/SF-Pro-Display-Medium.otf", 40)
    W = 454
    H = 172
    W1 = 206
    H1 = 1000
    W2 = 857
    H2 = 969
    W3 = 78
    H3 = 52
    d = ImageDraw.Draw(raifazen_main)
    d.text(((W), H), money, font=fnt, fill=(255, 255, 255, 255))
    d.text((W1, H1), number_card, font=fnt_card, fill=(155, 155, 155))
    d.text((W2, H2), money, font=fnt_card, fill=(0, 0, 0))
    d.text((W3, H3), time_n, font=fnt_time, fill=(255, 255, 255, 255))
    battery_percetage = int(round(int(text[3]) / 100, 1) * 100)
    battery = Image.open(f'Image source/battery_raifaz_main/{battery_percetage}.png')
    raifazen_main.paste(battery, (1009, 52))
    if message.text == "Баланс Райфайзинг⚔️":
        raifazen_main.save(f"ForScreen/example_raibalancer.png", "PNG")
        return open(f"ForScreen/example_raibalancer.png", "rb")
    else:
        raifazen_main.save(f"ForScreen/{message.chat.id}_raibalance.png", "PNG")
        return open(f"ForScreen/{message.chat.id}_raibalance.png", "rb")


def fake_tin_transfer(message):
    if message.text == "Перевод на Тинькофф💂‍♀":
        text = ["20000,4", "2000,4", "Кристина С", "+7 (912) 445-05-32", "21:30", "20"]
    else:
        text = message.text.split("\n")
    b = text[0].split(',')
    finish = '{0:,}'.format(int(b[0])).replace(',', ' ')
    if len(b) > 1:
        old_balance = str(finish) + ',' + b[1] + " ₽"
    else:
        old_balance = str(finish) + " ₽"
    new_balance = float(text[0].replace(',', '.')) - float(text[1].replace(',', '.'))
    # new_balance = '{0:,}'.format(new_balance).replace(',', ' ')
    if new_balance - int(new_balance) > 0:
        new_balance = '{0:,}'.format(new_balance).replace(',', ' ')
        new_balance = str(new_balance).replace('.', ',') + " ₽"
    else:
        new_balance = '{0:,}'.format(int(new_balance)).replace(',', ' ')
        new_balance = str(new_balance).replace('.', ',') + " ₽"
    print(new_balance)
    # new_balance = '{0:,}'.format(new_balance).replace(',', ' ')
    # transfer_amount = '{0:,}'.format(float(text[1].replace(',','.'))).replace(',', ' ')
    transfer_amount = text[1].replace(',', '.')
    if float(transfer_amount) - int(float(transfer_amount)) > 0:
        transfer_amount = '{0:,}'.format(float(transfer_amount)).replace(',', ' ')
        transfer_amount = '-' + transfer_amount.replace('.', ',') + " ₽"
    else:
        transfer_amount = '{0:,}'.format(int(transfer_amount)).replace(',', ' ')
        transfer_amount = '-' + transfer_amount + " ₽"
    name = text[2] + '.'
    phone_number = text[3]
    time_n = text[4]
    tink = Image.open("Image source/tink/trans.PNG")
    fnt_name = ImageFont.truetype("Fonts/SF-Pro-Display-Regular.otf", 50)
    fnt_transfer_amount = ImageFont.truetype("Fonts/SF-Pro-Text-Bold.otf", 80)
    fnt_time = ImageFont.truetype("Fonts/SF-Pro-Text-Bold.otf", 40)
    fnt_old_balance = ImageFont.truetype("Fonts/SF-Pro-Display-Regular.otf", 40)
    fnt_new_balance = ImageFont.truetype("Fonts/SF-Pro-Display-Regular.otf", 40)
    fnt_phone_number = ImageFont.truetype("Fonts/SF-Pro-Display-Medium.otf", 50)
    W0, H0 = 501, 608
    W1, H1 = 626, 608
    W2, H2 = 562.5, 723
    W3, H3 = 562.5, 919
    W4, H4 = 562.5, 1273
    W5, H5 = 79, 52
    w0, h0 = fnt_old_balance.getsize(old_balance)
    w2, h2 = fnt_transfer_amount.getsize(transfer_amount)
    w3, h3 = fnt_name.getsize(name)
    w4, h4 = fnt_phone_number.getsize(phone_number)
    d = ImageDraw.Draw(tink)
    d.text(((W0 - w0), H0), old_balance, font=fnt_old_balance, fill=(255, 255, 255, 255))
    d.text((W1, H1), new_balance, font=fnt_new_balance, fill=(255, 255, 255, 255))
    d.text(((W2 - w2 / 2), H2), transfer_amount, font=fnt_transfer_amount, fill=(255, 255, 255, 255))
    d.text(((W3 - w3 / 2), H3), name, font=fnt_name, fill=(0, 0, 0))
    d.text(((W4 - w4 / 2), H4), phone_number, font=fnt_phone_number, fill=(0, 0, 0))
    d.text((W5, H5), time_n, font=fnt_time, fill=(255, 255, 255, 255))
    d.line(((W0 - w0 - 3, 635), (W0 + 1, 635)), fill=(255, 255, 255, 255), width=3)
    battery_percetage = int(round(int(text[5]) / 100, 1) * 100)
    battery = Image.open(f'Image source/battery_tink_transfer/{battery_percetage}.png')
    tink.paste(battery, (1009, 52))
    if message.text == "Перевод на Тинькофф💂‍♀":
        tink.save(f"ForScreen/example_tin_transfer.png", "PNG")
        return open(f"ForScreen/example_tin_transfer.png", "rb")
    else:
        tink.save(f"ForScreen/{message.chat.id}_tin_transfer.png", "PNG")
        return open(f"ForScreen/{message.chat.id}_tin_transfer.png", "rb")


def fake_tin_balance(message):
    if message.text == "Баланс Тинькофф💂‍♀":
        text = ["10000,15", "Владимир", "октябре", "21:30", "20"]
    else:
        text = message.text.split("\n")
    b = text[0].split(',')
    finish = '{0:,}'.format(int(b[0])).replace(',', ' ')
    if len(b) > 1:
        money = str(finish) + ',' + b[1] + " ₽"
    else:
        money = str(finish) + " ₽"
    n1 = text[1][0]
    name = text[1]
    mount = text[2]
    time_n = text[3]
    tink = Image.open("Image source/tink/balance.png")
    fnt = ImageFont.truetype("Fonts/SF-Pro-Text-Bold.otf", 50)
    fnt_name = ImageFont.truetype("Fonts/SF-Pro-Display-Bold.otf", 65)
    fnt_mount = ImageFont.truetype("Fonts/SF-Pro-Display-Regular.otf", 45)
    fnt_time = ImageFont.truetype("Fonts/SF-Pro-Text-Bold.otf", 40)
    fnt_n1 = ImageFont.truetype("Fonts/SF-Pro-Text-Bold.otf", 40)
    W = 279
    H = 1453
    W1 = 197
    H1 = 308
    W2 = 256
    H2 = 1063
    W3 = 79
    H3 = 52
    W4 = 89
    H4 = 319
    d = ImageDraw.Draw(tink)
    d.text(((W), H), money, font=fnt, fill=(255, 255, 255, 255))
    d.text((W1, H1), name, font=fnt_name, fill=(255, 255, 255, 255))
    d.text((W2, H2), mount, font=fnt_mount, fill=(255, 255, 255, 255))
    d.text((W3, H3), time_n, font=fnt_time, fill=(255, 255, 255, 255))
    d.text((W4, H4), n1, font=fnt_n1, fill=(255, 255, 255, 255))
    battery_percetage = int(round(int(text[4]) / 100, 1) * 100)
    battery = Image.open(f'Image source/battery_tink_main/{battery_percetage}.png')
    tink.paste(battery, (1009, 52))
    if message.text == "Перевод на Тинькофф💂‍♀":
        tink.save(f"ForScreen/example_tin_balance.png", "PNG")
        return open(f"ForScreen/example_tin_balance.png", "rb")
    else:
        tink.save(f"ForScreen/{message.chat.id}_tin_balance.png", "PNG")
        return open(f"ForScreen/{message.chat.id}_tin_balance.png", "rb")


def fake_tin_card(message):
    if message.text == "Перевод на карту Сбербанк💂‍♀":
        text = ["20000,4", "2000,4", "Кристина С", "4276105265697684", "21:30", "20"]
    else:
        text = message.text.split("\n")
    b = text[0].split(',')
    finish = '{0:,}'.format(int(b[0])).replace(',', ' ')
    if len(b) > 1:
        old_balance = str(finish) + ',' + b[1] + " ₽"
    else:
        old_balance = str(finish) + " ₽"
    new_balance = float(text[0].replace(',', '.')) - float(text[1].replace(',', '.'))
    if new_balance - int(new_balance) > 0:
        new_balance = '{0:,}'.format(new_balance).replace(',', ' ')
        new_balance = str(new_balance).replace('.', ',') + " ₽"
    else:
        new_balance = '{0:,}'.format(int(new_balance)).replace(',', ' ')
        new_balance = str(new_balance).replace('.', ',') + " ₽"
    transfer_amount = text[1].replace(',', '.')
    if float(transfer_amount) - int(float(transfer_amount)) > 0:
        transfer_amount = '{0:,}'.format(float(transfer_amount)).replace(',', ' ')
        transfer_amount = '-' + transfer_amount.replace('.', ',') + " ₽"
    else:
        transfer_amount = '{0:,}'.format(int(transfer_amount)).replace(',', ' ')
        transfer_amount = '-' + transfer_amount + " ₽"
    name = text[2] + '.'
    phone_number1 = text[3][:6]
    phone_number2 = text[3][12:]
    phone_number = phone_number1 + "******" + phone_number2
    time_n = text[4]
    tink = Image.open("Image source/tink/card_tin.png")
    fnt_name = ImageFont.truetype("Fonts/SF-Pro-Display-Regular.otf", 50)
    fnt_transfer_amount = ImageFont.truetype("Fonts/SF-Pro-Text-Bold.otf", 80)
    fnt_time = ImageFont.truetype("Fonts/SF-Pro-Text-Bold.otf", 40)
    fnt_old_balance = ImageFont.truetype("Fonts/SF-Pro-Display-Regular.otf", 40)
    fnt_new_balance = ImageFont.truetype("Fonts/SF-Pro-Display-Regular.otf", 40)
    fnt_phone_number = ImageFont.truetype("Fonts/SF-Pro-Display-Medium.otf", 50)
    W0, H0 = 501, 730
    W1, H1 = 626, 735
    W2, H2 = 562.5, 842
    W3, H3 = 562.5, 1048
    W4, H4 = 562.5, 1393
    W5, H5 = 79, 52
    w0, h0 = fnt_old_balance.getsize(old_balance)
    w2, h2 = fnt_transfer_amount.getsize(transfer_amount)
    w3, h3 = fnt_name.getsize(name)
    w4, h4 = fnt_phone_number.getsize(phone_number)
    d = ImageDraw.Draw(tink)
    d.text(((W0 - w0), H0), old_balance, font=fnt_old_balance, fill=(255, 255, 255, 255))
    d.text((W1, H1), new_balance, font=fnt_new_balance, fill=(255, 255, 255, 255))
    d.text(((W2 - w2 / 2), H2), transfer_amount, font=fnt_transfer_amount, fill=(255, 255, 255, 255))
    d.text(((W3 - w3 / 2), H3), name, font=fnt_name, fill=(0, 0, 0))
    d.text(((W4 - w4 / 2), H4), phone_number, font=fnt_phone_number, fill=(0, 0, 0))
    d.text((W5, H5), time_n, font=fnt_time, fill=(255, 255, 255, 255))
    d.line(((W0 - w0 - 3, 756), (W0 + 1, 756)), fill=(255, 255, 255, 255), width=3)
    battery_percetage = int(round(int(text[5]) / 100, 1) * 100)
    battery = Image.open(f'Image source/battery_tink_transfer/{battery_percetage}.png')
    tink.paste(battery, (1009, 52))
    if message.text == "Перевод на карту Сбербанк💂‍♀":
        tink.save(f"ForScreen/example_tin_card.png", "PNG")
        return open(f"ForScreen/example_tin_card.png", "rb")
    else:
        tink.save(f"ForScreen/{message.chat.id}_tin_card.png", "PNG")
        return open(f"ForScreen/{message.chat.id}_tin_card.png", "rb")

