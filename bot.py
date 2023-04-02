import telegram
from telegram.ext import (CommandHandler, CallbackQueryHandler,
                          ConversationHandler, MessageHandler, Filters,
                          CallbackContext)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start(update: telegram.Update, context: CallbackContext) -> int:
    keyboard = [
        [InlineKeyboardButton("Botó 1", callback_data='1')],
        [InlineKeyboardButton("Botó 2", callback_data='2')],
        [InlineKeyboardButton("Botó 3", callback_data='3')],
        [InlineKeyboardButton("Botó 4", callback_data='4')],
        [InlineKeyboardButton("Botó 5", callback_data='5')],
        [InlineKeyboardButton("Botó 6", callback_data='6')],
        [InlineKeyboardButton("Botó 7", callback_data='7')],
        [InlineKeyboardButton("Botó 8", callback_data='8')],
        [InlineKeyboardButton("Botó 9", callback_data='9')],
        [InlineKeyboardButton("Botó 10", callback_data='10')],
        [InlineKeyboardButton("Botó 11", callback_data='11')],
        [InlineKeyboardButton("Botó 12", callback_data='12')],
        [InlineKeyboardButton("Botó 13", callback_data='13')],
        [InlineKeyboardButton("Botó 14", callback_data='14')],
        [InlineKeyboardButton("Botó 15", callback_data='15')],
        [InlineKeyboardButton("Botó 16", callback_data='16')],
        [InlineKeyboardButton("Botó 17", callback_data='17')],
        [InlineKeyboardButton("Botó 18", callback_data='18')],
        [InlineKeyboardButton("Botó 19", callback_data='19')],
        [InlineKeyboardButton("Botó 20", callback_data='20')],
        [InlineKeyboardButton("Botó 21", callback_data='21')],
        [InlineKeyboardButton("Botó 22", callback_data='22')],
        [InlineKeyboardButton("Botó 23", callback_data='23')],
        [InlineKeyboardButton("Botó 24", callback_data='24')],
        [InlineKeyboardButton("Botó 25", callback_data='25')],
        [InlineKeyboardButton("Botó 26", callback_data='26')],
        [InlineKeyboardButton("Botó 27", callback_data='27')],
        [InlineKeyboardButton("Botó 28", callback_data='28')],
        [InlineKeyboardButton("Botó 29", callback_data='29')],
        [InlineKeyboardButton("Botó 30", callback_data='30')],
        [InlineKeyboardButton("Botó 31", callback_data='31')],
        [InlineKeyboardButton("Botó 32", callback_data='32')]
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
