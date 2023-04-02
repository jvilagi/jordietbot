import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler, CommandHandler, Filters, MessageHandler, Updater


def start(update, context):
    button1 = InlineKeyboardButton(text='Botó 1', callback_data='button1')
    button2 = InlineKeyboardButton(text='Botó 2', callback_data='button2')
    button3 = InlineKeyboardButton(text='Botó 3', callback_data='button3')

    keyboard = [[button1], [button2], [button3]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        'Hola! Aquí tens els botons:',
        reply_markup=reply_markup
    )


def button_callback(update, context):
    query = update.callback_query
    query.answer()

    button = query.data
    if button == 'button1':
        query.edit_message_text('Has clicat el Botó 1')
    elif button == 'button2':
        query.edit_message_text('Has clicat el Botó 2')
    elif button == 'button3':
        query.edit_message_text('Has clicat el Botó 3')


def main():
    # Configuració del logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Inicialització del bot
    token = os.environ.get('6011630982:AAF8viJgzYgtBaVTz-ETPPMrGMOnQTNu1eM')
    updater = Updater(token)

    # Assignació dels handlers
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(button_callback))

    # Inici del bot
    port = int(os.environ.get('PORT', '8443'))
    updater.start_webhook(listen='0.0.0.0', port=port, url_path=token)
    updater.bot.setWebhook('https://{}.herokuapp.com/{}'.format(os.environ.get('jordietbot'), token))

    # Bucle principal del bot
    updater.idle()


if __name__ == '__main__':
    main()
