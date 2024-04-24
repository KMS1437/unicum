#Экономика
# -*- coding: utf-8 -*-

from telebot import types
import random
import telebot
import re
import sympy
import json
import os

bot = telebot.TeleBot("TOKEN")

moneys = 0

@bot.message_handler(commands=['plus'])
def add_money(message):
    global moneys
    amount = int(message.text.split()[1])
    moneys += amount
    bot.send_message(message.chat.id, "✅ Средства добавлены.")

@bot.message_handler(commands=['minus'])
def deduct_money(message):
    global moneys
    amount = int(message.text.split()[1])
    moneys -= amount
    bot.send_message(message.chat.id, "✅ Средства вычтены.")

@bot.message_handler(commands=['balance'])
def get_balance(message):
    bot.send_message(message.chat.id, f"💰 Баланс: {moneys} руб.")

if os.path.exists('persons.json'):
    with open('persons.json', 'r') as file:
        persons = json.load(file)
        admins = persons['admins']
        bans = persons['bans']
else:
    print("Файл persons.json не существует. Пожалуйста, убедитесь, что он создан и заполнен корректно.")


@bot.message_handler(commands=['code'])
def send_code(message):
    user_id = message.from_user.id
    print(f"ID пользователя {message.from_user.first_name}:", user_id)
    if user_id in admins:
        with open('economic.py', 'r', encoding='utf-8') as file:
            bot.send_message(message.chat.id, "*Код бота:*", parse_mode="Markdown")
            bot.send_document(message.chat.id, file)

    else:
        bot.send_message(message.chat.id, "Вы не админ. У вас нет доступа к этой команде")


def replace_superscript(text):
    superscripts = {
        '0': '⁰',
        '1': '¹',
        '2': '²',
        '3': '³',
        '4': '⁴',
        '5': '⁵',
        '6': '⁶',
        '7': '⁷',
        '8': '⁸',
        '9': '⁹'
    }

    def replace_match(match):
        return superscripts.get(match.group(0)[1], match.group(0))

    pattern = re.compile(r"\^(\d)")
    result = re.sub(pattern, replace_match, text)
    return result

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "*👋 Привет! Я бот по балансу ваших денег и работаю на Дмитрия Борисовича. Чем могу помочь?*",
                     parse_mode="Markdown")
    bot.send_message(message.chat.id, "Нажмите на кнопку или введите задачу:",
                     reply_markup=get_keyboard())


@bot.message_handler(commands=['info'])
def handle_info(message):
    bot.send_message(message.chat.id,
                     f'*Создатель:* @misakamozin\n*Дата первого создания:* 27 марта 2024\n*Описание проекта: * Проект был создан при поддержке учебного заведения "ЦДНИТТ при КузГТУ «УникУм»". Этот проект может помочь студентам сверить свой ответ по алгебре или физике с ответом бота.\n*Используемые библиотеки: * telebot, random, re, sympy, json, os',
                     parse_mode="Markdown")


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    user_input = message.text
    if message.from_user.id in bans:
        bot.send_message(message.chat.id, f"⚡ Вам заблокирован доступ к боту, {message.from_user.first_name}.")
    elif user_input == "🏆 Миша испорченный до невозможности":
        bot.send_message(message.chat.id, f"⚜ Однозначно, {message.from_user.first_name}!")
    elif user_input == "💀 Насколько ты Паскарь?":
        chance = random.randrange(1, 100)
        bot.send_message(message.chat.id, f"⚜ {message.from_user.first_name}, вы Паскарь на {chance}%")
    elif user_input == "💻 Как пользоваться этим ботом?":
        bot.send_message(message.chat.id,
                         f"⚜ {message.from_user.first_name}, напишите команду /minus, /plus, /balance.")
    elif user_input == "❓ Обновления проекта":
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton("Канал по проекту", url='https://t.me/project_unicum')
        markup.add(button1)
        bot.send_message(message.chat.id, "Обновления проекта:", reply_markup=markup)
    else:
        try:
            if re.match(r'^[a-zA-Z0-9+\-*/^().= ]+$', user_input):
                if "=" in user_input:
                    def money(user_input):
                        try:
                            result = eval(user_input)
                            return result
                        except Exception as e:
                            return f"Ошибка: {e}"
                else:
                    result = sympy.sympify(user_input)
                    expanded_result = sympy.expand(result)
                    response = f"⚜️ Ваш баланс: {moneys}"
            else:
                response = "🚫 Error: Invalid expression format."
        except Exception as e:
            response = f"🚫 Error: {e}"

        response = response.replace("*", "")
        bot.reply_to(message, response)


def get_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton("🏆 Миша испорченный до невозможности")
    button2 = types.KeyboardButton("💻 Как пользоваться этим ботом?")
    button3 = types.KeyboardButton("💀 Насколько ты Паскарь?")
    button4 = types.KeyboardButton("❓ Обновления проекта")
    markup.add(button1, button2, button3, button4)
    return markup


if __name__ == "__main__":
    bot.polling(none_stop=True)
