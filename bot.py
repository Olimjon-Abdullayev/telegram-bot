from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = "6625639343:AAGRQTAaF0YDlPxvRLxSSmHAMfue8QMHThI"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Assalomu alaykum, botimizga xush kelibsiz. Bu botga matn\
    yuborib uni uzbekchadan krillchaga yoki krillchadan uzbekchaga o'tkazishingiz mumkin")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        msg = to_cyrillic(msg)
    else:
        msg = to_latin(msg)
    bot.reply_to(message, msg)

bot.polling()