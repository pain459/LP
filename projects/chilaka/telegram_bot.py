import configparser
import nltk
import requests
from transformers import pipeline, Conversation
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Predefined responses for greetings and farewells
GREETINGS = ['hello', 'hi', 'hey', 'greetings', 'what\'s up']
FAREWELLS = ['bye', 'goodbye', 'see you', 'farewell']

# Load pre-trained model for conversational AI
conversational_pipeline = pipeline('conversational', model='microsoft/DialoGPT-medium')

# Read the token from the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')
TELEGRAM_TOKEN = config['telegram']['token']
OPENWEATHER_API_KEY = config['openweather']['api_key']

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hi! I am your chatbot. How can I help you today?')

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text.lower()
    response = await process_message(user_message, context)
    await update.message.reply_text(response)

async def process_message(message: str, context: CallbackContext) -> str:
    words = nltk.word_tokenize(message)
    if any(word in GREETINGS for word in words):
        return 'Hello! How can I assist you today?'
    elif any(word in FAREWELLS for word in words):
        return 'Goodbye! Have a great day!'
    elif 'weather' in message:
        location = extract_location(message)
        if location:
            weather_info = get_weather(location)
            response = evaluate_weather_question(message, weather_info)
            return response
        else:
            return 'Please provide a location for the weather update.'
    else:
        # Maintain conversation context
        if 'conversation' not in context.user_data:
            context.user_data['conversation'] = Conversation()
        conversation = context.user_data['conversation']
        conversation.add_user_input(message)
        result = conversational_pipeline(conversation)
        response = result.generated_responses[-1]
        return response

def extract_location(message: str) -> str:
    # Extract location from the message (simplified for this example)
    words = message.split()
    for word in words:
        if word.lower() not in GREETINGS + FAREWELLS:
            return word
    return None

def get_weather(location: str) -> dict:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def evaluate_weather_question(message: str, weather_info: dict) -> str:
    if weather_info.get('cod') != 200:
        return f"Could not retrieve weather information for {weather_info.get('message', 'unknown location')}."
    weather_description = weather_info['weather'][0]['description']
    temperature = weather_info['main']['temp']
    return f"The weather in {weather_info['name']} is currently {weather_description} with a temperature of {temperature}°C."

def main():
    # Initialize the Application
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    main()
