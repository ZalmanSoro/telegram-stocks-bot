from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from stocks_api import get_stock_price_by_symbol
from snp500 import get_symbols
import numpy as np
from charts import get_img
import requests


def stocks(update, context):
    symbols = get_symbols()
    print("len at stocks = {}".format(len(symbols)))
    keys = list(map(lambda symbol: InlineKeyboardButton(symbol, callback_data=symbol), symbols))
    print("keys len = {}".format(len(keys)))
    keyboard = np.array_split(keys, len(symbols) / 5)

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    price = get_stock_price_by_symbol(query.data)
    query.answer()
    query.edit_message_text(text='The closed price of {} is {}'.format(query.data, price))


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, and welcome to Stocks2020 Bot!"
                                                                    " what would you like to do?")
