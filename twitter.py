import tweepy
import os
import requests
from main import get_username

auth = tweepy.AppAuthHandler(os.environ['VIDDOWNLOADBOT_TWITTER_API'], os.environ['VIDDOWNLOADBOT_TWITTER_SECRET'])
api = tweepy.API(auth)

def twitter_download(bot, message, debug):
    if debug:
        print('(Twitter) Got valid request from ' + message.chat.first_name + ' - ' + get_username(message))
    # Extract status id
    if "?" in message.text:
        status_id = message.text[message.text.find("status/") + 7:message.text.find("?")]
    else:
        status_id = message.text[message.text.find("status/") + 7:]
    # Get tweet
    try:
        status = api.get_status(status_id)
        try:
            video_info = status.extended_entities['media'][0]['video_info']['variants']
            video_urls = []
            # Get all video urls
            for x in video_info:
                try:
                    if isinstance(x['bitrate'], int):
                        video_urls.append(x['url'])
                except:
                    pass
            # Select the last URL (the video with the highest bitrate)
            video_url = video_urls[-1]
            # Download video
            video = requests.get(video_url)
            open('twittervideo.mp4', 'wb').write(video.content)
            # Send video
            if debug:
                print('(Twitter) Sending video to ' + message.chat.first_name + ' - ' + get_username(message))
            bot.reply_to(message, "Sending video...")
            bot.send_video(message.chat.id, open('twittervideo.mp4', 'rb'))
            # Clean
            os.remove('twittervideo.mp4')
            if debug:
                print('(Twitter) Done: ' + message.chat.first_name + ' - ' + get_username(message))
        except:
            bot.reply_to(message, "That tweet doesn't contain a video")
            if debug:
                print('(Twitter) Tweet without video from ' + message.chat.first_name + ' - ' + get_username(message))
    except:
        bot.reply_to(message, "That's not a tweet :/")
        if debug:
            print('(Twitter) Invalid tweet from ' + message.chat.first_name + ' - ' + get_username(message))

