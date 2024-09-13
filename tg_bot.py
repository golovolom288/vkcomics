import shutil

from dotenv import load_dotenv
import telegram
import os
import time
import random
from get_comics import get_comics


def send_posts_tg_bot(hours, tg_bot_token, chat_id, alt, directory="images/"):
    photos = os.listdir(directory)
    random.shuffle(photos)
    bot = telegram.Bot(token=tg_bot_token)
    while True:
        for photo in photos:
            photo_path = os.path.join(directory, photo)
            with open(photo_path, "rb") as photo:
                bot.send_photo(chat_id=chat_id, photo=photo, caption=alt)
            shutil.rmtree("comics")
            time.sleep(int(hours*3600))


if __name__ == "__main__":
    load_dotenv()
    chat_id = os.environ["TG_GROUP_ID"]
    hours = int(os.environ["TG_TIME"])
    tg_bot_token = os.environ["TG_BOT_TOKEN"]
    send_posts_tg_bot(hours, tg_bot_token, chat_id, get_comics()[1], directory="comics/")
