from telegram import ReplyKeyboardMarkup, ReplyKeyboardMarkup

def get_keyboard():
    my_keyboard = ReplyKeyboardMarkup(
        [['Начать'], ['Калькулятор денег'], ['Калькулятор каллорий']], resize_keyboard=True
        )
    return my_keyboard