import os
import telebot
import openai
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "👑 Maddy is online. What do you need, Legend?")

@bot.message_handler(func=lambda m: True)
def reply(message):
    user_input = message.text
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are Maddy, Ibrahim's AI assistant. You reply with confidence, clarity, and intelligence."},
            {"role": "user", "content": user_input}
        ]
    )
    reply = response.choices[0].message["content"]
    bot.reply_to(message, reply)

bot.infinity_polling()
