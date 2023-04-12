import telebot
import openai

openai.api_key = ""
bot = telebot.TeleBot("6118628649:AAGMEpmDi9s7bw8Dm5krXnDHqOjJkw8vqYU")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hi, I'm your assistant. How can I help you today?")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "I can help you with a lot of things. Try sending me a message and I'll do my best to assist you.")

@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, "I'm online and ready to assist you.")

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, "I'm an chatbot created by Raja Josua Simanungkalit called KingJo.")

@bot.message_handler(func=lambda message: True)
def reply(message):
    completion = openai.Completion.create(engine="text-davinci-003", prompt=message.text, max_tokens=2048)
    bot.reply_to(message, completion.choices[0].text)

bot.polling()
