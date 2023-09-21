import os
from dotenv import load_dotenv
import telebot
from telebot import types
from random import shuffle
import django
django.setup()
from testlar.models import Test

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)
answers = []
questions = []
def data_cell():
    db = Test.objects.all()
    question: Test
    for question in db:
        questions.append(question.savol)
        answers.append(question.javoblar.split('-'))

count = 0

def makekeyboard(question_id: int):
    markup = types.InlineKeyboardMarkup()
    buttons = []
    for answer_id, answer in enumerate(answers[question_id]):
        buttons.append(types.InlineKeyboardButton(text=answer, callback_data=f"{question_id}_{answer_id}"))
    shuffle(buttons)
    for button in buttons:
        markup.add(button)
    return markup

@bot.message_handler(commands=['start'])
def handle_test(msg: types.Message):
    data_cell()
    bot.send_message(chat_id=msg.chat.id,
                    text=questions[0],
                    reply_markup=makekeyboard(0),
                    parse_mode='HTML')

@bot.callback_query_handler(func=lambda call:True)
def handle_answer(cb: types.CallbackQuery):
    global count
    global questions
    global answers
    question_id, answer_id = cb.data.split("_")
    if int(answer_id) == 0:
        count += 1
    if len(questions) > int(question_id) + 1:
        print(cb.data)
        bot.edit_message_text(chat_id=cb.message.chat.id, message_id=cb.message.message_id, text=questions[int(question_id) + 1], reply_markup=makekeyboard(int(question_id) + 1))
    else:
        bot.send_message(chat_id=cb.message.chat.id, text=f"Qoyil siz {len(questions)} ta savoldan, {count} ta savol topdingiz !!")
        count = 0
        questions = []
        answers = []

bot.infinity_polling()