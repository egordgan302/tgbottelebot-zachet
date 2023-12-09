import telebot
from telebot import types


bot = telebot.TeleBot("6575506276:AAERV4hw8lignyyBbFshkkdUK3vAEddtIHo")
try:
    with open('questions.txt', 'r') as file:
        questions = file.readlines()
except FileNotFoundError:
    print("File questions.txt not found")
    exit()

score = 0

# Функция для отправки вопроса и кнопок
def send_question(message):
    global score
    if questions:
        question = questions.pop(0).strip()
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        options = ["Option 1", "Option 2", "Option 3", "Option 4"]
        for option in options:
            markup.add(types.KeyboardButton(option))
        bot.send_message(message.chat.id, question, reply_markup=markup)
    else:
        score = 0
        bot.send_message(message.chat.id, f"The quiz is over. Your account: {score}")
        questions.clear()       


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to the world of absurdity {0.first_name}! This quiz is a survival game, during the quiz your soul belongs to me, good luck".format(message.from_user))
# Обработчик ответов пользователя
@bot.message_handler(func=lambda message: True)
def handle_answer(message):
    global score
    # Проверяем правильность ответа и увеличиваем счет, если ответ правильный
    if message.text == "Correct option":
        score += 1
    send_question(message)

# Запускаем бота
bot.polling()


    
