from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from commands import button, start, stocks
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

updater = Updater(token='1168329877:AAGZiLUM9TNhABPrDfl92QnV4vYKFVjs_Bg', use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

stocks_handler = CommandHandler('stocks', stocks)
dispatcher.add_handler(stocks_handler)

# img_handler = CommandHandler('img', img)
# dispatcher.add_handler(img_handler)

dispatcher.add_handler(CallbackQueryHandler(button))

updater.start_polling()
