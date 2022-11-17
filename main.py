import os
import sys
import telebot

from telebot import types
from dotenv import load_dotenv
from mako.template import Template

# load variables from .env file
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN") 
bot = telebot.TeleBot(TOKEN)

# check if token provided
if len(TOKEN) == 0:
    print("Please fill up u token into .env file")
    sys.exit(1)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.from_user.id, "Press buttons for interactiong with bot")

# static data
fcToday = """
overcast clouds ☁️
☀ temperature: 5.74 °C
💧 Umidity: 61%
📊 pressure: 1011 hPa
☁️ cloudiness: 100%
💨 wind: 2.68 Km\h
🌅 sunrise: 05:29:34
🌄 sunset: 14:48:57
"""

fcFiveDays = """
16/11/2022:
overcast clouds
Min: 2.15 - Max: 6.57 °C 

17/11/2022:
moderate rain
Min: 6.67 - Max: 10.99 °C 

18/11/2022:
moderate rain
Min: 5.95 - Max: 11.69 °C 

19/11/2022:
moderate rain
Min: 4.44 - Max: 12.32 °C 

20/11/2022:
light rain
Min: 4.24 - Max: 11.41 °C
"""

# format and send single forecast + menu
def single_forecast(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    todayBtn = types.InlineKeyboardButton('❮ 5 дней ❯', callback_data="today")
    markup.add(todayBtn)
    bot.send_message(message.from_user.id, fcToday, reply_markup=markup)

# handle all chat messages
@bot.message_handler(content_types=['text'])
def all_messages(message):
    # user city like: Таганрог, Москва etc. 
    single_forecast(message)

# handle callback  
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "today":
        bot.send_message(call.message.chat.id, Template(fcFiveDays).render())

# program execution entrypoint
def main():
    bot.infinity_polling()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
