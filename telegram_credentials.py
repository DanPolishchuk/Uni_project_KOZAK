from telethon import TelegramClient

api_id = "your api id"                               # api_id and api_hash are mandatory values for connecting to Telegram

api_hash = "your api hash"   # client, you can get them by logging in on www.my.telegram.org

client = TelegramClient("your account", api_id, api_hash)   # here we specify to which Telegram client we want to connect


