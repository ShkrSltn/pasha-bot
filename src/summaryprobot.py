import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I am your bot.")

def main():
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
