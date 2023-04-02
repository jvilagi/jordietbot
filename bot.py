import telegram
from telegram.ext import (Updater, CommandHandler, CallbackQueryHandler,
                          ConversationHandler, MessageHandler, Filters,
                          CallbackContext)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start(update: telegram.Update, context: CallbackContext) -> int:
    keyboard = [
        [button1 = InlineKeyboardButton("Botó 1", callback_data="1")],
        [button2 = InlineKeyboardButton("Botó 2", callback_data="2")],
        [button1 = InlineKeyboardButton("Botó 3", callback_data="3")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Selecciona una opció:', reply_markup=reply_markup)

    return 1

def button(update: telegram.Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    query.edit_message_text(text="Informació associada al botó {}".format(query.data))

def main() -> None:
    TOKEN = '6011630982:AAF8viJgzYgtBaVTz-ETPPMrGMOnQTNu1eM'
    updater = telegram.Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
