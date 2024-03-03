import telebot
from telebot import types
import os
import config

bot = telebot.TeleBot(config.TOKEN)

f = "\n \033[01;30m Bot Firstname: {} \033[0m".format(bot.get_me().first_name)
u = "\n\n \033[01;34m Bot username: {} \033[0m".format(bot.get_me().username)
i = "\n\n \033[01;32m Bot ID: {} \033[0m".format(bot.get_me().id)
c = "\n\n \033[01;31m Gracias papá :)  Estoy completamente en línea ahora :D \033[0m"
print(f + u + i + c)

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

bot.infinity_polling()