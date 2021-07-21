import telebot
import config
from keyboard import *
import requests
from googletrans import Translator

from messages import messages

bot = telebot.TeleBot(config.TOKEN)
translator = Translator()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, messages['greetings'].format(name=message.chat.first_name))
    bot.send_message(message.from_user.id, messages['choose_zodiac'], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.message:
        sign = call.data

        response = requests.post('https://aztro.sameerkumar.website/', params={'sign': sign})
        text = response.json().get('description')
        translated_text = translator.translate(text, src='en', dest='ru')

        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        bot.delete_message(call.message.chat.id, call.message.message_id)

        bot.send_message(call.message.chat.id, messages['horoscope'].format(
            name=call.message.chat.first_name,
            description=translated_text.text,
        ))


bot.polling(none_stop=True)
