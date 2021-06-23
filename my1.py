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
		bot.reply_to(message, "Выберите услугу", reply_markup = markup)
	elif message.text in buttons.buttons_list:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		button1 = types.KeyboardButton('Маникюр')
		button2 = types.KeyboardButton('Педикюр')
		button3 = types.KeyboardButton('Макияж')
		button4 = types.KeyboardButton('Наращивание')
		markup.add(button1, button2, button3, button4)
		bot.reply_to(message, "Выберите дату")



bot.polling()
