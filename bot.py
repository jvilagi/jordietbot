import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = "6011630982:AAFhEP6GSgdK8sLHQbo7LIZ7HW2nBwPYURw"

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Botó 1", callback_data="info_1")],
        [InlineKeyboardButton("Botó 2", callback_data="info_2")],
        # Afegir aquí la resta de botons
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("Tria un botó per obtenir més informació:", reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    info = {
        "info_1": "Aquesta és la informació del botó 1.",
        "info_2": "Aquesta és la informació del botó 2.",
        # Afegir aquí la resta d'informacions
    }

    query.edit_message_text(text=info[query.data])

def main() -> None:
    logging.basicConfig(level=logging.INFO)

    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
