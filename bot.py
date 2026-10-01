import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os

# ទាញយក Token ដោយសុវត្ថិភាពពី Environment Variables របស់ Railway
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # បង្កើតប៊ូតុង (Keyboard) តាមដែលអ្នកបានស្នើសុំ
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("🛍️ ហាងទំនិញ")
    btn2 = KeyboardButton("»  Tik Tok Kh 🇰🇭")
    markup.add(btn1, btn2)
    
    welcome_text = "សួស្តី! សូមជ្រើសរើសជម្រើសខាងក្រោម៖"
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    # កំណត់ការឆ្លើយតបនៅពេលគេចុចលើប៊ូតុងនីមួយៗ
    if message.text == "🛍️ ហាងទំនិញ":
        bot.reply_to(message, "សូមស្វាគមន៍មកកាន់ហាងទំនិញរបស់យើង! 🛒")
    elif message.text == "»  Tik Tok Kh 🇰🇭":
        bot.reply_to(message, "សូមទស្សនាវីដេអូនៅលើ Tik Tok របស់យើងទីនេះ៖ [ដាក់លីងរបស់អ្នកនៅទីនេះ]")
    else:
        bot.reply_to(message, "ខ្ញុំមិនយល់ទេ សូមប្រើប្រាស់ប៊ូតុងខាងក្រោម។")

if __name__ == "__main__":
    print("Bot កំពុងដំណើរការ...")
    bot.infinity_polling()
