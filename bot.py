from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
import settings
import ephem
import datetime
date = datetime.datetime.now()

def main():
    mybot = Updater(settings.TELEGRAM_KEY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", planet, pass_args=True))
    dp.add_handler(CommandHandler("wordcount", wordcount, pass_args=True))
    dp.add_handler(CommandHandler("calculate", calculate, pass_args=True))
    dp.add_handler(CommandHandler("wcalc", wcalc, pass_args=True))
    dp.add_handler(CommandHandler("help", helpp))


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

def planet (bot, update, args):
    text = '/planet'
    print(text)
    request = 'Enter the planet name, please. Usage of the bot: /planet planetname'
    update.message.reply_text(request)

    planet = args[0]
    print(planet)
    if planet.lower() == 'mercury':
        planet = ephem.Mercury(date)
        planet = ephem.constellation(planet)
        update.message.reply_text("Mercury is in {}".format(planet))


    elif planet.lower() == 'venus':
        planet = ephem.Venus(date)
        planet = ephem.constellation(planet)
        update.message.reply_text("Venus is in {}".format(planet))

    elif planet.lower() == 'mars':
        planet = ephem.Mars(date)
        planet = ephem.constellation(planet)
        update.message.reply_text("Mars is in {}".format(planet))

    elif planet.lower() == 'jupiter':
        planet = ephem.Jupiter(date)
        planet = ephem.constellation(planet)
        update.message.reply_text("Jupiter is in {}".format(planet))

    elif planet.lower() == 'saturn':
        planet = ephem.Saturn(date)
        planet = ephem.constellation(planet)
        update.message.reply_text("Saturn is in {}".format(planet))

    elif planet.lower() == 'uranus':
        planet = ephem.Uranus(date)
        planet = ephem.constellation(planet)
        update.message.reply_text("Uranus is in {}".format(planet))

    elif planet.lower() == 'neptune':
        planet = ephem.Neptune(date)
        planet = ephem.constellation(planet)
        update.message.reply_text("Neptune is in {}".format(planet))


    else:
        error = (
            'I can tell you the position of only 7 planets of our Solar System: ' 
            'Mercury, Venus, Mars, Jupiter, Saturn, Uranus and Neptune :c'
            )
        update.message.reply_text(error)



def wordcount(bot, update, args): 
    text = '/wordcount'
    print(text)
    request = 'Enter the string, please. Usage of the bot: /wordcount message'
    update.message.reply_text(request)
    string_count = len(args)
    logging.info(update.message.text)
    update.message.reply_text("{} words!".format(string_count))



def calculate(bot, update, args):
    text = '/calculate'
    print(text)
    logging.info(update.message.text)
    
    try:
        
        if len(args) == 1:
            if '+' in args[0]:
                elements = args[0][:-1].split('+')
                answer = sum(map(int, elements))
                update.message.reply_text("Answer: {}".format(answer))
    
            elif '-' in args[0]:
                elements = args[0][:-1].split('-')
                answer = int(elements[0]) - int(elements[1])
                update.message.reply_text("Answer: {}".format(answer))
    
            elif '*' in args[0]:
                elements = args[0][:-1].split('*')
                answer = int(elements[0]) * int(elements[1])
                update.message.reply_text("Answer: {}".format(answer))
    
            elif '/' in args[0]:
                try:
                    elements = args[0][:-1].split('/')
                    answer = int(elements[0]) / int(elements[1])
                    update.message.reply_text("Answer: {}".format(answer))
                except ZeroDivisionError:
                    zeroerr = update.message.reply_text("Can't divide by zero!")
                    return zeroerr

        else:
            spaceserr = update.message.reply_text("Don't use spaces please! Usage of bot: /calculate 1+1=")
            return spaceserr

    except IndexError:
        inderr = spaceserr = update.message.reply_text("""Error: You haven't entered the numbers :c
            Usage of bot: /calculate 1+1=""" )
        return inderr


 
def wcalc (bot, update, args):
    text = '/wcalc'
    print(text)
    logging.info(update.message.text)
    known = {
        'один': '1',
        'one': '1',
        'два': '2',
        'two': '2',
        'three': '3',
        'три': '3',
        'four': '4',
        'четыре': '4',
        'five': '5',
        'пять': '5',
        'six': '6',
        'шесть': '6',
        'seven': '7',
        'семь': '7',
        'eight': '8',
        'восемь': '8',
        'nine': '9',
        'девять': '9',
        'ten': '10',
        'десять': '10',
        'плюс': '+',
        'plus': '+',
        'minus': '-',
        'минус': '-',
        'умножить': '*',
        'multiply': '*',
        'поделить': '/',
        'divide': '/'
    }

    def prepare(args):
        result = ""
        for arg in args:
            if arg in known:
                result += known[arg]
        return result+"="

    calculate(bot, update, [prepare(args)])                



def helpp(bot, update):
    text1 = '/help'
    print(text1)

    text = """I understand the following commands: 
    /planet planetname - tells you the position of the planet
    /wordcount message - counts the words in your message
    /calculate 1+1= (+, -, *, /) - simple calculator
    /wcalc one plus one (minus, multiply, divide) - you can use words instead of numbers"""

    update.message.reply_text(text)

logging.info("Bot started")
main()

