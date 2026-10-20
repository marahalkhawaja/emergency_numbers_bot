from telegram import Bot

from config import BOT_TOKEN


def get_bot():
    return Bot(token=BOT_TOKEN)
