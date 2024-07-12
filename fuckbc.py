import requests
import random
import telebot
from getuseragent import UserAgent

# Your bot token from Telegram
BOT_TOKEN = '6489527313:AAG56ImMlkO3u8SviFnL_G1zadsScoB1ehI'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Send your Instagram username and post link in the format: username|link")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        data = message.text.split('|')
        if len(data) != 2:
            bot.reply_to(message, "Please provide the input in the format: username|link")
            return
        
        user, link = data[0], data[1]
        ua = UserAgent("ios").Random()
        email = f"tanji{random.randint(100000,999999)}@gmail.com"
        
        headers = {
            "Host": "api.likesjet.com",
            "content-length": "137",
            "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "sec-ch-ua-mobile": "?1",
            "user-agent": ua,
            "sec-ch-ua-platform": "\"Android\"",
            "origin": "https://likesjet.com",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://likesjet.com/",
            "accept-language": "en-XA,en;q=0.9,ar-XB;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5"
        }
        
        payload = {
            "instagram_username": user,
            "link": link,
            "email": email
        }
        
        res = requests.post('https://api.likesjet.com/freeboost/7', json=payload, headers=headers).json()
        bot.reply_to(message, res['message'])
    
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {str(e)}")

bot.polling()
