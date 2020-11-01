import telebot
#API token
with open(('c:/Users/sib20/OneDrive/Рабочий стол/BotITKvant/API.txt'), "r") as file:
    API = file.read()

bot = telebot.TeleBot(API)

#massage sent
@bot.message_handler(content_types=['text'])
def get_text_massages(message):
    if message.text.lower() == "run":
         bot.send_message(message.from_user.id, "Bot was started!")
    else:
        bot.send_message(message.from_user.id, "I not undestand your command((")

bot.polling(none_stop=True, interval=0)