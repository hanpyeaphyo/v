import telebot

# Telegram Config
TOKEN = '8057302563:AAHP3pluJYyNDDlWrDVjoc9uuzTmZW-4uCw'  # WARNING: Regenerate this token for security
CHAT_ID = '5671920054'  # Replace with your actual chat ID
bot = telebot.TeleBot(TOKEN)

# File paths inside EC2
file_paths = [
    '/home/ec2-user/bot.env',
    '/home/ec2-user/bot.py'
]

# Send files to Telegram
for file_path in file_paths:
    try:
        with open(file_path, 'rb') as f:
            bot.send_document(CHAT_ID, f)
        print(f"✅ {file_path} has been sent to Telegram.")
    except Exception as e:
        print(f"❌ Failed to send {file_path}: {e}")
