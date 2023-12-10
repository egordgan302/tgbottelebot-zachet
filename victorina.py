import telebot
import json

bot = telebot.TeleBot("")


try:
    with open('questions.json', 'r', encoding='utf-8') as file:
        questions = file.readlines()
except FileNotFoundError:
    print("File questions.json not found")
    exit()
def read_questions(file):
    with open(file, 'r', encoding='utf-8') as f:
        questions = json.load(f)
        return questions

questions_file = 'questions.json'
quiz_questions = read_questions(questions_file)
user_answers = {}  

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "dota 2: Welcome to the world of absurdity {0.first_name}! This quiz is a survival game, during the quiz your soul belongs to me, good luck? /start_quiz".format(message.from_user))

@bot.message_handler(commands=['start_quiz'])
def start_quiz(message):
    chat_id = message.chat.id
    user_answers[chat_id] = {'score': 0, 'current_question': 0}
    send_question(chat_id)

def send_question(chat_id):
    current_question = user_answers[chat_id]['current_question']
    if current_question < len(quiz_questions):
        question_data = quiz_questions[current_question]
        question = question_data['question']
        options = question_data['options']
        markup = create_markup(options)
        bot.send_message(chat_id, f"{question}\n\nchoose your path:", reply_markup=markup)
    else:
        finish_quiz(chat_id)

def create_markup(options):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for option in options:
        markup.add(telebot.types.KeyboardButton(option))
    return markup

def finish_quiz(chat_id):
    score = user_answers[chat_id]['score']
    bot.send_message(chat_id, f"The quiz is over. souls remained:: {score}/{len(quiz_questions)}")

@bot.message_handler(func=lambda message: True)
def check_answer(message):
    chat_id = message.chat.id
    current_question = user_answers[chat_id]['current_question']
    correct_answer = quiz_questions[current_question]['answer']
    user_answer = message.text

    if user_answer == correct_answer:
        user_answers[chat_id]['score'] += 1

    user_answers[chat_id]['current_question'] += 1
    send_question(chat_id)

bot.polling(none_stop=True)
