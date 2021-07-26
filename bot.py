import telebot
import config
from keyboard import *
import requests

from messages import messages

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, messages['greetings'].format(name=message.chat.first_name))
    bot.send_message(message.from_user.id, messages['choose_zodiac'], reply_markup=keyboard)


@bot.callback_query_handler(
    func=lambda c: c.data in ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius',
                              'capricorn', 'aquarius', 'pisces']
)
def get_sign(call):
    global sign
    sign = call.data

    bot.delete_message(call.message.chat.id, call.message.message_id - 1)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id, messages['choose_day'], reply_markup=daily_keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.message:
        day = call.data

        response = requests.post('https://aztro.sameerkumar.website/', params={'sign': sign, 'day': day})
        json = response.json()

        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, messages['horoscope'].format(
            compatibility=json.get('compatibility'),
            date=json.get('current_date'),
            description=json.get('description')
        ))


bot.polling(none_stop=True)
