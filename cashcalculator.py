from homework import *
from keyboard import *
from telegram import ReplyKeyboardRemove, ParseMode

from telegram.ext import ConversationHandler



def anketa_start(bot, update):
    bot.message.reply_text(
        'Как Вас зовут?', reply_markup=ReplyKeyboardRemove()
        )
    return 'user_name'


def anketa_get_name(bot, update):
    update.user_data['name'] = bot.message.text
    bot.message.reply_text('Какой у вас лимит на сегодня?')
    return 'user_cash'


def anketa_get_cash(bot, update):
    update.user_data['cash'] = bot.message.text
    bot.message.reply_text('сколько сегодня потратили?')
    return 'amount'


def anketa_get_amount(bot, update):
    update.user_data['amount'] = bot.message.text
    bot.message.reply_text('напишите комментарий к записи')
    return 'comment'

def anketa_get_comment(bot, update):
    update.user_data['comment'] = bot.message.text
    bot.message.reply_text('В какой валюте высести результат? rub/usd/eur')
    return 'currencies_code'


def anketa_currencies_code(bot, update):
    update.user_data['currencies_code'] = bot.message.text
    name, cash, amount, comment, currencies_code = (
        update.user_data['name'],
        update.user_data['cash'],
        update.user_data['amount'],
        update.user_data['comment'],
        update.user_data['currencies_code']
        )
    cash_calculator = CashCalculator(int(cash))
    cash_calculator.add_record(Record(amount=int(amount), comment=comment))
    calc = cash_calculator.get_today_cash_remained(currencies_code.lower())
    text = """Результат опроса:
    <b>Имя:</b> {}
    <b>Лимит на сегодня:</b> {}
    <b>Потрачено:</b> {}
    <b>Комментарий:</b> {}
    <b>{}</b>
    """.format(name,cash,amount,comment,calc)
    bot.message.reply_text(text, parse_mode=ParseMode.HTML)
    bot.message.reply_text(
        'Спасибо вам за то что воспользовались нашим калькулятором!', 
        reply_markup=get_keyboard()
        )
    return ConversationHandler.END