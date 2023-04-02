import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

def start(update, context):
    keyboard = [
        [
            InlineKeyboardButton("Button 1", callback_data='1'),
            InlineKeyboardButton("Button 2", callback_data='2'),
            InlineKeyboardButton("Button 3", callback_data='3'),
            InlineKeyboardButton("Button 4", callback_data='4')
        ],
        [
            InlineKeyboardButton("Button 5", callback_data='5'),
            InlineKeyboardButton("Button 6", callback_data='6'),
            InlineKeyboardButton("Button 7", callback_data='7'),
            InlineKeyboardButton("Button 8", callback_data='8')
        ],
        [
            InlineKeyboardButton("Button 9", callback_data='9'),
            InlineKeyboardButton("Button 10", callback_data='10'),
            InlineKeyboardButton("Button 11", callback_data='11'),
            InlineKeyboardButton("Button 12", callback_data='12')
        ],
        [
            InlineKeyboardButton("Button 13", callback_data='13'),
            InlineKeyboardButton("Button 14", callback_data='14'),
            InlineKeyboardButton("Button 15", callback_data='15'),
            InlineKeyboardButton("Button 16", callback_data='16')
        ],
        [
            InlineKeyboardButton("Button 17", callback_data='17'),
            InlineKeyboardButton("Button 18", callback_data='18'),
            InlineKeyboardButton("Button 19", callback_data='19'),
            InlineKeyboardButton("Button 20", callback_data='20')
        ],
        [
            InlineKeyboardButton("Button 21", callback_data='21'),
            InlineKeyboardButton("Button 22", callback_data='22'),
            InlineKeyboardButton("Button 23", callback_data='23'),
            InlineKeyboardButton("Button 24", callback_data='24')
        ],
        [
            InlineKeyboardButton("Button 25", callback_data='25'),
            InlineKeyboardButton("Button 26", callback_data='26'),
            InlineKeyboardButton("Button 27", callback_data='27'),
            InlineKeyboardButton("Button 28", callback_data='28')
        ],
        [
            InlineKeyboardButton("Button 29", callback_data='29'),
            InlineKeyboardButton("Button 30", callback_data='30'),
            InlineKeyboardButton("Button 31", callback_data='31'),
            InlineKeyboardButton("Button 32", callback_data='32')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query
    query.answer()

    button_number = query.data
    text = f'You pressed button number {button_number}'

    query.edit_message_text(text=text)


def main():
    token = '6011630982:AAF8viJgzYgtBaVTz-ETPPMrGMOnQTNu1eM'
    updater = Updater(token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
