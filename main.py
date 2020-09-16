import static

import telebot

bot_api = static.bot_api

@bot.message_handler(content_types=['text'])

if message.text == "Привет":
    bot.send_message(message.from_user.id, "Привет, для просмотра правил игры введи /help ")
elif message.text == "/help":
    bot.send_message(message.from_user.id, "Напиши привет")
else:
    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

#def game_info():
    



#def game(message):
