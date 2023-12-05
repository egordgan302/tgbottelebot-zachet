import telebot
from telebot import types

bot = telebot.TeleBot("6575506276:AAERV4hw8lignyyBbFshkkdUK3vAEddtIHo")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("ВИКТОРИНА"))
    bot.send_message(message.chat.id, "Привет, давай поиграем в викторину?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.lower() == "да":
        ask_questions(message.chat.id)

def ask_questions(chat_id):
    with open("questions.txt", encoding="utf-8") as file:
        questions = file.readlines()
    for question in questions:
        bot.send_message(chat_id, question.strip())

bot.polling()


    
