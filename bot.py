import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = "6011630982:AAFhEP6GSgdK8sLHQbo7LIZ7HW2nBwPYURw"

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("HOUSES LOCATION MAP", callback_data="map")
        ],
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

    update.message.reply_text("In each row of buttons are the members of the house.\nClick and the address and phone number will appear", reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    info = {
        "map": "CLICK TO DISPLAY THE MAP: \nhttps://bit.ly/irelandslc",
        "info_1": "PAU IGLESIAS\nBrady Stuart, Lorraine: \n24 The Dunes, Portmarnock \n(tel: 01 8462622)",
        "info_2": "LUYI LIN\nBrady Stuart, Lorraine: \n24 The Dunes, Portmarnock \n(tel: 01 8462622)",
        "info_3": "JOSÉ ANTONIO OROZCO\nBrady Stuart, Lorraine: \n24 The Dunes, Portmarnock \n(tel: 01 8462622)",
        "info_4": "JORDI LLOVICH\nChalkley John, Fiona: \n24 Beechpark, Portmarnock \n(tel: 01 8463522)",
        "info_5": "VÍCTOR ALONSO\nChalkley John, Fiona: \n24 Beechpark, Portmarnock \n(tel: 01 8463522)",
        "info_6": "MARTÍ GONZÁLEZ\nChalkley John, Fiona: \n24 Beechpark, Portmarnock \n(tel: 01 8463522)",
        "info_7": "MARINA DÍAZ-BENITO\nDoyle(Cronin) Dermot, Bernadette: \n165 Briar Walk, Portmarnock \n(tel: 01 8284787)",
        "info_8": "ANA TOLOSANO\nDoyle(Cronin) Dermot, Bernadette: \n165 Briar Walk, Portmarnock \n(tel: 01 18284787)",
        "info_9": "BEATRIZ GONZÁLEZ\nDoyle(Cronin) Dermot, Bernadette: \n165 Briar Walk, Portmarnock \n(tel: 01 8284787)",
        "info_10": "YAO YAO CHEN\nGleeson Eoghan, Maureen: \n32 Portmarnock Drive, Portmarnock \n(tel: 01 4432458)",
        "info_11": "ALEXANDRA LASCORZ\nGleeson Eoghan, Maureen: \n32 Portmarnock Drive, Portmarnock \n(tel: 01 4432458)",
        "info_12": "MAR DIJORT\nMc Dermott John, Sarah: \n13 Limetree Ave., Portmarnock \n(tel: 086 8643956)",
        "info_13": "CORAL FRUCTUOSO\nMc Dermott John, Sarah: \n13 Limetree Ave., Portmarnock \n(tel: 086 8643956)",
        "info_14": "AINA PLANA\nMooney, Linda: \n70 The Dunes, Portmarnock \n(tel: 086 3868543)",
        "info_15": "IMMA MARTÍNEZ\nMooney, Linda: \n70 The Dunes, Portmarnock \n(tel: 086 3868543)",
        "info_16": "OLGA CAMPS\nMooney, Linda: \n70 The Dunes, Portmarnock \n(tel: 086 3868543)",
        "info_17": "RITA SERRA\nMooney, Linda: \n70 The Dunes, Portmarnock \n(tel: 086 3868543)",
        "info_18": "ALEXIA BLANCO\nMoore A Edward, Ann: \n14 Limetree Avenue, Portmarnock \n(tel: 087 2408323)",
        "info_19": "MARTINA SECO\nMoore A Edward, Ann: \n14 Limetree Avenue, Portmarnock \n(tel: 087 2408323)",
        "info_20": "PAULA ESTELA\nMoore A Edward, Ann: \n14 Limetree Avenue, Portmarnock \n(tel: 087 2408323)",
        "info_21": "IRIA ÁLVAREZ\nO'Connor Tom, Evelyn: \n213 Ardilaun, Portmarnock \n(tel: 01 8463090)",
        "info_22": "MÒNICA ROCADENBOSCH\nO'Connor Tom, Evelyn: \n213 Ardilaun, Portmarnock \n(tel: 01 8463090)",
        "info_23": "BERTA CALABIA\nO'Connor Tom, Evelyn: \n213 Ardilaun, Portmarnock \n(tel: 01 8463090)",
        "info_24": "JANA LLAURADÓ\nMcIntyre Barn, Trena: 5\n4 Torcail, Portmarnock \n(tel: 01 8459920)",
        "info_25": "MIREIA SAEZ\nMcIntyre Barn, Trena: \n54 Torcail, Portmarnock \n(tel: 01 8459920)",
        "info_26": "CLÁUDIA MARTÍNEZ\nMcIntyre Barn, Trena: \n54 Torcail, Portmarnock \n(tel: 01 8459920)",
        "info_27": "LAURA MARTÍ\nArcher Simon, Deirdre: \n28 Carrickhill Walk, Portmarnock \n(tel: 01 8463979)",
        "info_28": "CARLA ALBA\nArcher Simon, Deirdre: \n28 Carrickhill Walk, Portmarnock \n(tel: 01 8463979)",
        "info_29": "FRANCESC XAVIER SUÑER\nLloyd B Eddie, Bridie: \n69 Carrick Court, Portmarnock \n(tel: 086 1302292)",
        "info_30": "GABRIEL ROMERO\nLloyd B Eddie, Bridie: \n69 Carrick Court, Portmarnock \n(tel: 086 1302292)",
        "info_31": "ZIHAO YANG\nLloyd Joe, Elaine: \n74 Portmarnock Drive, Portmarnock \n(tel: 087 6868776)",
        "info_32": "GERARDO ANDRÉS HERNÁNDEZ\nLloyd Joe, Elaine: \n74 Portmarnock Drive, Portmarnock \n(tel: 087 6868776)",
        "info_33": "SERGI & JORDI \nWilliams Peter, Norma: \n8 Waterside Crescent, Portmarnock \n(tel: 01 8461063)",
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
