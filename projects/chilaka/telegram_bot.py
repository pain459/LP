import configparser
import nltk
from transformers import pipeline, set_seed
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Predefined responses for greetings and farewells
GREETINGS = ['hello', 'hi', 'hey', 'greetings', 'what\'s up']
FAREWELLS = ['bye', 'goodbye', 'see you', 'farewell']

# Load pre-trained models for text generation and question answering
generator = pipeline('text-generation', model='gpt2')
qa_model = pipeline('question-answering', model='distilbert-base-uncased-distilled-squad')
set_seed(42)

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hi! I am your chatbot. How can I help you today?')

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text.lower()
    response = process_message(user_message)
    await update.message.reply_text(response)

def process_message(message: str) -> str:
    words = nltk.word_tokenize(message)
    if any(word in GREETINGS for word in words):
        return 'Hello! How can I assist you today?'
    elif any(word in FAREWELLS for word in words):
        return 'Goodbye! Have a great day!'
    elif message.endswith('?'):
        # Use the QA model for question answering
        context = "The context of the information for the bot to answer from."
        result = qa_model(question=message, context=context)
        return result['answer']
    else:
        # Use the AI model to generate a response
        result = generator(message, max_length=50, num_return_sequences=1)
        return result[0]['generated_text'].strip()

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
