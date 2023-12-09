import telebot
from telebot import types

# Создаем бота
bot = telebot.TeleBot("TOKEN")
try:
    with open('questions.txt', 'r') as file:
        questions = file.readlines()
except FileNotFoundError:
    print("Файл questions.txt не найден")
    exit()

# Инициализируем переменную для подсчета правильных ответов
score = 0

# Функция для отправки вопроса и кнопок
def send_question(message):
    global score
    if questions:
        question = questions.pop(0).strip()
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        options = ["Вариант 1", "Вариант 2", "Вариант 3", "Вариант 4"]
        for option in options:
            markup.add(types.KeyboardButton(option))
        bot.send_message(message.chat.id, question, reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f"Викторина завершена. Ваш счет: {score}")
        score = 0

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    send_question(message)

# Обработчик ответов пользователя
@bot.message_handler(func=lambda message: True)
def handle_answer(message):
    global score
    # Проверяем правильность ответа и увеличиваем счет, если ответ правильный
    if message.text == "Правильный вариант":
        score += 1
    send_question(message)

# Запускаем бота
bot.polling()


    
