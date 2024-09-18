from dotenv import load_dotenv
import telegram
import os
from get_comics import get_comics


def send_posts_tg_bot(tg_bot_token, chat_id, alt, directory="comics/"):
    bot = telegram.Bot(token=tg_bot_token)
    photo_path = os.path.join(directory, "comics.jpg")
    with open(photo_path, "rb") as photo:
        bot.send_photo(chat_id=chat_id, photo=photo, caption=alt)


if __name__ == "__main__":
    load_dotenv()
    chat_id = os.environ["TG_GROUP_ID"]
    tg_bot_token = os.environ["TG_BOT_TOKEN"]
    send_posts_tg_bot(tg_bot_token, chat_id, get_comics()[1], directory="comics/")
