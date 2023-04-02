import telegram
from telegram.ext import CallbackQueryHandler, CommandHandler, ConversationHandler, Filters, MessageHandler, Updater

TOKEN = '6011630982:AAF8viJgzYgtBaVTz-ETPPMrGMOnQTNu1eM'

# Estats per a la conversa amb el bot
FIRST, SECOND = range(2)

# Textos dels botons
boton_text = ['Botó 1', 'Botó 2', 'Botó 3', 'Botó 4', 'Botó 5', 'Botó 6', 'Botó 7', 'Botó 8', 'Botó 9', 'Botó 10',
              'Botó 11', 'Botó 12', 'Botó 13', 'Botó 14', 'Botó 15', 'Botó 16', 'Botó 17', 'Botó 18', 'Botó 19', 'Botó 20',
              'Botó 21', 'Botó 22', 'Botó 23', 'Botó 24', 'Botó 25', 'Botó 26', 'Botó 27', 'Botó 28', 'Botó 29', 'Botó 30',
              'Botó 31', 'Botó 32']

# Textos associats a cada botó
boton_info = ['Informació associada al botó 1', 'Informació associada al botó 2', 'Informació associada al botó 3',
              'Informació associada al botó 4', 'Informació associada al botó 5', 'Informació associada al botó 6',
              'Informació associada al botó 7', 'Informació associada al botó 8', 'Informació associada al botó 9',
              'Informació associada al botó 10', 'Informació associada al botó 11', 'Informació associada al botó 12',
              'Informació associada al botó 13', 'Informació associada al botó 14', 'Informació associada al botó 15',
              'Informació associada al botó 16', 'Informació associada al botó 17', 'Informació associada al botó 18',
              'Informació associada al botó 19', 'Informació associada al botó 20', 'Informació associada al botó 21',
              'Informació associada al botó 22', 'Informació associada al botó 23', 'Informació associada al botó 24',
              'Informació associada al botó 25', 'Informació associada al botó 26', 'Informació associada al botó 27',
              'Informació associada al botó 28', 'Informació associada al botó 29', 'Informació associada al botó 30',
              'Informació associada al botó 31', 'Informació associada al botó 32']

# Funció que s'executa quan es rep el comandament /start
def start(update, context):
    # Es mostra un missatge d'inici i els botons
    text = "Hola! Fes clic a un dels botons per obtenir més informació."
    buttons = [[
