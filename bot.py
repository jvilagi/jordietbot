import os
import psycopg2
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

if __name__ == '__main__':
    updater.start_polling()


# Configuració de la base de dades Postgres
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

# Funció per crear la taula d'alumnes si no existeix
def create_table():
    cur.execute('''CREATE TABLE IF NOT EXISTS alumnes
                   (id SERIAL PRIMARY KEY, nom TEXT, info TEXT, ubicacio TEXT)''')
    conn.commit()

# Funció per afegir un alumne a la base de dades
def add_alumne(nom, info, ubicacio):
    cur.execute("INSERT INTO alumnes (nom, info, ubicacio) VALUES (%s, %s, %s)", (nom, info, ubicacio))
    conn.commit()

# Funció per recuperar la llista d'alumnes de la base de dades
def get_alumnes():
    cur.execute("SELECT nom FROM alumnes")
    rows = cur.fetchall()
    return rows

# Funció per recuperar la informació d'un alumne de la base de dades
def get_info(nom):
    cur.execute("SELECT info FROM alumnes WHERE nom=%s", (nom,))
    rows = cur.fetchall()
    return rows[0][0]

# Funció per recuperar la ubicació d'un alumne de la base de dades
def get_ubicacio(nom):
    cur.execute("SELECT ubicacio FROM alumnes WHERE nom=%s", (nom,))
    rows = cur.fetchall()
    return rows[0][0]

# Funció per crear els botons d'alumnes
def create_alumnes_buttons():
    alumnes = get_alumnes()
    buttons = []
    for alumne in alumnes:
        nom = alumne[0]
        button = InlineKeyboardButton(text=nom, callback_data=nom)
        buttons.append([button])
    return buttons

#
