import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, Filters, MessageHandler, Updater

# Definim la funció per a la comanda /ababol
def ababol(update, context):
    # Creem els botons
    buttons = [[InlineKeyboardButton("Botó 1", callback_data='button1'),
                InlineKeyboardButton("Botó 2", callback_data='button2'),
                InlineKeyboardButton("Botó 3", callback_data='button3')],
               [InlineKeyboardButton("Botó 4", callback_data='button4'),
                InlineKeyboardButton("Botó 5", callback_data='button5'),
                InlineKeyboardButton("Botó 6", callback_data='button6')],
               [InlineKeyboardButton("Botó 7", callback_data='button7'),
                InlineKeyboardButton("Botó 8", callback_data='button8'),
                InlineKeyboardButton("Botó 9", callback_data='button9')],
               [InlineKeyboardButton("Botó 10", callback_data='button10')]]

    # Creem el markup amb els botons
    reply_markup = InlineKeyboardMarkup(buttons)

    # Enviem el missatge amb els botons
    update.message.reply_text('Aquí tens els teus botons:', reply_markup=reply_markup)

# Definim la funció per gestionar les respostes als botons
def button(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"Has premut el botó {query.data}")

# Configuració del bot i dels handlers
TOKEN = "6011630982:AAF8viJgzYgtBaVTz-ETPPMrGMOnQTNu1eM"
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Afegim els handlers
dispatcher.add_handler(CommandHandler("ababol", ababol))
dispatcher.add_handler(CallbackQueryHandler(button))

# Iniciem el bot
updater.start_polling()
