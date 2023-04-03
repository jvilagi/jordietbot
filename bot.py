import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = "6011630982:AAFhEP6GSgdK8sLHQbo7LIZ7HW2nBwPYURw"

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Pau", callback_data="info_1"),
            InlineKeyboardButton("Luyi", callback_data="info_2"),
            InlineKeyboardButton("José A.", callback_data="info_3")
        ],
        [
            InlineKeyboardButton("Jordi", callback_data="info_4"),
            InlineKeyboardButton("Víctor", callback_data="info_5"),
            InlineKeyboardButton("Martí", callback_data="info_6")
        ],
        [
            InlineKeyboardButton("Marina", callback_data="info_7"),
            InlineKeyboardButton("Ana", callback_data="info_8"),
            InlineKeyboardButton("Beatriz", callback_data="info_9")
        ],
        [InlineKeyboardButton("Luyi", callback_data="info_10")],
        [InlineKeyboardButton("Luyi", callback_data="info_11")],
        [InlineKeyboardButton("Luyi", callback_data="info_12")],
        [InlineKeyboardButton("Luyi", callback_data="info_13")],
        [InlineKeyboardButton("Luyi", callback_data="info_14")],
        [InlineKeyboardButton("Luyi", callback_data="info_15")],
        [InlineKeyboardButton("Luyi", callback_data="info_16")],
        [InlineKeyboardButton("Luyi", callback_data="info_17")],
        [InlineKeyboardButton("Luyi", callback_data="info_18")],
        [InlineKeyboardButton("Luyi", callback_data="info_19")],
        [InlineKeyboardButton("Luyi", callback_data="info_20")],
        [InlineKeyboardButton("Luyi", callback_data="info_21")],
        [InlineKeyboardButton("Luyi", callback_data="info_22")],
        [InlineKeyboardButton("Luyi", callback_data="info_23")],
        [InlineKeyboardButton("Luyi", callback_data="info_24")],
        [InlineKeyboardButton("Luyi", callback_data="info_25")],
        [InlineKeyboardButton("Luyi", callback_data="info_26")],
        [InlineKeyboardButton("Luyi", callback_data="info_27")],
        [InlineKeyboardButton("Luyi", callback_data="info_28")],
        [InlineKeyboardButton("Luyi", callback_data="info_29")],
        # Afegir aquí la resta de botons
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("Tria un botó per obtenir més informació:", reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    info = {
        "info_1": "Brady Stuart, Lorraine: 24 The Dunes, Portmarnock (tel:01-8462622)",
        "info_2": "Brady Stuart, Lorraine: 24 The Dunes, Portmarnock (tel:01-8462622)",
        "info_3": "Brady Stuart, Lorraine: 24 The Dunes, Portmarnock (tel:01-8462622)",
        "info_4": "Chalkley John, Fiona: 24 Beechpark, Portmarnock (tel:018463522)",
        "info_5": "Aquesta és la informació del botó 2.",
        "info_6": "Aquesta és la informació del botó 2.",
        "info_7": "Aquesta és la informació del botó 2.",
        "info_8": "Aquesta és la informació del botó 2.",
        "info_9": "Aquesta és la informació del botó 2.",
        "info_10": "Aquesta és la informació del botó 2.",
        "info_11": "Aquesta és la informació del botó 2.",
        "info_12": "Aquesta és la informació del botó 2.",
        "info_13": "Aquesta és la informació del botó 2.",
        "info_14": "Aquesta és la informació del botó 2.",
        "info_15": "Aquesta és la informació del botó 2.",
        "info_16": "Aquesta és la informació del botó 2.",
        "info_17": "Aquesta és la informació del botó 2.",
        "info_18": "Aquesta és la informació del botó 2.",
        "info_19": "Aquesta és la informació del botó 2.",
        "info_20": "Aquesta és la informació del botó 2.",
        "info_21": "Aquesta és la informació del botó 2.",
        "info_22": "Aquesta és la informació del botó 2.",
        "info_23": "Aquesta és la informació del botó 2.",
        "info_24": "Aquesta és la informació del botó 2.",
        "info_25": "Aquesta és la informació del botó 2.",
        "info_26": "Aquesta és la informació del botó 2.",
        "info_27": "Aquesta és la informació del botó 2.",
        "info_28": "Aquesta és la informació del botó 2.",
        "info_29": "Aquesta és la informació del botó 2.",
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
