import telebot

bot = telebot.TeleBot("TOKEN")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     "<b>⚜ Все боты:\n<a href='t.me/project_unicum_bot'>∑Алгебра</a>\n<a href='t.me/project_unicum2_bot'>💡Физика</a></b>",
                     parse_mode="HTML")

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    user_input = message.text
    if user_input == " ":
        bot.send_message(message.chat.id,
                         "Напиши /start")
    else:
        bot.send_message(message.chat.id,
                         "Напиши /start")

bot.polling()
