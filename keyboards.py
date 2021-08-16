from telebot import types

keyboard = types.InlineKeyboardMarkup()

key_aries = types.InlineKeyboardButton(text='♈️ Aries', callback_data='aries')
key_taurus = types.InlineKeyboardButton(text='♉️ Taurus', callback_data='taurus')
key_gemini = types.InlineKeyboardButton(text='♊️ Gemini', callback_data='gemini')\
key_cancer = types.InlineKeyboardButton(text='♋️ Cancer', callback_data='cancer')
key_leo = types.InlineKeyboardButton(text='♌️ Leo', callback_data='leo')
key_virgo = types.InlineKeyboardButton(text='♍️ Virgo', callback_data='virgo')
key_libra = types.InlineKeyboardButton(text='♎️ Libra', callback_data='libra')
key_scorpio = types.InlineKeyboardButton(text='♏️ Scorpio', callback_data='scorpio')
key_sagittarius = types.InlineKeyboardButton(text='♐️ Sagittarius', callback_data='sagittarius')
key_capricorn = types.InlineKeyboardButton(text='♑️ Capricorn', callback_data='capricorn')
key_aquarius = types.InlineKeyboardButton(text='♒️ Aquarius', callback_data='aquarius')
key_pisces = types.InlineKeyboardButton(text='♓️ Pisces', callback_data='pisces')

keyboard.add(key_aries, key_taurus, key_gemini, key_cancer, key_leo, key_virgo, key_virgo,
             key_libra, key_scorpio, key_saggitarius, key_capricorn, key_aquarius, key_pisces)

daily_keyboard = types.InlineKeyboardMarkup()

yesterday = types.InlineKeyboardButton(text='Yesterday', callback_data='yesterday')
today = types.InlineKeyboardButton(text='Today', callback_data='today')
tomorrow = types.InlineKeyboardButton(text='Tomorrow', callback_data='tomorrow')

daily_keyboard.add(yesterday, today, tomorrow)
