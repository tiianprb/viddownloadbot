# viddownloadbot

This is the source code for a Telegram bot that downloads videos from Twitter and sends it to the user

Test it on [@viddownloadbot](https://t.me/viddownloadbot)

## Deploying

You need to set 3 environment variables:

- VIDDOWNLOADBOT_TELEGRAM: A bot token for Telegram
- VIDDOWNLOADBOT_TWITTER: A Twitter API Key
- VIDDOWNLOADBOT_TWITTER_SECRET: The secret for the previous Twitter API Key

Then install `pyTelegramBotAPI` and `tweepy` from pip (`pip install pyTelegramBotAPI tweepy` or `python3 -m pip install pyTelegramBotAPI tweepy`)

And run the bot: `python3 main.py`

## License

MIT