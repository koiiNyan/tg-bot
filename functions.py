import telegram
import logging

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




"""




def calculator(string):
    
    try:

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
    return result



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

        


    custom_keyboard = [['1', '2', '3', '+'], 
                       ['4', '5', '6', '-'],
                       ['7', '8', '9', '*'],
                       ['0', '/', '=']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=update.message.chat.id,
                     text='Enter the number',  
                     reply_markup=reply_markup)
"""
