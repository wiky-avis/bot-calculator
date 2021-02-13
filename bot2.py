import os
from dotenv import load_dotenv
from telegram.ext import (
    Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
    )
from caloriescalculator import *
from cashcalculator import *
from keyboard import *

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TOKEN')


def sms(bot, update):
    print('Кто-то отправил команду /start. Что мне делать?')
    bot.message.reply_text(
        f'Здравствуйте, {bot.message.chat.first_name}! '
        '\nЗаполните пожалуйста анкету', 
        reply_markup=get_keyboard()
        )


def main():
    my_bot = Updater(TELEGRAM_TOKEN)
    my_bot.dispatcher.add_handler(CommandHandler('start', sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Начать'), sms))
    my_bot.dispatcher.add_handler(ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('Калькулятор денег'), anketa_start)
            ], 
        states={
            'user_name': [MessageHandler(Filters.text, anketa_get_name)],
            'user_cash': [MessageHandler(Filters.text, anketa_get_cash)],
            'amount': [MessageHandler(Filters.text, anketa_get_amount)],
            'comment': [MessageHandler(Filters.text, anketa_get_comment)],
            'currencies_code': [
                MessageHandler(Filters.text, anketa_currencies_code)
                ],
            }, 
        fallbacks=[]
        ))
    my_bot.dispatcher.add_handler(ConversationHandler(
        entry_points=[
            MessageHandler(Filters.regex('Калькулятор каллорий'), anketa_start_cal)
            ], 
        states={
            'user_name': [MessageHandler(Filters.text, anketa_get_name_cal)],
            'user_calories': [MessageHandler(Filters.text, anketa_get_cal)],
            'amount': [MessageHandler(Filters.text, anketa_get_amount_cal)],
            'comment': [MessageHandler(Filters.text, anketa_get_comment_cal)],
            }, 
        fallbacks=[]
        ))


    my_bot.start_polling()
    my_bot.idle()


if __name__ == '__main__':
    main()