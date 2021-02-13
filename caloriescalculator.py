from homework import *
from keyboard import *
from telegram import ReplyKeyboardRemove, ParseMode

from telegram.ext import ConversationHandler



def anketa_start_cal(bot, update):
    bot.message.reply_text(
        'Как Вас зовут?', reply_markup=ReplyKeyboardRemove()
        )
    return 'user_name'


def anketa_get_name_cal(bot, update):
    update.user_data['name'] = bot.message.text
    bot.message.reply_text('Какой у вас лимит на сегодня?')
    return 'user_calories'


def anketa_get_cal(bot, update):
    update.user_data['calories'] = bot.message.text
    bot.message.reply_text('сколько сегодня потратили?')
    return 'amount'


def anketa_get_amount_cal(bot, update):
    update.user_data['amount'] = bot.message.text
    bot.message.reply_text('напишите комментарий к записи')
    return 'comment'


def anketa_get_comment_cal(bot, update):
    update.user_data['comment'] = bot.message.text
    name, calories, amount, comment = (
        update.user_data['name'],
        update.user_data['calories'],
        update.user_data['amount'],
        update.user_data['comment'],
        )
    cal_calculator = CaloriesCalculator(int(calories))
    cal_calculator.add_record(Record(amount=int(amount), comment=comment))
    calc = cal_calculator.get_calories_remained()
    text = """Результат опроса:
    <b>Имя:</b> {}
    <b>Лимит на сегодня:</b> {}
    <b>Потрачено:</b> {}
    <b>Комментарий:</b> {}
    <b>{}</b>
    """.format(name,calories,amount,comment,calc)
    bot.message.reply_text(text, parse_mode=ParseMode.HTML)
    bot.message.reply_text(
        'Спасибо вам за то что воспользовались нашим калькулятором!', 
        reply_markup=get_keyboard()
        )
    return ConversationHandler.END