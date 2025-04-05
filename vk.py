import telebot

# Telegram Config
TOKEN = '8057302563:AAHP3pluJYyNDDlWrDVjoc9uuzTmZW-4uCw'
CHAT_ID = '5671920054'  # Example: '123456789'
bot = telebot.TeleBot(TOKEN)

# File Path inside EC2
file_path = '/home/ec2-user/bot.py'  # သင့် bot.py ရဲ့ တည်နေရာ

# Send file
try:
    with open(file_path, 'rb') as f:
        bot.send_document(CHAT_ID, f)
    print("✅ bot.py has been sent to Telegram.")
except Exception as e:
    print(f"❌ Failed to send file: {e}")
