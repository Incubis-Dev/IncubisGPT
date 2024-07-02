import telebot
from telebot import types
from RequestGPT import answer

token='7434524034:AAHMTksYyRPTRwtkZRvwvZ1ALJGVlPMVrps'
bot=telebot.TeleBot(token)
qq = []

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Привет ✌️ ")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Задать вопрос Yandex.GPT")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я GPT бот для Инкубиса, все запросы которые ты будешь делать через меня записываются".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Задать вопрос Yandex.GPT"):
        global returning
        a = bot.send_message(message.chat.id, 'Введите инструкцию:')
        bot.register_next_step_handler(a, manual)

def manual(message):
    qq.append(message.text)
    a = bot.send_message(message.chat.id, 'Введите запрос:')
    bot.register_next_step_handler(a, requesting)

def requesting(message): 
    y = message.text
    qq.append(y)
    print ("massiv do")
    print(qq) 
    ans = answer(qq)
    bot.send_message(message.chat.id, ans)
    del qq[0:3]
    print ("massiv posle")
    print(qq)

bot.infinity_polling()

