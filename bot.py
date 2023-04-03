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
        [
            InlineKeyboardButton("Yao Yao", callback_data="info_10"),
            InlineKeyboardButton("Alexandra", callback_data="info_11")
        ],
        [
            InlineKeyboardButton("Mar", callback_data="info_12"),
            InlineKeyboardButton("Coral", callback_data="info_13")
        ],
        [
            InlineKeyboardButton("Aina", callback_data="info_14"),
            InlineKeyboardButton("Imma", callback_data="info_15"),
            InlineKeyboardButton("Olga", callback_data="info_16"),
            InlineKeyboardButton("Rita", callback_data="info_17")
        ],
        [
            InlineKeyboardButton("Alexia", callback_data="info_18"),
            InlineKeyboardButton("Martina", callback_data="info_19"),
            InlineKeyboardButton("Paula", callback_data="info_20")
        ],
        [
            InlineKeyboardButton("Íria", callback_data="info_21"),
            InlineKeyboardButton("Mònica", callback_data="info_22"),
            InlineKeyboardButton("Berta", callback_data="info_23")
        ],
        [
            InlineKeyboardButton("Jana", callback_data="info_24"),
            InlineKeyboardButton("Mireia", callback_data="info_25"),
            InlineKeyboardButton("Clàudia", callback_data="info_26")
        ],
        [
            InlineKeyboardButton("Laura", callback_data="info_27"),
            InlineKeyboardButton("Carla", callback_data="info_28")
        ],
        [
            InlineKeyboardButton("F.Xavier", callback_data="info_29"),
            InlineKeyboardButton("Gabriel", callback_data="info_30")
        ],
        [
            InlineKeyboardButton("Zihao", callback_data="info_31"),
            InlineKeyboardButton("Gerardo A.", callback_data="info_32")
        ],
        [InlineKeyboardButton("Sergi & Jordi", callback_data="info_33")],
        # Afegir aquí la resta de botons
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("Tria un botó per obtenir més informació:", reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    info = {
        "info_1": "Brady Stuart, Lorraine: 24 The Dunes, Portmarnock (tel: 01 8462622)",
        "info_2": "Brady Stuart, Lorraine: 24 The Dunes, Portmarnock (tel: 01 8462622)",
        "info_3": "Brady Stuart, Lorraine: 24 The Dunes, Portmarnock (tel: 01 8462622)",
        "info_4": "Chalkley John, Fiona: 24 Beechpark, Portmarnock (tel: 01 8463522)",
        "info_5": "Chalkley John, Fiona: 24 Beechpark, Portmarnock (tel: 01 8463522",
        "info_6": "Chalkley John, Fiona: 24 Beechpark, Portmarnock (tel: 01 8463522",
        "info_7": "Doyle(Cronin) Dermot, Bernadette: 165 Briar Walk, Portmarnock (tel:01 8284787)",
        "info_8": "Doyle(Cronin) Dermot, Bernadette: 165 Briar Walk, Portmarnock (tel:01 18284787)",
        "info_9": "Doyle(Cronin) Dermot, Bernadette: 165 Briar Walk, Portmarnock (tel:01 8284787)",
        "info_10": "Gleeson Eoghan, Maureen: 32 Portmarnock Drive, Portmarnock (tel: 01 4432458)",
        "info_11": "Gleeson Eoghan, Maureen: 32 Portmarnock Drive, Portmarnock (tel: 01 4432458)",
        "info_12": "Mc Dermott John, Sarah: 13 Limetree Ave., Portmarnock (tel: 086 8643956)"
        "info_13": "Mc Dermott John, Sarah: 13 Limetree Ave., Portmarnock (tel: 086 8643956)",
        "info_14": "Mooney, Linda: 70 The Dunes, Portmarnock (tel: 086 3868543)",
        "info_15": "Mooney, Linda: 70 The Dunes, Portmarnock (tel: 086 3868543)",
        "info_16": "Mooney, Linda: 70 The Dunes, Portmarnock (tel: 086 3868543)",
        "info_17": "Mooney, Linda: 70 The Dunes, Portmarnock (tel: 086 3868543)",
        "info_18": "Moore A Edward, Ann: 14 Limetree Avenue, Portmarnock (tel: 087 2408323)",
        "info_19": "Moore A Edward, Ann: 14 Limetree Avenue, Portmarnock (tel: 087 2408323)",
        "info_20": "Moore A Edward, Ann: 14 Limetree Avenue, Portmarnock (tel: 087 2408323)",
        "info_21": "O'Connor Tom, Evelyn: 213 Ardilaun, Portmarnock (tel: 01 8463090)",
        "info_22": "O'Connor Tom, Evelyn: 213 Ardilaun, Portmarnock (tel: 01 8463090)",
        "info_23": "O'Connor Tom, Evelyn: 213 Ardilaun, Portmarnock (tel: 01 8463090)",
        "info_24": "McIntyre Barn, Trena: 54 Torcail, Portmarnock (tel: 01 8459920)",
        "info_25": "McIntyre Barn, Trena: 54 Torcail, Portmarnock (tel: 01 8459920)",
        "info_26": "McIntyre Barn, Trena: 54 Torcail, Portmarnock (tel: 01 8459920)",
        "info_27": "Archer Simon, Deirdre: 28 Carrickhill Walk, Portmarnock (tel:01 8463979)",
        "info_28": "Archer Simon, Deirdre: 28 Carrickhill Walk, Portmarnock (tel:01 8463979)",
        "info_29": "Lloyd B Eddie, Bridie: 69 Carrick Court, Portmarnock (tel:086 1302292)",
        "info_30": "Lloyd B Eddie, Bridie: 69 Carrick Court, Portmarnock (tel:086 1302292)",
        "info_31": "Lloyd Joe, Elaine: 74 Portmarnock Drive, Portmarnock (tel: 087 6868776)",
        "info_32": "Lloyd Joe, Elaine: 74 Portmarnock Drive, Portmarnock (tel: 087 6868776)",
        "info_33": "Williams Peter, Norma: 8 Waterside Crescent, Portmarnock (tel: 01 8461063)",
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
