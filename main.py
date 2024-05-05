import telebot
from telebot import types, TeleBot

bot = TeleBot("6757574098:AAFCbWlM8asjiROLipkWuiN1lXaM7d4oRvs")

back = types.InlineKeyboardButton(text=" المطور ",callback_data = "b1")

@bot.message_handler(commands=["start"])
def start(message):
 b = types.InlineKeyboardMarkup()
 b.row_width = 1
 b.add(back)
 bot.reply_to(message,f"انت مشترك راسل المطور لتفعيلك!", reply_markup=b)
@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
  if call.data == "b1":
   bot.send_message(call.message.chat.id,f"عذرآ البوت للاستخدام شخصي فقط المالك @Flaplex")
bot.polling()
