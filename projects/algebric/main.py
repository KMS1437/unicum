from telebot import types
import telebot
import re
from sympy import sympify, expand

bot = telebot.TeleBot('Максим тут нет токена')

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
    bot.send_message(message.chat.id, "*👋 Привет! Я бот по алгебре и работаю на Дмитрия Борисовича. Чем могу помочь?*", parse_mode="Markdown")
    bot.send_message(message.chat.id, "Нажмите на кнопку или введите алгебраическое выражение:", reply_markup=get_keyboard())

@bot.message_handler(commands=['sasat'])
def handle_sosi(message):
    bot.send_message(message.chat.id, f'*🍌Соси, {message.from_user.first_name}!*', parse_mode="Markdown")

@bot.message_handler(commands=['1000-7'])
def handle_dedinside(message):
    bot.send_message(message.chat.id, f'*🐷Малолетний дед инсайд {message.from_user.first_name}*', parse_mode="Markdown")

@bot.message_handler(commands=['fuckingsemen'])
def handle_semen(message):
    bot.send_message(message.chat.id, f'*Oh yes {message.from_user.first_name}*', parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    user_input = message.text
    if message.from_user.id == 5041299186:
        bot.send_message(message.chat.id, f"*⚡ Пошел лесом, {message.from_user.first_name}*", parse_mode="Markdown")
    elif user_input == "🍌 Fucking so horny dungeon full master Semen":
        bot.send_message(message.chat.id, text=f"*️⚜ Oh yes, {message.from_user.first_name}!*", parse_mode="Markdown")
    elif message.text == "❓ Обновления проекта":
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Канал по проекту", url='https://t.me/project_unicum')
        markup.add(button1)
    else:
        try:
            result = sympify(user_input)
            expanded_result = expand(result)
            result_str = replace_superscript(str(expanded_result).replace("**", "^"))
            response = f"*⚜️ Результат:* {result_str}"
        except Exception as e:
            response = f"*🚫 Ошибка:* {e}"
        bot.send_message(message.chat.id, response, parse_mode="Markdown")


def get_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton("🍌 Fucking so horny dungeon full master Semen")
    button2 = types.KeyboardButton("❓ Обновления проекта")
    markup.add(button1, button2)
    return markup

if __name__ == "__main__":
    bot.polling(none_stop=True)
