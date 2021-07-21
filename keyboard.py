from telebot import types

keyboard = types.InlineKeyboardMarkup()

key_aries = types.InlineKeyboardButton(text='♈️ Овен', callback_data='aries')
key_taurus = types.InlineKeyboardButton(text='♉️ Телец', callback_data='taurus')
key_gemini = types.InlineKeyboardButton(text='♊️ Близнецы', callback_data='gemini')
keyboard.add(key_aries, key_taurus, key_gemini)

key_cancer = types.InlineKeyboardButton(text='♋️ Рак', callback_data='cancer')
key_leo = types.InlineKeyboardButton(text='♌️ Лев', callback_data='leo')
key_virgo = types.InlineKeyboardButton(text='♍️ Дева', callback_data='virgo')
keyboard.add(key_cancer, key_leo, key_virgo)

key_libra = types.InlineKeyboardButton(text='♎️ Весы', callback_data='libra')
key_scorpio = types.InlineKeyboardButton(text='♏️ Скорпион', callback_data='scorpio')
key_sagittarius = types.InlineKeyboardButton(text='♐️ Стрелец', callback_data='sagittarius')
keyboard.add(key_libra, key_scorpio, key_sagittarius)

key_capricorn = types.InlineKeyboardButton(text='♑️ Козерог', callback_data='capricorn')
key_aquarius = types.InlineKeyboardButton(text='♒️ Водолей', callback_data='aquarius')
key_pisces = types.InlineKeyboardButton(text='♓️ Рыбы', callback_data='pisces')
keyboard.add(key_capricorn, key_aquarius, key_pisces)
