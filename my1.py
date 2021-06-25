import telebot
from telebot import TeleBot, types
from hola import TOKEN
import DBRec
import buttons


bot: TeleBot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard_send_welcome = types.ReplyKeyboardMarkup(resize_keyboard= True)
    button1 = types.KeyboardButton('ДА')
    keyboard_send_welcome.add(button1)

    bot.reply_to(message, "Здравствуйте, желаете записаться на прием?", reply_markup = keyboard_send_welcome)


@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.text == 'ДА':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Маникюр')
        button2 = types.KeyboardButton('Педикюр')
        button3 = types.KeyboardButton('Макияж')
        button4 = types.KeyboardButton('Наращивание')
        button5 = types.KeyboardButton('Стрижка')
        button6 = types.KeyboardButton('НАЗАД')
        markup.add(button1, button2, button3, button4, button5, button6)
        bot.send_message(message.chat.id, "Выберите услугу", reply_markup = markup)
    if message.text in buttons.buttons_list:
        bot.send_message(message.chat.id, 'Укажите Ваше имя')
    if message.text == 'Владимир':
        bot.send_message(message.chat.id,'Спасибо! Ваши данные добавлены в базу. Наш менеджер свяжется с Вами.')

        # phone_number = message.from_user.phone_number
        # client_name = message.from_user.client_name
        # date = message.from_user.date
        # time = message.from_user.time
		#
        # DBRec.db_rec(phone_number=DBRec.User.phone_number, user_name=DBRec.User.user_name, date=DBRec.User.date(), time=DBRec.User.time)



bot.polling()
