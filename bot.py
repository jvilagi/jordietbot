import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, Filters, MessageHandler, Updater

# Definim la funció per a la comanda /ababol
def ababol(update, context):
    # Creem els botons
    buttons = [[InlineKeyboardButton("Pau", callback_data='Brady Stuart, Lorraine: 24 The Dunes, Portmarnock (tel:01-8462622)'),
                InlineKeyboardButton("Luyi", callback_data='Brady Stuart, Lorraine: 24 The Dunes, Portmarnock (tel:01-8462622)'),
                InlineKeyboardButton("José A.", callback_data='Brady Stuart, Lorraine: 24 The Dunes, Portmarnock (tel:01-8462622)')],
               [InlineKeyboardButton("Jordi", callback_data='Chalkley John, Fiona: 24 Beechpark, Portmarnock (tel:01-8463522)'),
                InlineKeyboardButton("Víctor", callback_data='Chalkley John, Fiona: 24 Beechpark, Portmarnock (tel:01-8463522)'),
                InlineKeyboardButton("Martí", callback_data='Chalkley John, Fiona: 24 Beechpark, Portmarnock (tel:01-8463522)')],
               [InlineKeyboardButton("Marina", callback_data='Doyle(Cronin) Dermot, Bernadette: 165 Briar Walk, Portmarnock (tel:18284787)'),
                InlineKeyboardButton("Ana", callback_data='Doyle(Cronin) Dermot, Bernadette: 165 Briar Walk, Portmarnock (tel:18284787)'),
                InlineKeyboardButton("Beatriz", callback_data='Doyle(Cronin) Dermot, Bernadette: 165 Briar Walk, Portmarnock (tel:18284787)')],
               [InlineKeyboardButton("Botó 10", callback_data='button10')]]

    # Creem el markup amb els botons
    reply_markup = InlineKeyboardMarkup(buttons)

    # Enviem el missatge amb els botons
    update.message.reply_text('Aquí tens els teus botons:', reply_markup=reply_markup)

# Definim la funció per gestionar les respostes als botons
def button(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"{query.data}")

# Configuració del bot i dels handlers
TOKEN = "6011630982:AAF8viJgzYgtBaVTz-ETPPMrGMOnQTNu1eM"
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Afegim els handlers
dispatcher.add_handler(CommandHandler("ababol", ababol))
dispatcher.add_handler(CallbackQueryHandler(button))

# Iniciem el bot
updater.start_polling()
