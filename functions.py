import telegram
import logging
import ephem
from datetime import datetime
date = datetime.now()


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
    """






    custom_keyboard = [['1', '2', '3', '+'], 
                       ['4', '5', '6', '-'],
                       ['7', '8', '9', '*'],
                       ['0', '/', '=']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=update.message.chat.id,
                     text='Enter the number',  
                     reply_markup=reply_markup)
"""


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


def moon(bot, update):
    text = '/moon'
    print(text)
    next_full_moon = ephem.next_full_moon(date)
    update.message.reply_text("Next full moon: {}".format(next_full_moon))



def currdate(bot, update):
    text = '/date'
    print(text)
    currdate = (date.strftime ('%d.%m.%Y %H:%M'))
    update.message.reply_text("Current date: {}".format(currdate))



city = [
        'Москва', 'Альметьевск', 'Киев', 'Владимир', 'Ростов-на-Дону', 'Архангельск', 'Коломна', 'Анапа', 
        'Арзамас', 'Санкт-Петербург', 'Голицыно', 'Обнинск', 'Калуга'
       ]

def cities(bot, update, args):
    text = '/cities'
    print(text)


    user_input = args[0]

    while True: 
        
        if user_input in city:
            city.remove(user_input)
            for i in range(len(city)):
                if city[i][0] == user_input[-1].upper():
                    update.message.reply_text(city.pop(i))
                    break
            return
                
        else:
            update.message.reply_text("Я не знаю такого города!")
            break
        return



def ext_calc(bot, update, args):
    text = '/extcalc'
    print(text)
    logging.info(update.message.text)

    try:
        string = args[0]
        string = string.lower().replace(" ", "") 
        parts = string.split("+") 

        for plus in range(len(parts)): 
            if "-" in parts[plus]:
                parts[plus] = parts[plus].split("-")


        for plus in range (len(parts)):
            parts[plus] = precalculator(parts[plus])

        result = sum(parts)
    except ValueError:
        result = "Enter numbers, please!"
    except ZeroDivisionError:
        result = "Can't divide by zero!"
    return update.message.reply_text(result)



def precalculator(part):
    if type(part) is str:

        if "*" in part:
            result = 1
            for subpart in part.split("*"):
                result *= precalculator(subpart)
            return result
        

        elif "/" in part:
            parts = list(map(precalculator, part.split("/")))
            result = parts[0]
            for subpart in parts[1:]:
                result /= subpart
            return result

        else:
            return float(part)

    elif type(part) is list:
        for i in range(len(part)):
            part[i] = precalculator(part[i])

        return part[0] - sum(part[1:])
    return part