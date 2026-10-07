import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

# ទាញយក Token ពី Environment Variable (ងាយស្រួលពេលដាក់លើ Railway)
TOKEN = os.getenv('BOT_TOKEN', 'សូមដាក់_TOKEN_របស់អ្នកនៅទីនេះ')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # បង្កើត Button (2 column)
    markup = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton("👨🏻‍💻 គណនី", callback_data='account')
    btn2 = InlineKeyboardButton("🛍️ ហាងសេវា", callback_data='store')
    btn3 = InlineKeyboardButton("💸 ដាក់ប្រាក់", callback_data='deposit')
    # Link ទៅកាន់អ្នកគ្រប់គ្រងដោយផ្ទាល់
    btn4 = InlineKeyboardButton("💬 អ្នកគ្រប់គ្រង", url='https://t.me/Dumyy_ji2') 
    
    markup.add(btn1, btn2, btn3, btn4)
    
    text = (
        "សួរស្ដី! សូមស្វាគមន៌មកកាន់ Toad Store 24/7\n"
        "សូមជ្រើសរើសសេវាកម្មខាងក្រោម"
    )
    bot.send_message(message.chat.id, text, reply_markup=markup)

# ចាប់យកសកម្មភាពពេលគេចុចលើ Button
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'store':
        # ផ្ញើសារប្រាប់ពេលចុច ហាងសេវា
        bot.send_message(call.message.chat.id, "ប្រព័ន្ធកំពុង Update service .")
    elif call.data == 'account':
        bot.answer_callback_query(call.id, "កំពុងរៀបចំ...")
    elif call.data == 'deposit':
        bot.answer_callback_query(call.id, "កំពុងរៀបចំ...")

print("Bot កំពុងដំណើរការ...")
bot.infinity_polling()
