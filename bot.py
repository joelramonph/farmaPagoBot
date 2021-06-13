from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Hola Mundo soy Jivited')

if __name__ == '__main__' :

    updater = Updater(token='1849094192:AAEJl15yqmk4nmw-2pewiNWJlzDuaqjP4HQ', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    
    updater.start_polling()

    updater.idle()