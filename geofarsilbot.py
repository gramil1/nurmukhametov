import telebot, os
from telebot import types
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("Казань гид")
    markup.add(item1)
    bot.send_message(message.chat.id, "Привет! Чем могу помочь?", reply_markup=markup)
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'Казань гид':
        bot.send_message(message.chat.id, "Привет! Чем могу помочь?")
        bot.send_message(message.chat.id, "Я могу подсказать вам интересные места в городе Казань. Для этого отправьте мне свою геолокацию.")
    else:
        bot.send_message(message.chat.id, "Извините, я вас не понимаю. Попробуйте еще раз.")

@bot.message_handler(content_types=['location'])
def handle_location(message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    bot.send_message(message.chat.id, "Спасибо! Вот список интересных мест в вашем районе: ...")
bot.polling(none_stop=True, interval = 0)