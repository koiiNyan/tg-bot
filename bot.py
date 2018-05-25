import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PROXY = {'proxy_url': 'socks5://u0k12.tgproxy.me:1080',
    'urllib3_proxy_kwargs': {'username': 'telegram', 'password': 'telegram'}}

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
import functions
import settings
import ephem
from datetime import datetime
date = datetime.now()

def main():
    mybot = Updater(settings.TELEGRAM_KEY, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", functions.planet, pass_args=True))
    dp.add_handler(CommandHandler("wordcount", functions.wordcount, pass_args=True))
    dp.add_handler(CommandHandler("calculate", functions.calculate, pass_args=True))
    dp.add_handler(CommandHandler("wcalc", functions.wcalc, pass_args=True))
    dp.add_handler(CommandHandler("help", helpp))
    dp.add_handler(CommandHandler("moon", functions.moon))
    dp.add_handler(CommandHandler("date", functions.currdate))
    dp.add_handler(CommandHandler("extcalc", functions.ext_calc, pass_args=True))
    dp.add_handler(CommandHandler("cities", functions.cities, pass_args=True))


    mybot.start_polling()
    mybot.idle()

def greet_user(bot, update):
    text = 'Started'
    text1 = """Hello {}! 
Use /help for more info""".format(update.message.chat.first_name)
    print(text)
    update.message.reply_text(text1)



def talk_to_me(bot, update):
    user_text = update.message.text
    logging.info(user_text)
    print(user_text)
    update.message.reply_text("You said: " + user_text)



def helpp(bot, update):
    text1 = '/help'
    print(text1)

    text = """I understand the following commands: 
    /planet planetname - tells you the position of the planet
    /wordcount message - counts the words in your message
    /calculate 1+1= (+, -, *, /) - simple calculator
    /wcalc one plus one (minus, multiply, divide) - you can use words instead of numbers
    /moon - tells you when the next full moon is
    /date - tells you the current date
    /cities - игра в города (на русском) Пример: /cities Москва
    /extcalc - extended calculator, usage: /extcalc 1+1-2+3/4"""

    update.message.reply_text(text)



    







logging.info("Bot started")
main()

