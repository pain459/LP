import configparser
import requests
import spacy
import nltk
from datetime import datetime, timedelta
from transformers import pipeline, Conversation, BertTokenizer, BertForTokenClassification
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Predefined responses for greetings and farewells
GREETINGS = ['hello', 'hi', 'hey', 'greetings', 'what\'s up']
FAREWELLS = ['bye', 'goodbye', 'see you', 'farewell']

# Load pre-trained model for conversational AI
conversational_pipeline = pipeline('conversational', model='microsoft/DialoGPT-medium')

# Load pre-trained BERT model for NER
tokenizer = BertTokenizer.from_pretrained('dbmdz/bert-large-cased-finetuned-conll03-english')
model = BertForTokenClassification.from_pretrained('dbmdz/bert-large-cased-finetuned-conll03-english')
ner_pipeline = pipeline('ner', model=model, tokenizer=tokenizer)

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
        location, date = extract_location_and_date(message)
        if location:
            weather_info = get_weather(location, date)
            response = evaluate_weather_question(message, weather_info, date)
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

def extract_location_and_date(message: str) -> tuple:
    doc = nlp(message)
    location = None
    date = datetime.now().date()

    for ent in doc.ents:
        if ent.label_ == 'GPE':  # Geopolitical Entity (e.g., city names)
            location = ent.text
        elif ent.label_ == 'DATE':
            date_text = ent.text.lower()
            if 'tomorrow' in date_text:
                date = datetime.now().date() + timedelta(days=1)
            elif 'today' in date_text:
                date = datetime.now().date()

    if not location:
        # Use BERT NER if spaCy fails
        ner_results = ner_pipeline(message)
        for result in ner_results:
            if result['entity'] == 'B-LOC':
                location = result['word']
                break

    return location, date

def get_weather(location: str, date: datetime) -> dict:
    if date == datetime.now().date():
        # Current weather
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_API_KEY}&units=metric"
    else:
        # Forecast weather
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def evaluate_weather_question(message: str, weather_info: dict, date: datetime) -> str:
    if weather_info.get('cod') != 200:
        return f"Could not retrieve weather information for {weather_info.get('message', 'unknown location')}."
    
    if date == datetime.now().date():
        weather_description = weather_info['weather'][0]['description']
        temperature = weather_info['main']['temp']
        return f"The weather in {weather_info['name']} today is currently {weather_description} with a temperature of {temperature}°C."
    else:
        # Find the weather forecast for the next day
        for forecast in weather_info['list']:
            forecast_date = datetime.fromtimestamp(forecast['dt']).date()
            if forecast_date == date:
                weather_description = forecast['weather'][0]['description']
                temperature = forecast['main']['temp']
                return f"The weather forecast for {weather_info['city']['name']} on {date.strftime('%A')} is {weather_description} with a temperature of {temperature}°C."
        return f"Could not find the weather forecast for {weather_info['city']['name']} on {date.strftime('%A')}."

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
