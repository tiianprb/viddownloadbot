import telebot
import os
import threading
import time
from twitter import twitter_download

debug = False

# Set your bot token in an environment variable called VIDDOWNLOADBOT_TELEGRAM
bot = telebot.TeleBot(os.environ['5050150479:AAE3QJAgLW88isOmXbxfysK0sJFTgf0InDs'])

# Get username, for debug purposes
def get_username(message):
    if message.chat.username:
        return message.chat.username
    else:
        return 'no username'

# /start and /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi!\n"
                          "This bot will let you download Twitter videos. Just send me the "
                          "link to the tweet and I'll reply you in a few moments with the video.")


# Handle any other message
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if ("twitter.com/" in message.text) and ("/status/" in message.text):
        twitter_download(bot, message, get_username(message), debug)
    else:
        bot.reply_to(message, "That's not a valid link!")
        if debug:
            print('Invalid link from ' + message.chat.first_name + ' - ' + get_username(message))


bot.polling()

