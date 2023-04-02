import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Define a function that handles the /ababol command
def ababol_handler(update: Update, context: CallbackContext):
    # Define the buttons
    button1 = InlineKeyboardButton('Button 1', callback_data='1')
    button2 = InlineKeyboardButton('Button 2', callback_data='2')
    button3 = InlineKeyboardButton('Button 3', callback_data='3')
    buttons = [[button1, button2], [button3]]

    # Send the message with the buttons
    reply_markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text('Choose an option:', reply_markup=reply_markup)

# Define a function that handles the button callbacks
def button_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    # Get the button data
    button_data = query.data

    # Send a message with the button data
    message = f'The button pressed was {button_data}.'
    query.edit_message_text(text=message)

    # Remove the buttons
    query.message.reply_text('Buttons have been removed.', reply_markup=InlineKeyboardMarkup([[]]))

def main():
    # Set up the logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Set up the updater and dispatcher
    updater = Updater('6011630982:AAF8viJgzYgtBaVTz-ETPPMrGMOnQTNu1eM', use_context=True)
    dispatcher = updater.dispatcher

    # Add the command handler
    dispatcher.add_handler(CommandHandler('ababol', ababol_handler))

    # Add the callback query handler
    dispatcher.add_handler(CallbackQueryHandler(button_callback))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
