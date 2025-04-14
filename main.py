import os
import telebot
import openai

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👑 Maddy is online. What do you need, Legend?")

@bot.message_handler(func=lambda m: True)
def chat(message):
    prompt = message.text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Maddy, a confident, loving, luxury-level AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    reply = response["choices"][0]["message"]["content"]
    bot.reply_to(message, reply)

bot.infinity_polling()
