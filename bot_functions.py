import datetime
import json
import re
import logging

def sending_start_message(bot, message, types):
    bot.send_message(message.chat.id, 'Hola Mundo', parse_mode='html')
