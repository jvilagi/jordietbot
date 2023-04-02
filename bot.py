import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler, CommandHandler, Updater


# Funció que s'executa quan es rep el comandament /ababol
def start(update, context):
    # Creem els botons
    button1 = InlineKeyboardButton(text='Botó 1', callback_data='button1')
    button2 = InlineKeyboardButton(text='Botó 2', callback_data='button2')
    button3 = InlineKeyboardButton(text='Botó 3', callback_data='button3')

    # Creem el teclat amb els botons
    keyboard = [[button1], [button2], [button3]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Enviem el missatge amb el teclat
    update.message.reply_text(
        'Hola! Aquí tens els botons:',
        reply_markup=reply_markup
    )


# Funció que s'executa quan es prem un dels botons
def button_callback(update, context):
    # Obtenim la informació del botó premut
    query = update.callback_query
    query.answer()

    button = query.data
    # Mostrem la informació associada a cada botó
    if button == 'button1':
        query.edit_message_text('Has clicat el Botó 1')
    elif button == 'button2':
        query.edit_message_text('Has clicat el Botó 2')
    elif button == 'button3':
        query.edit_message_text('Has clicat el Botó 3')


def main():
    # Configuració del logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Obtenim el token del bot a partir de la variable d'entorn
    token = os.environ.get('6011630982:AAF8viJgzYgtBaVTz-ETPPMrGMOnQTNu1eM')

    # Creem l'objecte bot amb el token
    updater = Updater(token, use_context=True)

    # Assignem els handlers
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('ababol', start))
    dispatcher.add_handler(CallbackQueryHandler(button_callback))

    # Iniciem el bot
    updater.start_polling()

    # Bucle principal del bot
    updater.idle()


if __name__ == '__main__':
    main()
