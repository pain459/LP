import configparser
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hi! I am your chatbot. How can I help you today?')

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    await update.message.reply_text(f'You said: {user_message}')

def main():
    # Read the token from the config.ini file
    config = configparser.ConfigParser()
    config.read('config.ini')
    token = config['telegram']['token']
    
    # Initialize the Application
    application = Application.builder().token(token).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    main()
