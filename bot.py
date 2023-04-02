import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Define a function that handles the /ababol command
def ababol_handler(update: Update, context: CallbackContext):
    # Define the buttons
    buttons = [
        ['Button 1', 'Button 2'],
        ['Button 3']
    ]

    # Send the message with the buttons
    context.bot.send_message(chat_id=update.effective_chat.id, text='Choose an option:', reply_markup={'keyboard': buttons, 'resize_keyboard': True})

def main():
    # Set up the logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Set up the updater and dispatcher
    updater = Updater('6011630982:AAF8viJgzYgtBaVTz-ETPPMrGMOnQTNu1eM', use_context=True)
    dispatcher = updater.dispatcher

    # Add the command handler
    dispatcher.add_handler(CommandHandler('ababol', ababol_handler))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
